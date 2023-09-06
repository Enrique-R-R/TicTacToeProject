import random
import time


def choose_starting():

    if random.randint(0, 1) == 1:
        return True
    else:
        return False


class Game:

    def __init__(self):
        self.game_board = """
     │     │   
─────│─────│─────
     │     │   
─────│─────│─────
     │     │   
"""
        self.numbered_board = """
  1  │  2  │  3
─────│─────│─────
  4  │  5  │  6
─────│─────│─────
  7  │  8  │  9
"""
        self.open_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.player_turn = choose_starting()
        self.player_picks = []
        self.computer_picks = []
        self.game_over = False
        self.winning_combinations = [
                                        ["1", "2", "3"],
                                        ["1", "5", "9"],
                                        ["1", "4", "7"],
                                        ["2", "5", "8"],
                                        ["3", "5", "7"],
                                        ["3", "6", "9"],
                                        ["4", "5", "6"],
                                        ["7", "8", "9"]
                                    ]

    def next_move(self):
        if self.player_turn:
            self.player_moves()
            self.check_player_win()
        else:
            self.computer_moves()
            self.check_computer_win()
        self.check_game_over()

    def player_moves(self):
        print("Your Turn")
        picked_square = input(f"Please, pick a number to place your sign (X): {self.open_positions}]: ")

        while picked_square not in self.open_positions:
            print("Sorry, that square is not available.")
            picked_square = input(f"Please, pick a number to place your sign (X): {self.open_positions}: ")

        index = self.numbered_board.find(picked_square)
        self.open_positions.remove(picked_square)
        self.game_board = self.game_board[:index] + "X" + self.game_board[index + 1:]
        self.player_picks.append(picked_square)
        print(self.game_board)
        self.player_turn = False

    def computer_moves(self):
        print("Computer turn")
        time.sleep(1)

        picked_square = random.choice(self.open_positions)
        index = self.numbered_board.find(picked_square)
        self.open_positions.remove(picked_square)
        self.game_board = self.game_board[:index] + "O" + self.game_board[index + 1:]
        self.computer_picks.append(picked_square)
        print(self.game_board)
        self.player_turn = True

    def check_player_win(self):
        if len(self.player_picks) >= 3:
            for winning_line in self.winning_combinations:
                if all(x in self.player_picks for x in winning_line):
                    self.game_over = True
                    print("You have Won!")
                    break

    def check_computer_win(self):
        if len(self.computer_picks) >= 3:
            for winning_line in self.winning_combinations:
                if all(x in self.computer_picks for x in winning_line):
                    self.game_over = True
                    print("Computer has Won!")
                    break

    def check_game_over(self):
        if not self.open_positions and not self.game_over:
            print("It's a tie.")
            self.game_over = True


game = Game()

print("Welcome to the game of Tic tac toe.")
time.sleep(1)
print("The board has nine numbered squares, from 1 to 9, like this:")
print(game.numbered_board)
time.sleep(1)
print("To play, choose one of the numbers still left unchosen.")
time.sleep(1)
print("To win, get three in a row.")
print("You lose if your opponent gets three in a row.")
print("If all nine squares have been picked and neither player has won, the game is a draw.")
time.sleep(1)

go_again = ""

while not go_again:

    print(game.game_board)

    while not game.game_over:
        game.next_move()

    go_again = input("Do you want to go again? Type anything to stop playing: ")
