'''
curl 'https://ssb9s.capilanou.ca:8443/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term=202310&startDatepicker=&endDatepicker=&uniqueSessionId=6ublv1675196575054&pageOffset=0&pageMaxSize=10&sortColumn=subjectDescription&sortDirection=asc' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'Accept-Language: en-GB,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: JSESSIONID=EDF898FFEBA2F6E91E9F74065191DD28; BIGipServerSBS9S.app~SBS9S_pool=1862276268.64288.0000' \
  -H 'Referer: https://ssb9s.capilanou.ca:8443/StudentRegistrationSsb/ssb/classSearch/classSearch' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'X-Synchronizer-Token: 75d5b767-85d9-448e-9851-3b736e83c0b1' \
  -H 'sec-ch-ua: "Chromium";v="109", "Not_A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
'''

import requests, json
from pprint import pprint


headers = {
    'Cookie' : 'JSESSIONID=EDF898FFEBA2F6E91E9F74065191DD28; BIGipServerSBS9S.app~SBS9S_pool=1862276268.64288.0000',
    'Referer' : 'https://ssb9s.capilanou.ca:8443/StudentRegistrationSsb/ssb/classSearch/classSearch',
    'X-Synchronizer-Token' : '75d5b767-85d9-448e-9851-3b736e83c0b1'
}

url = 'https://ssb9s.capilanou.ca:8443/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term=202310&startDatepicker=&endDatepicker=&uniqueSessionId=6ublv1675196575054&pageOffset=0&pageMaxSize=40&sortColumn=subjectDescription&sortDirection=asc'

response = requests.request("GET", url, headers=headers)
data = json.loads(response.text)


for i in data['data']:
    for z in i['meetingsFaculty']:
        print(z['meetingTime']['campus'], z['meetingTime']['buildingDescription'] ,z['meetingTime']['room'], z['meetingTime']['tuesday'], 'Times:', z['meetingTime']['beginTime'], z['meetingTime']['endTime'])
