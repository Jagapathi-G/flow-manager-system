from pydantic import BaseModel
from typing import List


# Pydantic models for JSON validation
class Task(BaseModel):
    name: str
    description: str


class Condition(BaseModel):
    name: str
    description: str
    source_task: str
    outcome: str
    target_task_success: str
    target_task_failure: str


class Flow(BaseModel):
    id: str
    name: str
    start_task: str
    tasks: List[Task]
    conditions: List[Condition]


class FlowRequest(BaseModel):
    flow: Flow


class FlowExecutionResponse(BaseModel):
    flow_id: str
    response: bool
    execution_log: List[str]