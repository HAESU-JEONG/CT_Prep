def solution(id_list, report, k):
    answer = []
    report_list = []
    stop_list = []
    good_list = []
    
    report = set(report)
    report = list(report)

    for i in range(len(report)):
        tmp = report[i].split(" ")
        report_list.append(tmp[1])
    
    for i in range(len(id_list)):
        if report_list.count(id_list[i]) >= k:
            stop_list.append(id_list[i])
    
    for i in range(len(report)):
        tmp = report[i].split(" ")
        if stop_list.count(tmp[1]) == 1:
            good_list.append(tmp[0])
    
    for i in range(len(id_list)):
        answer.append(good_list.count(id_list[i]))
        
    return answer