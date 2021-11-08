import json
from threading import Thread


def find_summary_length(map_to_compute, result_arr, index):
    el_sum = 0
    for key in map_to_compute:
        el_sum = el_sum + map_to_compute[key]['meta']['track']['duration']
    result_arr[index] = el_sum


def main():
    with open("classical.json", "r", encoding="utf-8") as file:
        threads_num = 8

        values = json.load(file)

        result = [None] * threads_num
        threads = [None] * threads_num

        sum_to_check = 0
        for key in values:
            sum_to_check = sum_to_check + values[key]['meta']['track']['duration']

        print(sum_to_check)

        for i in range(threads_num):
            start_index = round(len(values) / threads_num * i)
            end_index = round(len(values) / threads_num * (i + 1))
            d1 = dict(list(values.items())[start_index:end_index])

            threads[i] = Thread(target=find_summary_length, args=(d1, result, i))
            threads[i].start()

        for i in range(threads_num):
            threads[i].join()

        print(sum(result))


if __name__ == '__main__':
    main()
