from typing import List
from schemas.flow_models import Flow
from tasks.task_directory import task_registry


class FlowManager:
    def __init__(self, flow_data: Flow):
        self.flow_id = flow_data.id
        self.start_task = flow_data.start_task
        self.tasks = {task.name: task for task in flow_data.tasks}
        self.conditions = {cond.source_task: cond for cond in flow_data.conditions}
        self.execution_log: List[str] = []

    def execute(self) -> bool:
        current_task = self.start_task
        while current_task != "end":
            if current_task not in task_registry:
                self.execution_log.append(f"Error: Task '{current_task}' not defined.")
                return False
            task_result = task_registry[current_task]()
            self.execution_log.append(f"Task '{current_task}' executed with result: {task_result}")

            if current_task in self.conditions:
                condition = self.conditions[current_task]
                if task_result and condition.outcome == "success":
                    current_task = condition.target_task_success
                else:
                    current_task = condition.target_task_failure
            else:
                # No condition means end (or chain to next if more logic needed)
                current_task = "end"

        self.execution_log.append("Flow completed.")
        return True


def run_flow(flow):
    manager = FlowManager(flow)
    response = manager.execute()
    return {
        "flow_id": manager.flow_id,
        "response": response,
        "execution_log": manager.execution_log
    }