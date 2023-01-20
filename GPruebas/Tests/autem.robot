*** Settings ***
Documentation  qweqwe 
Library  SeleniumLibrary
*** Variables ***
${url}=      https://saia2.psm.edu.ve/login/index.php 
*** Test Cases ***
qweqweqweqweqweqweqweqweqweqwqweqwqwqw
    [documentation]  qweqweqweqweqweqweqweqweqweqwqweqwqwqw
    Open Browser  ${url}  Chrome
    Wait Until Element Is Visible  id:b  timeout=5
    Set Focus To Element  id:b
    Input Text  id:b  c
    Input Password  id:e  f
    Click Element  id:h
     Page Should Contain   sssssss  timeout=5
    Close Browser
*** Keywords ***
