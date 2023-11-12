from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

NUMBER_OF_CATEGORIES=2
PRODUCTS_FOR_CATEGORY=5

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
                elif i >= len(products)-1:
                    break
            i+=1

    driver.back()

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

# driver.quit()