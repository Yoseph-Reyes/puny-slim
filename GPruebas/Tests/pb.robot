*** Settings ***
Documentation  prueba 
Library  SeleniumLibrary
*** Variables ***
${url}=      https://saia2.psm.edu.ve/login/index.php 
*** Test Cases ***
automatización
    [documentation]  automatización
    Open Browser  ${url}  Chrome
    Wait Until Element Is Visible  id:username  timeout=5
    Input Text  id:username  yoseph
    Input Password  id:password  12345678
    Click Element  id:loginbtn
    Page Should Contain  Las 'Cookies'  timeout=5
    Close Browser
*** Keywords ***
