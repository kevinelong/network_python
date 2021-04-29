from multiprocessing.pool import Pool


# Run many tasks against many devices


def run_many(device_list, task_list, pool_size=20):
    output = []
    with Pool(pool_size) as p:
        for task in task_list:
            task_results = p.imap_unordered(task, device_list)
            for result in task_results:
                output.append(result)
    return output


def func1(device):
    return "ran func1 on " + device


def func2(device):
    return "ran func2 on " + device


def func3(device):
    return "ran func2 on " + device


if __name__ == "__main__":
    results = run_many(
        [
            "127.0.0.1"
        ],
        [
            func1, func2, func3
        ]
    )
    print(results)
