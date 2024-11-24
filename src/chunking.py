from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

class Chunking:
    def __init__(self,chunk_size:int = 2000, chunk_overlap:int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_chunk(self,doc:Document):
        
        chunker =RecursiveCharacterTextSplitter(chunk_size = self.chunk_size,
                                                chunk_overlap = self.chunk_overlap)
        chunks = chunker.split_documents(doc)
        return chunks
    
    def chunk_merge(self,chunks):
        text = ""
        for chunk in chunks:
            text += chunk.page_content
        return text