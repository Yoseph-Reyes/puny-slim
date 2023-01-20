*** Settings ***
Documentation  fgdgd 
Library  SeleniumLibrary
*** Variables ***
${url}=      https://google.com 
*** Test Cases ***
fdgdgdg
    [documentation]  fdgdgdg
    Open Browser  ${url}  Chrome
    Wait Until Element Is Visible  id:  timeout=5
    Input Text  id:  
    Page Should Contain    timeout=5
    Close Browser
*** Keywords ***
