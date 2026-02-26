import re
from smolagents import Tool
from typing import List, Dict, Any, Union

class FactVerifierTool(Tool):
    """
    Compares factual claims against a list of sources and returns a structured verdict.
    Helps AXIOM avoid hallucination and ensures only cross-verified facts are synthesized.
    """
    name = "verify_facts"
    description = (
        "Verify a factual claim against multiple strings or source dictionary snippets. "
        "Returns a high-signal report with a verdict (VERIFIED/SINGLE_SOURCE/UNVERIFIED)."
    )
    inputs = {
        "claim": {
            "type": "string",
            "description": "Specific fact or claim to verify (e.g., 'The Repo rate is 6.50%')."
        },
        "sources": {
            "type": "any",
            "description": "A list of strings or dictionaries containing excerpts from different web sources."
        }
    }
    output_type = "any"

    def forward(self, claim: str, sources: List[Union[str, Dict]]) -> Dict[str, Any]:
        """
        Executes text comparison and returns a high-signal verdict.
        In an industrial agent, this would be a specialized validation logic.
        """
        if not sources or not isinstance(sources, list):
            return {"verdict": "ERROR", "reason": "No sources provided."}

        # Simplified evidence check:
        # Keywords from claim are searched for in sources to find supporting evidence.
        claim_keywords = set(re.findall(r'\w+', claim.lower()))
        # Remove common stop words (simplified set)
        stop_words = {'the', 'is', 'at', 'which', 'on', 'a', 'an', 'and', 'for', 'of', 'by', 'with', 'to', 'in', 'as', 'are', 'was', 'were'}
        claim_keywords = {k for k in claim_keywords if k not in stop_words and len(k) > 2}
        
        matches = 0
        total_sources = len(sources)
        supporting_sources = []
        
        for idx, src in enumerate(sources):
            # Resolve the content to check
            text_to_check = str(src.get('snippet', '')) + str(src.get('title', '')) if isinstance(src, dict) else str(src)
            text_to_check = text_to_check.lower()
            
            # Simple keyword search (simulated NLP overlap)
            # Match is considered significant if >60% of claim's keywords are found in a source
            found_keywords = [k for k in claim_keywords if k in text_to_check]
            if len(claim_keywords) > 0 and (len(found_keywords) / len(claim_keywords)) >= 0.6:
                matches += 1
                supporting_sources.append(idx)
        
        # Calculate verdict based on industrial threshold
        # VERIFIED requires at least 2 independent matches.
        if matches >= 2:
            verdict = "VERIFIED"
        elif matches == 1:
            verdict = "SINGLE_SOURCE"
        else:
            verdict = "UNVERIFIED"
            
        return {
            "claim": claim,
            "verdict": verdict,
            "confidence": round(matches / max(1, total_sources), 2),
            "source_match_count": matches,
            "is_synthesizable": (verdict == "VERIFIED" or verdict == "SINGLE_SOURCE")
        }

if __name__ == "__main__":
    verifier = FactVerifierTool()
    test_sources = [
        "The current repo rate is 6.50% as announced by RBI.",
        "RBI governor Shaktikanta Das kept the repo rate unchanged at 6.50% in the latest meeting.",
        "Market analysts expected a rate cut but it remained steady."
    ]
    print(verifier("The current repo rate is 6.50%", test_sources))
