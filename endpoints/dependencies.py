import json
from pathlib import Path
from fastapi import HTTPException

base_dir = Path(__file__).resolve().parent.parent
json_dir = base_dir/"flows"

## this is just one way of implementation,
# we could also load all the flows(jsons) in memory during service start
def get_flow_from_id(flow_id: str):
    path = json_dir / f"{flow_id}.json"
    if not path.exists():
        raise HTTPException(status_code=404, detail="Flow not found")

    flow = json.loads(path.read_text(encoding="utf-8"))
    return flow