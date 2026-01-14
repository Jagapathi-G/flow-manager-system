# Flow Manager System

A lightweight **Python-based Flow manager system** that executes tasks sequentially.  
Each task's result is evaluated against defined conditions to decide whether to proceed to the next task or terminate the flow early.

Perfect for building business logic flows, ETL pipelines with conditions, approval workflows, or any process that needs dynamic decision points.

## Flow Design & Execution Logic

The **Flow Manager System** is designed as a simple, lightweight, conditional workflow engine.  
It executes tasks in sequence while allowing branching based on task results.

### Core Concepts

| Concept             | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `start_task`        | Name of the first task to execute                                           |
| `tasks`             | List of all tasks that exist in this flow (name + metadata)                |
| `conditions`        | Rules that decide what happens **after** each task (success/failure path)  |
| `task_registry`     | Global dictionary that maps task names → actual executable functions       |
| `end`               | Special keyword that signals the flow has finished                         |

### How Tasks Depend on One Another

Tasks are **not** directly linked like in classic pipelines (task A → task B → task C).  
Instead, the next task is determined **dynamically** using **conditions**.

```text
Start
   ↓
Task A ──► [Condition] ──► Task B (if success)
   │                   └────► Task C (if failure)
   ▼
  "end"
```
- There is no fixed linear chain of tasks
- Every task can have zero or one condition attached
- If a task has no condition → flow ends after it (current_task = "end")
- If a task has a condition → next task is chosen based on result + desired outcome

  ### How Success/Failure is Evaluated
  Each task function must return a boolean value which says if the
  task execution is success or failure

  ### What Happens on Success / Failure
  On task success/failure next task is picked based on the condition's
  target_task_success/target_task_failure respectively and execution ends if no next task or end is mentioned. 
  

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
