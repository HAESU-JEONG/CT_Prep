def solution(id_list, report, k):
    answer = [0]  * len(id_list)
    # make list to return
    # 'answer' list's purpose : save number of mail

    reports = {x : 0 for x in id_list} 
    # make dictionary
    # dictionary's key => name in id_list
    # dictionary's value => initialize to zero
    # 'reports' dictionary is to check how many times the person have been reported

    report = set(report) # remove duplicate values

    for record in report:
        reported_person = record.split()[1] # save the second of the two names
        reports[reported_person] += 1 # add 1 to the value with 'reported_person' as an index

    for record in report:
        report_person, reported_person = record.split()
        if reports[reported_person] >= k: # if the value is greater than the 'k'
            answer[id_list.index(report_person)] += 1
            # id_list.index(report_person) => find index report_person in id_list
            # add 1 to the answer's value 
    
    return answer
