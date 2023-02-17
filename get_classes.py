import requests, json
from pprint import pprint
from dataclasses import dataclass

session = requests.Session()

termData = {'term': '202310'} # The server needs to know what term you want, this is hardcoded. otherwise, return is empty.
offset = 0 # Offset from the start. max requests is 200, increase by 200
requestSize = 200 # Maximum


#session.post('https://ssb9s.capilanou.ca:8443/StudentRegistrationSsb/ssb/term/search?mode=search', data=termData)

requestUrl = f"https://ssb9s.capilanou.ca:8443/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term={termData['term']}&startDatepicker=&endDatepicker=&pageOffset={offset}&pageMaxSize={requestSize}&sortColumn=subjectDescription&sortDirection=asc"

#data=json.loads(session.get(requestUrl).text)
with open('spring22_200_data', 'r') as f:
    data = json.loads(f.read())

@dataclass
class Room:
    roomname:str
    @classmethod
    def getClass(cls, data):
        section = data['meetingsFaculty'][0]['meetingTime']
        roomname = section['buildingDescription'] + section['room']
        return Room(roomname)

for i in data['data']:
    print(Room.getClass(i))
