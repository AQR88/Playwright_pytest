import pytest
import uuid
from playwright.sync_api import sync_playwright



def pytest_addoption(parser):
    parser.addoption(
        "--my_browser",
        action="store",
        default="chromium",
        help="Browser to run tests with: chromium, firefox, webkit"
    )



@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--my_browser")

@pytest.fixture(scope="function") 
def page(browser_type):
    with sync_playwright() as p:
        browser_type = browser_type.lower()
        if browser_type not in ["chromium", "firefox", "webkit"]:
            raise ValueError(f"Invalid browser_type: {browser_type}. Use one of: chromium, firefox, webkit")

        browser = getattr(p, browser_type).launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()



@pytest.fixture(scope="session")
def test_user():
    return {
        "name": "TymurTest",
        "email": f"tymur_{uuid.uuid4().hex[:6]}@example.com",
        "password": "TestPass123"
    }
@pytest.fixture(scope="function")
def ensure_registered_user(page, test_user):
    page.context.clear_cookies()
    page.goto("https://automationexercise.com")
    page.wait_for_load_state("networkidle")

    if page.locator("text=Logout").is_visible():
        page.click("text=Logout")
        page.wait_for_selector("text=Login to your account")

    page.click("text=Signup / Login")
    page.fill("input[name='name']", test_user["name"])
    page.fill("input[data-qa='signup-email']", test_user["email"])
    page.click("button[data-qa='signup-button']")

    if page.locator("text=Email Address already exist!").is_visible():
        return  

    page.check("#id_gender1")
    page.fill("#password", test_user["password"])
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

    assert page.locator("text=Logged in as").is_visible()



    