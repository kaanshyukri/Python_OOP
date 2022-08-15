from classes_and_objects.exercise.guild_system.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for name in self.tasks:
            if name.name == task_name:
                name.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        result = 0
        for task in self.tasks:
            if task.completed:
                result += 1
                self.tasks.remove(task)
        return f"Cleared {result} tasks."

    def view_section(self):
        result = f"Section {self.name}:"
        for task in self.tasks:
            result += "\n" + task.details()
        return result


