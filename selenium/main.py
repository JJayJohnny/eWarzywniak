from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

NUMBER_OF_CATEGORIES=2
PRODUCTS_FOR_CATEGORY=5
PRODUCTS_TO_DELETE=3

def randomMail():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '@' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=5)) + '.com'

def visitProduct(product, driver: webdriver.Firefox):
    product.click()
    try:
        productQuantities = driver.find_element(By.CLASS_NAME, "product-quantities")
        productQuantity = productQuantities.find_element(By.TAG_NAME, "span").get_attribute("data-stock")

        driver.find_element(By.ID, "quantity_wanted").send_keys(Keys.CONTROL, 'a')
        driver.find_element(By.ID, "quantity_wanted").send_keys(Keys.BACKSPACE)
        driver.find_element(By.ID, "quantity_wanted").send_keys(str(random.randint(1, int(productQuantity))))
    except:
        # out of stock
        driver.back()
        return 0
   
    driver.find_element(By.CLASS_NAME, "add-to-cart").click()
    
    WebDriverWait(driver=driver, timeout=5).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, "close")))

    driver.back()
    # sometimes one back is not enough
    if len(driver.find_elements(By.CLASS_NAME, "product")) == 0:
        driver.back()
    return 1

def visitCategory(category, driver: webdriver.Firefox, remainingProducts, addedProducts):
    category.click()

    products = driver.find_elements(By.CLASS_NAME, "product")
    newProducts = 0
    if len(products) >= min(PRODUCTS_FOR_CATEGORY, remainingProducts):
        i=0
        while newProducts < min(PRODUCTS_FOR_CATEGORY, remainingProducts):
            product = driver.find_elements(By.CLASS_NAME, "product")[i]
            if product.text not in addedProducts:
                if visitProduct(product, driver) == 1:
                    addedProducts.append(driver.find_elements(By.CLASS_NAME, "product")[i].text)
                    newProducts += 1
                if i >= len(products)-1:
                    break
            i+=1

    driver.back()


def searchProducts(driver: webdriver.Firefox):

    WebDriverWait(driver=driver, timeout=5).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, "ui-autocomplete-input")))
    driver.find_element(By.CLASS_NAME, "ui-autocomplete-input").send_keys("napoj")
    driver.find_element(By.CLASS_NAME, "ui-autocomplete-input").send_keys(Keys.ENTER)

    WebDriverWait(driver=driver, timeout=10).until(EC.visibility_of_element_located((By.CLASS_NAME, "h2")))

    visitedProducts = []
    added = False
    while not added:
        products = driver.find_elements(By.CLASS_NAME, "product")
        product = random.choice(products)
        products.remove(product)
        while product in visitedProducts:
            product = random.choice(products)
            products.remove(product)
        visitedProducts.append(product)

        if visitProduct(product, driver) == 1:
            added = True

def visitCart(driver: webdriver.Firefox):
    driver.find_element(By.ID, "_desktop_cart").click()

    for i in range(PRODUCTS_TO_DELETE):
        removeButtons = driver.find_elements(By.CLASS_NAME, "remove-from-cart")
        removeButtons[i].click()
    driver.refresh()

def registerAccount(driver: webdriver.Firefox):
    driver.find_element(By.CLASS_NAME, "user-info").click()

    driver.find_element(By.CLASS_NAME, "no-account").click()

    driver.find_element(By.ID, "field-id_gender-1").click()
    driver.find_element(By.ID, "field-firstname").send_keys("Imie")
    driver.find_element(By.ID, "field-lastname").send_keys("Nazwisko")
    driver.find_element(By.ID, "field-email").send_keys(randomMail())
    driver.find_element(By.ID, "field-password").send_keys("password123")
    driver.find_element(By.NAME, "customer_privacy").click()
    driver.find_element(By.NAME, "psgdpr").click()
    driver.find_element(By.CLASS_NAME, "form-control-submit").click()
    
    WebDriverWait(driver=driver, timeout=30).until(EC.visibility_of_element_located((By.CLASS_NAME, "banner")))
    banner = driver.find_element(By.CLASS_NAME, "banner")

def makeOrder(driver: webdriver.Firefox):
    driver.find_element(By.ID, "_desktop_cart").click()
    driver.find_element(By.CLASS_NAME, "btn-primary").click()

    driver.find_element(By.ID, "field-address1").send_keys("ul. Ulica 22")
    driver.find_element(By.ID, "field-postcode").send_keys("11-111")
    driver.find_element(By.ID, "field-city").send_keys("Miasto")
    driver.find_element(By.NAME, "confirm-addresses").click()

    driver.find_element(By.ID, "delivery_option_17").click()
    driver.find_element(By.NAME, "confirmDeliveryOption").click()

    driver.find_element(By.ID, "payment-option-2").click()
    driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()
    driver.find_element(By.ID, "payment-confirmation").find_element(By.CLASS_NAME, "btn-primary").click()

def downloadInvoice(driver: webdriver.Firefox):
    WebDriverWait(driver=driver, timeout=60).until(EC.visibility_of_element_located((By.CLASS_NAME, "account")))
    driver.find_element(By.CLASS_NAME, "account").click()

    driver.find_element(By.ID, "history-link").click()
    
    # orderActions = driver.find_element(By.CLASS_NAME, "order-actions")
    # for a in orderActions.find_elements(By.TAG_NAME, "a"):
    #     if a.text == "Szczegóły":
    #         a.click()
            # break
    
    WebDriverWait(driver=driver, timeout=10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td.text-sm-center:nth-child(6) > a:nth-child(1)")))
    driver.find_element(By.CSS_SELECTOR, "td.text-sm-center:nth-child(6) > a:nth-child(1)").click()

driver = webdriver.Firefox()

driver.get("https://localhost/")

driver.find_element(By.CLASS_NAME, "category").click()

addedProducts = []
visitedCategories = []

while len(addedProducts) < NUMBER_OF_CATEGORIES*PRODUCTS_FOR_CATEGORY:
    categoryMenu = driver.find_element(By.CLASS_NAME, "category-sub-menu")
    categories = categoryMenu.find_elements(By.TAG_NAME, "li")

    category = random.choice(categories)
    categories.remove(category)
    while category.text in visitedCategories:
        category = random.choice(categories)
        categories.remove(category)
    visitedCategories.append(category.text)
    
    visitCategory(category, driver, PRODUCTS_FOR_CATEGORY*NUMBER_OF_CATEGORIES - len(addedProducts), addedProducts)

searchProducts(driver)
visitCart(driver)
registerAccount(driver)
makeOrder(driver)
downloadInvoice(driver)