import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from main import app
from endpoints.dependencies import get_flow_from_id

client = TestClient(app)

SAMPLE_FLOW = {
   "flow":{
      "id":"flow123",
      "name":"Data processing flow",
      "start_task":"task1",
      "tasks":[
         {
            "name":"task1",
            "description":"Fetch data"
         },
         {
            "name":"task2",
            "description":"Process data"
         },
         {
            "name":"task3",
            "description":"Store data"
         }
      ],
      "conditions":[
         {
            "name":"condition_task1_result",
            "description":"Evaluate the result of task1. If successful, proceed to task2; otherwise, end the flow.",
            "source_task":"task1",
            "outcome":"success",
            "target_task_success":"task2",
            "target_task_failure":"end"
         },
         {
            "name":"condition_task2_result",
            "description":"Evaluate the result of task2. If successful, proceed to task3; otherwise, end the flow.",
            "source_task":"task2",
            "outcome":"success",
            "target_task_success":"task3",
            "target_task_failure":"end"
         }
      ]
   }
}

SAMPLE_FLOW_ID = {"flow_id": "flow123"}

def mock_get_flow_from_id(flow_id: str):
    return SAMPLE_FLOW

app.dependency_overrides[get_flow_from_id] = mock_get_flow_from_id

def test_execute_flow():
    response = client.post("/flow-manager/execute_flow", json=SAMPLE_FLOW)

    assert response.status_code == 201
    assert response.json()["response"] == True

def test_execute_flow_with_id():
    response = client.post("/flow-manager/execute_flow_with_id", params=SAMPLE_FLOW_ID)

    assert response.status_code == 201
    assert response.json()["response"] == True
