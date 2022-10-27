#Auto Metar V1.1.1 selenium v4

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

def metar(): #모든 METAR 받아오기(총 38개 공항)
    driver.get("https://global.amo.go.kr/obsMetar/ObsMetar.do")
    Class_metars = driver.find_element(By.CLASS_NAME,"dataT").text
    return Class_metars

#---------------------------------------------------------------------#
def list_metar(): # 모든 METAR 리스트화 (불필요 정보 제거)
    list_metars = metars.split('\n')
    del list_metars[0]
    return list_metars
#---------------------------------------------------------------------#
def rktl(): #RKTL 인덱싱하고 문자열 반환
    find_rktl = 'RKTL'
    for i in range(len(list_metars)):
        if find_rktl in list_metars[i]:
            rktl_metar = list_metars[i]
    return rktl_metar

def rknn(): #RKNN 인덱싱하고 문자열 반환        
    find_rknn = 'RKNN'
    for i in range(len(list_metars)):
        if find_rknn in list_metars[i]:
            rknn_metar = list_metars[i]
    return rknn_metar

def rkny(): #RKNY 인덱싱하고 문자열 반환          
    find_rkny = 'RKNY'
    for i in range(len(list_metars)):
        if find_rkny in list_metars[i]:
            rkny_metar = list_metars[i]
    return rkny_metar
    
def rkty(): #RKTY 인덱싱하고 문자열 반환      
    find_rkty = 'RKTY'
    for i in range(len(list_metars)):
        if find_rkty in list_metars[i]:
            rkty_metar = list_metars[i]
    return rkty_metar

def rkth(): #RKTH 인덱싱하고 문자열 반환        
    find_rkth = 'RKTH'
    for i in range(len(list_metars)):
        if find_rkth in list_metars[i]:
            rkth_metar = list_metars[i]
    return rkth_metar

def rkpu(): #RKPU 인덱싱하고 문자열 반환       
    find_rkpu = 'RKPU'
    for i in range(len(list_metars)):
        if find_rkpu in list_metars[i]:
            rkpu_metar = list_metars[i]
    return rkpu_metar

#-----------------------------------------------------------------#

def wind_rktl(): # "KT" 인덱싱, RKTL 바람 방향, 속도 반환
    index_rktl = rktl_metar.rfind('KT')
    if rktl_metar[int(index_rktl)-4] == "G" or rktl_metar[int(index_rktl)-3] == "G":
        rktl_winddir = rktl_metar[int(index_rktl)-9:int(index_rktl)-6]
        rktl_windspd = rktl_metar[int(index_rktl)-6:int(index_rktl)]
    else:
        rktl_winddir = rktl_metar[int(index_rktl)-5:int(index_rktl)-2]
        rktl_windspd = rktl_metar[int(index_rktl)-2:int(index_rktl)]
    return index_rktl, rktl_winddir,rktl_windspd

def wind_rknn():
    index_rknn = rknn_metar.rfind('KT')
    if rknn_metar[int(index_rknn)-4] == "G" or rknn_metar[int(index_rknn)-3] == "G":
        rknn_winddir = rknn_metar[int(index_rknn)-9:int(index_rknn)-6]
        rknn_windspd = rknn_metar[int(index_rknn)-6:int(index_rknn)]
    else:
        rknn_winddir = rknn_metar[int(index_rknn)-5:int(index_rknn)-2]
        rknn_windspd = rknn_metar[int(index_rknn)-2:int(index_rknn)]
    return index_rknn, rknn_winddir,rknn_windspd 

def wind_rkny():
    index_rkny = rkny_metar.rfind('KT')
    if rkny_metar[int(index_rkny)-4] == "G" or rkny_metar[int(index_rkny)-3] == "G":
        rkny_winddir = rkny_metar[int(index_rkny)-9:int(index_rkny)-6]
        rkny_windspd = rkny_metar[int(index_rkny)-6:int(index_rkny)]
    else:
        rkny_winddir = rkny_metar[int(index_rkny)-5:int(index_rkny)-2]
        rkny_windspd = rkny_metar[int(index_rkny)-2:int(index_rkny)]
    return index_rkny, rkny_winddir,rkny_windspd

def wind_rkty():
    index_rkty = rkty_metar.rfind('KT')
    if rkty_metar[int(index_rkty)-4] == "G" or rkty_metar[int(index_rkty)-3] == "G":
        rkty_winddir = rkty_metar[int(index_rkty)-9:int(index_rkty)-6]
        rkty_windspd = rkty_metar[int(index_rkty)-6:int(index_rkty)]
    else:
        rkty_winddir = rkty_metar[int(index_rkty)-5:int(index_rkty)-2]
        rkty_windspd = rkty_metar[int(index_rkty)-2:int(index_rkty)]
    return index_rkty, rkty_winddir,rkty_windspd

def wind_rkth():
    index_rkth = rkth_metar.rfind('KT')
    if rkth_metar[int(index_rkth)-4] == "G" or rkth_metar[int(index_rkth)-3] == "G":
        rkth_winddir = rkth_metar[int(index_rkth)-9:int(index_rkth)-6]
        rkth_windspd = rkth_metar[int(index_rkth)-6:int(index_rkth)]
    else:
        rkth_winddir = rkth_metar[int(index_rkth)-5:int(index_rkth)-2]
        rkth_windspd = rkth_metar[int(index_rkth)-2:int(index_rkth)]
    return index_rkth, rkth_winddir,rkth_windspd

