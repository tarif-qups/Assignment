
Feature: Open demoblaze Website And Sign Up

    Scenario: Open demoblaze Website And Sign Up
        Given User Open demoblaze Website
        When Click signup
        Then type sign up user name
        Then type sign up user password
        Then Click close button
        Then Check element present or not
        Then check element hidden or visisble
        Then check text
        Then check attribute
        Then check page url and title

    Scenario: Open demoblaze Website And Login
        Given User Open demoblaze Website
        When Click login
        Then type login user name
        Then type login user password
        Then Click login close button
        Then check login page title

    Scenario: Open demoblaze Website And Place order
        Given User Open demoblaze Website
        When click on cart
        Then click on place order
        Then type place order name
        Then type place order country
        Then type place order city
        Then type place order credit card
        Then type place order month
        Then type place order year
        Then click on place order close
        Then check cart page title

    Scenario: Open demoblaze Website And About us
        Given User Open demoblaze Website
        When click on about us
        # Then click on video
        # Then click on pause video
        Then click on about us close

    Scenario: Open demoblaze Website And Contact us
        Given User Open demoblaze Website
        When click on contact
        Then type contact email name
        Then type contact name
        Then type contact message
        Then click on contact

    Scenario: Open demoblaze Website And phones
        Given User Open demoblaze Website
        When click on Home
        Then click on home phone
        Then click on phone nexus6
        Then click on add to cart
        Then click on Home
        Then click on home cart
        # Then click on cart delete

    Scenario: Open demoblaze Website And laptops
        Given User Open demoblaze Website
        When click on laptops
        Then click on laptops sony
        Then click on add to laptops add to cart
        Then click on laptops cart
        Then click on laptops cart delete

    Scenario: Open demoblaze Website And laptops
        Given User Open demoblaze Website
        When click on monitors
        Then click on monitors apple
        Then click on add to monitors add to cart
        Then click on monitors cart
        Then click on monitors cart delete