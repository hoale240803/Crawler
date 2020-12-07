from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException #Timeout Exception Errors
from selenium.webdriver.support.ui import WebDriverWait # Wait time
from selenium.webdriver.support import expected_conditions as EC # for conditions



options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

## fix https://stackoverflow.com/questions/61561112/how-to-solve-getting-default-adapter-failed-error-when-launching-chrome-and-tr
driver = webdriver.Chrome(options=options, executable_path=r'E:\WorkSpace\_capstone\crawler\chrome-driver\chromedriver.exe')
driver.get("https://tatoeba.org/eng/downloads")

# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector

# link_text = driver.find_elements_by_link_text("Filename")
# href_tag_names = driver.find_elements_by_tag_name("a")
### click a element
# xpath=driver.find_element_by_xpath('//*[@id="main_content"]/div/div[2]/dl/dd[1]/p/a')
# xpath.click()
### input a textfile
# search_bar=driver.find_element_by_xpath('//*[@id="query"]')
# search_bar.click()
# search_bar.send_keys("hello")

### click search button
# btn_search=driver.find_element_by_xpath('//*[@id="new-search-bar"]/div/div[1]/button')
# btn_search.click()

###
def download_sentences_file():
    # tìm đến combobox download file và click()
    sentences_selection=driver.find_element_by_xpath('//*[@id="select_394"]')
    sentences_selection.click()
    # /html/body/div[7]/md-select-menu/md-content/md-option[1]
    ## //*[@id="main_content"]/div/div[1]/dl/dd[1]/p/a
    # lấy ra list các ngôn ngữ rồi xóa phần tử đầu và cuối(vì ko phải ngôn ngữ)
    md_options=driver.find_elements_by_xpath('/html/body/div[7]/md-select-menu/md-content/md-option')
    md_options.pop(0)
    md_options.pop(len(md_options)-1)
    print(len(md_options))
    # tiến hành download từng bộ ngôn ngữ sentences về
    for md_option in md_options:
        print(md_option.text)
        md_option.click()
        # click download
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[1]/dl/dd[1]/p/a").click()
        # click selection again to show list md-option (vì sau khi click thì combobox sẽ tắt nên click lại để nó hiện list ra)
        sentences_selection=driver.find_element_by_xpath('//*[@id="select_394"]')
        sentences_selection.click()

def search_sentence():
    timeout = 3 # time để dừng khi load trang

    try 
        element_present =EC.presence_of_element_located(By.XPATH, "xxx")
        WebDriverWait(driver,timeout).until(element_present)

        
    except TimeoutException:
        print("Timed out waiting for page load")
    finally:
        print("page loaded")

def load_sentence():
    path=r'E:\WorkSpace\_capstone\data\source\vie_sentences.tsv'
    f = open(path, encoding="utf8")
    for x in f:
        last_e=x.split("\t")
        print(last_e[2])

    
def write_sentence():
    f = open("demofile3.txt", "w")
    f.write("Woops! I have deleted the content!")
    f.close()
    
# close chrome
# driver.close()
