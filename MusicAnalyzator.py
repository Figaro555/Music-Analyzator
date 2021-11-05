import json
from multiprocessing import Process, Array


def find_summary_length(map_to_compute, result_arr, index, thread_n):
    start_index = round(len(map_to_compute) / thread_n * index)
    end_index = round(len(map_to_compute) / thread_n * (index + 1))
    el_sum = 0

    for key in list(map_to_compute.keys())[start_index: end_index]:
        el_sum = el_sum + map_to_compute[key]['meta']['track']['duration']
    result_arr[index] = el_sum


def main():
    with open("classical.json", "r", encoding="utf-8") as file:
        threads_num = 8

        values = json.load(file)

        shared_array = Array('d', threads_num)
        processes = [None] * threads_num

        for i in range(threads_num):
            processes[i] = Process(target=find_summary_length, args=(values, shared_array, i, threads_num))
            processes[i].start()

        for i in range(threads_num):
            processes[i].join()

        print(sum(shared_array))


if __name__ == '__main__':
    main()
