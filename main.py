import time
from selenium import webdriver
# import requests
from bs4 import BeautifulSoup
# import pandas as pd
# import numpy as np

# 프롬프트에서 아이디 비밀번호 입력 경우
# id = input("id를 입력하세요: ")
# pw = input("비밀번호를 입력하세요: ")

# 크롬 시작
browser = webdriver.Chrome()

# 아주대학교 포탈 이동
browser.get("https://eclass2.ajou.ac.kr/ultra/calendar")
browser.maximize_window()  # 창 최대화

# id, pw 입력
time.sleep(0.5)
browser.find_element_by_id("userId").send_keys('id')  # id 입력 (하드코딩)
# browser.find_element_by_id("userId").send_keys(id)  # id 입력 (프롬프트)
time.sleep(0.5)
browser.find_element_by_id("password").send_keys('pw')  # password 입력 (하드코딩)
# browser.find_element_by_id("password").send_keys(pw)  # password 입력 (프롬프트)

# login 버튼 클릭
time.sleep(0.5)
browser.find_element_by_id("loginSubmit").click()

# 캘린더 접속
browser.get("https://eclass2.ajou.ac.kr/ultra/calendar")

# 월로 변경
time.sleep(1)
browser.find_element_by_id("bb-calendar1-deadline").click()

# 과제 크롤링

time.sleep(1)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
assignments = soup.select('.element-details')
a = 1
for assignment in assignments:
    assignment_name = assignment.select_one('.name > a')
    assignment_deadline = assignment.select_one('.content > span')
    assignment_lecture = assignment.select_one('.content > a')
    print("순번: " + str(a))
    print("강의명: "+assignment_lecture.get_text().strip()[24:])
    print("과제 이름: "+assignment_name.get_text().strip())
    print("마감일: "+assignment_deadline.get_text().strip())
    print("\n")
    a = a+1

# 창 종료
browser.close()
