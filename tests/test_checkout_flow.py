# import allure
# import pytest
# from playwright.sync_api import expect

# @allure.step("Add product to cart")
# def add_product_to_cart(page):
#     page.goto("https://automationexercise.com")
#     page.click("text=Products")
#     page.hover(".productinfo >> nth=0")
#     page.click("text=Add to cart >> nth=0")
#     page.click("text=Continue Shopping")

# @allure.step("Proceed to Checkout")
# def proceed_to_checkout(page):
#     page.click("text=Cart")
#     assert "/view_cart" in page.url
#     page.click("text=Proceed To Checkout")

# @allure.step("Place order with payment")
# def place_order(page):
#     page.wait_for_selector("textarea[name='message']", timeout=10000)
#     page.fill("textarea[name='message']", "Automated order by Tymur.")
#     page.click("text=Place Order")
#     page.fill("input[name='name_on_card']", "Tymur TestCard")
#     page.fill("input[name='card_number']", "4111111111111111")
#     page.fill("input[name='cvc']", "123")
#     page.fill("input[name='expiry_month']", "12")
#     page.fill("input[name='expiry_year']", "2026")
#     page.click("text=Pay and Confirm Order")
#     page.wait_for_selector("text=Your order has been placed successfully!", timeout=10000)
#     assert page.locator("text=Your order has been placed successfully!").is_visible()


# @allure.step("Delete account")
# def delete_account(page):
#     page.click("text=Delete Account")
#     assert page.get_by_text("ACCOUNT DELETED!").is_visible()
#     page.click("text=Continue")


# def test_place_order_register_during_checkout(page, test_user):
#     add_product_to_cart(page)
#     page.click("text=Cart")
#     proceed_to_checkout(page)
#     page.click("text=Register / Login")
#     page.fill("input[name='name']", test_user["name"])
#     page.fill("input[data-qa='signup-email']", test_user["email"])
#     page.click("button[data-qa='signup-button']")
#     page.check("#id_gender1")
#     page.fill("#password", test_user["password"])
#     page.select_option("#days", "10")
#     page.select_option("#months", "5")
#     page.select_option("#years", "1999")
#     page.check("#newsletter")
#     page.check("#optin")
#     page.fill("#first_name", "Tymur")
#     page.fill("#last_name", "Testovich")
#     page.fill("#company", "TestCorp")
#     page.fill("#address1", "123 Test Street")
#     page.fill("#address2", "Suite 456")
#     page.select_option("#country", "Canada")
#     page.fill("#state", "TestState")
#     page.fill("#city", "TestCity")
#     page.fill("#zipcode", "12345")
#     page.fill("#mobile_number", "1234567890")
#     page.click("button[data-qa='create-account']")
#     page.click("text=Continue")
#     page.click("text=Cart")
#     proceed_to_checkout(page)
#     place_order(page)
#     delete_account(page)


# def test_place_order_after_registration(page, ensure_registered_user, test_user):
#     add_product_to_cart(page)
#     page.click("text=Cart")
#     proceed_to_checkout(page)
#     place_order(page)
#     delete_account(page)


# def test_place_order_login_before_checkout(page, ensure_registered_user, test_user):
#     page.goto("https://automationexercise.com")
#     page.click("text=Signup / Login")
#     page.fill("input[data-qa='login-email']", test_user["email"])
#     page.fill("input[data-qa='login-password']", test_user["password"])
#     page.click("button[data-qa='login-button']")
#     add_product_to_cart(page)
#     proceed_to_checkout(page)
#     place_order(page)
#     delete_account(page)


# def test_verify_address_details_in_checkout(page, ensure_registered_user):
#     add_product_to_cart(page)
#     page.click("text=Cart")
#     proceed_to_checkout(page)
#     # assert page.locator("text=Your delivery address").is_visible()
#     expect(page.locator("text=Your delivery address")).to_be_visible()

#     assert page.locator("text=Your billing address").is_visible()
#     delete_account(page)


# def test_download_invoice_after_order(page, test_user):
#     add_product_to_cart(page)
#     page.click("text=Cart")
#     proceed_to_checkout(page)
#     page.click("text=Register / Login")
#     page.fill("input[name='name']", test_user["name"])
#     page.fill("input[data-qa='signup-email']", test_user["email"])
#     page.click("button[data-qa='signup-button']")
#     page.check("#id_gender1")
#     page.fill("#password", test_user["password"])
#     page.select_option("#days", "10")
#     page.select_option("#months", "5")
#     page.select_option("#years", "1999")
#     page.check("#newsletter")
#     page.check("#optin")
#     page.fill("#first_name", "Tymur")
#     page.fill("#last_name", "Testovich")
#     page.fill("#company", "TestCorp")
#     page.fill("#address1", "123 Test Street")
#     page.fill("#address2", "Suite 456")
#     page.select_option("#country", "Canada")
#     page.fill("#state", "TestState")
#     page.fill("#city", "TestCity")
#     page.fill("#zipcode", "12345")
#     page.fill("#mobile_number", "1234567890")
#     page.click("button[data-qa='create-account']")
#     page.click("text=Continue")
#     page.click("text=Cart")
#     proceed_to_checkout(page)
#     place_order(page)
#     # page.click("text=Download Invoice")
#     page.wait_for_selector("text=Download Invoice", timeout=10000)
#     page.click("text=Download Invoice")
#     page.click("text=Continue")
#     delete_account(page)