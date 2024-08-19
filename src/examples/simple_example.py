from src.ai_graph.key_value_store import inject_storage_objects
from src.ai_graph.nodes.executable_node import ExecutableNode


class Document:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


class SummarizedDocument:
    def __init__(self, title: str, summary: str):
        self.title = title
        self.summary = summary


class JoinedDocument:
    def __init__(self, summary: str):
        self.summary = summary


class DocumentSummarizer(ExecutableNode):
    def __init__(self, document: Document):
        self.document = document

    @inject_storage_objects(Document)
    async def _execute_node(self, shared_storage) -> JoinedDocument:
        self.ope


document_summarizer = ExecutableNode
