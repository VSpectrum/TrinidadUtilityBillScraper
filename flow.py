import requests as req
from bs4 import BeautifulSoup as bs


def scrape_flow(account_id, passwd):
    sess = req.Session()
    payload = {
        "ctl00$cphMain$userName": account_id,
        "ctl00$cphMain$loginButton": "Log in",
        "ctl00$cphMain$password": passwd,
    }
    url = "https://myaccount.discoverflow.co/Trinidad/Login/Login.aspx"
    response = sess.get(url)
    soup = bs(response.text, "html.parser")
    view_state = soup.find("input", {"id": "__VIEWSTATE"})["value"]
    event_val = soup.find("input", {"id": "__EVENTVALIDATION"})["value"]

    payload["__VIEWSTATE"] = view_state
    payload["__EVENTVALIDATION"] = event_val
    response = sess.post(url, data=payload)

    response = sess.get(
        "https://myaccount.discoverflow.co/Trinidad/Payment/MPayment.aspx"
    )
    soup = bs(response.text, "html.parser")

    try:
        bill = float(
            soup.find(
                "input", {"name": "ctl00$cphMain$WzdPaymentWizard$inputCurrentBalance"}
            )["value"]
        )
        return bill

    except ValueError:
        return "Error"
