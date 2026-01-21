import json

def show_list():
    try:
        with open("todos.json",'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File does not exists.")
        return
    except json.JSONDecodeError:
        print("file is corrupted.")
        return
    if not data:
        print("No tasks available.")
        return
    try:
        sorted_tasks = sorted(data, key=lambda task: task["priority"])
    except Exception as e:
        print("Error while sorting tasks: ",e)

    for task in sorted_tasks:
        print(task)


def add_task(title, date, priority):
    new_task = {
        "title": title,
        "date": date,
        "priority": priority,
        "done": False
    }

    try:
        with open("todos.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    except json.JSONDecodeError:
        print("Todo file is corrupted.")
        return

    for task in data:
        if task.get("title") == title:
            print("Task with this title already exists.")
            return

    data.append(new_task)

    with open("todos.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Task added successfully.")


def delete_task(taskname):
    try:
        with open("todos.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("No todo file found.")
        return
    except json.JSONDecodeError:
        print("Todo file is corrupted.")
        return
    
    found = False
    newdata=[]
    
    for task in data:
        if task['title']==taskname:
            found = True
            continue
        else:
            newdata.append(task)
    if found==False:
        print("Task not found.")
            
    if found == True:
        with open("todos.json",'w') as f:
            json.dump(newdata,f,indent=2)
        print("Task deleted successfully.")


def mark_done(title):
    try:
        with open("todos.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("No todo file found.")
        return
    except json.JSONDecodeError:
        print("Todo file is corrupted.")
        return
    found = False
    for task in data:
        if task["title"]==title:
            task["done"]=True
            found = True
            break
    if found==False:
        print("Task not found.")
        return
    if found==True:
        with open("todos.json",'w') as f:
            json.dump(data,f,indent=2)
        print("Task marked as done.")
            