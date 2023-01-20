*** Settings ***
Documentation  Prueba HDTP 
Library  SeleniumLibrary
*** Variables ***
${url}=      https://saia2.psm.edu.ve/login/index.php 
*** Test Cases ***
Una prueba hije pute
    [documentation]  Una prueba hije pute
    Open Browser  ${url}  Chrome
    Wait Until Element Is Visible  id:username  timeout=5
    Set Focus To Element  id:username
    Input Text  id:username  yoseph
    Input Password  id:password  clave
    Click Element  id:rememberusername
    Input Text  id:loginbtn  
    Page Should Contain  " Las Cookies deben estar habilitadas en su navegador"  timeout=5
    Close Browser
*** Keywords ***
