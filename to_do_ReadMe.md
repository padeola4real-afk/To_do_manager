# TO DO LIST MANAGER

- A simple command-line To-Do List Manager built with python.
- This application helps users organize their daily tasks, set priorities, track due date and track both pending and competed task.

- The project is part of my Python backend development learning journey. It has helped me practise input validation, file handling, date calculations, JSON data storage, and automated testing.
  
  

## FEATURES

## Features

- **Add Tasks:** Create tasks with a description, priority, and optional due date.
- **View Tasks:** Display tasks in an organized table.
- **Mark Tasks as Complete:** Update a task's status when it is finished.
- **Edit Tasks:** Update task descriptions, priorities, and due dates.
- **Delete Tasks:** Remove tasks that are no longer needed.
- **Filter Tasks:** View tasks by status or priority.
- **Due Date Tracking:** Calculate the days remaining until a deadline and identify overdue tasks.
- **Input Validation:** Reject invalid menu selections, empty descriptions, and past due dates.
- **Automatic Data Saving:** Save task data to `tasks.json`.
- **Persistent Storage:** Load previously saved tasks when the application starts.
- **Exit:** Leave the application through the menu.


## TOOLS/REQUIREMENTS

- Python 3
- Linux or macOS is recommended.

The application uses Python's standard library and does not require
third-party packages.

Some of the standard-library modules used include:

- `json` — reading and writing task data.
- `os` — interacting with the operating system.
- `datetime` — handling dates and calculating deadlines.
- `time` — controlling delays where needed to simulate interaction.
- `unittest` — running automated tests.
- `unittest.mock` — mocking input and capturing output during tests.

The application uses `os.system("clear")` to clear the terminal.
On Windows, this may need to be changed to use `cls` instead.

## RUN THE APPLICATION

```python3 main.py``` or ```python main.py```

## RUN UNITTEST

```python -m unittest -v test_utils.py```

- The file tasks.json is automatically created the first time you use the app and read automatically on startup as empty file. If the file is missing, the app starts with an empty list. If it contains invalid JSON, the app prints a warning and starts with an empty list; the next save then replaces the damaged file.

## USAGE

- Main menu looks like this:

```
===================================================================================================================
                                                 TO DO LIST MANAGER                                                
===================================================================================================================


        Select an action from the listed options

            1. Add task
            2. View tasks
            3. Mark task as Complete
            4. Edit task
            5. Delete task
            6. Filter tasks
            7. Exit

    Enter selected option:   
```

Choose an option by entering its corresponding number.

After completing an action, the application asks whether you want
to continue.

- Enter `y` to return to the main menu.
- Enter `n` to exit the application.

The terminal screen is cleared between actions, and task data is
saved automatically after each relevant change.


## VIEWING TASK

|S/N | Description                    | Priority             | Status               | Due Date        | Days Remain|
|--- | ------------------------------ | -------------------- | -------------------- | --------------- | -----------|
|1   | Buy groceries                  | high                 | pending              | 2026-10-25      | 5 day      |
|2   | Pay rent                       | medium               | pending              | None            | N/A        |

- The S/N number is how you pick a task for completing, editing or deleting. The list is shown again at that moment, so the number you choose always matches what is on screen.


## INPUT RULES

| Field |	Rule |
|-----| -----|
Description	   | Required, up to 30 characters; leading and trailing spaces are trimmed|
Priority	   | Chosen from a menu: high, medium, low or other|
Due date	   | Typed as `DD/MM/YYYY`, or press Enter to skip; dates in the past are rejected|
Task selection | The S/N number shown in the table, which must be within the listed range|

## TASK DATA STRUCTURE

| Field	     | Value |
|----        | ----  |
|description | Task text, up to 30 characters|
|status	     | "pending" or "completed"|
|priority    | "high", "medium", "low" or "other"|
|due_date    | "YYYY-MM-DD" text, or null when no due date was set|
|added_date  | The date the task was created, as "YYYY-MM-DD" text|

## DATA STORAGE

- Tasks are stored in `tasks.json` in project folder as object keyed by task_ID
```
    {
        "1": {
            "description": "buy Broceries",
            "status": "pending",
            "priority": "medium",
            "due_date": "2026-10-20",
            "added_date": "2026-10-20"
        },

        "3": {
        "description": "Pay rent",
        "status": "completed",
        "priority": "medium",
        "due_date": null,
        "added_date": "2026-10-20"
        }

    }   
```
## PROJECT STRUCTURE

File              | Responsibility
|----             | ----|
|`main.py`	      | The menu loop, the task operations and loading and saving|
|`utils.py`       | Shared helpers for input, validation and dates|
|`tasks.json`     | Stores saved tasks data and is created automatically when needed|
|`test_utils.py`  | Contains automated test for utils function|
|`to_do_readMe.md`| Documents the project, its feature and how to run it|


## DESIGNS NOTE

### Task IDs

Tasks are stored in a dictionary of dictionaries, with each task
identified by a unique ID.

Task IDs remain stable throughout a task's lifetime. When a task is
deleted, its ID is not reused, so gaps may appear in the IDs.

The application displays S/N numbers separately from the actual task
IDs. Whenever tasks are displayed, the application generates fresh
sequential numbers starting from 1. This keeps the displayed numbering
consistent even when some task IDs are missing.

### Date Handling

JSON does not directly support Python `date` objects. Therefore,
dates are converted to strings when saving tasks and converted back
to Python `date` objects when loading them.

### Days Remaining

The number of days remaining is calculated when a task is displayed
rather than stored in the JSON file. This ensures the countdown
reflects the current date.

### Optional Due Dates

Tasks without a due date store `null` in the JSON file. The `due_date`
key remains present, allowing the application to distinguish between
a task with no due date and one with an assigned due date.

## POSSIBLE IMPROVEMENTS

- Search tasks by keyword instead of scanning the whole table
- Combine filters, such as pending tasks with high priority
- Sort tasks by due date and highlight overdue ones
- Keep a backup of a corrupted `tasks.json` instead of replacing it
- Make screen clearing work on Windows