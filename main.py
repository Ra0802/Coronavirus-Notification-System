"""
Description : A python mini-project that triggers a real-time notification
about Coronavirus cases. It extracts data from worldometers website.
"""

from plyer import notification
import requests
from bs4 import BeautifulSoup as bs
from bs4 import Comment


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=r"C:\Users\Rahul\Desktop\Python Programming\Real Time Notify System\icon.ico",
        timeout=15
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    myHtmlData = getData(
        'https://www.worldometers.info/coronavirus/country/india/')
    # print(myHtmlData)

    soup = bs(myHtmlData, 'html.parser')

    myData = ""

    for data in soup.find_all(id='maincounter-wrap'):
        myData += data.get_text()

    dataList = myData.split('\n')

    message = "Confirmed Cases : " + \
        dataList[3] + "\nRecovered : " + \
        dataList[13] + "\nDeaths : " + dataList[8]

    notifyMe("Coronavirus Notification [INDIA]", message)
