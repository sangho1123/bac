from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime, timedelta
import time

# Chrome 드라이버 경로 설정
chrome_driver_path = 'C:/Users/sanghojeong9210/Downloads/chromedriver_win64/chromedriver.exe'

# Selenium WebDriver 설정
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=service, options=options)

# 페이지 로드
url = 'http://www.korearatings.com/cms/frCmnCon/index.do?MENU_ID=360'
driver.get(url)

try:
    wait = WebDriverWait(driver, 30)  # 30초로 대기 시간 증가
    print("페이지 로드 대기 중...")

    # '대상' 버튼 클릭
    target_button_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn dropdown-toggle responsive mgr20' and @data-bs-toggle='dropdown']")))
    target_button_element.click()
    print("'대상' 버튼 클릭 완료")

    # 전체 선택 체크박스 클릭 (선택 해제)
    checkbox_all_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='form-check-input' and @id='checkAll']")))
    if checkbox_all_element.is_selected():
        checkbox_all_element.click()
        print("전체 선택 체크박스 클릭 완료")

    # 회사채 체크박스 클릭
    checkbox_corp_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='form-check-input' and @id='gbn_01']")))
    checkbox_corp_element.click()
    print("회사채 체크박스 클릭 완료")
    
        # '대상' 버튼 클릭
    target_button_element.click()
    print("'대상' 버튼 클릭 완료")


    # 시작 날짜를 오늘 날짜 기준 3개월 전으로 설정
    start_date_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='startDt']")))
    three_months_ago = (datetime.now() - timedelta(days=85)).strftime('%Y-%m-%d')
    driver.execute_script(f"document.getElementById('startDt').value = '{three_months_ago}'")
    print(f"시작 날짜를 {three_months_ago}로 설정 완료")



    # 등급검색 버튼 클릭
    search_button_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary btn-search' and @onclick='fn_dataSearch();']")))
    search_button_element.click()
    print("등급검색 버튼 클릭 완료")

        # 대기



# 테이블 로드 대기
    print("페이지 로드 대기 중...")
    table_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'GridMain'))
    )
    data0 = table_container
    print("테이블 컨테이너 찾음")
    df = pd.DataFrame(data0) 
    df.to_excel('KR_recent_ratings_raw0.xlsx', index=False)
    
    # 테이블의 모든 행 찾기
    rows = table_container.find_elements(By.TAG_NAME, 'tr')
    data = []
    data1 = rows
    df = pd.DataFrame(data1) 
    df.to_excel('KR_recent_ratings_raw.xlsx', index=False)
    
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if len(cells) > 100:  # 최소한 필요한 열의 개수 체크
            company_name = cells[2].text.strip()  # 회사명
            rating_date = cells[9].text.strip()  # 평가일
            data.append({'Company Name': company_name, 'Rating Date': rating_date})



    # DataFrame 생성 및 엑셀 파일로 저장
    df = pd.DataFrame(data) 
    df.to_excel('KR_recent_ratings.xlsx', index=False)
    print("데이터가 엑셀 파일로 저장되었습니다: KR_recent_ratings.xlsx")

except Exception as e:
    print(f"오류 발생: {e}")

finally:
    driver.quit()
