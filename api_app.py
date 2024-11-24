from fastapi import FastAPI, File, UploadFile, HTTPException,Form
from fastapi.responses import JSONResponse
from src.pipeline import rag_pipeline,qa_pipeline
import os


app = FastAPI()

if not os.path.exists("data"):
    os.makedirs("data",exist_ok=True) 

def main_pipeline(filename,filepath,query):
    if not os.path.exists(os.path.join("vec_db",filename)):
        pipeline = rag_pipeline(db_path=os.path.join("vec_db",filename),filepath=filepath)
        llm_response = qa_pipeline(b_path=os.path.join("vec_db",filename),query=query)
        return llm_response
    
@app.get("/")
def home_page():
    return JSONResponse(content={"message": "Welcome to Custom document QA Pipeline"})

@app.post("/qa")
async def process_file(file:UploadFile = File(...),
                       query : str = Form(...)):
    try:
        save_file_path = os.path.join("data",file.filename)
        with open(save_file_path,"wb") as f:
            f.write(file.file.read())
        extension = os.path.splitext(file.filename)[-1]
        if extension not in [".pdf",".docx"]:
            raise HTTPException(
                status_code=400, detail="Unsupported file type. Upload a PDF or DOCX file."
            )

        response = main_pipeline(filename=file.filename,filepath=save_file_path)
        os.remove(save_file_path)
        return JSONResponse(content={"query": query, "response": response})


    except Exception as e:
        raise HTTPException (status_code=500,detail=str(e))




