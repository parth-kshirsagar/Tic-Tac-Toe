"""
\\              //\\
 \\            //  \\
  \\          //    \\
   \\        //      \\  
    \\      //        \\  f"sine"
     \\    //          \\
      \\  //            \\
       \\//              \\
"""
import os


class TicTacToe:
    def __init__(self):
        self.values = [z for z in range(1, 10)]
        self.winner = None

    def print_board(self):
        for n in range(1, len(self.values) + 1):
            print(self.values[n - 1], end=' | ')
            if n in [3 * x for x in range(1, 3)]:
                print("\n--+---+---")

    def is_valid(self, index):
        if self.values[index - 1] in [u for u in range(1, 10)] or self.values[index - 1] != 'X' or \
                self.values[index - 1] != 'O':
            return True
        else:
            return False

    def play(self, index, player):
        if self.is_valid(index):
            self.values[index - 1] = player
            return self.values
        else:
            print("Invalid Sqaure. You Are Disqualified By Lord.High.Commander")
            return None

    def check_win(self, player):
        for x in range(1):
            if self.values[x] == self.values[x + 1] == self.values[x + 2] == player or \
                    self.values[x] == self.values[x + 3] == self.values[x + 6] == player or \
                    self.values[0] == self.values[4] == self.values[8] == player or \
                    self.values[2] == self.values[4] == self.values[6] == player:
                self.winner = player
                return True


if __name__ in '__main__':
    t = TicTacToe()
    for i in range(9):
        os.system("clear")
        t.print_board()
        if i % 2 == 0:
            letter = 'X'
            t.play(int(input("\nPlayer X : ")), letter)
            if t.check_win(letter):
                print("{} IS THE WINNER!!!".format(t.winner))
                break
        else:
            letter = 'O'
            t.play(int(input("\nPlayer O : ")), letter)
            if t.check_win(letter):
                print("{} IS THE WINNER!!!".format(t.winner))
                break
