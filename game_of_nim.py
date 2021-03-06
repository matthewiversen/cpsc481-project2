from games import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""

    def __init__(self, board=[3,1]):
        moves = []
        for row in range(len(board)):
            for match_amount in range(1, board[row] + 1):
                moves.append((row, match_amount))
        
        self.initial = GameState(to_move='MAX', utility=0, board=board, moves=moves)


    def result(self, state, move):
        """Updates and returns state based on the given move"""

        row_to_update = move[0]
        matches_to_remove = move[1]

        # create a new board of the new state, because state is a tuple which is unchangable
        new_board = state.board.copy()

        # remove the matches based on the given move
        new_board[row_to_update] -= matches_to_remove

        # calculate new moves
        new_moves = []
        for row in range(len(new_board)):
            for match_amount in range(1, new_board[row] + 1):
                new_moves.append((row, match_amount))

        return GameState(to_move=("MAX" if state.to_move == "MIN" else "MIN"),
                        utility=self.utility(state, state.to_move), 
                        board=new_board, 
                        moves=new_moves)


    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        
        return state.moves


    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""

        if self.terminal_test(state):
            return (1 if state.to_move == "MAX" else -1)
        else:
            return 0


    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        
        if len(state.moves) == 0:
            return True
        else:
            return


    def display(self, state):
        """Display the board"""

        board = state.board
        print("board: ", board)


    def to_move(self, state):
        """Return the player whose move it is in this state."""

        return state.to_move


if __name__ == "__main__":

    nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance

    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first 
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")