def wind_rkpu():
    index_rkpu = rkpu_metar.rfind('KT')
    if rkpu_metar[int(index_rkpu)-4] == "G" or rkpu_metar[int(index_rkpu)-3] == "G":
        rkpu_winddir = rkpu_metar[int(index_rkpu)-9:int(index_rkpu)-6]
        rkpu_windspd = rkpu_metar[int(index_rkpu)-6:int(index_rkpu)]
    else:
        rkpu_winddir = rkpu_metar[int(index_rkpu)-5:int(index_rkpu)-2]
        rkpu_windspd = rkpu_metar[int(index_rkpu)-2:int(index_rkpu)]
    return index_rkpu, rkpu_winddir,rkpu_windspd

#-------------------------------------------------------------------#

def vis_rktl():
    if "CAVOK" in rktl_metar:
        rktl_vis = "CAVOK"
    elif rktl_metar[int(index_rktl)+6] == "V":
        rktl_vis = rktl_metar[int(index_rktl)+11:int(index_rktl)+16]
    else:
        rktl_vis = rktl_metar[int(index_rktl)+3:int(index_rktl)+8]
    return rktl_vis

def vis_rknn():
    if "CAVOK" in rknn_metar:
        rknn_vis = "CAVOK"
    elif rknn_metar[int(index_rknn)+6] == "V":
        rknn_vis = rknn_metar[int(index_rknn)+11:int(index_rknn)+16]
    else:
        rknn_vis = rknn_metar[int(index_rknn)+3:int(index_rknn)+8]
    return rknn_vis

def vis_rkny():
    if "CAVOK" in rkny_metar:
        rkny_vis = "CAVOK"
    elif rkny_metar[int(index_rkny)+6] == "V":
        rkny_vis = rkny_metar[int(index_rkny)+11:int(index_rkny)+16]
    else:
        rkny_vis = rkny_metar[int(index_rkny)+3:int(index_rkny)+8]
    return rkny_vis

def vis_rkty():
    if "CAVOK" in rkty_metar:
        rkty_vis = "CAVOK"
    elif rkty_metar[int(index_rkty)+6] == "V":
        rkty_vis = rkty_metar[int(index_rkty)+11:int(index_rkty)+16]
    else:
        rkty_vis = rkty_metar[int(index_rkty)+3:int(index_rkty)+8]
    return rkty_vis

def vis_rkth():
    if "CAVOK" in rkth_metar:
        rkth_vis = "CAVOK"
    elif rkth_metar[int(index_rkth)+6] == "V":
        rkth_vis = rkth_metar[int(index_rkth)+11:int(index_rkth)+16]
    else:
        rkth_vis = rkth_metar[int(index_rkth)+3:int(index_rkth)+8]
    return rkth_vis

def vis_rkpu():
    if "CAVOK" in rkpu_metar:
        rkpu_vis = "CAVOK"
    elif rkpu_metar[int(index_rkpu)+6] == "V":
        rkpu_vis = rkpu_metar[int(index_rkpu)+11:int(index_rkpu)+16]
    else:
        rkpu_vis = rkpu_metar[int(index_rkpu)+3:int(index_rkpu)+8]
    return rkpu_vis

#--------------------------------------------------------------------#

