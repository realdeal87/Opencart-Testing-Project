*** Settings ***
Documentation  Тесты для панели администратора на Robotframework
Library  Selenium2Library
Resource  admin_panel_keywords.robot
Test Setup  Setup Test
Test Teardown  Teardown Test

*** Variables ***
${URL}  http://localhost/opencart/admin
${BROWSER}  Firefox
${USERNAME}  Realdeal87
${PASSWORD}  K1x9Z5b8!
@{FIELDS}  Robot  Framework  BDD
${DESCRIPTION}  Just a description!

*** Test Cases ***
Create a new product
    Login as Admin
    Go to Products
    Add a new product with required fields  @{FIELDS}
    Save changes
    Waiting for alert success

Edit a product
    Login as Admin
    Go to Products
    Edit a product number  5
    Add description  ${DESCRIPTION}
    Save changes
    Waiting for alert success

Delete a product
    Login as Admin
    Go to Products
    Select a product number  3
    Delete a product
    Confirm action
    Waiting for alert success

Copy a product
    Login as Admin
    Go to Products
    Select a product number  2
    Copy a product
    Waiting for alert success
