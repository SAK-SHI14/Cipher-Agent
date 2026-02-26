import re
from smolagents import Tool
from typing import List, Union, Dict, Any

class ClaimsVerifierTool(Tool):
    """
    Cross-references claims against a multi-source dataset to confirm statistical consensus.
    """
    name = "verify_claims"
    description = (
        "Verify a list of factual claims against an eivdence dataset. "
        "Flags claims as VERIFIED only if confirmed across multiple distinct sources."
    )
    inputs = {
        "claim": {
            "type": "string",
            "description": "Specific intelligence claim to verify."
        },
        "evidence_pool": {
            "type": "any",
            "description": "A collection of source strings or snippets used as ground truth."
        }
    }
    output_type = "any"

    def forward(self, claim: str, evidence_pool: List[Union[str, Dict]]) -> Dict[str, Any]:
        if not evidence_pool or not isinstance(evidence_pool, list):
            return {"status": "NO_EVIDENCE"}

        claim_lexemes = set(re.findall(r'\w+', claim.lower()))
        stops = {'the', 'is', 'at', 'on', 'a', 'an', 'and', 'for', 'of', 'by', 'it', 'was', 'to', 'in', 'are'}
        target_words = {w for w in claim_lexemes if w not in stops and len(w) > 2}
        
        matches = 0
        for src in evidence_pool:
            text = str(src.get('snippet', '')) + str(src.get('title', '')) if isinstance(src, dict) else str(src)
            text = text.lower()
            
            found = [w for w in target_words if w in text]
            if len(target_words) > 0 and (len(found) / len(target_words)) >= 0.7:
                matches += 1
        
        verdict = "VERIFIED" if matches >= 2 else "UNCONFIRMED"
        
        return {
            "claim": claim,
            "verdict": verdict,
            "matches": matches,
            "conf_score": round(matches / max(1, len(evidence_pool)), 2)
        }