def cld_rktl():
    list_cld_rktl = []
    if "CAVOK" in rktl_metar:
        list_cld_rktl.append("CAVOK")
    elif "NCD" in rktl_metar:
        list_cld_rktl.append("NCD")
    elif "SKC" in rktl_metar:
        list_cld_rktl.append("SKC")
    elif "NSC" in rktl_metar:
        list_cld_rktl.append("NSC")
    elif "FEW" in rktl_metar:
        index_few_rktl = rktl_metar.rfind('FEW')
        list_cld_rktl.append(rktl_metar[int(index_few_rktl):int(index_few_rktl)+6])
    
    if rktl_metar.count("SCT") == 1:
        index_sct_rktl = rktl_metar.rfind('SCT')
        list_cld_rktl.append(rktl_metar[int(index_sct_rktl):int(index_sct_rktl)+6])
    elif rktl_metar.count("SCT") == 2:
        index_sct_rktl = rktl_metar.find('SCT')
        list_cld_rktl.append(rktl_metar[int(index_sct_rktl):int(index_sct_rktl)+6])
        index_sct2_rktl = rktl_metar.rfind('SCT')
        list_cld_rktl.append(rktl_metar[int(index_sct2_rktl):int(index_sct2_rktl)+6])
    elif rktl_metar.count("SCT") == 3:
        index_sct_rktl = rktl_metar.find('SCT')
        list_cld_rktl.append(rktl_metar[int(index_sct_rktl):int(index_sct_rktl)+6])
        removed_rktl_metar = rktl_metar[int(index_sct_rktl)+7:]
        index_sct2_rktl = removed_rktl_metar.find('SCT')
        list_cld_rktl.append(removed_rktl_metar[int(index_sct2_rktl):int(index_sct2_rktl)+6])
        index_sct3_rktl = removed_rktl_metar.rfind('SCT')
        list_cld_rktl.append(removed_rktl_metar[int(index_sct3_rktl):int(index_sct3_rktl)+6])
        
    if rktl_metar.count("BKN") == 1:
        index_bkn_rktl = rktl_metar.rfind('BKN')
        list_cld_rktl.append(rktl_metar[int(index_bkn_rktl):int(index_bkn_rktl)+6])
    elif rktl_metar.count("BKN") == 2:
        index_bkn_rktl = rktl_metar.find('BKN')
        list_cld_rktl.append(rktl_metar[int(index_bkn_rktl):int(index_bkn_rktl)+6])
        index_bkn2_rktl = rktl_metar.rfind('BKN')
        list_cld_rktl.append(rktl_metar[int(index_bkn2_rktl):int(index_bkn2_rktl)+6])
    elif rktl_metar.count("BKN") == 3:
        index_bkn_rktl = rktl_metar.find('BKN')
        list_cld_rktl.append(rktl_metar[int(index_bkn_rktl):int(index_bkn_rktl)+6])
        removed_rktl_metar = rktl_metar[int(index_bkn_rktl)+7:]
        index_bkn2_rktl = removed_rktl_metar.find('BKN')
        list_cld_rktl.append(removed_rktl_metar[int(index_bkn2_rktl):int(index_bkn2_rktl)+6])
        index_bkn3_rktl = removed_rktl_metar.rfind('BKN')
        list_cld_rktl.append(removed_rktl_metar[int(index_bkn3_rktl):int(index_bkn3_rktl)+6])
        
    if rktl_metar.count("OVC") == 1:
        index_ovc_rktl = rktl_metar.rfind('OVC')
        list_cld_rktl.append(rktl_metar[int(index_ovc_rktl):int(index_ovc_rktl)+6])
    elif rktl_metar.count("OVC") == 2:
        index_ovc_rktl = rktl_metar.find('OVC')
        list_cld_rktl.append(rktl_metar[int(index_ovc_rktl):int(index_ovc_rktl)+6])
        index_ovc2_rktl = rktl_metar.rfind('OVC')
        list_cld_rktl.append(rktl_metar[int(index_ovc2_rktl):int(index_ovc2_rktl)+6])
    elif rktl_metar.count("OVC") == 3:
        index_ovc_rktl = rktl_metar.find('OVC')
        list_cld_rktl.append(rktl_metar[int(index_ovc_rktl):int(index_ovc_rktl)+6])
        removed_rktl_metar = rktl_metar[int(index_ovc_rktl)+7:]
        index_ovc2_rktl = removed_rktl_metar.find('OVC')
        list_cld_rktl.append(removed_rktl_metar[int(index_ovc2_rktl):int(index_ovc2_rktl)+6])
        index_ovc3_rktl = removed_rktl_metar.rfind('OVC')
        list_cld_rktl.append(removed_rktl_metar[int(index_ovc3_rktl):int(index_ovc3_rktl)+6])
    cld_rktl = ' '.join(list_cld_rktl)
    return cld_rktl

