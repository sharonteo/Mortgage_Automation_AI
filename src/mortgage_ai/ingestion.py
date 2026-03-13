class Document:
    """
    Simple document wrapper for mortgage-related text.
    """
    def __init__(self, content: str, filename: str | None = None, metadata: dict | None = None):
        self.content = content
        self.text = content      # pipeline uses .text
        self.filename = filename
        self.metadata = metadata or {}


def load_text_document(path: str) -> Document:
    """
    Load a plain text file and wrap it in a Document.
    """
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return Document(content=content, filename=path)