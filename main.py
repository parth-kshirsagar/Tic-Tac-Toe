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
values = [i for i in range(1, 10)]
def print_board():
    os.system("clear")
    print("\t     |     |     ")
    print(f"\t  {values[0]}  |  {values[1]}  |  {values[2]}  ")
    print("\t_____|_____|_____")
    print("\t     |     |     ")
    print(f"\t  {values[3]}  |  {values[4]}  |  {values[5]}  ")
    print("\t_____|_____|_____")
    print("\t     |     |     ")
    print(f"\t  {values[6]}  |  {values[7]}  |  {values[8]}  ")
    print("\t     |     |     ")
    print('\n')
def check_winner():
    #Horizontal
    if values[0] == values[1] and values[1] == values[2]:
        print(f"\tPlayer {values[1]} is the winner")
        return True
    elif values[3] == values[4] and values[4] == values[5]:
        print(f"\tPlayer {values[4]} is the winner")
        return True
    elif values[6] == values[7] and values[8] == values[5]:
        print(f"\tPlayer {values[7]} is the winner")
        return True
    # Vertical
    elif values[0] == values[3] and values[3] == values[6]:
        print(f"\tPlayer {values[3]} is the winner")
        return True
    elif values[1] == values[4] and values[4] == values[7]:
        print(f"\tPlayer {values[4]} is the winner")
        return True
    elif values[2] == values[5] and values[5] == values[8]:
        print(f"\tPlayer {values[7]} is the winner")
        return True
    # Slanted
    elif values[0] == values[4] and values[4] == values[8]:
        print(f"\tPlayer {values[4]} is the winner")
        return True
    elif values[2] == values[4] and values[4] == values[6]:
        print(f"\tPlayer {values[4]} is the winner")
        return True
def inputs():
    for i in range(9):
        if i % 2 == 0:
            x = int(input("Player X : "))
            if values[x - 1] == "O":
                print("Try again")
                x = int(input("Player X : "))
                values[x - 1] = "X"
                if values[x - 1] == "O":
                    print("Try again")
                    x = int(input("Player X : "))
                    values[x - 1] = "X"
                else:
                    print("Player X Disqualified")
                    break
            else:
                values[x - 1] = "X"
            print_board()
            if check_winner() == True:
                break
        else:
            o = int(input("Player O : "))
            if values[o - 1] == "X":
                print("Try again")
                x = int(input("Player O : "))
                values[o - 1] = "O"
                if values[o - 1] == "X":
                    print("Try again")
                    x = int(input("Player O : "))
                    values[o - 1] = "O"
                else:
                    print("Player O Disqualified")
                    break
            else:
                values[o - 1] = "O"
            print_board()
            if check_winner() == True:
                break

################################################################
#                        Driver Program                        #
################################################################
if __name__ == '__main__':
    print_board()
    inputs()