def cld_rknn():
    list_cld_rknn = []
    if "CAVOK" in rknn_metar:
        list_cld_rknn.append("CAVOK")
    elif "NCD" in rknn_metar:
        list_cld_rknn.append("NCD")
    elif "SKC" in rknn_metar:
        list_cld_rknn.append("SKC")
    elif "NSC" in rknn_metar:
        list_cld_rknn.append("NSC")
    elif "FEW" in rknn_metar:
        index_few_rknn = rknn_metar.rfind('FEW')
        list_cld_rknn.append(rknn_metar[int(index_few_rknn):int(index_few_rknn)+6])
    
    if rknn_metar.count("SCT") == 1:
        index_sct_rknn = rknn_metar.rfind('SCT')
        list_cld_rknn.append(rknn_metar[int(index_sct_rknn):int(index_sct_rknn)+6])
    elif rknn_metar.count("SCT") == 2:
        index_sct_rknn = rknn_metar.find('SCT')
        list_cld_rknn.append(rknn_metar[int(index_sct_rknn):int(index_sct_rknn)+6])
        index_sct2_rknn = rknn_metar.rfind('SCT')
        list_cld_rknn.append(rknn_metar[int(index_sct2_rknn):int(index_sct2_rknn)+6])
    elif rknn_metar.count("SCT") == 3:
        index_sct_rknn = rknn_metar.find('SCT')
        list_cld_rknn.append(rknn_metar[int(index_sct_rknn):int(index_sct_rknn)+6])
        removed_rknn_metar = rknn_metar[int(index_sct_rknn)+7:]
        index_sct2_rknn = removed_rknn_metar.find('SCT')
        list_cld_rknn.append(removed_rknn_metar[int(index_sct2_rknn):int(index_sct2_rknn)+6])
        index_sct3_rknn = removed_rknn_metar.rfind('SCT')
        list_cld_rknn.append(removed_rknn_metar[int(index_sct3_rknn):int(index_sct3_rknn)+6])
        
    if rknn_metar.count("BKN") == 1:
        index_bkn_rknn = rknn_metar.rfind('BKN')
        list_cld_rknn.append(rknn_metar[int(index_bkn_rknn):int(index_bkn_rknn)+6])
    elif rknn_metar.count("BKN") == 2:
        index_bkn_rknn = rknn_metar.find('BKN')
        list_cld_rknn.append(rknn_metar[int(index_bkn_rknn):int(index_bkn_rknn)+6])
        index_bkn2_rknn = rknn_metar.rfind('BKN')
        list_cld_rknn.append(rknn_metar[int(index_bkn2_rknn):int(index_bkn2_rknn)+6])
    elif rknn_metar.count("BKN") == 3:
        index_bkn_rknn = rknn_metar.find('BKN')
        list_cld_rknn.append(rknn_metar[int(index_bkn_rknn):int(index_bkn_rknn)+6])
        removed_rknn_metar = rknn_metar[int(index_bkn_rknn)+7:]
        index_bkn2_rknn = removed_rknn_metar.find('BKN')
        list_cld_rknn.append(removed_rknn_metar[int(index_bkn2_rknn):int(index_bkn2_rknn)+6])
        index_bkn3_rknn = removed_rknn_metar.rfind('BKN')
        list_cld_rknn.append(removed_rknn_metar[int(index_bkn3_rknn):int(index_bkn3_rknn)+6])
        
    if rknn_metar.count("OVC") == 1:
        index_ovc_rknn = rknn_metar.rfind('OVC')
        list_cld_rknn.append(rknn_metar[int(index_ovc_rknn):int(index_ovc_rknn)+6])
    elif rknn_metar.count("OVC") == 2:
        index_ovc_rknn = rknn_metar.find('OVC')
        list_cld_rknn.append(rknn_metar[int(index_ovc_rknn):int(index_ovc_rknn)+6])
        index_ovc2_rknn = rknn_metar.rfind('OVC')
        list_cld_rknn.append(rknn_metar[int(index_ovc2_rknn):int(index_ovc2_rknn)+6])
    elif rknn_metar.count("OVC") == 3:
        index_ovc_rknn = rknn_metar.find('OVC')
        list_cld_rknn.append(rknn_metar[int(index_ovc_rknn):int(index_ovc_rknn)+6])
        removed_rknn_metar = rknn_metar[int(index_ovc_rknn)+7:]
        index_ovc2_rknn = removed_rknn_metar.find('OVC')
        list_cld_rknn.append(removed_rknn_metar[int(index_ovc2_rknn):int(index_ovc2_rknn)+6])
        index_ovc3_rknn = removed_rknn_metar.rfind('OVC')
        list_cld_rknn.append(removed_rknn_metar[int(index_ovc3_rknn):int(index_ovc3_rknn)+6])
    cld_rknn = ' '.join(list_cld_rknn)
    return cld_rknn

