from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routes import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API", docs_url="/docs")

# CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks.router, prefix="/api/tasks", tags=["tasks"])

@app.get("/health")
def health_check():
    return {"status": "healthy"}
