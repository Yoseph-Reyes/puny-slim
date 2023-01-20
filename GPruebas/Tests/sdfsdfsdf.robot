*** Settings ***
Documentation  sdfsdfsdf 
Library  SeleniumLibrary
*** Variables ***
${url}=      http://127.0.0.1:8000/login 
*** Test Cases ***
sdfsdfsdf
    [documentation]  sdfsdfsdf
    Open Browser  ${url}  Chrome
    Wait Until Element Is Visible  id:  timeout=5
    Input Text  id:  
    Page Should Contain    timeout=5
    Close Browser
*** Keywords ***
