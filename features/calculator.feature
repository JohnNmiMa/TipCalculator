Feature: Confirming that the tip calculator form displays

    Scenario: check that the form displays
        When I go to the tip calculator
        Then I should see the calculator form

    Scenario: check that the form submits successfully
        When I go to the tip calculator
        And I submit the form with a valid total and tip percentage
        Then I should see the results page

    Scenario: check that the form computes correctly
        When I go to the tip calculator
        And I submit the form with a $50 total and 20% tip
        Then I should see a $10 tip amount

    Scenario Outline: check that the form catches negative form entries
        When I go to the tip calculator
        And I submit the form with a negative <meal cost> or <tip> amount
        Then I should see a warning

        Examples: Form Entries
            | meal cost | tip  |
            | -50       |  20  |
            |  50       | -20  |

    @wip
    Scenario Outline: check that the form catches non-number values
        When I go to the tip calculator
        And I submit the form with a non-number <meal> or <tip> value
        Then I should see an invalid input warning

        Examples: Form Entries
            | meal  |  tip   |
            | fifty |     20 |
            |    50 | twenty |
            | fifty | twenty |

