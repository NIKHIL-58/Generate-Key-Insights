from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Generate Key Insights API", description="Extract insights from a long story")

# Register routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the Generate Key Insights API!"}
