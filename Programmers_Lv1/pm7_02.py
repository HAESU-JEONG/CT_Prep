def solution(id_list, report, k):
    report_dict = dict()  # id of reports
    report_count_dict = dict()  # number of reports
    ban_id = []
    answer = []

    for i in range(len(id_list)):
        report_dict[id_list[i]] = []  # Create a dictionary by ID
        report_count_dict[id_list[i]] = 0

    for i in range(0, len(report)):
        report_list = report[i].split()
        report_dict[report_list[0]].append(report_list[1])

    for i in report_dict.keys():
        # List cannot be duplicated
        report_dict[i] = list(set(report_dict[i]))
        for j in report_dict.values():
            if i in j:
                report_count_dict[i] += 1

    # Find ban id
    for i in report_count_dict.keys():
        if report_count_dict[i] >= k:
            ban_id.append(i)

    temp = 0

    for i in report_dict.keys():
        for j in ban_id:
            if j in report_dict[i]:
                temp += 1
        answer.append(temp)
        temp = 0

    return answer
