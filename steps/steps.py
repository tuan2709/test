from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

@given('we stay at Hot Deal page')
def step(context):
   context.browser.get('https://www.fahasa.com/deal-hot-pages')

@when('click to add a book')
def step(context):
   driver = context.browser
   xBooks = driver.find_elements(By.XPATH, "//a[@class='product-image']")
   xBooks[0].click()

@then('cart add this book to cart')
def step(context):
   assert context.browser.title.find(r"Sách") >= 0