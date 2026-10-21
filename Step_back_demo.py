tasks = [    
    {"id": 1, "title": "Learn Python", "completed": False}, 
    {"id": 2, "title": "Practice prompting", "completed": True}]

def find_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


def complete_task(task_id):
    task = find_task(task_id)
    if task is None:
        print(f"Error: Task with ID {task_id} not found")
        return False

    task["completed"] = True
    print(f"Task {task_id} completed successfully")
    return True


complete_task(99)

