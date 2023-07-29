from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
dosya = open("iyiyorumlar.txt", "a", encoding='utf-8')
chrome_options = Options()
chrome_options.add_argument("--headless") 
ark = ("C:\\Users\\PC\\Downloads\\chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, executable_path=ark)
url = "https://www.trendyol.com/oldubil/on-odemeli-kart-p-313718199/yorumlar"
driver.get(url)
time.sleep(9)
driver.find_element_by_xpath("//*[@id='onetrust-accept-btn-handler']").click()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 100);")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div/div[1]/div/div[6]/div[2]/div[2]/div[1]").click()
time.sleep(6)
html_content = driver.page_source
driver.quit()
soup = BeautifulSoup(html_content, "html.parser")
comments = soup.find_all("p")
for comment in comments:
    if not comment.has_attr("class") and not comment.has_attr("div") and not comment.has_attr("span") and not comment.has_attr("id"):
        if comment.text != "10.000’lerce yeni ürünü ve sezon trendlerini büyük indirimlerle yakalamak için,":
            if comment.text != "Sepetinizde Ürün Bulunmamaktadır.":
                if comment.text != "Popüler Marka ve Mağazalar":
                    if comment.text != "Popüler Sayfalar":
                        dosya.write(comment.text+"\n")
                        print(comment.text)


dosya.close()




