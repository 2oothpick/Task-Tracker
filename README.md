Task Tracker project from roadmap.sh

A simple CLI to track what you do, have done, and are currently working on

# Requirements
Application should run in the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file.
The user should be able to:
- Add, Update and Delete tasks
- Mark a task as in progress or done
- List all tasks
- Lists all tasks that are done
- lists all tasks that are not done
- List all tasks that are in progress

**Example**
The list of commands and their usage:

```
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress

```
