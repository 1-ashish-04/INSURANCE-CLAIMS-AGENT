from app.services.llm.groq_client import GroqClient
from app.utils.prompt_loader import PromptLoader
from app.utils.json_parser import JSONParser

class Extractor:

    def __init__(self):

        self.llm = GroqClient()

    def extract(self, document_text: str):

        prompt = PromptLoader.load(
            "extraction_prompt.txt"
        )

        full_prompt = f"""
{prompt}

DOCUMENT

{document_text}
"""

        response = self.llm.generate(full_prompt)

        return JSONParser.parse(response)