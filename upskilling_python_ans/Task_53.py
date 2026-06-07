"""
Task Scheduler
• Objective: Use classes, the datetime module, lists, and sorting to manage tasks.
• Task: Create a task scheduler that prioritizes tasks by due date and identifies overdue
tasks.
"""
from datetime import datetime

class Task:

    def __init__(self, name, due_date):

        self.name = name

        self.due_date = datetime.strptime(
            due_date,
            "%Y-%m-%d"
        )

    def is_overdue(self):

        return self.due_date < datetime.today()


tasks = [

    Task("Python Training", "2026-06-10"),

    Task("Project Report", "2026-06-05"),

    Task("Team Meeting", "2026-06-03")
]

tasks.sort(
    key=lambda task: task.due_date
)

print("Task Schedule")

for task in tasks:

    status = "Overdue" if task.is_overdue() else "Pending"

    print(
        task.name,
        "-",
        task.due_date.date(),
        "-",
        status
    )