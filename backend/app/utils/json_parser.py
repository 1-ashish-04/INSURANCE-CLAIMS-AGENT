import json
import re


class JSONParser:

    @staticmethod
    def parse(response: str):

        response = response.strip()

        response = re.sub(
            r"^```json",
            "",
            response
        )

        response = re.sub(
            r"^```",
            "",
            response
        )

        response = re.sub(
            r"```$",
            "",
            response
        )

        response = response.strip()

        return json.loads(response)