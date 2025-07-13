# import allure
# import pytest

# def test_verify_test_cases_page(page):
#     page.goto("https://automationexercise.com")
#     page.click("text=Test Cases")
#     assert "/test_cases" in page.url

# def test_verify_all_products_and_details(page):
#     page.goto("https://automationexercise.com")
#     page.click("text=Products")
#     assert page.locator(".productinfo").first.is_visible()
#     page.click("text=View Product")
#     assert page.get_by_text("Availability").is_visible()
#     assert page.get_by_text("Condition").is_visible()
#     assert page.get_by_text("Brand").is_visible()

# def test_search_product(page):
#     page.goto("https://automationexercise.com")
#     page.click("text=Products")
#     page.fill("input#search_product", "Dress")
#     page.click("button#submit_search")
#     assert page.get_by_text("Searched Products").is_visible()
#     assert page.locator(".productinfo").first.is_visible()

# def test_subscription_on_home(page):
#     page.goto("https://automationexercise.com")
#     page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#     assert page.locator("text=Subscription").is_visible()
#     page.fill("#susbscribe_email", "tymur@example.com")
#     page.click("i.fa.fa-arrow-circle-o-right")
#     assert page.get_by_text("You have been successfully subscribed!").is_visible()

# def test_subscription_on_cart(page):
#     page.goto("https://automationexercise.com")
#     page.click("text=Cart")
#     page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#     assert page.locator("text=Subscription").is_visible()
#     page.fill("#susbscribe_email", "tymur@example.com")
#     page.click("i.fa.fa-arrow-circle-o-right")
#     assert page.get_by_text("You have been successfully subscribed!").is_visible()

# def test_add_products_to_cart(page):
#     page.goto("https://automationexercise.com")
#     page.click("text=Products")
#     page.hover(".productinfo >> nth=0")
#     page.click("text=Add to cart >> nth=0")
#     page.click("text=Continue Shopping")
#     page.hover(".productinfo >> nth=1")
#     page.click("text=Add to cart >> nth=1")
#     page.click("text=Cart")
#     assert page.locator(".cart_description").nth(0).is_visible()
#     assert page.locator(".cart_description").nth(1).is_visible()

# def test_verify_product_quantity(page):
#     page.goto("https://automationexercise.com")
#     page.click("text=View Product >> nth=0")
#     page.fill("input#quantity", "4")
#     page.click("button.cart")
#     page.click("text=Cart")
#     quantity = page.locator("input.cart_quantity").input_value()
#     assert quantity == "4"

# def test_add_review_on_product(page):
#     page.goto("https://automationexercise.com")
#     page.click("text=Products")
#     page.click("text=View Product >> nth=0")
#     assert page.locator("text=Write Your Review").is_visible()
#     page.fill("input[name='name']", "TymurTest")
#     page.fill("input[name='email']", "tymur@example.com")
#     page.fill("textarea[name='review']", "This product rocks!")
#     page.click("button#button-review")
#     assert page.get_by_text("Thank you for your review.").is_visible()

# def test_add_to_cart_from_recommended_items(page):
#     page.goto("https://automationexercise.com")
#     page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#     assert page.locator("text=RECOMMENDED ITEMS").is_visible()
#     page.click("xpath=(//a[contains(text(),'Add to cart')])[last()]")
#     page.click("text=View Cart")
#     assert page.locator(".cart_description").first.is_visible()