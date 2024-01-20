def print_board_empty(length, width):
    print("  " + " ".join(str(i) for i in range(width)))
    for i in range(length):
        print(" "+ ("*-" * width) + "*")
        print(str(i) + ("|?" * width) + "|")
    print(" "+ ("*-" * width) + "*")
    
def print_board(sweep):
    print("  " + " ".join(str(i) for i in range(sweep.width)))
    for i in range(sweep.length):
        print(" "+ ("*-" * sweep.width) + "*")
        print(str(i), end="")
        for j in range(sweep.width):
            if (sweep.checked[i][j] == 1):
                if (sweep.mines[i][j] == 0):
                    print("| ", end="")
                else:
                    print("|" + str(sweep.mines[i][j]), end="")
            else:
                print("|?", end="")
        print("|")
    print(" "+ ("*-" * sweep.width) + "*")
    
def print_board_answers(sweep):
    print("  " + " ".join(str(i) for i in range(sweep.width)))
    for i in range(sweep.length):
        print(" "+ ("*-" * sweep.width) + "*")
        print(str(i), end="")
        for j in range(sweep.width):
            if (sweep.mines[i][j] == 0):
                print("| ", end="")
            elif (sweep.mines[i][j] == -1):
                print("|X", end="")
            else:
                print("|" + str(sweep.mines[i][j]), end="")
        print("|")
    print(" "+ ("*-" * sweep.width) + "*")
    