def cld_rkny():
    list_cld_rkny = []
    if "CAVOK" in rkny_metar:
        list_cld_rkny.append("CAVOK")
    elif "NCD" in rkny_metar:
        list_cld_rkny.append("NCD")
    elif "SKC" in rkny_metar:
        list_cld_rkny.append("SKC")
    elif "NSC" in rkny_metar:
        list_cld_rkny.append("NSC")
    elif "FEW" in rkny_metar:
        index_few_rkny = rkny_metar.rfind('FEW')
        list_cld_rkny.append(rkny_metar[int(index_few_rkny):int(index_few_rkny)+6])
    
    if rkny_metar.count("SCT") == 1:
        index_sct_rkny = rkny_metar.rfind('SCT')
        list_cld_rkny.append(rkny_metar[int(index_sct_rkny):int(index_sct_rkny)+6])
    elif rkny_metar.count("SCT") == 2:
        index_sct_rkny = rkny_metar.find('SCT')
        list_cld_rkny.append(rkny_metar[int(index_sct_rkny):int(index_sct_rkny)+6])
        index_sct2_rkny = rkny_metar.rfind('SCT')
        list_cld_rkny.append(rkny_metar[int(index_sct2_rkny):int(index_sct2_rkny)+6])
    elif rkny_metar.count("SCT") == 3:
        index_sct_rkny = rkny_metar.find('SCT')
        list_cld_rkny.append(rkny_metar[int(index_sct_rkny):int(index_sct_rkny)+6])
        removed_rkny_metar = rkny_metar[int(index_sct_rkny)+7:]
        index_sct2_rkny = removed_rkny_metar.find('SCT')
        list_cld_rkny.append(removed_rkny_metar[int(index_sct2_rkny):int(index_sct2_rkny)+6])
        index_sct3_rkny = removed_rkny_metar.rfind('SCT')
        list_cld_rkny.append(removed_rkny_metar[int(index_sct3_rkny):int(index_sct3_rkny)+6])
        
    if rkny_metar.count("BKN") == 1:
        index_bkn_rkny = rkny_metar.rfind('BKN')
        list_cld_rkny.append(rkny_metar[int(index_bkn_rkny):int(index_bkn_rkny)+6])
    elif rkny_metar.count("BKN") == 2:
        index_bkn_rkny = rkny_metar.find('BKN')
        list_cld_rkny.append(rkny_metar[int(index_bkn_rkny):int(index_bkn_rkny)+6])
        index_bkn2_rkny = rkny_metar.rfind('BKN')
        list_cld_rkny.append(rkny_metar[int(index_bkn2_rkny):int(index_bkn2_rkny)+6])
    elif rkny_metar.count("BKN") == 3:
        index_bkn_rkny = rkny_metar.find('BKN')
        list_cld_rkny.append(rkny_metar[int(index_bkn_rkny):int(index_bkn_rkny)+6])
        removed_rkny_metar = rkny_metar[int(index_bkn_rkny)+7:]
        index_bkn2_rkny = removed_rkny_metar.find('BKN')
        list_cld_rkny.append(removed_rkny_metar[int(index_bkn2_rkny):int(index_bkn2_rkny)+6])
        index_bkn3_rkny = removed_rkny_metar.rfind('BKN')
        list_cld_rkny.append(removed_rkny_metar[int(index_bkn3_rkny):int(index_bkn3_rkny)+6])
        
    if rkny_metar.count("OVC") == 1:
        index_ovc_rkny = rkny_metar.rfind('OVC')
        list_cld_rkny.append(rkny_metar[int(index_ovc_rkny):int(index_ovc_rkny)+6])
    elif rkny_metar.count("OVC") == 2:
        index_ovc_rkny = rkny_metar.find('OVC')
        list_cld_rkny.append(rkny_metar[int(index_ovc_rkny):int(index_ovc_rkny)+6])
        index_ovc2_rkny = rkny_metar.rfind('OVC')
        list_cld_rkny.append(rkny_metar[int(index_ovc2_rkny):int(index_ovc2_rkny)+6])
    elif rkny_metar.count("OVC") == 3:
        index_ovc_rkny = rkny_metar.find('OVC')
        list_cld_rkny.append(rkny_metar[int(index_ovc_rkny):int(index_ovc_rkny)+6])
        removed_rkny_metar = rkny_metar[int(index_ovc_rkny)+7:]
        index_ovc2_rkny = removed_rkny_metar.find('OVC')
        list_cld_rkny.append(removed_rkny_metar[int(index_ovc2_rkny):int(index_ovc2_rkny)+6])
        index_ovc3_rkny = removed_rkny_metar.rfind('OVC')
        list_cld_rkny.append(removed_rkny_metar[int(index_ovc3_rkny):int(index_ovc3_rkny)+6])
    cld_rkny = ' '.join(list_cld_rkny)
    return cld_rkny

def cld_rkty():
    list_cld_rkty = []
    if "CAVOK" in rkty_metar:
        list_cld_rkty.append("CAVOK")
    elif "NCD" in rkty_metar:
        list_cld_rkty.append("NCD")
    elif "SKC" in rkty_metar:
        list_cld_rkty.append("SKC")
    elif "NSC" in rkty_metar:
        list_cld_rkty.append("NSC")
    elif "FEW" in rkty_metar:
        index_few_rkty = rkty_metar.rfind('FEW')
        list_cld_rkty.append(rkty_metar[int(index_few_rkty):int(index_few_rkty)+6])
    
    if rkty_metar.count("SCT") == 1:
        index_sct_rkty = rkty_metar.rfind('SCT')
        list_cld_rkty.append(rkty_metar[int(index_sct_rkty):int(index_sct_rkty)+6])
    elif rkty_metar.count("SCT") == 2:
        index_sct_rkty = rkty_metar.find('SCT')
        list_cld_rkty.append(rkty_metar[int(index_sct_rkty):int(index_sct_rkty)+6])
        index_sct2_rkty = rkty_metar.rfind('SCT')
        list_cld_rkty.append(rkty_metar[int(index_sct2_rkty):int(index_sct2_rkty)+6])
    elif rkty_metar.count("SCT") == 3:
        index_sct_rkty = rkty_metar.find('SCT')
        list_cld_rkty.append(rkty_metar[int(index_sct_rkty):int(index_sct_rkty)+6])
        removed_rkty_metar = rkty_metar[int(index_sct_rkty)+7:]
        index_sct2_rkty = removed_rkty_metar.find('SCT')
        list_cld_rkty.append(removed_rkty_metar[int(index_sct2_rkty):int(index_sct2_rkty)+6])
        index_sct3_rkty = removed_rkty_metar.rfind('SCT')
        list_cld_rkty.append(removed_rkty_metar[int(index_sct3_rkty):int(index_sct3_rkty)+6])
        
    if rkty_metar.count("BKN") == 1:
        index_bkn_rkty = rkty_metar.rfind('BKN')
        list_cld_rkty.append(rkty_metar[int(index_bkn_rkty):int(index_bkn_rkty)+6])
    elif rkty_metar.count("BKN") == 2:
        index_bkn_rkty = rkty_metar.find('BKN')
        list_cld_rkty.append(rkty_metar[int(index_bkn_rkty):int(index_bkn_rkty)+6])
        index_bkn2_rkty = rkty_metar.rfind('BKN')
        list_cld_rkty.append(rkty_metar[int(index_bkn2_rkty):int(index_bkn2_rkty)+6])
    elif rkty_metar.count("BKN") == 3:
        index_bkn_rkty = rkty_metar.find('BKN')
        list_cld_rkty.append(rkty_metar[int(index_bkn_rkty):int(index_bkn_rkty)+6])
        removed_rkty_metar = rkty_metar[int(index_bkn_rkty)+7:]
        index_bkn2_rkty = removed_rkty_metar.find('BKN')
        list_cld_rkty.append(removed_rkty_metar[int(index_bkn2_rkty):int(index_bkn2_rkty)+6])
        index_bkn3_rkty = removed_rkty_metar.rfind('BKN')
        list_cld_rkty.append(removed_rkty_metar[int(index_bkn3_rkty):int(index_bkn3_rkty)+6])
        
    if rkty_metar.count("OVC") == 1:
        index_ovc_rkty = rkty_metar.rfind('OVC')
        list_cld_rkty.append(rkty_metar[int(index_ovc_rkty):int(index_ovc_rkty)+6])
    elif rkty_metar.count("OVC") == 2:
        index_ovc_rkty = rkty_metar.find('OVC')
        list_cld_rkty.append(rkty_metar[int(index_ovc_rkty):int(index_ovc_rkty)+6])
        index_ovc2_rkty = rkty_metar.rfind('OVC')
        list_cld_rkty.append(rkty_metar[int(index_ovc2_rkty):int(index_ovc2_rkty)+6])
    elif rkty_metar.count("OVC") == 3:
        index_ovc_rkty = rkty_metar.find('OVC')
        list_cld_rkty.append(rkty_metar[int(index_ovc_rkty):int(index_ovc_rkty)+6])
        removed_rkty_metar = rkty_metar[int(index_ovc_rkty)+7:]
        index_ovc2_rkty = removed_rkty_metar.find('OVC')
        list_cld_rkty.append(removed_rkty_metar[int(index_ovc2_rkty):int(index_ovc2_rkty)+6])
        index_ovc3_rkty = removed_rkty_metar.rfind('OVC')
        list_cld_rkty.append(removed_rkty_metar[int(index_ovc3_rkty):int(index_ovc3_rkty)+6])
    cld_rkty = ' '.join(list_cld_rkty)
    return cld_rkty

