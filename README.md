# Sprint_6

## Финальный проект 6 спринта
<hr>

## Студент: Андрей Панин

## <h>Когорта: #21</h>
<hr>

## <h>Project: Яндекс.Самокат</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve ./allure-results


<hr>

<h3 align="left" style="color:yellow">Project files and description:</h3>

| Название файла                           | Содержание файла                                              |
|------------------------------------------|---------------------------------------------------------------|
| allure-results.dir                       | Папка с отчетами Allure                                         |                                                               |
| locators                                 | Директория с локаторами                                       |
| main_page_locators.py                    | Локаторы главной страницы Я.Самокат                           |
| order_form_page_one_locators.py          | Локаторы первой страницы формы заказа Самоката                |
| order_form_page_two_locators.py          | Локаторы второй страницы формы заказа Самоката                |
| transition_locators.py                   | Локаторы для перехода на веб-страницы                         |
| pages                                    | Директория с page objects                                     |
| main_page.py                             | Главные методы работы с элементами на странице                |
| main_page_check_key_questions_section.py | Методы для проверки текста ответов на "Вопросы о важном"      |
| order_form_page_one.py                   | Методы для первой страницы оформления заказа                  |
| order_form_page_two.py                   | Методы для второй страницы оформления заказа                  |
| transitions.py                           | Методы для редиректов                                         |
| tests                                    | Директория с тестами                                          |
| conftest.py                              | Фикстуры                                                      |
| test_first_set_of_data.py                | Тесты c первым набором данных                                 |
| test_key_questions.py                    | Тесты на проверку текста в ответах раздела "Вопросы о важном" |
| test_second_set_of_data.py               | Тесты со вторым набором данных                                |
| curl.py                                  | Файл с url-ами                                                |
| data.py                                  | Файл с тестовыми данными                                      |
| helpers.py                               | Хэлперы для тестов                                            |
| README.md                                | README-файл                                                   |
| requirements.txt                         | Файл с зависимостями                                          |
