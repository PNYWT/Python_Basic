import requests

url = "https://covid19.ddc.moph.go.th/api/Cases/today-cases-all"

#Case toDay
response=requests.get(url)
data=response.json()
print(data)

print("Date ::",data[0]['txn_date'])

for i in data:
    print("Date : ",i['txn_date'])
    print("New case : ",i['new_case'])
    print("Total case : ",i['total_case'])
    print("New case excludeabroad : ",i['new_case_excludeabroad'])
    print("Total case excludeabroad : ",i['total_case_excludeabroad'])
    print("New death : ",i['new_death'])
    print("Total death : ",i['total_death'])
    print("New recovered : ",i['new_recovered'])
    print("Total recovered : ",i['total_recovered'])
    print("Update date : ",i['update_date'])