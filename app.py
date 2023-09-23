from flask import Flask, request

task_list = [
{       
        "id": 1,
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
    request_info = request.get_json()
    new_task = {'id': len(task_list) +1, 
            "title": request_info["title"], 
            "due": request_info["due"], 
            "assignee": request_info["assignee"], 
            "description": request_info["description"], 
            "priority": request_info["priority"], 
            "status": request_info["status"]
}
    task_list.append(new_task)
    return new_task, 201

@app.route("/tasks/<int:task_id>",methods = ["PUT"])
def update_tasks(task_id):
    data = request.get_json()
    for task in task_list:
        if task["id"] == task_id:
            task["title"] = data["title"]
            task["due"] = data["due"]
            task["assignee"] = data["assignee"] 
            task["description"] = data["description"]
            task["priority"] = data["priority"]
            task["status"] = data["status"]
            return task
    return {f"Error: Task with id {task_id} not found"}


@app.route("/tasks/<int:task_id>",methods = ["DELETE"])
def delete_tasks(task_id):
    for task in task_list:
        if task["id"] == task_id:
            task_list.remove(task)
            return "Task Deleted"
    return 'Error: id not found'
    
            
            





    




