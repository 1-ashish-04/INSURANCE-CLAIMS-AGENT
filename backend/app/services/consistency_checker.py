from datetime import datetime


class ConsistencyChecker:

    VALID_CLAIM_TYPES = {
        "vehicle",
        "injury",
        "property",
        "theft",
        "fire"
    }

    @classmethod
    def check(cls, claim: dict):

        issues = []

        # Estimated Damage
        damage = claim.get("estimatedDamage")

        if damage is not None and damage < 0:
            issues.append(
                "Estimated Damage cannot be negative."
            )

        # Initial Estimate
        estimate = claim.get("initialEstimate")

        if estimate is not None and estimate < 0:
            issues.append(
                "Initial Estimate cannot be negative."
            )

        # Incident Date
        incident_date = claim.get("incidentDate")

        if incident_date:
            try:

                date = datetime.strptime(
                    incident_date,
                    "%d-%b-%Y"
                )

                if date > datetime.now():

                    issues.append(
                        "Incident Date cannot be in the future."
                    )

            except Exception:
                pass

        # Claim Type
        claim_type = claim.get("claimType")

        if claim_type:

            if claim_type.lower() not in cls.VALID_CLAIM_TYPES:

                issues.append(
                    "Unknown Claim Type."
                )

        return issues