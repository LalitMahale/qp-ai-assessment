from document_process import Document_loader
from chunking import Chunking
from db import Vectordb

# path = r"C:\Users\lalit\Downloads\1706234818539.pdf"
# doc = Document_loader(doc_path=path).data_extractor()
# chunk = Chunking().split_chunk(doc=doc)
# Vectordb().store_vectors(chunks=chunk)
query = "how to load csv file?"
retriever = Vectordb().vector_retriever(query=query)
text = Chunking(chunk_overlap=50,chunk_size=500).chunk_merge(chunks=retriever)
print(text)
