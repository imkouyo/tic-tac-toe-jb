# write your code here
from collections import Counter

# compose_steps = input("Enter cells:")
compose_steps = "_________"
discompose_steps = list(compose_steps)
chess_count = Counter(compose_steps)
WIN_METHOD = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
              (0, 3, 6), (1, 4, 7), (2, 5, 8),
              (0, 4, 8), (2, 4, 6)]
answer = ""
steps = 0
CHESS = ['O', 'X']
while True:
    position = []
    try:
        position = [int(x) for x in input("Enter the coordinates").split()]
    except ValueError:
        print("You should enter numbers!")
    if len(position) != 2:
        print("You should enter numbers!")
    elif position[0] > 3 or position[1] > 3:
        print("Coordinates should be from 1 to 3!")
    elif discompose_steps[(position[1] - 1 + (position[0] - 1) * 3)] != '_':
        print("This cell is occupied! Choose another one!")
    else:
        steps += 1
        coordinates = (position[1] - 1 + (position[0] - 1) * 3)
        discompose_steps[coordinates] = CHESS[steps % 2]
        PANEL = f"""---------
| {discompose_steps[0]} {discompose_steps[1]} {discompose_steps[2]} |
| {discompose_steps[3]} {discompose_steps[4]} {discompose_steps[5]} |
| {discompose_steps[6]} {discompose_steps[7]} {discompose_steps[8]} |
---------
"""
        print(PANEL)
        for method in WIN_METHOD:
            chess_type = discompose_steps[method[0]]
            for chess in method:
                if chess_type == discompose_steps[chess]:
                    continue
                else:
                    chess_type = None
                    break
            if chess_type is not None and chess_type != '_':
                answer += chess_type
        if answer == 'X' or answer == 'O':
            print(PANEL)
            print("{} wins".format(answer))
            break
        elif steps == 9:
            print(PANEL)
            print("Draw")
            break









