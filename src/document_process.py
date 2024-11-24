from langchain_community.document_loaders import PyPDFLoader, UnstructuredWordDocumentLoader
import os

class Document_loader:
    def __init__(self,doc_path):
        self.doc = doc_path


    def data_extractor(self):
        file_extension = os.path.splitext(self.doc)[-1]
        if file_extension == ".pdf":
            loader = PyPDFLoader(self.doc)
            pdf_doc = loader.load()
            return pdf_doc

        elif (file_extension == ".docx") or (file_extension == ".doc"):
            loader = UnstructuredWordDocumentLoader(self.doc)
            doc = loader.load()
            return doc

if __name__ == "__main__":
    path = r"C:\Users\lalit\Downloads\1706234818539.pdf"
    doc = Document_loader(path).data_extractor()
    # print(os.path.splitext(path))
    print(doc)