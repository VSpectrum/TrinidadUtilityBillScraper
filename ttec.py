import requests
from bs4 import BeautifulSoup as bs


class scrape_ttec:
    def __init__(self, username, passwd):
        """
        scrape_ttec("my_username", "my_password") initializes the logged in session with ttec
        """
        self.session = requests.Session()
        payload = {"userid": username, "pin": passwd, "JavaScript": "enabled"}
        url = "https://cwa.ttec.co.tt/CSPROD_cwa/uwpqutil.p_VALLOGIN"
        self.session.post(url, data=payload)

    def bill_for(self, account_number: str):
        """
        scrape_ttec_object.bill_for("123456678") returns the money you owe to ttec as a float
        """
        account = self.session.get(
            "https://cwa.ttec.co.tt/CSPROD_cwa/uwpqmult.p_uwapacct?accountnbr=" + account_number
        )
        soup = bs(account.text, "html.parser")
        tds = [x.get_text().replace(" ", "") for x in soup.find_all("td") if x.get_text().replace(" ", "") != ""]
        try:
            account_bill = float(tds[7].replace(",", ""))
            return account_bill

        except ValueError:
            return "Error"
