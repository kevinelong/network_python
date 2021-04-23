
class UserInterface:  # also controller?
    def __init__(self, app):
        self.app = app
        self.selected_task = None
        self.selected_list = None

    def show_options(self):
        print("OPTIONS:")
        for index, item in enumerate(self.app.device_lists, 1):
            print(index, item)
        for index, task in enumerate(self.app.user_tasks, 1):
            print(index, task)

    def interact(self):
        while True:
            self.show_options()

            list_number = input("Enter list number:")
            self.selected_list = self.app.device_lists[int(list_number) - 1]
            print(self.selected_list.name + " is selected.")

            task_number = input("Enter task number:")
            self.selected_task = self.app.user_tasks[int(task_number) - 1]
            print(self.selected_task.name + " is selected.")

            confirm = input("Enter 'run' to execute, 'q' to quit, or any other value to re-make selections:")
            if confirm == "run":
                results = self.app.apply_task_to_list(self.selected_task, self.selected_list)
                print(results)
            elif confirm == "q":
                break  # break out of forever loop and exit
            else:
                print("aborting run, re-make-selections")
