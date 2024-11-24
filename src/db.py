from langchain.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

class Vectordb:

    def embedding_model(self,model_name:str):
        embedding_model = HuggingFaceEmbeddings(model_name = model_name)
        return embedding_model


    def store_vectors(self,chunks):
        emb = self.embedding_model(model_name="sentence-transformers/all-MiniLM-L6-v2")
        db = Chroma.from_documents(documents=chunks,
                                   embedding=emb,
                                   persist_directory = "emb_database/")
        return True


    def vector_retriever(self,query:str,db_path:str="emb_database/",K:int=3):
        emb = self.embedding_model(model_name="sentence-transformers/all-MiniLM-L6-v2")
        similar_chunk = Chroma(persist_directory=db_path,embedding_function=emb).similarity_search(query=query,k=K)
        return similar_chunk