def cld_rkth():
    list_cld_rkth = []
    if "CAVOK" in rkth_metar:
        list_cld_rkth.append("CAVOK")
    elif "NCD" in rkth_metar:
        list_cld_rkth.append("NCD")
    elif "SKC" in rkth_metar:
        list_cld_rkth.append("SKC")
    elif "NSC" in rkth_metar:
        list_cld_rkth.append("NSC")
    elif "FEW" in rkth_metar:
        index_few_rkth = rkth_metar.rfind('FEW')
        list_cld_rkth.append(rkth_metar[int(index_few_rkth):int(index_few_rkth)+6])
    
    if rkth_metar.count("SCT") == 1:
        index_sct_rkth = rkth_metar.rfind('SCT')
        list_cld_rkth.append(rkth_metar[int(index_sct_rkth):int(index_sct_rkth)+6])
    elif rkth_metar.count("SCT") == 2:
        index_sct_rkth = rkth_metar.find('SCT')
        list_cld_rkth.append(rkth_metar[int(index_sct_rkth):int(index_sct_rkth)+6])
        index_sct2_rkth = rkth_metar.rfind('SCT')
        list_cld_rkth.append(rkth_metar[int(index_sct2_rkth):int(index_sct2_rkth)+6])
    elif rkth_metar.count("SCT") == 3:
        index_sct_rkth = rkth_metar.find('SCT')
        list_cld_rkth.append(rkth_metar[int(index_sct_rkth):int(index_sct_rkth)+6])
        removed_rkth_metar = rkth_metar[int(index_sct_rkth)+7:]
        index_sct2_rkth = removed_rkth_metar.find('SCT')
        list_cld_rkth.append(removed_rkth_metar[int(index_sct2_rkth):int(index_sct2_rkth)+6])
        index_sct3_rkth = removed_rkth_metar.rfind('SCT')
        list_cld_rkth.append(removed_rkth_metar[int(index_sct3_rkth):int(index_sct3_rkth)+6])
        
    if rkth_metar.count("BKN") == 1:
        index_bkn_rkth = rkth_metar.rfind('BKN')
        list_cld_rkth.append(rkth_metar[int(index_bkn_rkth):int(index_bkn_rkth)+6])
    elif rkth_metar.count("BKN") == 2:
        index_bkn_rkth = rkth_metar.find('BKN')
        list_cld_rkth.append(rkth_metar[int(index_bkn_rkth):int(index_bkn_rkth)+6])
        index_bkn2_rkth = rkth_metar.rfind('BKN')
        list_cld_rkth.append(rkth_metar[int(index_bkn2_rkth):int(index_bkn2_rkth)+6])
    elif rkth_metar.count("BKN") == 3:
        index_bkn_rkth = rkth_metar.find('BKN')
        list_cld_rkth.append(rkth_metar[int(index_bkn_rkth):int(index_bkn_rkth)+6])
        removed_rkth_metar = rkth_metar[int(index_bkn_rkth)+7:]
        index_bkn2_rkth = removed_rkth_metar.find('BKN')
        list_cld_rkth.append(removed_rkth_metar[int(index_bkn2_rkth):int(index_bkn2_rkth)+6])
        index_bkn3_rkth = removed_rkth_metar.rfind('BKN')
        list_cld_rkth.append(removed_rkth_metar[int(index_bkn3_rkth):int(index_bkn3_rkth)+6])
        
    if rkth_metar.count("OVC") == 1:
        index_ovc_rkth = rkth_metar.rfind('OVC')
        list_cld_rkth.append(rkth_metar[int(index_ovc_rkth):int(index_ovc_rkth)+6])
    elif rkth_metar.count("OVC") == 2:
        index_ovc_rkth = rkth_metar.find('OVC')
        list_cld_rkth.append(rkth_metar[int(index_ovc_rkth):int(index_ovc_rkth)+6])
        index_ovc2_rkth = rkth_metar.rfind('OVC')
        list_cld_rkth.append(rkth_metar[int(index_ovc2_rkth):int(index_ovc2_rkth)+6])
    elif rkth_metar.count("OVC") == 3:
        index_ovc_rkth = rkth_metar.find('OVC')
        list_cld_rkth.append(rkth_metar[int(index_ovc_rkth):int(index_ovc_rkth)+6])
        removed_rkth_metar = rkth_metar[int(index_ovc_rkth)+7:]
        index_ovc2_rkth = removed_rkth_metar.find('OVC')
        list_cld_rkth.append(removed_rkth_metar[int(index_ovc2_rkth):int(index_ovc2_rkth)+6])
        index_ovc3_rkth = removed_rkth_metar.rfind('OVC')
        list_cld_rkth.append(removed_rkth_metar[int(index_ovc3_rkth):int(index_ovc3_rkth)+6])
    cld_rkth = ' '.join(list_cld_rkth)
    return cld_rkth

