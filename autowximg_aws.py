#Autosig V1.1.2 selenium v4

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
from PIL import Image

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

def sigmet():
    driver.get("https://global.amo.go.kr/amis/awx/GisSigmetImage.do")
    driver.set_window_size(900, 1100)
    #driver.set_window_size(800, 900)
    driver.implicitly_wait(1)
    image_sigmet = driver.find_element(By.TAG_NAME, 'body')
    # image_sigmet_png = image_sigmet.screenshot('./sigmet.png')
    image_sigmet_png = image_sigmet.screenshot('./3_sigmet_'+file_time+'.png')
    Class_sigmet = driver.find_element(By.CLASS_NAME,"con_all2").text
    return Class_sigmet

def airmet():
    driver.get("https://global.amo.go.kr/amis/awx/GisAirmetImage.do")
    driver.set_window_size(900, 1100)
    #driver.set_window_size(826, 862)
    driver.implicitly_wait(1)
    image_airmet = driver.find_element(By.TAG_NAME, 'body')
    image_airmet_png = image_airmet.screenshot('./4_airmet_'+file_time+'.png')
    Class_airmet = driver.find_element(By.CLASS_NAME,"con_all2").text
    return Class_airmet

def radar():
    driver.get("https://global.amo.go.kr/kama/raid/radar.do")
    width = driver.execute_script("return document.body.scrollWidth")
    height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(width, height) #스크롤 할 수 있는 모든 부분을 지정
    # driver.set_window_size(800, 900)
    #1080해상도
    driver.find_element(By.ID,'kmaRadar').click()
    driver.find_element(By.ID,'kmaRadar').send_keys(Keys.TAB)
    #1080해상도
    driver.implicitly_wait(3)
    image_radar = driver.find_element(By.TAG_NAME, 'body')
    image_radar_png = image_radar.screenshot('./5_radar_'+file_time+'.png')


#------------------------------------------------------------------------#
def nosig():
    if rktl_airmet == "번호 현상 발표시각(UTC) 유효시간(UTC) 내용\n- - - - -":
        nosig_airmet_rktl = "NO AIRMET IN EFFECT"
    else:
        rktl_airmet_split = rktl_airmet.split("\n")
        del rktl_airmet_split[0]
        nosig_airmet_rktl = "".join(rktl_airmet_split)
        
    if rktl_sigmet == "번호 현상 발표시각(UTC) 유효시간(UTC) 내용\n- - - - -":
        nosig_sigmet_rktl = "NO SIGMET IN EFFECT"
    else:
        rktl_sigmet_split = rktl_sigmet.split("\n")
        del rktl_sigmet_split[0]
        nosig_sigmet_rktl = "".join(rktl_sigmet_split)
    return nosig_airmet_rktl, nosig_sigmet_rktl

def crop_sigmet():
    sigmet_img_path = os.getcwd() + '/3_sigmet_'+ file_time +'.png'
    sigmet_img = Image.open(sigmet_img_path)
    #sigmet_crop_img = sigmet_img.crop((30, 150, 800, 900)) # (left,upper,right,lower)
    sigmet_crop_img = sigmet_img.crop((30, 150, 800, 1000)) # (left,upper,right,lower)
    sigmet_crop_img.save(sigmet_img_path)

def crop_airmet():
    airmet_img_path = os.getcwd() + '/4_airmet_'+ file_time +'.png'
    airmet_img = Image.open(airmet_img_path)
    #airmet_crop_img = airmet_img.crop((30, 150, 800, 900)) # (left,upper,right,lower)
    airmet_crop_img = airmet_img.crop((30, 150, 800, 1000)) # (left,upper,right,lower)
    airmet_crop_img.save(airmet_img_path)

def crop_radar():
    radar_img_path = os.getcwd() + '/5_radar_'+ file_time +'.png'
    radar_img = Image.open(radar_img_path)
    #radar_crop_img = radar_img.crop((75, 250, 900, 1100)) # (left,upper,right,lower)
    radar_crop_img = radar_img.crop((75, 250, 900, 1100)) # (left,upper,right,lower)
    radar_crop_img.save(radar_img_path)

#함수 실행 부분

rktl_airmet = airmet()
# print(rktl_airmet)

rktl_sigmet = sigmet()
# print(rktl_sigmet)

rktl_nosig_airmet, rktl_nosig_sigmet = nosig()

rktl_radar = radar()

crop_radar()
crop_sigmet()
crop_airmet()

#-------------------------------------------------------------#

import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = 'wx-report-365712-719ac571257f.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(
        '/Users/jeongdonghee/Python/wx-report-365712-719ac571257f.json', scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1vjOUQjJf0m7P--4lKQmvDkiQhhACd26c785h1Pwr4hg/edit#gid=0'
# 스프레스시트 문서 가져오기 
doc = gc.open_by_url(spreadsheet_url)
# 시트 선택하기
worksheet = doc.worksheet('SIGMET_AIRMET')
# 시트 가져오기
#cell_data = worksheet.acell('B1').value

# 셀에 입력하기

#시간
worksheet.update_acell('A1', file_time)

#SIGMET
worksheet.update_acell('B2', '/WX_IMG/3_sigmet_'+ file_time +'.png')
worksheet.update_acell('C2', rktl_nosig_sigmet)

#AIRMET
worksheet.update_acell('B3', '/WX_IMG/4_airmet_'+ file_time +'.png')
worksheet.update_acell('C3', rktl_nosig_airmet)


#RADAR
worksheet.update_acell('B4', '/WX_IMG/5_radar_'+ file_time +'.png')

driver.quit()