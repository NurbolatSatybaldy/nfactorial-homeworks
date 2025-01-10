from fastapi import FastAPI
from math import factorial

app = FastAPI()

@app.get("/{num}")
def nfactorial(num: int):
    return {"nfactorial": factorial(num)}

