import pandas as pd
import codecs
from bs4 import BeautifulSoup
f = codecs.open("data_test_ayaru.html", 'r', 'utf-8')
html = f.read()
soup = BeautifulSoup(html,"lxml")
nickname = soup.find("span", class_="_1ilcntDWasuYGV-RN333Xx")
nickname1 = nickname.find_next("span", class_="_1ilcntDWasuYGV-RN333Xx")
nickname2 = nickname1.find_next("span", class_="_1ilcntDWasuYGV-RN333Xx")

fio = soup.find("span", class_="_2Og6V03ZvntWkFzKd6CMvB")
fio1 = fio.find_next("span", class_="_2Og6V03ZvntWkFzKd6CMvB")
fio2 = fio1.find_next("span", class_="_2Og6V03ZvntWkFzKd6CMvB")

job_title = soup.find("span", class_="_20BGuOUUuFT4KLHq-HDXhw")
job_title1 = job_title.find_next("span", class_="_20BGuOUUuFT4KLHq-HDXhw")
job_title2 = job_title1.find_next("span", class_="_20BGuOUUuFT4KLHq-HDXhw")

comment = soup.find("span", class_="_3Nq8cP7r3XHE5zBnc92u5y _1ZhmRzcT_xwwbFuBvVoGLa")
comment1 = comment.find_next("span", class_="_3Nq8cP7r3XHE5zBnc92u5y _1ZhmRzcT_xwwbFuBvVoGLa")
comment2 = comment1.find_next("span", class_="_3Nq8cP7r3XHE5zBnc92u5y _1ZhmRzcT_xwwbFuBvVoGLa")
print(comment2)

d = {'№': [1, 2, 3], 'НикНейм': [nickname, nickname1, nickname2], 'ФИО': [fio, fio1, fio2], 'Должность': [job_title, job_title1, job_title2], 'Комментарий': [comment, comment1, comment2]}
col = ['№', 'НикНейм', 'ФИО', 'Должность', 'Комментарий']
df = pd.DataFrame(data=d, columns=col)
print(df)

df.to_excel("output.xlsx", engine='xlsxwriter')

