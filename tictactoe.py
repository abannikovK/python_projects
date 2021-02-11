def print_filed(current_state_l):
    print(" -------")
    print("| " + current_state_l[0] + " " + current_state_l[1] + " " + current_state_l[2] + " |")
    print("| " + current_state_l[3] + " " + current_state_l[4] + " " + current_state_l[5] + " |")
    print("| " + current_state_l[6] + " " + current_state_l[7] + " " + current_state_l[8] + " |")
    print(" -------")


def check_coordinates(coordinates, current_state_l):
    try:
        if coordinates[0].isdigit() == False or coordinates[1].isdigit() == False:
            print("You should enter numbers!")
            return False
        elif (
                int(coordinates[0]) > 3 or int(coordinates[0]) < 1
                or int(coordinates[1]) > 3 or int(coordinates[1]) < 1
        ):
            print("Coordinates should be from 1 to 3!")
            return False
        elif (
                (coordinates == ["1", "1"] and current_state_l[0] != " ") or (
                coordinates == ["1", "2"] and current_state_l[1] != " ")
                or (coordinates == ["1", "3"] and current_state_l[2] != " ") or (
                        coordinates == ["2", "1"] and current_state_l[3] != " ")
                or (coordinates == ["2", "2"] and current_state_l[4] != " ") or (
                        coordinates == ["2", "3"] and current_state_l[5] != " ")
                or (coordinates == ["3", "1"] and current_state_l[6] != " ") or (
                        coordinates == ["3", "2"] and current_state_l[7] != " ")
                or (coordinates == ["3", "3"] and current_state_l[8] != " ")
        ):
            print("This cell is occupied!")
            return False
        else:
            return True
    except Exception:
        return False


def update_field(player, coordinates):
    if coordinates == ["1", "1"]:
        currentState[0] = player
    elif coordinates == ["1", "2"]:
        currentState[1] = player
    elif coordinates == ["1", "3"]:
        currentState[2] = player
    elif coordinates == ["2", "1"]:
        currentState[3] = player
    elif coordinates == ["2", "2"]:
        currentState[4] = player
    elif coordinates == ["2", "3"]:
        currentState[5] = player
    elif coordinates == ["3", "1"]:
        currentState[6] = player
    elif coordinates == ["3", "2"]:
        currentState[7] = player
    elif coordinates == ["3", "3"]:
        currentState[8] = player

    return currentState


