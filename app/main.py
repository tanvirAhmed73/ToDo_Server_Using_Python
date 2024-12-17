 from fastapi import FastAPI
from app.core.database import engine
from app.models.task import Base
from app.api.v1.endpoints.task import router as task_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="TODO API", version="1.0.0")

# Include routers
app.include_router(task_router, prefix="/api/v1", tags=["tasks"])