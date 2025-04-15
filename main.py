from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import datetime
import time

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# Windows 경로로 명확히 지정
service = Service("C:/Users/박경서/work/macro-01/chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)

# 1. 정각 대기 후 접속
target_time = "14:00:58"
while True:
    now = datetime.datetime.now().strftime('%H:%M:%S')
    if now == target_time:
        driver.get("https://www.interpark.com/")
        break
    time.sleep(0.1)

# 2. 안심번호 수동 입력 대기
input("수동 입력 후 엔터 >> ")
time.sleep(2)  # 페이지 로딩

# 3. 좌석 선택
driver.find_element(By.XPATH, "//area[@title='A열 1번']").click()
driver.find_element(By.XPATH, "//area[@title='A열 2번']").click()

# 4. 인원수 선택
Select(driver.find_element(By.ID, "Adult")).select_by_value("2")

# 5. 다음 단계
driver.find_element(By.ID, "NextStepImage").click()
time.sleep(2)

# 6. 결제수단 선택
driver.find_element(By.XPATH, "//input[@value='무통장입금']").click()

# 7. 결제 버튼
driver.find_element(By.ID, "btnPayment").click()
