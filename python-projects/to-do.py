# To-Do List App
# │
# ├── User Interface (Console)
# │   ├── Display Menu
# │   │   ├── 1. Add Task
# │   │   ├── 2. View Tasks
# │   │   ├── 3. Mark Task as Done
# │   │   ├── 4. Delete Task
# │   │   └── 5. Exit
# │
# ├── Task Structure
# │   ├── Task ID
# │   ├── Title
# │   ├── Description (Optional)
# │   └── Status (Pending / Done)
# │
# ├── Core Functions
# │   ├── add_task()
# │   ├── view_tasks()
# │   ├── mark_done(task_id)
# │   ├── delete_task(task_id)
# │   └── save_tasks() / load_tasks()
# │
# ├── Data Storage
# │   ├── File Handling
# │   │   ├── tasks.json or tasks.txt
# │   │   ├── Load tasks at startup
# │   │   └── Save tasks on exit or after changes
# │
# └── Bonus Features (Optional)
#     ├── Due Dates
#     ├── Priority Tags (Low/Med/High)
#     ├── Sort/Filter by Status or Date
#     └── Simple GUI (Tkinter) or Web Interface (Flask)
task = {}
def add_task(hub_task):
    number_task = int(input("task number "))
    update_task = input("enter a task ")
    hub_task[number_task] = update_task
add_task(task)

def view_task():
    view = input("do you wanna view your tasks y/n ").lower()
    if view == "y":
        print(task)
view_task()

def mark_done():
    mark_task = int(input("enter the task to marked as done"))
    task[mark_task] = "done"
    print(task)
mark_done()

def delete_task():
    delete = int(input("enter the taksk which u want to delete"))
    del task[delete]
delete_task()

def changes_tasks():
    changes_in_tasks = input("are there any changes in the task").lower()
    if changes_in_tasks == "y":
        the_task = int(input("in which task do you have changes"))
        the_change = input("what is the change")
        task[the_task]=the_change
changes_tasks()