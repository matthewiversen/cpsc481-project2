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
        
        self.state = GameState(to_move='MAX', utility=0, board=board, moves=moves)


    def result(self, state, move):
        """Updates and returns state based on the given move"""

        row_to_update = move[0]
        matches_to_remove = move[1]

        # removed the matches based on the give move
        state.board[row_to_update] -= matches_to_remove

        # calculate new moves
        new_moves = []
        for row in range(len(state.board)):
            for match_amount in range(1, state.board[row] + 1):
                new_moves.append((row, match_amount))
                
        return GameState(to_move=('MAX' if state.to_move == "MIN" else "MIN"), utility=0, board=state.board, moves=new_moves)


    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves


    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        pass
        # raise NotImplementedError


    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        pass
        # raise NotImplementedError


    def display(self, state):
        board = state.board
        print("board: ", board)


if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search

    nim.display(nim.state) # must be [0, 5, 3, 1]
    print("available moves:", nim.actions(nim.state)) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    

    print(nim.state)
    nim.state = nim.result(nim.state, (2,2))
    # nim.actions = 
    print(nim.state)
        
    # print(nim.result(nim.initial, (1,3) ))

    # utility = nim.play_game(alpha_beta_player, query_player) # computer moves first 
    # if (utility < 0):
    #     print("MIN won the game")
    # else:
    #     print("MAX won the game")
