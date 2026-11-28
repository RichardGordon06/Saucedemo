import allure
from selenium.webdriver.common.by import By


@allure.title('Тестирование локаторов Saucedemo')
def test_locators(browser):
    browser.get("https://www.saucedemo.com/")
    login = 'standard_user'
    password = 'secret_sauce'
    log_field = browser.find_element(By.ID, 'user-name')
    pass_field = browser.find_element(By.NAME, 'password')
    enter_button = browser.find_element(By.CLASS_NAME, 'submit-button')
    tag = browser.find_element(By.TAG_NAME, 'form')
    log_field.send_keys(login)
    pass_field.send_keys(password)
    enter_button.click()
    link = browser.find_element(By.LINK_TEXT, 'Sauce Labs Bike Light')
    partial_link = browser.find_element(By.PARTIAL_LINK_TEXT, 'Backpack')

    #XPATH
    atribute = browser.find_element(By.XPATH, "//select[@aria-label='Sort products']")
    text = browser.find_element(By.XPATH, "//div[text() = 'Sauce Labs Onesie']")
    contain_atribute = browser.find_element(By.XPATH, "//div[contains(@id,'menu')]")
    contain_text = browser.find_element(By.XPATH, "//div[contains(text(),'Onesie')]")
    ancestor = browser.find_element(By.XPATH, "//div[@class='inventory_item']/ancestor::body")
    descendant = browser.find_element(By.XPATH, "//div[@class='inventory_list']/descendant::button[1]")
    following_sibling = browser.find_element(By.XPATH, "//ul[@class='social']//following-sibling::div")
    parent = browser.find_element(By.XPATH, "//div[@class='inventory_item']/parent::div")
    preceding_sibling = browser.find_element(By.XPATH, "//ul[@class='social']//preceding-sibling::li[1]")
    atribute_and = browser.find_element(By.XPATH, "//a[@id='item_5_title_link' and @aria-label='View details for Sauce Labs Fleece Jacket']")

    #CSS
    class_ = browser.find_element(By.CSS_SELECTOR, ".social")
    class_class = browser.find_elements(By.CSS_SELECTOR, ".bm-item.menu-item")  #Не нашёл одиночного элемента с таким локатором, пришлось делать elementS
    class__class = browser.find_element(By.CSS_SELECTOR, ".social .social_x")
    id = browser.find_element(By.CSS_SELECTOR, "#inventory_sidebar_link")
    tagname = browser.find_element(By.CSS_SELECTOR, "head")
    tagname_class = browser.find_element(By.CSS_SELECTOR, "div.right_component")
    attribute_value_1 = browser.find_element(By.CSS_SELECTOR, "[data-test=shopping-cart-link]")
    attribute_value_2 = browser.find_elements(By.CSS_SELECTOR, "[aria-label~='Jacket']") #Не нашёл одиночного элемента с таким локатором, пришлось делать elementS
    attribute_value_3 = browser.find_element(By.CSS_SELECTOR, "[data-test|='product']")
    attribute_value_4 = browser.find_element(By.CSS_SELECTOR, "[aria-label^='Cart']")
    #attribute_value_5 = browser.find_element(By.CSS_SELECTOR, "[aria-label$='items']") С этим селектором проблема из-за символа $, он падает с ошибкой, мол Selenium не понимает $
    attribute_value_6 = browser.find_element(By.CSS_SELECTOR, "[data-test*='active']")

