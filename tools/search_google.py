from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def google_search(keyword):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    
    # 구글 검색창에 keyword를 넣어서 검색 실시
    url = "https://www.google.com/search?q=" + keyword + "&sxsrf=AB5stBjztTkg52tW1DpB7DGcN-cPBaIY2Q%3A1689743132266&source=hp&ei=HG-3ZPqBDtCsoAT2pJz4DQ&iflsig=AD69kcEAAAAAZLd9LAXArOLU-JyzxLJN9cjuhEOs6Bio&ved=0ahUKEwj6_6HZ_5mAAxVQFogKHXYSB98Q4dUDCAs&uact=5&oq=%EA%B2%80%EC%83%89%EC%96%B4&gs_lp=Egdnd3Mtd2l6IgnqsoDsg4nslrQyBRAAGIAEMgUQABiABDIFEC4YgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAESK8MUJ4FWIELcAF4AJABAJgBkQGgAfUGqgEDMS43uAEDyAEA-AEBqAIKwgIHECMY6gIYJ8ICBxAjGIoFGCfCAgQQIxgnwgIREC4YgAQYsQMYgwEYxwEY0QPCAgsQABiABBixAxiDAcICCxAuGIAEGLEDGIMBwgIEEAAYA8ICChAAGIAEGBQYhwI&sclient=gws-wiz"
    driver.get(url)
