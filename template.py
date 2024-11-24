import os
from pathlib import Path

list_file = [
    "app.py",
    "src/prompt.py",
    "src/document_process.py",
    "src/db.py",
    "src/pipeline.py",
    "src/chunking.py",
    ".gitignore",
    "Dockerfile",
    ".dockerignore",
    "api_app.py",

]


for file in list_file:
    file = Path(file)
    folder, filename = os.path.split(file)

    if folder != "":
        os.makedirs(folder, exist_ok=True)
    
    if (not os.path.exists(folder)) or (os.path.getsize(folder) == 0):
        with open(file,"w") as f:
            pass

