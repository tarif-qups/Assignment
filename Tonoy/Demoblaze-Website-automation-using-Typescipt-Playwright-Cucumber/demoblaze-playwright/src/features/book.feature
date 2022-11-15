
Feature: Open rokomari Website And Show all Famous Writers

    Scenario: Open rokomari Website And Show all Famous Writers
        Given User Open The Rokomari Website
        # And After Open website Click Cross Button Of Add
        And Click On The Book Button
        And Click On The Author Button
        Then Verify The Famous Authors Are Available

    Scenario: Open rokomari Website And Search you favorite author
        Given User Open The Rokomari Website
        # And After Open website Click Cross Button Of Add
        And Click On The Book Button
        And Click On The Author Button
        Then Verify The Famous Authors Are Available
        And Search Your Favorite Author Ayman Sadiq
        Then Dr. Khandaker Abdullah Jahangir Author Details Is Available
