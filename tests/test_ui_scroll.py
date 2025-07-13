# import allure

# def test_scroll_up_using_arrow_button(page):
#     with allure.step("Відкриваємо головну сторінку"):
#         page.goto("https://automationexercise.com")

#     with allure.step("Скролимо вниз до футера"):
#         page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#         assert page.locator("text=SUBSCRIPTION").is_visible()

#     with allure.step("Натискаємо стрілку вгору"):
#         page.click("xpath=//i[@class='fa fa-angle-up']")
#         page.wait_for_timeout(1000)

#     with allure.step("Перевіряємо заголовок нагорі"):
#         assert page.locator("text=Full-Fledged practice website for Automation Engineers").is_visible()


# def test_scroll_up_manual_scroll(page):
#     with allure.step("Відкриваємо головну сторінку"):
#         page.goto("https://automationexercise.com")

#     with allure.step("Скролимо вниз до футера"):
#         page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#         assert page.locator("text=SUBSCRIPTION").is_visible()

#     with allure.step("Скролимо вручну вгору"):
#         page.evaluate("window.scrollTo(0, 0)")
#         page.wait_for_timeout(1000)

#     with allure.step("Перевіряємо заголовок нагорі"):
#         assert page.locator("text=Full-Fledged practice website for Automation Engineers").is_visible()