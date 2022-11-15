Feature: Perform get requests for user

  Background:
    * url 'https://restcountries.com/v3.1'
    * header Accept = 'application/json'

#    Simple Get Request
  Scenario: Perform get request for User
    Given url 'https://restcountries.com/v3.1/name/bangladesh'
    When method GET
    Then status 200
    And print response
    And print responseStatus
    And print responseTime
    And print responseHeaders
    And print responseCookies


##    Get with Background
#  Scenario: Perform get request
#    Given path '/name/bangladesh'
#    When method GET
#    Then status 200
#    And print response

    #    Get with Path, Params
  Scenario: get demo 3
    Given path '/name/bangladesh'
    When method GET
    Then status 200
    And match response[0].idd.root != null
    And match response[0].capital[0] == 'Dhaka'
    And print response[0].currencies.BDT.name != null
    And match response[0].capital[0] != null
    And assert response[0].latlng.length != 0
    And print response[0].idd.suffixes[0]
    And assert response[0].idd.suffixes[0] == '80'


