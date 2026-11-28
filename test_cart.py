import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title('Тестирование корзины товаров Saucedemo')
@allure.severity(allure.severity_level.MINOR)
def test_cart(browser):
    browser.get("https://www.saucedemo.com/")
    login = 'standard_user'
    password = 'secret_sauce'
    log_field = browser.find_element(By.ID, 'user-name')
    pass_field = browser.find_element(By.NAME, 'password')
    log_field.send_keys(login)
    pass_field.send_keys(password)
    enter_button = browser.find_element(By.CLASS_NAME, 'submit-button')
    enter_button.click()
    product_text = browser.find_element(By.XPATH, '//*[@id="item_1_title_link"]/div').text
    product_price_text = browser.find_element(By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']/ancestor::div[@class='inventory_item']//div[@class='inventory_item_price']").text
    product = browser.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    product.click()
    cart_link = browser.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    cart_link.click()
    WebDriverWait(browser, 10).until(EC.url_contains("cart.html"))
    product_in_cart = browser.find_element(By.XPATH, '//*[@id="item_1_title_link"]/div').text
    price_in_cart = browser.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div').text
    with allure.step('Проверка названия товара, на странице товаров и в корзине'):
        assert product_in_cart == product_text, f'Название выбранного товара {product_text}, не совпадает с {product_in_cart.text} товаром находящимся в корзине'
    with allure.step('Проверка цены товара, на странице товаров и в корзине'):
        assert product_price_text == price_in_cart, f'Цена {product_price_text} не совпадает с ценой {price_in_cart} в корзине'
