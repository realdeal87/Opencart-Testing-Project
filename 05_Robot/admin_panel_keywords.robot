*** Keywords ***
Setup Test
    Open Browser  ${URL}  ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout  10 seconds

Login as Admin
    Input Text  id:input-username  ${USERNAME}
    Input Text  id:input-password  ${PASSWORD}
    Click Button  Login

Go to Products
    Click Link  Catalog
    Click Link  Products

Select a product number
    [Arguments]  ${NUMBER}
    ${NUMBER}=  Evaluate  ${NUMBER} - 1
    @{ELEMENTS}=  Get WebElements  xpath://input[@name='selected[]']
    Select Checkbox  @{ELEMENTS}[${NUMBER}]

Edit a product number
    [Arguments]  ${NUMBER}
    ${NUMBER}=  Evaluate  ${NUMBER} - 1
    @{ELEMENTS}=  Get WebElements  xpath://a[@data-original-title='Edit']
    Click Link  @{ELEMENTS}[${NUMBER}]

Add a new product with required fields
    [Arguments]  @{FIELDS}
    Click Link  xpath://a[@data-original-title='Add New']
    Input Text  id:input-name1  @{FIELDS}[0]
    Input Text  id:input-meta-title1  @{FIELDS}[1]
    Click Link  link:Data
    Input Text  id:input-model  @{FIELDS}[2]

Add description
    [Arguments]  ${DESCRIPTION}
    Input Text  class:note-editable  ${DESCRIPTION}

Copy a product
    Click Button  xpath://button[@data-original-title='Copy']

Delete a product
    Click Button  xpath://button[@data-original-title='Delete']

Save changes
    Click Button  xpath://button[@data-original-title='Save']

Confirm action
    Handle Alert

Waiting for alert success
    Wait Until Page Contains  Success

Teardown Test
    Close Browser