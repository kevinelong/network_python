import json

from nornir.core.inventory import Host
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Task, Result

nr = InitNornir(config_file="config.yaml")

print(nr.inventory.hosts)
print(nr.inventory.groups)
print(nr.inventory.defaults.dict())

print(nr.filter(site="cmh", role="spine").inventory.hosts.keys())

print(json.dumps(Host.schema(), indent=4))


def hello_world(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} says hello world!"
    )


result = nr.run(task=hello_world)
print_result(result)


def say(task: Task, text: str) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} says {text}"
    )


result = nr.run(
    name="Saying goodbye in a very friendly manner",
    task=say,
    text="buhbye!"
)
print_result(result)