*** Settings ***
Resource  ../Resources/resource.robot
Resource  ../Resources/BasePage.robot

Test Setup  Open_ANDROID_Test_App
Test Teardown  Quit Application

*** Test Cases ***
OPEN_APP
    Action_For_LOGIN
    Action_For_link