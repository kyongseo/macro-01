from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# 본인 경로로 수정
service = Service("C:/Users/박경서/work/macro-01/chromedriver.exe")

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(service=service, options=options)

# 네이버 로그인 페이지 접속
driver.get("https://nid.naver.com/nidlogin.login")
time.sleep(1)

# 아이디, 비밀번호 입력
driver.find_element(By.ID, "id").send_keys("네이버아이디")
driver.find_element(By.ID, "pw").send_keys("비밀번호")

# 로그인 버튼 클릭
driver.find_element(By.ID, "log.login").click()

# 결과 확인 대기
input("로그인 성공 여부 확인 후 엔터 >>> ")
