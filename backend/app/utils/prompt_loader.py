from pathlib import Path


class PromptLoader:

    @staticmethod
    def load(prompt_name: str) -> str:
        """
        Load a prompt template from the prompts folder.
        """

        prompt_path = (
            Path(__file__).resolve().parent.parent
            / "prompts"
            / prompt_name
        )

        with open(prompt_path, "r", encoding="utf-8") as file:
            return file.read()