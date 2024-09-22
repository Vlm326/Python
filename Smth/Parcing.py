from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

links_list = []

# Цикл по страницам
for i in range(1, 41):
    url = f'-{i}'
    try:
        driver.get(url)
        print(f"Обработка страницы {i}...")
        
        body = driver.find_element(By.TAG_NAME, 'body')
        page_text = body.text
        
        for link_type in ():
            if link_type in page_text:
                start_index = page_text.find(link_type)
                links_list.append(page_text[start_index-20:start_index+30])
                print(f"Найдена ссылка: {link_type}")
    except Exception as e:
        print(f"Ошибка при обработке страницы {i}: {e}")

print("Список всех найденных ссылок:")
for link in links_list:
    print(link)

driver.quit()