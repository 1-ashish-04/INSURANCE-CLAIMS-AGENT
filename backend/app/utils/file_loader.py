from pathlib import Path

from app.utils.pdf_reader import PDFReader


class FileLoader:

    @staticmethod
    def load(file_path: str) -> str:

        suffix = Path(file_path).suffix.lower()

        if suffix == ".pdf":
            return PDFReader.extract_text(file_path)

        elif suffix == ".txt":
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()

        else:
            raise ValueError("Unsupported file type.")