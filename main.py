import json, os, time
from datetime import date
from utils import get_input, validate_input, is_empty, priority_selection, get_date, date_calculator, get_description, header_printer, exit_application


def main():
    tasks = load_task()
    last_id = (max(tasks.keys(), default=0))
    

    header_printer("TO DO LIST MANAGER")
    while True:
        print("""
        Select an action from the listed options

            1. Add task
            2. View tasks
            3. Mark task as Complete
            4. Edit task
            5. Delete task
            6. Filter tasks
            7. Exit
        """)
        action = get_input("Enter selected option:  ", ["1", "2", "3", "4", "5", "6", "7"])


        match action:
            case "1":
                last_id += 1
                add_task(tasks, last_id)
            case "2":
                view_tasks(tasks)
            case "3":
                mark_complete_task(tasks)
            case "4":
                edit_task(tasks)
            case "5":
               delete_task(tasks)
            case "6":
                filter_task(tasks)
            case "7":
                exit_application()
                break
        save_task(tasks)
        print()

        try_again_decision = get_input("Do you want to perform another action? [y / n]: ", ["y", "n"])
        if try_again_decision == "n":
            exit_application()
            break

        print("Returning to home page......")
        time.sleep(2)
        os.system("clear")


def add_task(tasks, last_id):
    header_printer("ADD TASK")
    description = get_description()
    print()
    priority = priority_selection() 
    due_date = get_date()

    tasks[last_id] = {
        "description" : description,
        "status" : "pending",
        "priority": priority,
        "due_date": due_date,
        "added_date": date.today()
    }
    print("Working................")
    time.sleep(2)
    print("Task successfully added")



def view_tasks(tasks):
    print()
    if is_empty(tasks):
        return

   
    serial_num = 1
    id_lookup = {}

    print("Loading............... \n")
    time.sleep(2)

    print(f"{'S/N':<3} | {'Added Date':<20} | {'Description':<30} | {'Priority':<20} | {'Status':<20} | {'Due Date':<15} | {'Days Remain':<15}")
    print(f"{'-' * 3} + {'-' * 20} + {'-' * 30} + {'-' * 20} + {'-' * 20} + {'-' * 15} + {'-' *12}")

    for task_id, task in tasks.items():
        days_to_due = date_calculator(task["due_date"])

        print(f"{serial_num:<3} | {str(task["added_date"]):<20} | {task['description']:<30} | {task['priority']:<20} | {task['status']:<20} | {str(task['due_date']):<15} | {days_to_due:<15}")
        id_lookup[serial_num] = task_id
        serial_num += 1
    return id_lookup




def  mark_complete_task(tasks):
    if is_empty(tasks):
        return

    header_printer("MARK TASK AS COMPLETE")
    task_id = id_mapper(tasks, "Enter S/N ID of task to be marked complete:   ")
    to_update = tasks[task_id]
    print("Status Updating in progress.......")
    time.sleep(2)
    to_update["status"] = "completed"
    print(f"[{to_update["description"]}] status has been marked completed")


def delete_task(tasks):
    if is_empty(tasks):
        return

    header_printer("DELETE TASK")
    task_id = id_mapper(tasks, "Enter S/N ID of the task to be deleted:    ")

    try_again_decision = get_input("Do you want to proceed 1. [yes]  2. [no]:    ", ["1", "2", "yes", "no"])
    if try_again_decision == "1" or try_again_decision == "yes":
        print("Deleting.............")
        time.sleep(1)
        print(f"[{tasks[task_id]["description"]}] has been successfully deleted")
        del tasks[task_id]
    else:
        print("Aborting.......")
        time.sleep(2)
        print("Task Deletion Aborted")
        return





def filter_task(tasks):
    if is_empty(tasks):
        return

    header_printer("FILTER TASK")
    pending_tasks = {key:value for key, value in tasks.items() if value["status"] == "pending"}
    completed_tasks = {key:value for key, value in tasks.items() if value["status"] == "completed"}

    print("""
        [1] pending task        [2] completed task
        [3] Priority
    """)
    user_input = get_input("Enter selected option:  ", ["1", "2", "3"])

    if user_input == "1":
        if not pending_tasks: 
            print("No pending task currently. All task are marked complete")
            return
        filtered_task = pending_tasks
    elif user_input == "2":
        if not completed_tasks:
            print("All task are currently pending")
            return
        filtered_task = completed_tasks
    
    else:
       filtered_task = filter_priority(tasks)
       if not filtered_task:
           print("working.......")
           time.sleep(2)
           print("Selected Priority task is Currently Empty\n")
           return
    view_tasks(filtered_task)
   


def edit_task(tasks):
    if is_empty(tasks):
        return

    header_printer("EDIT TASK")
    print("""
        [1]. Update description     [2]. Change Due Date
        [3]. Change Priority        [4].  Change Status
    """)

    user_input = get_input("Choose an action:   ", ["1", "2", "3", "4"])
    task_id = id_mapper(tasks, "Enter S/N number of the task to be updated: ")


    match user_input:
        case "1":
            updated_description = get_description("Enter new Description: ")
            print("Updating.......")
            time.sleep(2)
            tasks[task_id]["description"] = updated_description
            print(f"Description successfully changed to [{updated_description}]")

        case "2":
            due_date = get_date()
            print("Updating Due Date.............")
            time.sleep(2)
            tasks[task_id]["due_date"] = due_date
            print("Date successfully updated")

        case "3":
            priority = priority_selection()
            print("Updating priority...........")
            time.sleep(2)
            tasks[task_id]["priority"] = priority
            print(f"Priority has been succssfully changed to {priority}")

        case "4":
            print("Updating Status..........")
            time.sleep(2)
            if tasks[task_id]["status"] == "pending":
                tasks[task_id]["status"] = "completed"
                print("Status successfully updated from Pending to Completed")
            else:
                tasks[task_id]["status"] = "pending"
                print("Status successfully updated from Completed to Pending")
            


def load_task():
    tasks = {}
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            try: 
                saved_tasks = json.load(file) 
               
                for id, task in saved_tasks.items():
                    if task["due_date"] is not None:
                        task["due_date"] = date.fromisoformat(task["due_date"]) 

                    task["added_date"] = date.fromisoformat(task["added_date"])
                    tasks[int(id)] = task

            except json.JSONDecodeError:
                print("WARNING!!!\nFile exist but needed attention")

    return tasks



def save_task(tasks):
    task_to_save = {}

    for task_id, task in tasks.items():
        task_copy = task.copy()
        if task_copy["due_date"] is not None:
            task_copy["due_date"] = task_copy["due_date"].isoformat()
        task_copy["added_date"] = task_copy["added_date"].isoformat()
        task_to_save[task_id] = task_copy

    with open("tasks.json", "w") as file:
        json.dump(task_to_save, file, indent=4)



def id_mapper(tasks, text):

    id_lookup = view_tasks(tasks)
    print()
    user_input = validate_input(text, len(tasks))
    task_id = id_lookup[user_input]
    return task_id


def filter_priority(tasks):
   user_input = priority_selection()
   to_display_priority = {key:value for key, value in tasks.items() if value["priority"] == user_input}
   return to_display_priority
                



if __name__ == "__main__":
    main()

