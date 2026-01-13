import json

def show_list():
    with open("todos.json",'r') as f:
        data = json.load(f)

    sorted_tasks = sorted(data, key=lambda task: task["priority"])

    for task in sorted_tasks:
        print(task)

def add_task(title,date, priority):
    dict={"title":title,
          "date":date,
          "priority":priority,
          "done":False}
    
    with open("todos.json",'r')as f:
        data = json.load(f)

    data.append(dict)

    with open("todos.json",'w') as f:
        json.dump(data,f,indent=2)
    print("Task added successfully.")

def delete_task(taskname):
    with open("todos.json",'r') as f:
        data = json.load(f)
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
    with open("todos.json",'r') as f:
        data=json.load(f)
        found = False
        for task in data:
            if task["title"]==title:
                task["done"]=True
                found = True
                break
        if found==False:
            print("Task not found.")
    if found==True:
        with open("todos.json",'w') as f:
            json.dump(data,f,indent=2)
        print("Task marked as done.")
            