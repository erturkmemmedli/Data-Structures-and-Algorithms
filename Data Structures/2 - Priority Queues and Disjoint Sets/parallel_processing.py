from collections import namedtuple
import heapq

Process = namedtuple("Process", ["thread", "started_at"])

def parallel_process(thread, process_times):
    result = []
    my_heap = []
    heapq.heapify(my_heap)
    for i in range(len(process_times)):
        if i < thread:
            heapq.heappush(my_heap, (process_times[i], i))
            result.append(Process(i, 0))
        else:
            minimum = heapq.heappop(my_heap)
            heapq.heappush(my_heap, (minimum[0] + process_times[i], minimum[1]))
            result.append(Process(minimum[1], minimum[0]))
    return result

def main():
    thread, amount = map(int, input().split())
    process_times = list(map(int, input().split()))
    assert amount == len(process_times)

    parallel_processes = parallel_process(thread, process_times)

    for time in parallel_processes:
        print(time.thread, time.started_at)

if __name__ == "__main__":
    main()