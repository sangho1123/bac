import json
from urllib.request import urlopen
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 사용을 위해서 세팅
font_path = "C:/Windows/Fonts/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# URL을 통해 JSON 데이터 가져오기
url = "https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=MjhlYTcwNWU0MGU5NTYwMjRiNWI1M2I2MWNmODdiZmI=&itmId=13103114424T1+13103114424T2+&objL1=13102114424A.0001+13102114424A.0002+13102114424A.0010+13102114424A.0013+13102114424A.0014+&objL2=13102114424B.0003+13102114424B.0004+&objL3=&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=Y&newEstPrdCnt=5&orgId=408&tblId=DT_408_2006_S0039"
with urlopen(url) as response:
    json_file = response.read()

# JSON 데이터를 파이썬 객체로 변환
py_json = json.loads(json_file.decode('utf-8'))

# 데이터를 리스트로 저장
data = []
for item in py_json:
    row = [
        item.get('C1_NM', ''),  # 행정구역별
        item.get('C2_NM', ''),  # 유형별
        item.get('DT', ''),  # 데이터 값
        item.get('PRD_DE', '')  # 연도
    ]
    data.append(row)

# 데이터를 연도별로 그룹화
years = sorted(set(item[3] for item in data))
regions = sorted(set(item[0] for item in data))
types = sorted(set(item[1] for item in data if item[1]))

# 테이블 데이터 구성
table_data = []
for region in regions:
    for typ in types:
        row = [region, typ]
        for year in years:
            value = next((item[2] for item in data if item[0] == region and item[1] == typ and item[3] == year), "")
            row.append(value)
        table_data.append(row)

# 테이블 만들기
fig, ax = plt.subplots(figsize=(12, 6))  # 크기 조절    
column_labels = ["행정구역별", "유형별"] + [f"{year}" for year in years]
ax.axis('tight')
ax.axis('off')
ax.table(cellText=table_data, colLabels=column_labels, loc="center", cellLoc='center', colColours=["yellow"] * len(column_labels))

# 테이블 표시
plt.show()
