from fastapi import FastAPI
app = FastAPI(title="Creator-AI")

@app.get("/") 
def root(): 
    return {"message": "Creator-AI is running!"}
