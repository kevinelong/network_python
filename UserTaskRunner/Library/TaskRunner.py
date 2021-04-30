class Device:
    def __init__(self, ip, name=None):
        self.ip = ip
        self.name = name if name != None else str(ip)

    def __str__(self):
        return self.name + ":" + self.ip


class DeviceList:
    def __init__(self, name, device_list):
        self.name = name
        self.device_list = device_list

    def __str__(self):
        return f"Name: {self.name} ({len(self.device_list)})"


class User:
    pass


class Task:
    def __init__(self, name, command, expected_pattern=None):
        self.name = name
        self.command = command
        self.expected_pattern = expected_pattern
        self.subtasks = []  # child tasks?

    def run(self, device):
        # TODO run and also run subprocess tasks
        message = "Ran generic task."
        return TaskResult(self, device, message)

    def __str__(self):
        return self.name


class TaskResult:
    def __init__(self, task, device, message="success"):
        self.task = task
        self.device = device
        self.message = message

    def __str__(self):
        return self.task.name + " " + self.device.name + " " + self.message


class ResultSet:
    def __init__(self, device_list, result_list):
        self.device_list = device_list
        self.result_list = result_list

    def __str__(self):
        title = self.result_list[0].task.name
        MAX = 80
        remaining = MAX - len(title)
        padding = remaining // 2
        header = (padding * "=") + title + (padding * "=")
        lines = [str(item.device) + " " + item.message for item in self.result_list]
        return header + "\n" + "\n".join(lines)
