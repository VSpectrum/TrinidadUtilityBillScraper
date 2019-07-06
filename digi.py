import requests
from bs4 import BeautifulSoup as bs


class scrape_digi:
    def __init__(self, msisdn, password):
        self.sess = requests.Session()
        payload_dict = {
            "cliendId": "90",
            "loginType": "ANY",
            "msisdn": msisdn,
            "password": password,
            "showCaptcha": "",
            "tabSelected": "0",
        }
        self.sess.post(
            "https://digicelid.digicelgroup.com/login.do?originalURI=https%3A%2F%2Fdigicelid.digicelgroup.com%2Fpermissions.do%3Fresponse_type%3Dcode%26client_id%3D90%26scope%3DGET_ACCOUNT%26redirect_uri%3Dhttps%253A%252F%252Fbillpaynow.digicelgroup.com%253A8080%252Fbill-pay-now%252FOAuthReceiver%26country_code%3DJAM%26state%3DaccountTypeValue%253D0",
            data=payload_dict,
        )

    def bill_for(self, account_number: str):
        account_sess = self.sess.get(
            "https://billpaynow.digicelgroup.com:8080/bill-pay-now/billPay?accountTypeValue=1&playAccountNumber=" + account_number
        )
        soup = bs(account_sess.text, "html.parser")
        try:
            account_bill = float(
                soup.find("h4", class_="digi-currency")
                .text.replace("TT", "")
                .replace("$", "")
                .replace(" ", "")
            )
            return account_bill

        except ValueError:
            return "Error"
