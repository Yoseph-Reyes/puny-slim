*** Settings ***
Documentation   preuba de saia 
Library  SeleniumLibrary
*** Variables ***
${url}=      https://saia2.psm.edu.ve/login/index.php 
*** Test Cases ***
 prueba de saia
    [documentation]   prueba de saia
    Open Browser  ${url}  Chrome
    Wait Until Element Is Visible  id:username  timeout=5
    Set Focus To Element  id:username
    Input Text  id:username  yoseph
    Input Password  id:password  clave
    Click Element  id:loginbtn
     Page Should Contain   " Las Cookies deben estar habilitadas en su navegador"  timeout=5
    Close Browser
*** Keywords ***
