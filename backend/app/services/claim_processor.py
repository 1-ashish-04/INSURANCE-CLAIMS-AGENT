from app.services.extractor import Extractor
from app.services.validator import ClaimValidator
from app.services.router import ClaimRouter
from app.services.reasoning import ReasoningEngine


class ClaimProcessor:

    def __init__(self):
        self.extractor = Extractor()

    def process(self, document_text):

        extracted = self.extractor.extract(document_text)

        missing = ClaimValidator.validate(extracted)

        route = ClaimRouter.determine_route(
            extracted,
            missing
        )

        reasoning = ReasoningEngine.generate(
            route,
            missing
        )

        return {
            "extractedFields": extracted,
            "missingFields": missing,
            "recommendedRoute": route,
            "reasoning": reasoning
        }