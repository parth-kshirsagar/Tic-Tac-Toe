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
def inputs_and_check_winner():
    for i in range(9):
        if i % 2 == 0:
            x = int(input("Player X : "))
            values[x - 1] = "X"
            print_board()
        else:
            o = int(input("Player O : "))
            values[o - 1] = "O"
            print_board()

################################################################
#                        Driver Program                        #
################################################################
if __name__ == '__main__':
    print_board()
    inputs_and_check_winner()