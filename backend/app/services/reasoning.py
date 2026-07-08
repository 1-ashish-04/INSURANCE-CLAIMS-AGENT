class ReasoningEngine:

    @staticmethod
    def generate(route, missing_fields):

        if route == "Investigation Flag":
            return (
                "Description contains potential fraud indicators."
            )

        if route == "Manual Review":
            return (
                "Mandatory fields are missing: "
                + ", ".join(missing_fields)
            )

        if route == "Specialist Queue":
            return (
                "Claim type is Injury and requires specialist handling."
            )

        if route == "Fast-track":
            return (
                "Estimated damage is below ₹25,000 and all mandatory fields are present."
            )

        return (
            "Claim does not meet criteria for any special routing."
        )