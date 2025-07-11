from fastapi import FastAPI

app=FastAPI()

@app.get("/Welcome")
async def root():
    return {"message":"Weclome to my Rag app ready for Production"}