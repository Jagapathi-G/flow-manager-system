from typing import Dict

###
# Tasks 1, 2 & 3 are written as sample tasks,
# In production the task_functions redirect to actual tasks
###


def task1() -> bool:
    # Simulate fetching data
    print("Executing Task1: Fetch data")
    return True  # or False


def task2() -> bool:
    # Simulate processing data
    print("Executing Task2: Process data")
    return True  # or False


def task3() -> bool:
    # Simulate storing data
    print("Executing Task3: Store data")
    return True  # or False


# Map task names to functions
task_registry: Dict[str, callable] = {
    "task1": task1,
    "task2": task2,
    "task3": task3
    ## this registry can be extended
}