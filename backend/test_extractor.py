from app.services.extractor import Extractor

text = """
Policy Number: POL12345

Policyholder Name:
John Smith

Incident Date:
15 June 2025

Estimated Damage:
₹20,000

Initial Estimate:
₹18,500

Claim Type:
Vehicle Damage
"""

extractor = Extractor()

response = extractor.extract(text)

print(type(response))
print(response)