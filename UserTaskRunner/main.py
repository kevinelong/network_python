"""
Interact with the user to select (one or more tasks). Display results (also progress?).
Apply a Task to a list of device IPs and log the result-details for each device the task is run on.

NOUNS (people, places, things) - Classes/Modules
VERBS (Action Words) - Functions/Methods on the classes
ADJECTIVES (Describe) - Attributes/Properties

NOUNS:
    USER, WAN W/R / LAN Read, UI(UserInterface), UserTask, Tasks (Child Tasks?), ResultList
    Device, , Logger, ResultDetail, App(Application)

VERBS:
    Interact, Select, Apply/Run, Log, Export, Import, Run

ADJECTIVE:
    Name
    IP Address
    AccessMode (Limited, Restricted)
    DeviceList

USER STORIES:
# STORY - NARATIVE
# USE CASE

# Create catalog item
# As a:       store manager
# I want to:  add catalog items
# So as to:   make them available for sale.

# Add item to inventory
# As a:       As a warehouse manage
# I want to:  Take an item into inventory
# So as to:   Track increasing inventory levels.

# Add item to cart.
# As a:       As a store customer
# I want to:  create a set of items
# So as to:   so i can pay once for many things to save time.


"""
from UserInterface import UserInterface
from WebInterface import WebInterface
from TaskRunner import Task, Device, DeviceList, ResultSet, TaskResult
import json
from flask import Flask, redirect, request, session, make_response


class Application:  # Model/Controller
    def __init__(self):
        self.device_lists = [
            DeviceList("Demo", [
                Device("demo", "127.0.0.1")
            ])
        ]
        self.user_tasks = [
            Task("ARP", "arp -a")
        ]
        self.user_interface = None

    @staticmethod
    def apply_task_to_list(task, device_list):
        # TODO create concurrent thread to send task command to all ips in the devicelist
        output = []
        for ip in device_list.device_list:
            print("running" + task.name)
            output.append(task.run(ip))
        return ResultSet(device_list, output)

    def import_list(self, file_path):
        pass

    def export_results(self):
        pass


app = Application()
# ui = UserInterface(app)
# ui.interact()

web = Flask(__name__)
web.secret_key = b'kevinelong'

style = f'\n<style>\n{open("style.css", "r").read()}\n</style>\n'


@web.route('/')
def index():
    return f"{style}" + open("index.html", "r").read()


@web.route('/data/')
def data():
    global app
    output = {
        "lists": [item.name for item in app.device_lists],
        "tasks": [item.name for item in app.user_tasks]
    }
    response = make_response(json.dumps(output, indent=4))
    response.headers['Content-Type'] = 'application/json'
    return response


@web.route('/run', methods=['POST'])
def run():
    tasks = request.form['tasks']
    lists = request.form['lists']
    results = app.apply_task_to_list(app.user_tasks[int(tasks)], app.device_lists[int(lists)])
    text = str(results)
    return text.replace("\n", "<br>")


web.run()
