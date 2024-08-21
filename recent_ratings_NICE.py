import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta

# 날짜 설정
end_date = datetime.now().strftime('%Y-%m-%d')
start_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')

# 요청 URL
url = f'https://www.nicerating.com/disclosure/dayRatingNews.do?today={end_date}&cmpCd=&seriesNm=&secuTyp=BOND&strDate={start_date}&endDate={end_date}'

# HTTP GET 요청
response = requests.get(url, verify=False)  # SSL 인증서 검증 비활성화
if response.status_code != 200:
    raise Exception("Failed to load page")

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 데이터 저장용 리스트 초기화
data = []

# 테이블에서 등급 정보 추출 (id를 사용하여 테이블 찾기)
table = soup.find('table', {'id': 'tbl1'})
if not table:
    raise Exception("Could not find the ratings table")

rows = table.find('tbody').find_all('tr')
for row in rows:
    cols = row.find_all('td')
    if len(cols) > 9:  # 필요한 데이터가 포함된 행인지 확인
        company_name = cols[0].text.strip().replace('(주)', '')  # "(주)" 제거
        rating_date = cols[9].text.strip()
        data.append({'Company Name': company_name, 'Rating Date': rating_date})

# 데이터프레임 생성
df = pd.DataFrame(data)

# 엑셀 파일로 저장
df.to_excel('NICE_recent_ratings.xlsx', index=False)

print("엑셀 파일로 저장 완료: NICE_recent_ratings.xlsx")
