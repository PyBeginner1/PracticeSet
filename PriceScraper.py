#requests is for pulling the page from the mentioned url
import requests
#BS is to parse the page & send individual data
from bs4 import BeautifulSoup
#smtp is for simple mail transfer protocol
import smtplib

URL = "https://www.amazon.in/Sony-ILCE-7M3K-Full-Frame-Mirrorless-Interchangeable/dp/B07DPSQRFF/ref=sr_1_3?dchild=1&keywords=sony+a7&qid=1617246451&sr=8-3"
headers = {"User_Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

def check_price():
    #pulls data from the url
    page = requests.get(URL, headers =headers)
    # Parses the page & prints individual data
    soup = BeautifulSoup(page.content,'html.parser')
    # finding the individual data like title & price
    title = soup.find(id ="productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    converted_price = (price[:-3])
    if converted_price < '1,54,000':
        sendmail()
    print(title.strip())
    print(converted_price)



def sendmail():
    server = smtplib.SMTP('smtp.gmail.com',587)         #587 is standard port of smtp
    #ehlo is used to establish connection
    server.ehlo()
    #transport layer security
    server.starttls()
    server.ehlo()

    server.login('shashvathn@gmail.com', '')        #no password given
    subject = "Price has dropped"
    body = "Check the link https://www.amazon.in/Sony-ILCE-7M3K-Full-Frame-Mirrorless-Interchangeable/dp/B07DPSQRFF/ref=sr_1_3?dchild=1&keywords=sony+a7&qid=1617246451&sr=8-3"
    msg = f"Subject:{subject}\n\n {body}"
    server.sendmail(
        'shashvathn@gmail.com',
        'shashvath.82@gmail.com',
        msg
    )
    print("Email has been sent")
    server.close()

check_price()