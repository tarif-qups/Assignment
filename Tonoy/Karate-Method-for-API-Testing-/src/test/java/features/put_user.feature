Feature: Perform put requests for user

    Scenario: PUT a Single User in reqres.in
      * def user =
      """ {
    "email": "tonoyvgxsgvghxv@gmail.com",
    "first_name": "Tonoy",
    "last_name": "Saha",
    "avatar": "https://hasan ali/img/faces/2-image.jpg",
    "id": "632",
    "createdAt": "2022-11-07T09:20:54.178Z"
}
            """
      Given url 'https://reqres.in/api/users/234'
       And request user
       When method put
       Then status 200

      Scenario: Put demo 1
        Given url 'https://reqres.in/api/users/2'
        And request {"name": "Shekhor", "job": "Teacher"}
        When method PUT
        Then status 200
        And print response
        And match response == {"name": "Shekhor","job": "Teacher","updatedAt": "#ignore"}