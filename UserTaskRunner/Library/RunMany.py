from multiprocessing.pool import Pool


# Run many tasks against many devices
def run_many(device_list, task_list, pool_size=20):
    output = []
    with Pool(pool_size) as p:
        for task in task_list:
            task_results = p.imap_unordered(task.run, device_list)
            for result in task_results:
                output.append(result)
    return output
