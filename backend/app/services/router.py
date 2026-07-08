class ClaimRouter:

    FRAUD_KEYWORDS = [
        "fraud",
        "staged",
        "inconsistent"
    ]

    @classmethod
    def determine_route(cls, claim, review_items):

        description = (
            claim.get("description") or ""
        ).lower()

        if any(
            word in description
            for word in cls.FRAUD_KEYWORDS
        ):
            return "Investigation Flag"

        if review_items:
            return "Manual Review"

        claim_type = (
            claim.get("claimType") or ""
        ).lower()

        if claim_type == "injury":
            return "Specialist Queue"

        damage = claim.get("estimatedDamage")

        if damage is not None and damage < 25000:
            return "Fast-track"

        return "Standard Processing"