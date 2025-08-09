from selenium import webdriver
import time






'''
请先配置selenium的chromedriver，并将chromedriver的路径添加到环境变量中。

'''
#print(driver.get_cookies())
def get_cookies(url:str=r'https://www.goofish.com/'):
    options = webdriver.ChromeOptions()
    #options.debugger_address="127.0.0.1:9222"
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--user-data-dir=/home/fs/data/seleniumDocument')
    driver=webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(0.5)
    print(driver.title)
    #print(cookies:=driver.get_cookies())
    driver.get_screenshot_as_file("./ts.png")
    cookies=driver.get_cookies()
    #print(driver.page_source)
    driver.close()
    
    ckstr=''

    for cookie in cookies:
        #print(cookie)
        ckstr+=cookie['name']+'='+cookie['value']+';'
    return ckstr
    
    
    
if __name__ == '__main__':

    #cookies=get_cookies(url="https://www.goofish.com/search?spm=a21ybx.item.searchHistory.1.29793da6E2i00Q&q=4070s")
    cookies=get_cookies(url="https://www.goofish.com/")
    print(cookies)
