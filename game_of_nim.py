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

        # removed the matches based on the given move
        state.board[row_to_update] -= matches_to_remove

        # calculate new moves
        new_moves = []
        for row in range(len(state.board)):
            for match_amount in range(1, state.board[row] + 1):
                new_moves.append((row, match_amount))
        
        print(state)
        print(new_moves)
        print()

        return GameState(to_move=('MAX' if state.to_move == "MIN" else "MIN"),
                        utility=self.utility(state, self.to_move), 
                        board=state.board, 
                        moves=new_moves)


    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves


    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""

        if self.terminal_test(state):
            if player == "MAX":
                return 1
            elif player == "MIN":
                return -1 
            else:
                return 0


    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""

        # s = sum(state.board)
        # if s <= 0:
        #     return True
        # else:
        #     return False

        if len(state.moves) == 0:
            print("End of the game has been detected!!!")
            return True
        else:
            return False

            
    def display(self, state):
        """Display the board"""

        board = state.board
        print("board: ", board)


    def to_move(self, state):
        """Return the player whose move it is in this state."""

        return state.to_move


if __name__ == "__main__":

    nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search

    print(nim.initial.board) # must be [0,5,3,1] - CORRECT
    print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)] - CORRECT
    print(nim.result(nim.initial, (1,3))) # CORRECT

    # display board
    # nim.display(nim.initial) 
    
    # prints availble moves
    # print("available moves:", nim.actions(nim.initial))
    
    # some test turns
    # print(nim.initial)
    # nim.initial = nim.result(nim.initial, (2,3))
    # print(nim.initial)
    # nim.initial = nim.result(nim.initial, (1,5))
    # print(nim.initial)
    # nim.state = nim.result(nim.state, (3,1))
    # print(nim.state)

    # gets the utility, use after determining that the game is done
    # print(nim.utility(nim.initial, nim.initial.to_move))

    # check if the board is empty
    # print(nim.terminal_test(nim.initial))
        
    

    # print(nim.initial)
    print()
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first 
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