def cld_rkpu():
    list_cld_rkpu = []
    if "CAVOK" in rkpu_metar:
        list_cld_rkpu.append("CAVOK")
    elif "NCD" in rkpu_metar:
        list_cld_rkpu.append("NCD")
    elif "SKC" in rkpu_metar:
        list_cld_rkpu.append("SKC")
    elif "NSC" in rkpu_metar:
        list_cld_rkpu.append("NSC")
    elif "FEW" in rkpu_metar:
        index_few_rkpu = rkpu_metar.rfind('FEW')
        list_cld_rkpu.append(rkpu_metar[int(index_few_rkpu):int(index_few_rkpu)+6])
    
    if rkpu_metar.count("SCT") == 1:
        index_sct_rkpu = rkpu_metar.rfind('SCT')
        list_cld_rkpu.append(rkpu_metar[int(index_sct_rkpu):int(index_sct_rkpu)+6])
    elif rkpu_metar.count("SCT") == 2:
        index_sct_rkpu = rkpu_metar.find('SCT')
        list_cld_rkpu.append(rkpu_metar[int(index_sct_rkpu):int(index_sct_rkpu)+6])
        index_sct2_rkpu = rkpu_metar.rfind('SCT')
        list_cld_rkpu.append(rkpu_metar[int(index_sct2_rkpu):int(index_sct2_rkpu)+6])
    elif rkpu_metar.count("SCT") == 3:
        index_sct_rkpu = rkpu_metar.find('SCT')
        list_cld_rkpu.append(rkpu_metar[int(index_sct_rkpu):int(index_sct_rkpu)+6])
        removed_rkpu_metar = rkpu_metar[int(index_sct_rkpu)+7:]
        index_sct2_rkpu = removed_rkpu_metar.find('SCT')
        list_cld_rkpu.append(removed_rkpu_metar[int(index_sct2_rkpu):int(index_sct2_rkpu)+6])
        index_sct3_rkpu = removed_rkpu_metar.rfind('SCT')
        list_cld_rkpu.append(removed_rkpu_metar[int(index_sct3_rkpu):int(index_sct3_rkpu)+6])
        
    if rkpu_metar.count("BKN") == 1:
        index_bkn_rkpu = rkpu_metar.rfind('BKN')
        list_cld_rkpu.append(rkpu_metar[int(index_bkn_rkpu):int(index_bkn_rkpu)+6])
    elif rkpu_metar.count("BKN") == 2:
        index_bkn_rkpu = rkpu_metar.find('BKN')
        list_cld_rkpu.append(rkpu_metar[int(index_bkn_rkpu):int(index_bkn_rkpu)+6])
        index_bkn2_rkpu = rkpu_metar.rfind('BKN')
        list_cld_rkpu.append(rkpu_metar[int(index_bkn2_rkpu):int(index_bkn2_rkpu)+6])
    elif rkpu_metar.count("BKN") == 3:
        index_bkn_rkpu = rkpu_metar.find('BKN')
        list_cld_rkpu.append(rkpu_metar[int(index_bkn_rkpu):int(index_bkn_rkpu)+6])
        removed_rkpu_metar = rkpu_metar[int(index_bkn_rkpu)+7:]
        index_bkn2_rkpu = removed_rkpu_metar.find('BKN')
        list_cld_rkpu.append(removed_rkpu_metar[int(index_bkn2_rkpu):int(index_bkn2_rkpu)+6])
        index_bkn3_rkpu = removed_rkpu_metar.rfind('BKN')
        list_cld_rkpu.append(removed_rkpu_metar[int(index_bkn3_rkpu):int(index_bkn3_rkpu)+6])
        
    if rkpu_metar.count("OVC") == 1:
        index_ovc_rkpu = rkpu_metar.rfind('OVC')
        list_cld_rkpu.append(rkpu_metar[int(index_ovc_rkpu):int(index_ovc_rkpu)+6])
    elif rkpu_metar.count("OVC") == 2:
        index_ovc_rkpu = rkpu_metar.find('OVC')
        list_cld_rkpu.append(rkpu_metar[int(index_ovc_rkpu):int(index_ovc_rkpu)+6])
        index_ovc2_rkpu = rkpu_metar.rfind('OVC')
        list_cld_rkpu.append(rkpu_metar[int(index_ovc2_rkpu):int(index_ovc2_rkpu)+6])
    elif rkpu_metar.count("OVC") == 3:
        index_ovc_rkpu = rkpu_metar.find('OVC')
        list_cld_rkpu.append(rkpu_metar[int(index_ovc_rkpu):int(index_ovc_rkpu)+6])
        removed_rkpu_metar = rkpu_metar[int(index_ovc_rkpu)+7:]
        index_ovc2_rkpu = removed_rkpu_metar.find('OVC')
        list_cld_rkpu.append(removed_rkpu_metar[int(index_ovc2_rkpu):int(index_ovc2_rkpu)+6])
        index_ovc3_rkpu = removed_rkpu_metar.rfind('OVC')
        list_cld_rkpu.append(removed_rkpu_metar[int(index_ovc3_rkpu):int(index_ovc3_rkpu)+6])
    cld_rkpu = ' '.join(list_cld_rkpu)
    return cld_rkpu


