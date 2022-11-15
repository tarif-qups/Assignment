*** Settings ***
Library  AppiumLibrary
Library  BuiltIn


*** Variables ***
""" Desired Capabilities For Simulator Device """
${ANDROID_AUTOMATION_NAME}        UiAutomator2
${ANDROID_APP}                    ${CURDIR}/../APK/Praava Health_v1.19_apkpure.com.apk
${ANDROID_PLATFORM_NAME}          Android
${ANDROID_PLATFORM_VERSION}       %{ANDROID_PLATFORM_VERSION=9}
${ANDROID_DEVICE_NAME}            Tonoy
${NO_RESET}                       False


#""" Desired Capabilities For Real Device """
#${REMOTE_URL}   http://127.0.0.1:4723/wd/hub
#${platformName}    iOS
#${appium:platformVersion}    15.6
#${appium:deviceName}    iPhone 11
##${appium:app}    /Users/qups/Library/Developer/Xcode/DerivedData/UICatalog-ejiokmvvhyiblpcfjtdcyyiledfg/Build/Products/Debug-iphoneos/UICatalog.app
#${appium:app}    ${CURDIR}/../APP/UICatalog.app
#${appium:automationName}    XCUITest
#${appium:noReset}    true
#${appium:udid}    00008030-001C25213A23C02E
#${appium:includeSafariInWebviews}    True
#${appium:newCommandTimeout}    3600
#${appium:connectHardwareKeyboard}    True


*** Keywords ***
""" ******* Open Application For Simulator Device ******* """
Open_ANDROID_Test_App
  open application  http://127.0.0.1:4723/wd/hub  automationName=${ANDROID_AUTOMATION_NAME}
  ...  app=${ANDROID_APP}  platformName=${ANDROID_PLATFORM_NAME}  platformVersion=${ANDROID_PLATFORM_VERSION}
  ...  deviceName=${ANDROID_DEVICE_NAME}  noReset=${NO_RESET}
  sleep  10



#""" ******* Open Application For Real Device ******* """
#Open_iOS_Real_Device_App
#  open application    ${REMOTE_URL}   platformName=${platformName}
#  ...  appium:platformVersion=${appium:platformVersion}  appium:deviceName=${appium:deviceName}
#  ...  appium:app=${appium:app}  appium:automationName=${appium:automationName}
#  ...  appium:noReset=${appium:noReset}  appium:udid=${appium:udid}
#  ...  appium:newCommandTimeout=${appium:newCommandTimeout}