import allure
from playwright.sync_api import expect

def test_contact_us_form(page):
    with allure.step("Відкриваємо Contact Us"):
        page.goto("https://automationexercise.com")
        page.click("text=Contact Us")

    with allure.step("Перевірка 'GET IN TOUCH'"):
        expect(page.locator("text=Get In Touch")).to_be_visible()

    with allure.step("Заповнюємо форму"):
        page.fill("input[name='name']", "TymurTest")
        page.fill("input[name='email']", "tymur@example.com")
        page.fill("input[name='subject']", "Feedback")
        page.fill("textarea[name='message']", "Автоматизоване повідомлення через Playwright.")
        page.set_input_files("input[name='upload_file']", "README.md")

    with allure.step("Відправляємо форму"):
        page.click("input[type='submit']")
        page.once("dialog", lambda dialog: dialog.accept())
        page.wait_for_load_state("networkidle")

    with allure.step("Перевірка успішного повідомлення"):
        expect(page.locator("text=Success! Your details have been submitted successfully.")).to_be_visible()

    with allure.step("Повернення на домашню сторінку"):
        page.click("text=Home")
        expect(page).to_have_url("https://automationexercise.com/")


