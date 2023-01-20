*** Settings ***
Documentation  Pueba Interna 
Library  SeleniumLibrary
*** Variables ***
${url}=      http://127.0.0.1:5000/scrapper 
*** Test Cases ***
Desarrollo de Prueba interna del sistema
    [documentation]  Desarrollo de Prueba interna del sistema
    Open Browser  ${url}  Chrome
    Wait Until Element Is Visible  id:webs  timeout=5
    Input Text  id:webs  https://packaging.python.org/en/latest/tutorials/installing-packages/
    Element Should Be Visible  css:[href='/logout']  timeout=5
    Close Browser
*** Keywords ***
