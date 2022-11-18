import random
import string
from datetime import timedelta
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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

def register_new_account(driver):
    try:
        driver.get("http://localhost:8080/logowanie?create_account=1")
        
        gender = driver.find_element(By.ID, "field-id_gender-1")
        gender.click()

        firstname = driver.find_element(By.ID, "field-firstname")
        firstname.send_keys("Janusz")

        lastname = driver.find_element(By.ID, "field-lastname")
        lastname.send_keys("Kowalski")

        email = driver.find_element(By.ID, "field-email")
        email.send_keys(random_char(15).lower() + "@some.email.com")

        password = driver.find_element(By.ID, "field-password")
        password.send_keys("abrakadabra")

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
        
        driver.find_element_by_xpath("//button[@class='btn btn-primary form-control-submit float-xs-right']").click()
        return True
    except:
        pass

def add_random_product_to_basket(driver, amount):
    try:
        product_pages = []
        product_pages.append("http://localhost:8080/2-strona-glowna")
        for i in range(2, 40):
            product_pages.append(f"http://localhost:8080/2-strona-glowna?page={i}")
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

        driver.find_element_by_xpath("//button[@class='btn btn-primary add-to-cart']").click()
        driver.get(link)
        return True
    except:
        pass

def remove_random_product_from_basket(driver):
    try:
        driver.get("http://localhost:8080/koszyk?action=show")

        products = driver.find_elements(By.CLASS_NAME, "remove-from-cart")
        for i in range(0, len(products)):
            products[i] = products[i].get_attribute("href")
        product = random.choice(products)
        driver.get(product)
        return True
    except:
        pass

def select_cash_on_delivery(driver):
    try:
        cod = driver.find_element(By.ID, "payment-option-2")
        cod.click()
        return True
    except:
        pass

def select_delivery_method(driver):
    li = []
    li.append(driver.find_element(By.ID, "delivery_option_17"))
    li.append(driver.find_element(By.ID, "delivery_option_16"))
    li.append(driver.find_element(By.ID, "delivery_option_14"))
    try:
        random.choice(li).click()
    except:
        pass

    try:
        driver.find_element_by_xpath("//button[@name='confirmDeliveryOption']").click()
        return True
    except:
        pass

def confirm_order(driver):
    try:
        conditions_to_approve = driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]")
        conditions_to_approve.click()
        driver.find_element_by_xpath("//button[@class='btn btn-primary center-block']").click()
        return True
    except:
        pass

def do_checkout(driver):
    try:
        driver.get("http://localhost:8080/zam%C3%B3wienie")

        address = driver.find_element(By.NAME, "address1")
        address.send_keys("Gabriela Narutowicza 11/12")
        
        postcode = driver.find_element(By.NAME, "postcode")
        postcode.send_keys("80-233")

        city = driver.find_element(By.NAME, "city")
        city.send_keys("Gdańsk")

        driver.find_element_by_xpath("//button[@name='confirm-addresses']").click()

        if select_delivery_method(driver):
            if select_cash_on_delivery(driver):
                if confirm_order(driver):
                    return True
    except:
        pass

def check_order_status(driver):
    try:
        driver.get("http://localhost:8080/historia-zamowien")

        li = driver.find_elements(By.TAG_NAME, "a")
        for x in li:
            if x.text.lower().endswith("szczegóły"):
                link = x.get_attribute("href")
                driver.get(link)
                return True
    except:
        pass

def run_test_scenario():
    driver = webdriver.Edge(executable_path = r"C:\Users\strielok\Documents\Repo\studia\projekt_biznes_elektroniczny\tests\msedgedriver.exe")
    driver.minimize_window()

    print("Executing register_new_account...")
    assert register_new_account(driver), "register new account with valid data should succeed"
    print("Executing add_random_product_to_basket #1...")
    assert add_random_product_to_basket(driver, random.randint(1, 5)) == True, "add product #1 to basket should succeed"
    print("Executing add_random_product_to_basket #2...")
    assert add_random_product_to_basket(driver, random.randint(1, 5)) == True, "add product #2 to basket should succeed"
    print("Executing add_random_product_to_basket #3...")
    assert add_random_product_to_basket(driver, random.randint(1, 5)) == True, "add product #3 to basket should succeed"
    print("Executing add_random_product_to_basket #4...")
    assert add_random_product_to_basket(driver, random.randint(1, 5)) == True, "add product #4 to basket should succeed"
    print("Executing add_random_product_to_basket #5...")
    assert add_random_product_to_basket(driver, random.randint(1, 5)) == True, "add product #5 to basket should succeed"
    print("Executing add_random_product_to_basket #6...")
    assert add_random_product_to_basket(driver, random.randint(1, 5)) == True, "add product #6 to basket should succeed"
    print("Executing add_random_product_to_basket #7...")
    assert add_random_product_to_basket(driver, random.randint(1, 5)) == True, "add product #7 to basket should succeed"
    print("Executing add_random_product_to_basket #8...")
    assert add_random_product_to_basket(driver, random.randint(1, 5)) == True, "add product #8 to basket should succeed"
    print("Executing add_random_product_to_basket #9...")
    assert add_random_product_to_basket(driver, random.randint(1, 5)) == True, "add product #9 to basket should succeed"
    print("Executing add_random_product_to_basket #10...")
    assert add_random_product_to_basket(driver, random.randint(1, 5)) == True, "add product #10 to basket should succeed"
    print("Executing remove_random_product_from_basket...")
    assert remove_random_product_from_basket(driver), "remove random product from non-empty basket should succeed"
    print("Executing do_checkout...")
    assert do_checkout(driver), "checkout of non-empty basket should succeed"
    print("Executing check_order_status...")
    assert check_order_status(driver), "check order status when order has been placed should succeed"
    print("All OK!")

run_test_scenario()

# Workaround to keep brower window opened after test execution
while True:
    pass
