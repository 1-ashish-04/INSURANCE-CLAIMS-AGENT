from app.services.extractor import Extractor
from app.services.validator import ClaimValidator
from app.services.router import ClaimRouter
from app.services.reasoning import ReasoningEngine
from app.services.consistency_checker import ConsistencyChecker

class ClaimProcessor:

    def __init__(self):
        self.extractor = Extractor()

    def process(self, document_text):

        extracted = self.extractor.extract(document_text)

        missing = ClaimValidator.validate(extracted)

        issues = ConsistencyChecker.check(extracted)

        # Treat consistency issues the same as missing fields
        all_review_items = missing + issues

        route = ClaimRouter.determine_route(
            extracted,
            all_review_items
        )

        reasoning = ReasoningEngine.generate(
            route,
            all_review_items
)

        return {
            "extractedFields": extracted,
            "missingFields": missing,
            "consistencyIssues": issues,
            "recommendedRoute": route,
            "reasoning": reasoning
        }