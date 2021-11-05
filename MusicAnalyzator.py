import json
from threading import Thread


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

        result = [None] * threads_num
        threads = [None] * threads_num

        for i in range(threads_num):
            threads[i] = Thread(target=find_summary_length, args=(values, result, i, threads_num))
            threads[i].start()

        for i in range(threads_num):
            threads[i].join()

        print(sum(result))


if __name__ == '__main__':
    main()
