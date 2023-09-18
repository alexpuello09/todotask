from flask import Flask, request

task_list = [
{
        "title": "Task",
        "due": "Date",
        "assignee": "responsible",
        "description": "Description",
        "priority": "e.g., high, medium, low",
        "status": "e.g., pending, in-progress, completed"
}
]


app = Flask(__name__)

@app.get("/tasks")
def get_task():
    return task_list, 200

@app.post("/tasks")
def create_tasks():
    request_data = request.get_json()
    new_task = {
    "title": request_data["title"],
    "due": request_data["due"],
    "assignee": request_data["assignee"],
    "description": request_data["description"],
    "priority": request_data["priority"],
    "status": request_data["status"]
}
    task_list.append(new_task)
    return new_task, 201







