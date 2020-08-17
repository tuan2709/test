from selenium import webdriver

def before_all(context):
	context.browser = webdriver.Chrome(
		executable_path=r"D:\automation\Behave\testFahasa\chromedriver.exe"
	)
    
def after_all(context):
	context.browser.quit()