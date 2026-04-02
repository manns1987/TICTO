from app.tictactoe import TicTacToe

def test_make_move():
    game = TicTacToe()
    assert game.make_move(0, "X") == True
    assert game.make_move(0, "O") == False

def test_winner():
    game = TicTacToe()
    game.board = ["X","X","X"," "," "," "," "," "," "]
    assert game.check_winner("X") == True

def test_draw():
    game = TicTacToe()
    game.board = ["X","O","X","X","O","O","O","X","X"]
    assert game.is_draw() == True