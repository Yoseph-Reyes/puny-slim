*** Settings ***
Documentation  12345 
Library  SeleniumLibrary
*** Variables ***
${url}=      https://saia2.psm.edu.ve/login/index.php 
*** Test Cases ***
qwert
    [documentation]  qwert
    Open Browser  ${url}  Chrome
    Wait Until Element Is Visible  id:  timeout=5
    Input Text  id:  
    Page Should Contain    timeout=5
    Close Browser
*** Keywords ***
