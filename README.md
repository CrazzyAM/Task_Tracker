# Task_Tracker

Task Tracker CLI created with Python

# How to Run the Project

## Prerequisites

Before running the project, ensure you have the following installed:

1. Python 3.x in Ubuntu
   
   ```sh
   sudo apt update
   sudo apt install python3
   ```
2. Python 3.x in Windows
    
    Download Python from [here](https://www.python.org/downloads/)

## Steps to Run the Project

1. **Clone the Repository**

   ```sh
   git clone https://github.com/CrazzyAM/Task_Tracker.git
   cd Task_tracker
   ```

2. **Usage**
   To add a task:
   python3 task.py add "Task description"

   To list all tasks:
   python3 task.py list-all

   To list all tasks that are done:
   python3 task.py list-done

   To list all tasks that are not done: 
   python3 task.py list-not-done

   To update the task
   python3 task.py update "id" "Task description"

   To delete the task
   python3 task.py delete "id"

   To Mark a task as in progress  
   python3 task.py mark-in-progress "id"

   To Mark a task as in done  
   python3 task.py mark-as-done "id"


4. **Additional Information**
   Ensure you are in the project directory before running the commands.
   "id" is the ID(integer) of the task you want to update or delete.

# Project URL:https://roadmap.sh/projects/task-tracker