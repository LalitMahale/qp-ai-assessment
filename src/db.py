from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

class Vectordb:

    def embedding_model(self,model_name:str):
        try:
            embedding_model = HuggingFaceEmbeddings(model_name = model_name)
            return embedding_model
        except :
            return False


    def store_vectors(self,chunks,db_name:str = "emb_database/"):
        try:
            emb = self.embedding_model(model_name="sentence-transformers/all-MiniLM-L6-v2")
            db = Chroma.from_documents(documents=chunks,
                                    embedding=emb,
                                    persist_directory = db_name)
            return True
        except:
            return False

    def vector_retriever(self,query:str,db_path:str="emb_database/",K:int=3):
        try:
            emb = self.embedding_model(model_name="sentence-transformers/all-MiniLM-L6-v2")
            similar_chunk = Chroma(persist_directory=db_path,embedding_function=emb).similarity_search(query=query,k=K)
            return similar_chunk
        except :
            return False

