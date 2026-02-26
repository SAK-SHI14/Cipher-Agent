from smolagents import Tool
from typing import List, Dict, Any, Union
import difflib
import re

class FactVerifierTool(Tool):
    name = "fact_verifier"
    description = (
        "Compares a specific claim against a list of source snippets to provide a verdict "
        "of Support, Contradict, or Inconclusive. This is used for cross-checking information."
    )
    inputs = {
        "claim": {
            "type": "string",
            "description": "The specific claim to verify (e.g., 'OpenAI CEO is Sam Altman')."
        },
        "sources": {
            "type": "any",
            "description": "A list of strings or dictionaries containing snippets from different sources."
        }
    }
    output_type = "any"

    def forward(self, claim: str, sources: Any) -> Dict[str, Any]:
        """
        The logic for verification. 
        In an industrial system, this could invoke a specialized model or cross-reference 
        with factual databases. 
        For this prototype, it summarizes the findings based on textual overlap or 
        presence of key entities (case-insensitive search).
        """
        if not sources or not isinstance(sources, list):
            return {"verdict": "NoSources", "confidence": 0, "reason": "No sources provided."}

        # Simplified evidence check:
        # We look for keywords from the claim in the sources
        claim_keywords = set(re.findall(r'\w+', claim.lower()))
        # Remove common stop words (simplified set)
        stop_words = {'the', 'is', 'at', 'which', 'on', 'a', 'an', 'and', 'for', 'of', 'by', 'with', 'to', 'in', 'as'}
        claim_keywords = {k for k in claim_keywords if k not in stop_words and len(k) > 2}
        
        matches = 0
        total_sources = len(sources)
        supporting_sources = []
        contradicting_sources = []
        
        for idx, src in enumerate(sources):
            # source could be a dict or a string
            text_to_check = str(src.get('snippet', '')) + str(src.get('title', '')) if isinstance(src, dict) else str(src)
            text_to_check = text_to_check.lower()
            
            # Simple keyword search:
            # If at least 70% of keywords are found in source, it's a potential match
            found_keywords = [k for k in claim_keywords if k in text_to_check]
            if len(claim_keywords) > 0 and (len(found_keywords) / len(claim_keywords)) >= 0.6:
                matches += 1
                supporting_sources.append(idx)
        
        # Threshold-based verdict
        confidence = round(matches / max(1, total_sources), 2)
        
        if matches >= 2:
            verdict = "VERIFIED"
        elif matches == 1:
            verdict = "SINGLE_SOURCE"
        else:
            verdict = "UNVERIFIED"
            
        return {
            "verdict": verdict,
            "confidence": confidence,
            "count": matches,
            "claim": claim
        }

if __name__ == "__main__":
    verifier = FactVerifierTool()
    test_sources = [
        {"snippet": "Sam Altman is the CEO of OpenAI as of 2024.", "title": "OpenAI News"},
        "The current head of OpenAI is Sam Altman, who returned in late 2023.",
        "Mira Murati is the CTO, not current CEO."
    ]
    print(verifier("Sam Altman is OpenAI CEO", test_sources))
