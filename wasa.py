import requests

def scrape_wasa(email, passwd):
    sess = requests.Session()
    payload = {'inputEmail': email, 'inputPassword': passwd}
    url = "https://novobillpay.com/wasa/main/login"
    sess.post(url, data=payload)

    wasa_page = sess.get("https://novobillpay.com/wasa/main/profile")
    
    current_balance_loc = wasa_page.text.find("Current Balance:") + len("Current Balance:")
    till_br = wasa_page.text.find("<br", current_balance_loc)
    try:
        current_balance = float(wasa_page.text[current_balance_loc:till_br].replace(" ","").replace("$",""))
        return current_balance

    except ValueError:
        return "Error"
    