
from datetime import datetime, date
import time


def get_input(text, valid_options=None):

    while True:
        user_input = input(text).strip()

        if valid_options is None:
            return user_input
        
        if user_input in valid_options:
            print()
            return user_input
    
        print("Invalid selection choose Again\n")
      
    
        



def validate_input(text, valid_range):
    while True:
        try:
            user_input = int(get_input(text))
            print()
            if 1 <= user_input <= valid_range:
                return user_input
            
            print("Selection out of range\nChoose withing the specified range\n")
            
        except ValueError:
            print("Invalid Input\nEnter valid number")
            print()




def is_empty(tasks):
    if not tasks:
        print("Working...........")
        time.sleep(2)
        print("Task list is currently Empty\nSelect [1] in the main menu to add a task")
        return True
    return False



def priority_selection():

    print("""
            Select priority
            [1]. High       [2]. Medium 
            [3]. Low        [4]. Other
        """)

    priorities = {
            "1" : "high",
            "2": "medium",
            "3": "low",
            "4": "other"
        }
    user_input = get_input("Choose desired priority:   ", ["1", "2", "3", "4"])
    return priorities[user_input]


def get_date():
    while True:
        typed_input = input("Enter due date (DD/MM/YYYY) or press [Enter] to skip:    ").strip()
        if not typed_input:
            return None
        
        try:
            due_date = datetime.strptime(typed_input, "%d/%m/%Y").date()
            if due_date < date.today():
                print("Due Date can not be in the past\n")
                continue

            return due_date
        except ValueError:
            print("Invalid Date. Use the format: (DD/MM/YYYY)\n")


def date_calculator(due_date):
    if due_date is None:
        return "N/A"

    days_remain = (due_date - date.today()).days

    if days_remain < 0:
        days_overdue = abs(days_remain)
        unit = "day" if days_overdue == 1 else "days"
        return f"Overdue by {days_overdue} {unit}"
    
    elif days_remain == 0:
        return f"Due Today"
    else:
        unit = "day" if days_remain == 1 else "days"
        return f"{days_remain} {unit}"


def get_description(text=None):

    if text is None:
        text = "Enter task description:    "
    
    while True:
        description = get_input(text)
        description = " ".join(description.split())

        if not description:
            print("Description can not be empty: Enter some text\n")
            continue
        elif len(description) > 30 :
            print("Description must not exceed 30 characters\n")
            continue
        
        return description


def header_printer(text):

    print("=" * 115)
    padding = (115 - len(text)) // 2
    print(" " * padding + text)
    print("=" * 115)
    print()


def exit_application():
    print()
    print("Exiting" + "." * 10)
    time.sleep(1)
    print("write with Intent to Execute\nSee you soon")

