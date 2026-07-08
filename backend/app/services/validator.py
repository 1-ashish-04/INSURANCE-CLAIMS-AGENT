class ClaimValidator:

    REQUIRED_FIELDS = {
        "policyNumber": "Policy Number",
        "policyholderName": "Policyholder Name",
        "effectiveDates": "Effective Dates",
        "incidentDate": "Incident Date",
        "incidentTime": "Incident Time",
        "location": "Location",
        "description": "Description",
        "claimant": "Claimant",
        "contactDetails": "Contact Details",
        "assetType": "Asset Type",
        "assetId": "Asset ID",
        "estimatedDamage": "Estimated Damage",
        "claimType": "Claim Type",
        "attachments": "Attachments",
        "initialEstimate": "Initial Estimate",
    }

    @classmethod
    def validate(cls, claim: dict):

        missing = []

        for field, display_name in cls.REQUIRED_FIELDS.items():

            value = claim.get(field)

            if value is None:
                missing.append(display_name)

            elif isinstance(value, str) and value.strip() == "":
                missing.append(display_name)

        return missing