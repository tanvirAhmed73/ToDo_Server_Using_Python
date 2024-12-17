 from pydantic import BaseModel, ConfigDict

class TaskBase(BaseModel):
    title: str
    description: str
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class TaskResponse(BaseModel):
    message: str