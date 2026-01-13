from fastapi import APIRouter, HTTPException, Depends
from schemas.flow_models import FlowRequest
from service.flow_manager import run_flow
from endpoints.dependencies import get_flow_from_id


flow_router = APIRouter(prefix="/flow-manager")


@flow_router.post("/execute_flow", status_code=201)
async def execute_flow(request: FlowRequest):
    return run_flow(request.flow)


# if flow is already being stored and can be called using id
@flow_router.post("/execute_flow_with_id", status_code=201)
async def execute_flow_with_id(request: dict = Depends(get_flow_from_id)):
    flow_payload = FlowRequest.model_validate(request)
    return run_flow(flow_payload.flow)

