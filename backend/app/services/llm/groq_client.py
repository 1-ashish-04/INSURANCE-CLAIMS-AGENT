from groq import Groq

from app.core.config import settings
from app.services.llm.base import BaseLLM


class GroqClient(BaseLLM):

    def __init__(self):
        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def generate(self, prompt: str) -> str:

        response = self.client.chat.completions.create(
            model=settings.MODEL_NAME,
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content