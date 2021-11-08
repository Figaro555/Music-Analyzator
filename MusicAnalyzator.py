import json
from concurrent.futures import ThreadPoolExecutor


def find_summary_length(map_to_compute):
    el_sum = 0
    for key in map_to_compute:
        el_sum = el_sum + map_to_compute[key]['meta']['track']['duration']
    return el_sum


def main():
    with open("classical.json", "r", encoding="utf-8") as file, ThreadPoolExecutor() as executor:
        threads_num = 8

        values = json.load(file)

        features = [None] * threads_num

        sum_to_check = 0
        for key in values:
            sum_to_check = sum_to_check + values[key]['meta']['track']['duration']

        print(sum_to_check)

        total_length = 0

        for i in range(threads_num):
            start_index = round(len(values) / threads_num * i)
            end_index = round(len(values) / threads_num * (i + 1))
            dictionary_part = dict(list(values.items())[start_index:end_index])

            features[i] = executor.submit(find_summary_length, dictionary_part)

        for i in range(threads_num):
            total_length += features[i].result()

        print(total_length)


if __name__ == '__main__':
    main()
