# https://yenthaptam.streamlit.app/
# https://github.com/tuoitho/dkmh_hcmute
import time

import requests

mamon = 'ENGL130137_03'
url = "https://dangkyapi.hcmute.edu.vn/api/Regist/RegistScheduleStudyUnit?TurnID=45&Action=REGIST&StudyProgramID=22110"
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6ImFkbWluIiwibmJmIjoxNjM0NjYwNjIwLCJleHAiOjE2MzQ2NjA2MjAsImlhdCI6MTYzNDY2MDYyMCwiaXNzIjoiQ2FwaXRhbCBTZXJ2aWNlIFNlcnZpY2VzIiwiYXVkIjoiQ2FwaXRhbCBTZXJ2aWNlIFNlc232323nZpY2VzIn0.1'
headers = {
    "authorization": "Bearer "+token,
}
arr = ['ENGL130137_03', 'LLCT220514_03']
while True:
    for mamon in arr:
        body = [
            {
                "CurriculumID": "233"+mamon,
                # may cai o duoi k can quan tam, chi can CurriculumID de dang ky, chuyen nhom moi can
                "ScheduleStudyUnitAlias": "PHED130715_17",
                "CurriculumName": "Anh Văn 1",
                "StudyUnitID": "233PHED130715",
                "TypeName": "Lý thuyết",
                "Credits": 3,
                "StudentQuotas": "10-50",
                "StudyUnitTypeID": 1,
                "MaxStudentNumber": 50,
                "NumberOfStudents": 21,
                "Schedules": " Thứ",
                "ProfessorName": " Nguyễn Thị Ngọc Hà",
                "IsRegisted": False,
                "ListOfClassStudentID": "",
                "NumberOfChilds": 0,
                "FeeDebt": "",
                "ParentID": "",
                "UpdateDate": "06/12/2024 09:22:40",
                "NumberRegistOfEmpty": 29,
                "IsHocTrucTuyen": "",
                "isOpen": True,
                "isOpenChilrentTask": False
            }
        ]
        response = requests.post(url, headers=headers, json=body)
        print(response.text)
        print(time.ctime())
        try:
            if not response.text[0] == '{':
                break
        except:
            print("token het han")
        time.sleep(1)
