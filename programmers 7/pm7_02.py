from collections import Counter

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo" ,"frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):
    answer = []
    stop_id=[]
    reported_people = []
    dic_id = {}
    tmp = 0

    #중복 제거 = 한 사람이 같은 사람을 여러번 신고한 경우 제거
    report = list(set(report)) 

    #id 딕셔너리에 저장 후 value값으로 리스트 설정
    for i in id_list:
        dic_id[i] = [] #누가 누굴 신고했는지 저장 

    #report 분리 -> 딕셔너리의 키값이 rp1인 경우에 value값에 rp2를 추가한다.(리스트라서 가능)
    for i in report :
        rp1, rp2 = "".join(i).split()
        dic_id[rp1].append(rp2)
        reported_people.append(rp2)
     
    # reported_people리스트에서 같은 값을 count해서 , 딕셔너리에 넣는다. 
    dic_report = Counter(reported_people) #몇번 신고당했는지 세고 저장

    #dic_report에서 만약 value값이 k 이상이면 stop_id 리스트에 추가
    for i in dic_report:
        if int(dic_report.get(i)) >= k:
            stop_id.append(i)
        
    #stop_id가 dic_id의 value값에 있다면 tmp를 하나 늘려 본인이 신고넣은 사람 중 몇명이 차단먹었는지 통보 가능하게    
    for i in dic_id.values():
        for j in stop_id:
            if j in i:
                tmp += 1
        answer.append(tmp)
        tmp = 0
    
    return(answer)
    #print(answer)
    
solution(id_list, report, k)