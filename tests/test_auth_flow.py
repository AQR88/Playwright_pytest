import allure
import pytest

@allure.step("Go to Signup/Login")
def go_to_signup_login(page):
    page.goto("https://automationexercise.com") 
    page.wait_for_timeout(1000)
    page.click("a[href='/login']")
    allure.attach(page.screenshot(), name="SignupLogin", attachment_type=allure.attachment_type.PNG)

@allure.step("Register new user")
def register_user(page, name, email):
    page.fill("input[name='name']", name)
    page.fill("input[data-qa='signup-email']", email)
    page.click("button[data-qa='signup-button']")
    page.check("#id_gender1")
    page.fill("#password", "TestPass123")
    page.select_option("#days", "10")
    page.select_option("#months", "5")
    page.select_option("#years", "1999")
    page.check("#newsletter")
    page.check("#optin")
    page.fill("#first_name", "Tymur")
    page.fill("#last_name", "Testovich")
    page.fill("#company", "TestCorp")
    page.fill("#address1", "123 Test Street")
    page.fill("#address2", "Suite 456")
    page.select_option("#country", "Canada")
    page.fill("#state", "TestState")
    page.fill("#city", "TestCity")
    page.fill("#zipcode", "12345")
    page.fill("#mobile_number", "1234567890")
    page.click("button[data-qa='create-account']")
    page.click("text=Continue")

@allure.step("Login with credentials")
def login_user(page, email, password):
    page.fill("input[data-qa='login-email']", email)
    page.fill("input[data-qa='login-password']", password)
    page.click("button[data-qa='login-button']")

@allure.step("Delete account")
def delete_account(page):
    page.click("text=Delete Account")
    assert page.get_by_text("ACCOUNT DELETED!").is_visible()
    page.click("text=Continue")


def test_register_user(page, test_user):
    go_to_signup_login(page)
    register_user(page, test_user["name"], test_user["email"])
    assert page.locator("text=Logged in as").is_visible()
    delete_account(page)


def test_login_user_correct(page, ensure_registered_user, test_user):
    go_to_signup_login(page)
    login_user(page, test_user["email"], test_user["password"])
    assert page.locator("text=Logged in as").is_visible()
    delete_account(page)


def test_login_user_incorrect(page):
    go_to_signup_login(page)
    login_user(page, "invalid@example.com", "WrongPass123")
    assert page.locator("text=Your email or password is incorrect!").is_visible()


def test_logout_user(page, ensure_registered_user, test_user):
    go_to_signup_login(page)
    login_user(page, test_user["email"], test_user["password"])
    assert page.locator("text=Logged in as").is_visible()
    page.click("text=Logout")
    assert page.locator("text=Login to your account").is_visible()


def test_register_existing_email(page, ensure_registered_user, test_user):
    go_to_signup_login(page)
    page.fill("input[name='name']", "ExistingUser")
    page.fill("input[data-qa='signup-email']", test_user["email"])
    page.click("button[data-qa='signup-button']")
    assert page.locator("text=Email Address already exist!").is_visible()