#------------------------------------------------------------------------#
#함수 실행 부분
metars = metar()
list_metars = list_metar()

rktl_metar = rktl()
rknn_metar = rknn()
rkny_metar = rkny()
rkty_metar = rkty()
rkth_metar = rkth()
rkpu_metar = rkpu()

index_rktl, rktl_winddir, rktl_windspd = wind_rktl()
index_rknn, rknn_winddir, rknn_windspd = wind_rknn()
index_rkny, rkny_winddir, rkny_windspd = wind_rkny()
index_rkty, rkty_winddir, rkty_windspd = wind_rkty()
index_rkth, rkth_winddir, rkth_windspd = wind_rkth()
index_rkpu, rkpu_winddir, rkpu_windspd = wind_rkpu()

rktl_vis = vis_rktl()
rknn_vis = vis_rknn()
rkny_vis = vis_rknn()
rkty_vis = vis_rknn()
rkth_vis = vis_rknn()
rkpu_vis = vis_rknn()

rktl_cld = cld_rktl()
rknn_cld = cld_rknn()
rkny_cld = cld_rkny()
rkty_cld = cld_rkty()
rkth_cld = cld_rkth()
rkpu_cld = cld_rkpu()

#-------------------------------------------------------------#

# 바람 방향과 속도 합치기
rktl_wind = rktl_winddir+rktl_windspd
rknn_wind = rknn_winddir+rknn_windspd
rkny_wind = rkny_winddir+rkny_windspd
rkty_wind = rkty_winddir+rkty_windspd
rkth_wind = rkth_winddir+rkth_windspd
rkpu_wind = rkpu_winddir+rkpu_windspd

#-------------------------------------------------------------#
#구글 스프레드 시트 업로드

import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = 'wx-report-365712-719ac571257f.json'
#credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
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

#시간
worksheet.update_acell('A1', file_time)

#RKTL
worksheet.update_acell('B2', rktl_wind)
worksheet.update_acell('C2', rktl_vis)
worksheet.update_acell('D2', rktl_cld)
worksheet.update_acell('E2', rktl_metar)

#RKNN
worksheet.update_acell('B3', rknn_wind)
worksheet.update_acell('C3', rknn_vis)
worksheet.update_acell('D3', rknn_cld)
worksheet.update_acell('E3', rknn_metar)

#RKNY
worksheet.update_acell('B4', rkny_wind)
worksheet.update_acell('C4', rkny_vis)
worksheet.update_acell('D4', rkny_cld)
worksheet.update_acell('E4', rkny_metar)

#RKTY
worksheet.update_acell('B5', rkty_wind)
worksheet.update_acell('C5', rkty_vis)
worksheet.update_acell('D5', rkty_cld)
worksheet.update_acell('E5', rkty_metar)

#RKTH
worksheet.update_acell('B6', rkth_wind)
worksheet.update_acell('C6', rkth_vis)
worksheet.update_acell('D6', rkth_cld)
worksheet.update_acell('E6', rkth_metar)

#RKPU
worksheet.update_acell('B7', rkpu_wind)
worksheet.update_acell('C7', rkpu_vis)
worksheet.update_acell('D7', rkpu_cld)
worksheet.update_acell('E7', rkpu_metar)

driver.quit()