*** Settings ***
Documentation  Prueba Autem 
Library  SeleniumLibrary
*** Variables ***
${url}=      https://autem.cl 
*** Test Cases ***
Prueba de Concepto con Autem
    [documentation]  Prueba de Concepto con Autem
    Open Browser  ${url}  Chrome
    Wait Until Element Is Visible  id:wpforms-110-field_0  timeout=5
    Input Text  id:wpforms-110-field_0  pb
    Input Text  id:wpforms-110-field_0-last  preuba
    Input Text  id:wpforms-110-field_1  1@2.com
    Input Text  id:wpforms-110-field_3  456789123
    Input Text  id:wpforms-110-field_5  cualquiera
    Select From List By Label  id:wpforms-110-field_4  Servicio de Ingeniería
    Input Text  id:wpforms-110-field_2  wezesfhjyllllllllsdfss
    Click Element  id:wpforms-submit-110
    Page Should Contain  Teléfono  timeout=5
    Close Browser
*** Keywords ***
