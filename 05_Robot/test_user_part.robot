*** Settings ***
Documentation  Тесты для пользовательской части на Robotframework
Library  UserPart.py  ${BROWSER}  ${URL}
Library  Selenium2Library
Test Setup  Open Web Browser
Test Teardown  Close Web Browser

*** Variables ***
${URL}  http://localhost/opencart/
${BROWSER}  Chrome

*** Test Cases ***
Search product by text, add found product to wishlist by number
    Search Product  Canon
    Add to wishlist Product number   1
    Check Alert Success

Go to catalog Monitors, add two products to compare by number
    Go to Monitors
    Add to compare Product number  1
    Check Alert Success
    Add to compare Product number  2
    Check Alert Success

Add product to cart defined quantity
    Choose Product  iPhone
    Add product to cart quantity   5
    Check Alert Success

List product images by quantity, add product to cart defined quantity
    Choose Product  MacBook
    List images quantity  3
    Add product to cart quantity  3
    Check Alert Success