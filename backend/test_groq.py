from app.services.llm.groq_client import GroqClient

llm = GroqClient()

response = llm.generate(
    "Say Hello"
)

print(response)