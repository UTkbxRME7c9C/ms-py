import ms
import pfuncs

# No cases, assume input is valid.
def main():
    l = int(input("Enter length: "))
    w = int(input("Enter width: "))
    
    pfuncs.print_board_empty(l,w)

    obj = ms.sweeper(l,w,3)
    initW = int(input("Enter top coordinate: "))
    initL = int(input("Enter side coordinate: "))
    
    obj.generate_mines(initL,initW)
    pfuncs.print_board(obj)

    wincase = 0
    while (wincase == 0):
        initW = int(input("Enter top coordinate: "))
        initL = int(input("Enter side coordinate: "))
        if (obj.checked[initL][initW] == 1):
            print("Already checked!")
        elif (obj.mines[initL][initW] == -1):
            print("You lose!")
            pfuncs.print_board_answers(obj)
            wincase = 1
        else:
            obj.set_checked(initL,initW)
            if (obj.check_win()):
                print("You win!")
                pfuncs.print_board_answers(obj)
                wincase = 2
            else:
                pfuncs.print_board(obj)
    

if __name__ == "__main__":
    main()
