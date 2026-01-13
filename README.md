# Flow Manager System

A lightweight **Python-based workflow orchestrator** that executes tasks sequentially with conditional branching.  
Each task's result is evaluated against defined conditions to decide whether to proceed to the next task or terminate the flow early.

Perfect for building business logic flows, ETL pipelines with conditions, approval workflows, or any process that needs dynamic decision points.

## ✨ Features

- Sequential task execution
- Conditional branching based on task results
- Clean separation of concerns (tasks, flows, schemas, endpoints)
- Easy to extend with new tasks
- REST API endpoints (using FastAPI – assumed from project structure)
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
- `http://127.0.0.1:8000`. → Interactive API documentation (Swagger)

## 🛠️ Tech Stack

- Python 3.11
- FastAPI
- Pydantic (for data validation)
- pytest (for testing)

## 📌 To Do / Roadmap

- Implement flow persistence (database storage)
- Add retry mechanism & error handling policies
- Flow visualization

## Fork the Project
- Create your Feature Branch (git checkout -b feature/amazing-feature)
- Commit your Changes (git commit -m 'Add some amazing feature')
- Push to the Branch (git push origin feature/amazing-feature)
- Open a Pull Request

## 📄 License
MIT License
