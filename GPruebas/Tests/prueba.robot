*** Settings ***
Documentation  preuba de saia 
Library  SeleniumLibrary
*** Variables ***
${url}=      https://saia2.psm.edu.ve/login/index.php 
*** Test Cases ***
prueba de saia
    [documentation]  prueba de saia
    Open Browser  ${url}  Chrome
    Wait Until Element Is Visible  id:  timeout=5
    Set Focus To Element  id:
    Input Text  id:  
    Page Should Contain    timeout=5
    Close Browser
*** Keywords ***
