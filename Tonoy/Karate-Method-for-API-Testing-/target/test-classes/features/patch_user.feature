Feature: Perform patch requests for user

  Scenario: Patch a Single User in reqres.in
    * def user =
      """ {
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}
            """
    Given url 'https://reqres.in/api/users/2'
    And request {"first_name": "Saha"}
    When method patch
    Then status 200
    And print response
    And match response == {"first_name": "Saha","updatedAt": "#ignore"}