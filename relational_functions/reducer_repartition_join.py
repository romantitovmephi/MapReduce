import sys


last_user_id = None
query_list = []
url_list = []

for line in sys.stdin:
    current_user_id = line.strip().split('\t')[0]
    info = line.strip().split('\t')[1] 
    if last_user_id != None and current_user_id != last_user_id: # при user1 -> user2 и тд
        for query in query_list:
            for url in url_list:
                print(f"{last_user_id}\t{query}\t{url}") # джоины для предыдущего юзера
        query_list.clear()    # чистим списки для нового юзера
        url_list.clear()
        if info.strip().split(':')[0] == 'query':
            query_list.append(info.strip().split(':')[1])
        else: 
            url_list.append(info.strip().split(':')[1])
    elif last_user_id == None or current_user_id == last_user_id:  # учитывая первую строку
        if info.strip().split(':')[0] == 'query':
            query_list.append(info.strip().split(':')[1])
        else: 
            url_list.append(info.strip().split(':')[1])
    last_user_id = current_user_id

if last_user_id: # учитывая последнюю строку при завершении ввода
    for query in query_list:
        for url in url_list:
            print(f"{last_user_id}\t{query}\t{url}")