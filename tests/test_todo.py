import allure
from playwright.sync_api import expect


@allure.feature('TodoMVC')
@allure.story('Добавление задачи')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Добавление новой задачи в TodoMVC')
def test_add_todo(page):
    with allure.step('Открыть страницу TodoMVC'):
        page.goto("https://demo.playwright.dev/todomvc/#/")

    with allure.step('Добавить новую задачу'):
        input_field = page.get_by_placeholder("What needs to be done?")
        input_field.click()
        input_field.fill("Создать первый сценарий playwright")
        input_field.press("Enter")


@allure.feature('Locators')
@allure.story('Использование locator.and_')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Клик по кнопке с составным локатором')
def test_locator_and(page):
    with allure.step('Открыть страницу с примером локаторов'):
        page.goto("https://zimaev.github.io/locatorand/")

    with allure.step('Найти кнопку с role и title и кликнуть'):
        selector = page.get_by_role("button", name="Sing up") \
            .and_(page.get_by_title("Sing up today"))
        selector.click()


@allure.feature('Form elements')
@allure.story('Checkboxes and radios')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Работа с чекбоксами и радиокнопками')
def test_checkbox(page):
    with allure.step('Открыть страницу с чекбоксами и радиокнопками'):
        page.goto('https://zimaev.github.io/checks-radios/')

    with allure.step('Кликнуть по чекбоксам и радиокнопкам'):
        page.locator("text=Default checkbox").click()
        page.locator("text=Checked checkbox").click()
        page.locator("text=Default radio").click()
        page.locator("text=Default checked radio").click()
        page.locator("text=Checked switch checkbox input").click()


@allure.feature('Form elements')
@allure.story('Select')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Выбор нескольких значений в select')
def test_select_multiple(page):
    with allure.step('Открыть страницу с select'):
        page.goto('https://zimaev.github.io/select/')

    with allure.step('Выбрать несколько значений'):
        page.select_option('#skills', value=["playwright", "python"])


@allure.feature('UI interactions')
@allure.story('Drag and Drop')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Перетаскивание элемента drag and drop')
def test_drag_and_drop(page):
    with allure.step('Открыть страницу drag and drop'):
        page.goto('https://zimaev.github.io/draganddrop/')

    with allure.step('Перетащить элемент в область drop'):
        page.drag_and_drop("#drag", "#drop")


@allure.feature('Dialogs')
@allure.story('Browser dialogs')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Обработка confirmation диалога')
def test_dialogs(page):
    with allure.step('Открыть страницу с диалогами'):
        page.goto("https://zimaev.github.io/dialog/")

    with allure.step('Принять confirmation диалог'):
        page.on("dialog", lambda dialog: dialog.accept())
        page.get_by_text("Диалог Confirmation").click()


@allure.feature('Tabs')
@allure.story('Work with new tab')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка открытия новой вкладки')
def test_new_tab(page):
    with allure.step('Открыть страницу с вкладками'):
        page.goto("https://zimaev.github.io/tabs/")

    with allure.step('Открыть Dashboard в новой вкладке'):
        with page.context.expect_page() as tab:
            page.get_by_text("Переход к Dashboard").click()

    with allure.step('Проверить URL и кнопку выхода'):
        new_tab = tab.value
        assert new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"
        sign_out = new_tab.locator('.nav-link', has_text='Sign out')
        assert sign_out.is_visible()


@allure.feature('TodoMVC')
@allure.story('Работа с задачами')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Добавление и завершение задач')
def test_todo(page):
    with allure.step('Открыть страницу TodoMVC'):
        page.goto('https://demo.playwright.dev/todomvc/#/')
        expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")

    with allure.step('Добавить две задачи'):
        input_field = page.get_by_placeholder('What needs to be done?')
        expect(input_field).to_be_empty()

        input_field.fill("Закончить курс по playwright")
        input_field.press('Enter')

        input_field.fill("Добавить в резюме, что умею автоматизировать")
        input_field.press('Enter')

    with allure.step('Проверить количество задач'):
        todo_item = page.get_by_test_id('todo-item')
        expect(todo_item).to_have_count(2)

    with allure.step('Отметить первую задачу выполненной'):
        todo_item.get_by_role('checkbox').nth(0).click()
        expect(todo_item.nth(0)).to_have_class('completed')
