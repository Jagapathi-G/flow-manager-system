# Flow Manager System

A lightweight **Python-based workflow manager system** that executes tasks sequentially.  
Each task's result is evaluated against defined conditions to decide whether to proceed to the next task or terminate the flow early.

Perfect for building business logic flows, ETL pipelines with conditions, approval workflows, or any process that needs dynamic decision points.

## ✨ Features

- Sequential task execution
- Clean separation of concerns (tasks, flows, schemas, endpoints)
- Easy to extend with new tasks
- REST API endpoints (using FastAPI)
- Input/output schema validation
- Unit tests ready structure

## 🚀 Quick Start

1. Clone the repository

```bash
git clone https://github.com/Jagapathi-G/flow-manager-system.git
cd flow-manager-system
```

2. Install dependencies

```bash
pip install -r requirements.txt
```


3. Run the application

```bash
uvicorn main:app --reload
```

4. (Expected) Open your browser at:
- `http://127.0.0.1:8000/docs`. → Interactive API documentation (Swagger)

## Usage

### API Endpoint
- **Endpoint**: `POST /flow-manager/execute_flow`
- **Parameters**:
  - `flow` (json): json containing tasks and conditions
#### Example Request
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/flow-manager/execute_flow' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
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
}'
```

#### Example Response
```json
{
  "flow_id": "flow123",
  "response": true,
  "execution_log": [
    "Task 'task1' executed with result: True",
    "Task 'task2' executed with result: True",
    "Task 'task3' executed with result: True",
    "Flow completed."
  ]
}
```
### API Endpoint
- additional endpoint if flow is already stored and can be identified with flow_id. 
- **Endpoint**: `POST /flow-manager/execute_flow`
- **Parameters**:
  - `flow_id` (string): flow_id of the stored json 
#### Example Request
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/flow-manager/execute_flow_with_id?flow_id=flow123' \
  -H 'accept: application/json' \
  -d ''
```

#### Example Response
```json
{
  "flow_id": "flow123",
  "response": true,
  "execution_log": [
    "Task 'task1' executed with result: True",
    "Task 'task2' executed with result: True",
    "Task 'task3' executed with result: True",
    "Flow completed."
  ]
}
```


## 🛠️ Tech Stack

- Python 3.11
- FastAPI
- Pydantic (for data validation)
- pytest (for testing)

## 📌 To Do / Roadmap

- Implement flow persistence (database storage)
- Add retry mechanism & error handling policies
- Flow visualization

## 📄 License
MIT License
