import requests, json
from pprint import pprint
from dataclasses import dataclass

session = requests.Session()

termData = {'term': '202310'} # The server needs to know what term you want, this is hardcoded. otherwise, return is empty.
offset = 0 # Offset from the start. max requests is 200, increase by 200
requestSize = 200 # Maximum


session.post('https://ssb9s.capilanou.ca:8443/StudentRegistrationSsb/ssb/term/search?mode=search', data=termData)

requestUrl = f"https://ssb9s.capilanou.ca:8443/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term={termData['term']}&startDatepicker=&endDatepicker=&pageOffset={offset}&pageMaxSize={requestSize}&sortColumn=subjectDescription&sortDirection=asc"

data=json.loads(session.get(requestUrl).text)['data']
#with open('spring22_200_data', 'r') as f:
#    data = json.loads(f.read())['data']
'''
 Valid classes are those without an empty "meetingsFaculty" and not a "None" building in the meetingTime dictionary.
 "meetingsFaculty" is an array. some classes are both online and in person. or have lab/lecture



 For graphing the schedule for one day of the week, we need the room numbers and begin, end times.

 For the class of dow. It needs to have the roomname, begintime, endtime.


 CREATE A SET OF CLASS NAMES AND THEN GATHER THEM LIKE THAT
'''
@dataclass
class Monday:
    roomname:str
    begintime: int
    endtime: int
    # test
    index: int
    # test

    @classmethod
    def room(cls, data, num):
        roomname = data['buildingDescription'] + data['room']
        begintime = data['beginTime']
        endtime = data['endTime']
        #test
        index = num
        #test

        return Monday(roomname, begintime, endtime, index)

def roomSearch(data):
    c = 0
    monday = []
    for i in data:
    #    print(c)
        if (len(i['meetingsFaculty']) != 0) and (len([e for e in [d for d in i['meetingsFaculty']]]) != 0):
            for f in i['meetingsFaculty']:
                if (f['meetingTime']['building'] != None) and (f['meetingTime']['building'] != "ON") :
                    section = f['meetingTime']
                    roomname = (section['buildingDescription'] + section['room'])
    #                print(roomname)
                    if section['monday'] == True:
                        monday.append(Monday.room(section, c))
    
    
    
        c += 1
    print(monday)
    return monday
    #for i in monday:
    #    print(i.roomname, i.begintime, i.endtime, i.index)
roomSearch(data)
#for i in range(15):
#    requestUrl = f"https://ssb9s.capilanou.ca:8443/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term={termData['term']}&startDatepicker=&endDatepicker=&pageOffset={offset}&pageMaxSize={requestSize}&sortColumn=subjectDescription&sortDirection=asc"
#    data=json.loads(session.get(requestUrl).text)['data']
#    roomSearch(data)
#    offset += 200
