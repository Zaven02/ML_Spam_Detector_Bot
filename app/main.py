from fastapi import FastAPI
from app.model import spam_classifier
from app.schemas import TextRequest

# Initialize FastAPI
app = FastAPI()

@app.post("/predict/")
def predict(request: TextRequest):
    result = spam_classifier(request.text)
    return {"label": result[0]["label"], "score": result[0]["score"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)