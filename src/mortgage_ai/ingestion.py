class Document:
    """
    Represents a mortgage-related document (W-2, paystub, bank statement, etc.)
    with its content, filename, and optional metadata.
    """
    def __init__(self, content: str, filename: str | None = None, metadata: dict | None = None):
        self.content = content
        self.filename = filename
        self.metadata = metadata or {}

def load_text_document(path: str) -> Document:
    """
    Loads a text file from disk and wraps it in a Document object.
    This simulates OCR or LLM-based text extraction.
    """
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return Document(content=content, filename=path)