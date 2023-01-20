*** Settings ***
Documentation  Documentacion 
Library  SeleniumLibrary
*** Variables ***
${url}=      https://saia2.psm.edu.ve/login/index.php 
*** Test Cases ***
prueba de ejecución del login del sistema
    [documentation]  prueba de ejecución del login del sistema
    Open Browser  ${url}  Chrome
    Wait Until Element Is Visible  id:username  timeout=5
    Input Text  id:username  yoseph
    Input Password  id:password  clave
    Click Element  id:loginbtn
    Page Should Contain  Las 'Cookies'  timeout=5
    Close Browser
*** Keywords ***
