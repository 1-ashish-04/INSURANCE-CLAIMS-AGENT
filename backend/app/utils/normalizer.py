import re


class Normalizer:

    @staticmethod
    def parse_currency(value):

        if value is None:
            return None

        if isinstance(value, (int, float)):
            return float(value)

        cleaned = re.sub(r"[^\d.]", "", str(value))

        if cleaned == "":
            return None

        return float(cleaned)