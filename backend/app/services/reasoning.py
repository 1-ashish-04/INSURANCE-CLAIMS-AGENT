class ReasoningEngine:

    @staticmethod
    def generate(route, review_items):

        if route == "Investigation Flag":
            return (
                "Description contains potential fraud indicators."
            )

        if route == "Manual Review":
            return (
                "Manual review required due to: "
                + ", ".join(review_items)
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