Feature: Basic Decision Flow
  Some basic decisions in a board game can be check quickly without
  applying artificial intelligence. Such as checking winner and draw.
  Again, this feature focus on the state change when an action is applied.

  Scenario: X becomes the winner
    Given board states listed as below that 2 Xs in a row or diagonal
    | game |    state     |
    |  1   |X,O,O,X,X,O,,,|
    |  2   |X,,,,X,,O,O,  |
    And X is the next player
    When X moves to one of the empty cells
    | game | next_move |
    |  1   |     7     |
    |  2   |     9     |
    Then X becomes the winner

  Scenario: O becomes the winner
    Given board states listed as below that 2 Os in a row or diagonal
    | game |     state     |
    |  1   |X,X,O,O,O,,X,X,|
    |  2   |X,,,X,O,,O,X,  |
    And O is the next player
    When O moves to one of the empty cells
    | game | next_move |
    |  1   |     6     |
    |  2   |     3     |
    Then O becomes the winner

  Scenario: Block X
    Given a board state that 2 Xs in a row or diagonal
    | game |    state    |
    |  1   |X,O,O,X,X,,,,|
    |  2   |X,X,,O,,,,,  |
    And O is the next player
    When O moves to one of the empty cells
    | game | next_move |
    |  1   |     6     |
    |  2   |     3     |
    Then X is forced to move to other cell

  Scenario: Block O
    Given a board state that 2 Os in a row or diagonal
    | game |     state    |
    |  1   |X,,,,X,,O,O,  |
    |  2   |X,X,O,O,O,,X,,|
    And X is the next player
    When X moves to one of the empty cells
    | game | next_move |
    |  1   |     9     |
    |  2   |     6     |
    Then O is forced to move to other cell

  Scenario: Game is draw
    Given a board state that only a cell open
    And either X or O is the next player
    When X or O moves to the only empty cell
    Then no winner is determined
