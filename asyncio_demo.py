# https://realpython.com/python-concurrency/
"""
Concurrency does not imply "true" parallelism.
Threads and Async IO are forms of concurrency by are not "true" parallelism.
At this time only python Multiprocessing is true parallelism.
which is best depends on if you are io bound, cpu bound, and if extra setup especially of pool

“Use async IO when you can; use threading when you must.” + Use multiprocessing if its worth it.

ASYNC IO is the newest to python Coming in at Version 3.7
"""

# BASE SYNCHRONOUS VERSION
import time


def count():
    print("One")
    time.sleep(1)
    print("Two")


def main():
    for _ in range(3):
        count()


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

# ASYNC IO VERSION

import asyncio


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    import time

    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
