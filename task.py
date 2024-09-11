import sys
import json
import os

TASKS_FILE = "tasks.json"

def get_data_dump():
    with open(TASKS_FILE, "r") as f:
        data = json.load(f)
        f.close()
        return data

def validate_exist_jsonfile():
    if os.path.exists(TASKS_FILE):
        return True
    else:
        return False

def get_json_data(last_id):
    return {
        "ID": last_id + 1,
        "tasks_name": sys.argv[2],
        "Status": "Yet to start",
    }

def get_id():
    with open(TASKS_FILE, "r") as f:
        data = json.load(f)
        f.close()
        print(data)
        return data[-1]["ID"]

def first_element():
    last_id = 0
    data = []
    data.append(get_json_data(last_id))
    with open(TASKS_FILE, "w") as f:
        json.dump(data, f, indent = 4 )
        f.close()
        print(f"Task added successfully to {TASKS_FILE}")
        sys.exit(0)

def add():
    if validate_exist_jsonfile():
        with open(TASKS_FILE, "r") as f:
            try:
                data = json.load(f)
                f.close()
                last_id = get_id()
                data.append(get_json_data(last_id))
                with open(TASKS_FILE, "w") as f:
                    json.dump(data, f, indent = 4 )
                    f.close()
                    print(f"Task added successfully to {TASKS_FILE}")    
                    sys.exit(0)
            except json.decoder.JSONDecodeError:
                first_element()
            
    else:
        first_element()

def delete():
    try:
        data = get_data_dump()
        for i in range(len(data)):
            if data[i]["ID"] == int(sys.argv[2]):
                data.pop(i)
                with open(TASKS_FILE, "w") as f:
                    json.dump(data, f, indent = 4)
                    f.close()
                print("Task deleted successfully")
                sys.exit(0)
        print("Task not found")
    except json.decoder.JSONDecodeError:
        print("The list of tasks is empty")

def update():
    try:
        data = get_data_dump()
        for i in range(len(data)):
            if data[i]["ID"] == int(sys.argv[2]):
                data[i]["tasks_name"] = sys.argv[3]
                with open(TASKS_FILE, "w") as f:
                    json.dump(data, f, indent = 4)
                    f.close()
                print("Task updated successfully")
                sys.exit(0)
        print("Task not found")
    except json.decoder.JSONDecodeError:
        print("The list of tasks is empty")

def mark_as_done():
    try:
        data =  get_data_dump()
        for i in range(len(data)):
            if data[i]["ID"] == int(sys.argv[2]):
                data[i]["Status"] = "Done"
                with open(TASKS_FILE, "w") as f:
                    json.dump(data, f, indent = 4)
                    f.close()
                print("Task marked as done successfully - ID: ", data[i]["ID"])
                sys.exit(0)
        print("Task not found")
    except json.decoder.JSONDecodeError:
        print("The list of tasks is empty")

def mark_in_progress():
    try:
        data =  get_data_dump()
        for i in range(len(data)):
            if data[i]["ID"] == int(sys.argv[2]):
                data[i]["Status"] = "In Progress"
                with open(TASKS_FILE, "w") as f:
                    json.dump(data, f, indent = 4)
                    f.close()
                print("Task marked as in progress successfully - ID: ", data[i]["ID"])
                sys.exit(0)
        print("Task not found")
    except json.decoder.JSONDecodeError:
        print("The list of tasks is empty")

def list_all():
    try:
        data = get_data_dump()
        for i in range(len(data)):
            print(f"ID: {data[i]['ID']},\t Name: {data[i]['tasks_name']},\t Status: {data[i]['Status']}")
    except json.decoder.JSONDecodeError:
        print("The list of tasks is empty")
    
def list_done():
    try:
        data = get_data_dump()
        for i in range(len(data)):
            if data[i]["Status"] == "Done":
                print(f"ID: {data[i]['ID']},\t Name: {data[i]['tasks_name']},\t Status: {data[i]['Status']}")
    except json.decoder.JSONDecodeError:
        print("The list of tasks is empty")

def list_not_done():
    try:
        data = get_data_dump()
        for i in range(len(data)):
            if data[i]["Status"] != "Done":
                print(f"ID: {data[i]['ID']},\t Name: {data[i]['tasks_name']},\t Status: {data[i]['Status']}")
    except json.decoder.JSONDecodeError:    
        print("The list of tasks is empty")

def main():

    if len(sys.argv) == 1:
        print("Please enter a valid option")
        sys.exit(1)
    
    match sys.argv[1]:
        case "add":
            add()
        case "delete":
            delete()
        case "update":
            update()
        case "mark-as-done":
            mark_as_done()
        case "mark-in-progress":
            mark_in_progress()
        case "list-all":
            list_all()
        case "list-done":
            list_done()
        case "list-not-done":
            list_not_done()
        case _:
            print("Please enter a valid option")
            sys.exit(1)

if __name__ == "__main__":
    main()