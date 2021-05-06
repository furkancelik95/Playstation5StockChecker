import requests
from bs4 import BeautifulSoup
import time
import sys
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = 'sender@gmail.com'
msg['To'] = 'receiver@gmail.com'
msg['Subject'] = 'Çabuk PLAYSTATION 5 STOKTA!'
message = 'Vatan Bilgisayar linki: https://www.vatanbilgisayar.com/sony-playstation-5-digital-surum-oyun-konsolu.html?utm_source=search&utm_medium=playstation%205&utm_campaign=playstation%205'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('sender@gmail.com', 'SENDEREMAILPASSWORD')

while(True):   
    URL = 'https://www.vatanbilgisayar.com/sony-playstation-5-digital-surum-oyun-konsolu.html?utm_source=search&utm_medium=playstation%205&utm_campaign=playstation%205'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    job_elems = soup.find_all('div', class_='d-cell col-xs-12 short-basket-button')

    for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
        title_elem = job_elem.find('a', class_='btn btn-success btn-stock')
        result = str(title_elem)
        result = result.replace('<a class="btn btn-success btn-stock"><span class="icon-shopping-card hidden-sm hidden-md hidden-lg"></span>','')
        result = result.replace('</a>','')
        print(result)

        if result=='ÇOK YAKINDA' or result=='TÜKENDİ' or result=='None':
            print('Stokta yok')
            time.sleep(60)
        else:
            mailserver.sendmail('sender@gmail.com','receiver@gmail.com',msg.as_string())
            mailserver.quit()
            sys.exit()