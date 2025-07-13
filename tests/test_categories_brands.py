import allure
@allure.step("Delete account")
def delete_account(page):
    page.click("text=Delete Account")
    assert page.get_by_text("ACCOUNT DELETED!").is_visible()
    page.click("text=Continue")

def test_remove_products_from_cart(page):
    page.goto("https://automationexercise.com")
    page.click("text=Products")
    page.hover(".productinfo >> nth=0")
    page.click("text=Add to cart >> nth=0")
    page.click("text=Continue Shopping")
    page.click("text=Cart")

    with allure.step("Видаляємо товар"):
        page.click("xpath=//a[@class='cart_quantity_delete']")
        page.wait_for_timeout(1000)
        assert not page.locator(".cart_description").first.is_visible()


def test_view_category_products(page):
    page.goto("https://automationexercise.com")
    assert page.locator(".left-sidebar").is_visible()

    with allure.step("Вибираємо категорію Women → Dress"):
        page.click("text=Women")
        page.click("xpath=//a[contains(text(),'Dress')]")
        assert page.locator("text=WOMEN - DRESS PRODUCTS").is_visible()

    with allure.step("Вибираємо категорію Men → Tshirts"):
        page.click("h4.panel-title a[href='#Men']")
        page.wait_for_selector("xpath=//a[contains(text(),'Tshirts')]", state="visible")
        page.click("xpath=//a[contains(text(),'Tshirts')]")
        assert page.locator("text=MEN - TSHIRTS PRODUCTS").is_visible()


def test_view_and_cart_brand_products(page):
    page.goto("https://automationexercise.com")
    page.click("text=Products")

    with allure.step("Вибираємо бренд Babyhug"):
        page.click("xpath=//a[text()='Babyhug']")
        assert page.locator("text=Brand - Babyhug Products").is_visible()

    with allure.step("Вибираємо бренд Kookie Kids"):
        page.click("xpath=//a[text()='Kookie Kids']")
        assert page.locator("text=Brand - Kookie Kids Products").is_visible()


def test_cart_after_login(page, ensure_registered_user, test_user):
    page.goto("https://automationexercise.com")
    page.click("text=Products")
    page.fill("input#search_product", "Dress")
    page.click("button#submit_search")
    page.click("text=Add to cart >> nth=0")
    page.click("text=Cart")
    page.wait_for_selector(".cart_description", state="visible")
    assert page.locator(".cart_description").first.is_visible()

    with allure.step("Перевірка корзини після логіну"):
        page.click("text=Cart")
        assert page.locator(".cart_description").first.is_visible()
        delete_account(page)