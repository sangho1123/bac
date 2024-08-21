import json
from urllib.request import urlopen
import openpyxl
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Font
import os

# URL을 통해 JSON 데이터 가져오기
url = "https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=MjhlYTcwNWU0MGU5NTYwMjRiNWI1M2I2MWNmODdiZmI=&itmId=13103114424T1+13103114424T2+&objL1=13102114424A.0001+13102114424A.0002+13102114424A.0010+13102114424A.0013+13102114424A.0014+&objL2=13102114424B.0003+13102114424B.00030001+13102114424B.00030002+13102114424B.00030003+13102114424B.00030004+13102114424B.00030005+13102114424B.00030006+13102114424B.00030007+13102114424B.00030008+13102114424B.00030009+13102114424B.0005+13102114424B.00050001+13102114424B.00050002+13102114424B.00050003+13102114424B.00050004+13102114424B.00050005+&objL3=&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=Y&newEstPrdCnt=5&orgId=408&tblId=DT_408_2006_S0039"
with urlopen(url) as response:
    json_file = response.read()

# JSON 데이터를 파이썬 객체로 변환
py_json = json.loads(json_file.decode('utf-8'))

# 엑셀 워크북과 시트 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "KOSIS Data"

# 데이터 헤더 추가
headers = ["행정구역별", "유형별", "2019", "2020", "2021", "2022", "2023"]
ws.append(headers)

# 데이터를 리스트로 저장 및 엑셀 시트에 추가
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
            # value를 숫자로 변환할 수 있는지 확인하고 변환
            try:
                value = float(value.replace(",", ""))
            except ValueError:
                pass  # 숫자가 아니면 변환하지 않음
            row.append(value)
        table_data.append(row)

# 엑셀 시트에 데이터 추가
for row in table_data:
    ws.append(row)

# 차트 생성
chart = BarChart()
chart.type = "col"
chart.style = 10
chart.title = "KOSIS Data Chart"
chart.y_axis.title = 'Value'
chart.x_axis.title = 'Year'

# 데이터 범위 설정
data = Reference(ws, min_col=3, min_row=1, max_col=7, max_row=len(table_data) + 1)
categories = Reference(ws, min_col=1, min_row=2, max_row=len(table_data) + 1)
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

# 차트를 시트에 추가
ws.add_chart(chart, "J5")

# 엑셀 파일 저장
file_path = "kosis_data.xlsx"
wb.save(file_path)

# 결과 파일 경로 출력
print(f"엑셀 파일이 '{os.path.abspath(file_path)}'에 저장되었습니다.")
