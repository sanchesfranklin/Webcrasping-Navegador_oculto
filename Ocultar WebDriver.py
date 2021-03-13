from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  
chrome_options.add_argument("--headless")
WINDOW_SIZE = "1920,1080"


chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

driver = webdriver.Chrome("C:/Users/Sanches Santos/Documents/scrapping_itsa4/chromedriver.exe", chrome_options=chrome_options)
url = "https://www.infomoney.com.br/cotacoes/itausa-itsa4/"
driver.get(url)
valor_itsa4 = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[1]/div/div[3]/div[1]/p')
valor_itsa4 = valor_itsa4.get_attribute("innerHTML")
valor_itsa4 = valor_itsa4.replace(',' , '.')
valor_itsa4 = float(valor_itsa4)

print('O preço de ITSA4 é: {}'.format(valor_itsa4)) 