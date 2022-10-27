#Auto TAF V1.1.0 selenium v4

# 1. Selenium 4
from http.server import executable
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# 2. os
import os
import urllib.request as req

# 3. 날짜
import datetime
days = ['월','화','수','목','금','토','일']
day = datetime.datetime.today().weekday()
file_time = str(datetime.datetime.now().strftime('%Y%m%d%H%M'))

# 4. Pillow
#from PIL import Image

#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
chrome_options.add_argument("headless")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)

#웹페이지 해당 주소 이동
driver.implicitly_wait(1)   # 초 대기
driver.maximize_window()  # 화면 최대화
    
def taf(): #모든 TAF 받아오기(총 23개 공항)
    driver.get("https://global.amo.go.kr/airfcst/AirFcstBeforeList.do")
    ID_tafs = driver.find_element(By.ID,"contentsTb1").text
    return ID_tafs

#---------------------------------------------------------------------#
def list_taf(): # 모든 TAF 리스트화 (불필요 정보 제거)
    list_tafs = tafs.split('=')
    del list_tafs[0]
    return list_tafs
#---------------------------------------------------------------------#

def taf_rkny(): #RKNY 인덱싱하고 문자열 반환          
    find_rkny = 'RKNY'
    for i in range(len(list_tafs)):
        if find_rkny in list_tafs[i]:
            rkny_taf = list_tafs[i]
    return rkny_taf

def taf_rkth(): #RKTH 인덱싱하고 문자열 반환        
    find_rkth = 'RKTH'
    for i in range(len(list_tafs)):
        if find_rkth in list_tafs[i]:
            rkth_taf = list_tafs[i]
    return rkth_taf

def taf_rkpu(): #RKPU 인덱싱하고 문자열 반환       
    find_rkpu = 'RKPU'
    for i in range(len(list_tafs)):
        if find_rkpu in list_tafs[i]:
            rkpu_taf = list_tafs[i]
    return rkpu_taf

#-----------------------------------------------------------------#

#함수 실행 부분

tafs = taf()
list_tafs = list_taf()

rkny_taf = taf_rkny()
rkth_taf = taf_rkth()
rkpu_taf = taf_rkpu()

#-------------------------------------------------------------#

import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = 'wx-report-365712-719ac571257f.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1vjOUQjJf0m7P--4lKQmvDkiQhhACd26c785h1Pwr4hg/edit#gid=0'
# 스프레스시트 문서 가져오기 
doc = gc.open_by_url(spreadsheet_url)
# 시트 선택하기
worksheet = doc.worksheet('FCST')
# 시트 가져오기
#cell_data = worksheet.acell('B1').value

# 셀에 입력하기

#시간
worksheet.update_acell('A1', file_time)

#RKTH
worksheet.update_acell('B2', rkth_taf)

#RKNY
worksheet.update_acell('B3', rkny_taf)

#RKPU
worksheet.update_acell('B4', rkpu_taf)

driver.quit()