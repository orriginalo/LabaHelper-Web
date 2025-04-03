import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import os
from utils.markdown_compiler import load_markdown_with_code
from rich import print

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Разрешаем только нужные домены
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все HTTP-методы
    allow_headers=["*"],  # Разрешаем все заголовки
)

def load_labs_data() -> dict:
    with open("data/data.json", encoding="utf-8") as file:
        return json.load(file)

@app.get("/")
def root():
    return {"hello" : "world"}

@app.get("/labs")
def get_all_labs():
    try:
        labs_data = load_labs_data()  # Загружаем labs_data
        
        labs = {"labs": []}
        labs_dirs = os.listdir("data\\Labs")
        labs_dirs.sort(key=lambda folder: int(folder[4:]))
        
        for file in labs_dirs:
            lab_number = file[4:]
            if lab_number in labs_data:
                lab_name = labs_data[lab_number]["name"]
            else:
                lab_name = f"Лабораторная работа {lab_number}"
            labs["labs"].append({
                "id": file,
                "name": lab_name,
                "markdown": load_markdown_with_code(lab_number)
            })

        return labs
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/lab/{lab_num}")
def get_lab(lab_num: str):
    try:
        return {"markdown": load_markdown_with_code(lab_num)}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=5000)
    uvicorn.run(app)