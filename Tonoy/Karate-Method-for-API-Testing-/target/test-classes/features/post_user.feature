Feature: Perform post requests for user


  Background:
    * url 'https://reqres.in/api/'
    * header Accept = 'application/json'
    * def expectedOutput = read("response1.json")

  Scenario: Post a Single User in reqres.in
  * def user =
  """ {
    "email": "tonoyvgxsgvghxv@gmail.com",
    "first_name": "hasan",
    "last_name": "Ali",
    "avatar": "https://hasan ali/img/faces/2-image.jpg"
}
        """
  Given url 'https://reqres.in/api/users'
    And request user
    When method post
    Then status 201

    #simple Post method
    Scenario: Post Demo 1
      Given url 'https://reqres.in/api/users'
      And request {"name": "Tonoy","job": "Student"}
      When method post
      Then status 201
      And print response

      #Post scenario with Background
  Scenario: Post Demo 2
    Given path '/users'
    And request {"name": "Tonoy","job": "Student"}
    When method post
    Then status 201
    And print response

    #Post scenario with Background asssr
  Scenario: Post Demo 3
    Given path '/users'
    And request {"name": "Tonoy","job": "Student"}
    When method post
    Then status 201
    And print response
    And match response == {"name": "Tonoy","job": "Student","id": "#string","createdAt": "#ignore"}

    #Post scenario with get response from file
#  Scenario: Post Demo 4
#    Given path '/users'
#    And request {"name": "Tonoy","job": "Student"}
#    When method post
#    Then status 201
#    And match response == expectedOutput
#    And match $ == expectedOutput
#    And print response


