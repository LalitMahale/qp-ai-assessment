A powerful **Question-Answering (QA)** application that can process questions and extract answers from uploaded documents (`docx` and `pdf`) or directly from user queries. Choose between the interactive **Streamlit** interface or the developer-friendly **FastAPI** RESTful API.

### Problem Statement
[Problem statement](qp-ai-assessment\readme\README.md)



## How to Use

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or later
- pip (Python package manager)

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

---

### **Using Streamlit**

1. **Run the Streamlit App:**

   Use the following command to start the Streamlit server:
   ```bash
   streamlit run app_streamlit.py
   ```

2. **Access the Application:**

   Once the server starts, it will provide a URL (e.g., `http://localhost:8501`). Open this URL in your web browser to access the application.

3. **Upload Files or Ask Questions:**

   - Upload a `docx` or `pdf` file.
   - Type your question in the input box to get answers based on the uploaded document.

---

### **Using FastAPI**

1. **Run the FastAPI App:**

   Use the following command to start the FastAPI server:
   ```bash
   uvicorn app_fastapi:app --reload
   ```

2. **Access the API:**

   The FastAPI application will be available at `http://127.0.0.1:8000`.

3. **API Documentation:**

   FastAPI provides interactive API documentation:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

4. **Making API Requests:**

   #### Upload `docx` or `pdf` File for QA:
   Send a `POST` request with a file and question. Example using `curl`:
   ```bash
   curl -X POST "http://127.0.0.1:8000/qa-file" \
   -F "file=@path_to_your_file.pdf" \
   -F "question=Your question here"
   ```

   #### Ask a Question via Query:
   Send a `GET` request with a query string:
   ```bash
   curl -X GET "http://127.0.0.1:8000/qa-query?question=Your%20question%20here"
   ```

---

## API Endpoints

1. **File-based QA** (`POST /qa-file`):
   - **Description**: Accepts a `docx` or `pdf` file and answers the provided question.
   - **Request**:
     - Form Data: 
       - `file`: The uploaded document.
       - `question`: The question to be answered.
   - **Response**: JSON containing the answer to the question.

2. **Query-based QA** (`GET /qa-query`):
   - **Description**: Accepts a question and answers it based on pre-loaded or default data.
   - **Request**:
     - Query Parameter: `question` (the query string).
   - **Response**: JSON containing the answer.

---



## Feedback and Contributions
We welcome contributions! Feel free to open an issue or submit a pull request to enhance the functionality or fix bugs.

---

## License
MIT License

---