def check_game(currentStateL):
    # counts
    x_count = currentStateL.count("X")
    o_count = currentStateL.count("O")
    empty_count = currentStateL.count(" ")
    # counts on vectors
    horizontal1st = currentStateL[0:3]
    hor_count1X = horizontal1st.count("X")
    hor_count1O = horizontal1st.count("O")
    horizontal2nd = currentStateL[3:6]
    hor_count2X = horizontal2nd.count("X")
    hor_count2O = horizontal2nd.count("O")
    horizontal3rd = currentStateL[6:]
    hor_count3X = horizontal3rd.count("X")
    hor_count3O = horizontal3rd.count("O")
    vertical1st = [horizontal1st[0], horizontal2nd[0], horizontal3rd[0]]
    ver_count1X = vertical1st.count("X")
    ver_count1O = vertical1st.count("O")
    vertical2nd = [horizontal1st[1], horizontal2nd[1], horizontal3rd[1]]
    ver_count2X = vertical2nd.count("X")
    ver_count2O = vertical2nd.count("O")
    vertical3rd = [horizontal1st[2], horizontal2nd[2], horizontal3rd[2]]
    ver_count3X = vertical3rd.count("X")
    ver_count3O = vertical3rd.count("O")
    diagonalleft2right = [horizontal1st[0], horizontal2nd[1], horizontal3rd[2]]
    diag_count1X = diagonalleft2right.count("X")
    diag_count1O = diagonalleft2right.count("O")
    diagonalright2left = [horizontal1st[2], horizontal2nd[1], horizontal3rd[0]]
    diag_count2X = diagonalright2left.count("X")
    diag_count2O = diagonalright2left.count("O")

    # general calcs
    hor_flag = False
    if hor_count1O == 3 or hor_count1X == 3:
        hor_flag = True
    elif hor_count2O == 3 or hor_count2X == 3:
        hor_flag = True
    elif hor_count3O == 3 or hor_count3X == 3:
        hor_flag = True
    else:
        hor_flag = False

    diag_flag = False
    if diag_count1O == 3 or diag_count1X == 3:
        diag_flag = True
    elif diag_count2O == 3 or diag_count2X == 3:
        diag_flag = True
    else:
        diag_flag = False

    ver_flag = False
    if ver_count1O == 3 or ver_count1X == 3:
        ver_flag = True
    elif ver_count2O == 3 or ver_count2X == 3:
        ver_flag = True
    elif ver_count3O == 3 or ver_count3X == 3:
        ver_flag = True
    else:
        ver_flag = False

    # win calcs
    x_wins = False
    o_wins = False

    if hor_count1X == 3 or hor_count2X == 3 or hor_count3X == 3 or ver_count1X == 3 or ver_count2X == 3 or ver_count3X == 3:  # or diag_count1X == 3 or diag_count2X == 3:
        x_wins = True
    if hor_count1O == 3 or hor_count2O == 3 or hor_count3O == 3 or ver_count1O == 3 or ver_count2O == 3 or ver_count3O == 3:  # or diag_count1O == 3 or diag_count2O == 3:
        o_wins = True

    game_not_finished = empty_count > 0 and hor_flag == False and ver_flag == False and diag_flag == False
    impossible = (((x_count - o_count > 1) or (o_count - x_count > 1)) or (o_wins and x_wins)) and empty_count == 0
    draw = empty_count == 0 and hor_flag == False and ver_flag == False  # and diag_flag == False
    x_won = draw == False and impossible == False and x_wins == True
    o_won = draw == False and impossible == False and o_wins == True

    if impossible:
        return "Impossible"
    elif game_not_finished:
        result = "Game not finished"
    elif draw:
        return "Draw"
    elif x_won:
        return "X wins"
    elif o_won:
        return "O wins"


# initialize the game field
x_player = ""
o_player = ""
win_counter = 1
initial_game_state = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
currentState = initial_game_state
# print empty field
print("---------------------Hi! You are now starting Tic Tac Toe Game!---------------------")
print_filed(initial_game_state)

# starting the game
while True:
    win_counter += 1

    while True:  # Loop for getting right coords for X
        # Get X player coords
        x_player = input("Enter the X coordinates: ").split()
        # Check whether they were entered correctly
        if check_coordinates(x_player, currentState) == False:
            continue
        break

    # Update field state
    update_field("X", x_player)

    # Print updated field
    print_filed(currentState)

    if win_counter > 3:
        # Check game state
        if check_game(currentState) == "Impossible":
            print("Impossible state! Restart!")
            break
        elif check_game(currentState) == "Draw":
            print("Draw")
            break
        elif check_game(currentState) == "X wins":
            print("X wins")
            break
        elif check_game(currentState) == "O wins":
            print("O wins")
            break



    while True:  # Loop for getting right coords for O
        # Get O player coords
        o_player = input("Enter the O coordinates: ").split()
        # Check whether they were entered correctly
        if check_coordinates(o_player, currentState) == False:
            continue
        break

    # Update field
    update_field("O", o_player)

    # Print updated field
    print_filed(currentState)

    if win_counter > 3:
        # Check game state
        if check_game(currentState) == "Impossible":
            print("Impossible state! Restart!")
            break
        elif check_game(currentState) == "Draw":
            print("Draw")
            break
        elif check_game(currentState) == "X wins":
            print("X wins")
            break
        elif check_game(currentState) == "O wins":
            print("O wins")
            break

