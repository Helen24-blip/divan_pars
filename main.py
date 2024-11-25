import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация веб-драйвера
driver = webdriver.Chrome()

# URL страницы
url = "https://www.divan.ru/category/svet"
driver.get(url)

# Ждем, чтобы контент загрузился
time.sleep(5)

# Открываем CSV файл для записи
with open('lights.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Записываем заголовки в CSV
    writer.writerow(['Название', 'Цена', 'Ссылка'])

    # Находим все элементы с товарами
    lights = driver.find_elements(By.CSS_SELECTOR, 'div.LlPhw')

    for light in lights:
        try:
            # Извлекаем название
            name = light.find_element(By.CSS_SELECTOR, 'div.lsooF span').text

            # Извлекаем цену
            price = light.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text

            # Извлекаем ссылку
            url = light.find_element(By.TAG_NAME, 'a').get_attribute('href')

            # Пишем данные в CSV
            writer.writerow([name, price, url])
        except Exception as e:
            print(f"Ошибка при обработке элемента: {e}")

# Закрываем драйвер
driver.quit()
print("Данные успешно сохранены в файл lights.csv")
