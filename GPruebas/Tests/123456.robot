*** Settings ***
Documentation  123456 
Library  SeleniumLibrary

*** Variables ***
${url}=      https://saia2.psm.edu.ve/login/index.php 
*** Test Cases ***
xsxsd
    [documentation]  xsxsd
    Open Browser  ${url}  Chrome
  
    Wait Until Element Is Visible  id:username  timeout=5
    Input Text  id:username  yoseph
    Input Password  id:password  clave
    Click Element  id:loginbtn
    Element Should Be Visible  css:[href='/logout']  timeout=5
    Close Browser
*** Keywords ***
