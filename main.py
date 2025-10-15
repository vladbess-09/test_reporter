import csv
import argparse
from tabulate import tabulate


def init_argpars():
    params = argparse.ArgumentParser()
    params.add_argument('--files', type=str, nargs="+", help='dir for files')
    params.add_argument("--report", type=str, help="name of report")
    return params.parse_args()


def read_file(path_to_file_list):
    list_of_value = []
    list_of_title = ['name', 'brand', 'price', 'rating']
    list_of_value.append(list_of_title)
    for i in path_to_file_list:
        with open(i) as f:
            reader = csv.reader(f)
            for row in reader:
                if row != list_of_title:
                    list_of_value.append(row)

    return list_of_value


def average_rating(list_of_val):
    report_list = []
    count = 0
    for i in list_of_val:
        report_list.append([i[0], i[-1]])

    report_list.sort(key=lambda row: row[1], reverse=True)
    for i in report_list:
        report_list[count].insert(0, count)
        count += 1
    return report_list


def select_report(flag_for_report, list_of_val):
    if flag_for_report == "average-rating":
        return average_rating(list_of_val)
    else:
        print("not valide name for report")
        raise SystemExit(1)


if __name__ == "__main__":
    args = init_argpars()
    list_of_val = read_file(args.files)
    ans = select_report(args.report, list_of_val)
    print(tabulate(ans[1:], headers=ans[0]))

