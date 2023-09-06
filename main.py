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
        self.computer_difficulty = "Easy"
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

        if self.computer_difficulty == "Easy":
            picked_square = self.computer_easy_moves()
        else:
            picked_square = self.computer_hard_moves()

        index = self.numbered_board.find(picked_square)
        self.open_positions.remove(picked_square)
        self.game_board = self.game_board[:index] + "O" + self.game_board[index + 1:]
        self.computer_picks.append(picked_square)
        print(self.game_board)
        self.player_turn = True

    def set_computer_dificulty(self):
        answer = input("Do you want to play in hard mode? (Type anything to confirm): ")
        if answer:
            self.computer_difficulty = "Hard"
        else:
            self.computer_difficulty = "Easy"

    def computer_easy_moves(self):
        return random.choice(self.open_positions)

    def computer_hard_moves(self):
        print("Computer turn")

        if "5" in self.open_positions:
            return "5"
        elif len(self.open_positions) == 8:
            return "1"
        elif len(self.open_positions) == 7:
            if self.player_picks[0] in ("1", "2", "4"):
                return "9"
            elif self.player_picks[0] in ("3", "6"):
                return "7"
            elif self.player_picks[0] in ("7", "8"):
                return "3"
            else:
                return "1"
        elif len(self.open_positions) == 6:
            pick = self.check_close_win(self.player_picks)
            if pick:
                return pick
            else:
                if self.computer_picks[0] == "5":
                    if "2" in self.open_positions:
                        return "2"
                    else:
                        if "9" in self.open_positions:
                            return "1"
                        else:
                            return "3"
                else:
                    return random.choice(self.open_positions)

        else:
            pick = self.check_close_win(self.computer_picks)
            if pick:
                return pick
            else:
                pick = self.check_close_win(self.player_picks)
                if pick:
                    return pick
                else:
                    return random.choice(self.open_positions)

    def check_close_win(self, picks):
        temp_picks = picks.copy()
        for i in self.open_positions:
            temp_picks.append(i)
            for winning_line in self.winning_combinations:
                if all(x in temp_picks for x in winning_line):
                    return i
            temp_picks.remove(i)
        return ""

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

    game.set_computer_dificulty()
    print(game.game_board)

    while not game.game_over:
        game.next_move()

    game = Game()
    go_again = input("Do you want to go again? Type anything to stop playing: ")

