#environment.py
from board_space import BoardSpace


class Environment():
    def __init__(self, diamensions: tuple, hospitality: int): #Hospitality = chance of food
        self.diamensions = diamensions
        self.hospitality = hospitality
        self.board = [[BoardSpace((i,j), "Empty") for i in range(diamensions[0])] for j in range(diamensions[1])]
    
    def __setitem__(self, coords, value):
        x,y = coords[0], coords[1]
        self.board[x][y] = BoardSpace((x,y), value)
        
        
    def __getitem__(self, key):
        return getattr(self, key)

        
        """
         x,y = coords[0], coords[1]
        new_board_space = BoardSpace(value)  # Create a new BoardSpace with the desired item
        new_board = self.board
        for space in new_board:
            if space.coords == coords:
                new_board[x][y] = new_board_space
        self.board = new_board
        """