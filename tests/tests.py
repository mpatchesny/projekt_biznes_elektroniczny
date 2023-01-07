import random
import string
import time
import pathlib
from datetime import timedelta
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

SLEEP_TIME_SECS = 3

# https://stackoverflow.com/questions/59231343/how-to-make-random-email-generator
def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

# https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

def register_new_account(driver, url, email_addr, pwd):
    try:
        driver.get(url)

        gender = driver.find_element(By.ID, "field-id_gender-1")
        gender.click()

        firstname = driver.find_element(By.ID, "field-firstname")
        firstname.send_keys("Janusz")

        lastname = driver.find_element(By.ID, "field-lastname")
        lastname.send_keys("Kowalski")

        email = driver.find_element(By.ID, "field-email")
        email.send_keys(email_addr)

        password = driver.find_element(By.ID, "field-password")
        password.send_keys(pwd)

        birthday = driver.find_element(By.ID, "field-birthday")
        d = random_date(datetime.strptime('1975-01-01', '%Y-%m-%d'), datetime.strptime('2000-12-31', '%Y-%m-%d'))
        birthday.send_keys(d.strftime('%Y-%m-%d'))

        check1 = driver.find_element(By.NAME, "optin")
        check1.click()

        check2 = driver.find_element(By.NAME, "customer_privacy")
        check2.click()

        check3 = driver.find_element(By.NAME, "newsletter")
        check3.click()

        check4 = driver.find_element(By.NAME, "psgdpr")
        check4.click()
        
        driver.find_element(By.XPATH, "//button[@class='btn btn-primary form-control-submit float-xs-right']").click()
        return True
    except Exception as e:
        print(e)

def is_logged_in(driver, url):
    driver.get(url)
    email = driver.find_element(By.ID, "field-email")
    return email is None

def login(driver, url, email_addr, pwd):
    try:
        driver.get(url)
        email = driver.find_element(By.ID, "field-email")
        email.send_keys(email_addr)

        password = driver.find_element(By.ID, "field-password")
        password.send_keys(pwd)

        driver.find_element(By.ID, "submit-login").click()
        return True
    except Exception as e:
        print(e)

def add_random_product_to_basket(driver, amount, url):
    try:
        product_pages = []
        product_pages.append(url)
        for i in range(2, 40):
            product_pages.append(f"{url}?page={i}")
        driver.get(random.choice(product_pages))

        links = []
        products = driver.find_elements(By.CLASS_NAME, "thumbnail")
        for x in products:
            if x.tag_name == "a":
                links.append(x.get_attribute("href"))
        link = random.choice(links)
        driver.get(link)

        quantity = driver.find_element(By.ID, "quantity_wanted")
        quantity.send_keys(Keys.CONTROL, 'a')
        quantity.send_keys(Keys.BACKSPACE)
        quantity.send_keys(amount)

        driver.find_element(By.XPATH, "//button[@class='btn btn-primary add-to-cart']").click()
        time.sleep(SLEEP_TIME_SECS)
        driver.get(link)
        return True
    except Exception as e:
        print(e)

def remove_random_product_from_basket(driver, url):
    try:
        driver.get(url)

        products = driver.find_elements(By.CLASS_NAME, "remove-from-cart")
        for i in range(0, len(products)):
            products[i] = products[i].get_attribute("href")
        product = random.choice(products)
        driver.get(product)
        return True
    except Exception as e:
        print(e)

def select_cash_on_delivery(driver):
    try:
        cod = driver.find_element(By.ID, "payment-option-2")
        cod.click()
        return True
    except Exception as e:
        print(e)

def select_delivery_method(driver):
    li = []
    li.append(driver.find_element(By.ID, "delivery_option_17"))
    li.append(driver.find_element(By.ID, "delivery_option_16"))
    li.append(driver.find_element(By.ID, "delivery_option_14"))
    try:
        random.choice(li).click()
    except Exception as e:
        print(e)

    try:
        driver.find_element(By.XPATH, "//button[@name='confirmDeliveryOption']").click()
        return True
    except Exception as e:
        print(e)

def confirm_order(driver):
    try:
        conditions_to_approve = driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]")
        conditions_to_approve.click()
        driver.find_element(By.XPATH, "//button[@class='btn btn-primary center-block']").click()
        return True
    except Exception as e:
        print(e)

def do_checkout(driver, url):
    try:
        driver.get(url)
        time.sleep(SLEEP_TIME_SECS)

        address = driver.find_element(By.NAME, "address1")
        address.send_keys("Gabriela Narutowicza 11/12")
        
        postcode = driver.find_element(By.NAME, "postcode")
        postcode.send_keys("80-233")

        city = driver.find_element(By.NAME, "city")
        city.send_keys("Gdańsk")

        driver.find_element(By.XPATH, "//button[@name='confirm-addresses']").click()

        if select_delivery_method(driver):
            time.sleep(SLEEP_TIME_SECS)
            if select_cash_on_delivery(driver):
                time.sleep(SLEEP_TIME_SECS)
                if confirm_order(driver):
                    time.sleep(SLEEP_TIME_SECS)
                    return True
    except Exception as e:
        print(e)

def check_order_status(driver, url):
    try:
        driver.get(url)
        time.sleep(SLEEP_TIME_SECS)

        li = driver.find_elements(By.TAG_NAME, "a")
        for x in li:
            if x.text.lower().endswith("szczegóły"):
                link = x.get_attribute("href")
                driver.get(link)
                return True
    except Exception as e:
        print(e)

def run_test_scenario():
    driver_path = pathlib.Path(__file__).parent.joinpath('geckodriver.exe')
    driver = webdriver.Firefox(executable_path = driver_path)
    # driver.minimize_window()

    protocol = "https"
    host = "localhost"
    port = "17229"
    url = f"{protocol}://{host}:{port}/"
    email = None
    email = random_char(15).lower() + "@some.email.com"
    pwd = "abrakadabra"

    n = 7
    print(f"Waiting {n} seconds before start...")
    time.sleep(n)

    print("Executing register_new_account...")
    assert register_new_account(driver, f"{url}logowanie?create_account=1", email_addr=email, pwd=pwd), "register new account with valid data should succeed"
    time.sleep(SLEEP_TIME_SECS)

    if not is_logged_in(driver, f"{url}moje-konto"):
        print("User not logged in, performing login...")
        time.sleep(SLEEP_TIME_SECS)
        assert login(driver, f"{url}moje-konto", email, pwd,), "login should suceed"
        time.sleep(SLEEP_TIME_SECS)

    for i in range(1, 11):
        print(f"Executing add_random_product_to_basket #{i}...")
        assert add_random_product_to_basket(driver, random.randint(1, 5), f"{url}2-strona-glowna") == True, f"add product #{i} to basket should succeed"
        time.sleep(SLEEP_TIME_SECS)

    print("Executing remove_random_product_from_basket...")
    assert remove_random_product_from_basket(driver, f"{url}koszyk?action=show"), "remove random product from non-empty basket should succeed"
    time.sleep(SLEEP_TIME_SECS)

    print("Executing do_checkout...")
    assert do_checkout(driver, f"{url}zam%C3%B3wienie"), "checkout of non-empty basket should succeed"
    time.sleep(SLEEP_TIME_SECS)
    
    print("Executing check_order_status...")
    assert check_order_status(driver, f"{url}historia-zamowien"), "check order status when order has been placed should succeed"
    time.sleep(SLEEP_TIME_SECS)
    
    print("All OK!")

run_test_scenario()

# Workaround to keep browser window opened after test execution
while True:
    pass
