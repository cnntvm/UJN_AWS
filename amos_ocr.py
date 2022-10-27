from PIL import Image
from pytesseract import *
import cv2
import os
from PIL import Image

#1. 이미지 크롭
def crop_amos():
    amos_img_path = os.getcwd() + '/2022-10-19-15-34.png'
    amos_fullimg_path = os.getcwd() + '/2022-10-19-15-34_full.png'
    amos_img = Image.open(amos_img_path)
    amos_crop_img = amos_img.crop((130, 610, 990, 650)) # (left,upper,right,lower)
    amos_crop_img.save(amos_fullimg_path)
    return amos_fullimg_path

amos_fullimg = crop_amos()

#2. OCR

amos_full_img = Image.open(amos_fullimg)

#pytesseract.tesseract_cmd = r'/Users/jeongdonghee/opt/anaconda3/envs/env1/bin/pytesseract'
#pytesseract.tesseract_cmd = '/Users/jeongdonghee/opt/anaconda3/envs/env1/bin/pytesseract'
#text = str(pytesseract.image_to_string(img)) #한글은 'kor'
amos_full = pytesseract.image_to_string(amos_full_img, lang = 'eng')

print(amos_full)

#3. 구글스프레드 시트 업로드

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
worksheet = doc.worksheet('AIRPORT')
# 시트 가져오기
#cell_data = worksheet.acell('B1').value

# 셀에 입력하기

#OCR
worksheet.update_acell('E8', amos_full)