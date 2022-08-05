import random

your_sheet = [" ", " ", " ", " ", " "]

cpu_sheet = [" ", " ", " ", " ", " "]

keeper_u_left = '''
  _______________
|| \ O           ||
||   | |         ||
||    \ \        ||
'''
keeper_u_right = '''
  _______________
||           O / ||
||          | |  ||
||         / /   ||
'''
keeper_m_right = '''
  _______________
||       ___  __ ||
||       ___ O__ ||
||               ||
'''
keeper_m_left = '''
  _______________
|| __  ___       ||
|| __O ___       ||
||               ||
'''
keeper_b_right = '''
  _______________
||               ||
||       ___  __ ||
||       ___ O__ ||
'''
keeper_b_left = '''
  _______________
||               ||
|| __  ___       ||
|| __O ___       ||
'''
keeper_u_middle = '''
  _______________
||      |o|      ||
||      | |      ||
||      / \      ||
'''
keeper_m_middle = '''
  _______________
||    __ o __    ||
||      | |      ||
||      / \      ||
'''
keeper_b_middle = '''
  _______________
||               ||
||    __ 0 __    ||
||    __| |__    ||

'''

u_right = "ur"
u_left = "ul"
u_middle = "um"
b_right = "br"
b_left = "bl"
b_middle = "bm"
m_right = "mr"
m_left = "ml"
m_middle = "mm"

any_direction = [
    u_left, u_middle, u_right, b_left, b_middle, b_right, m_left, m_middle,
    m_right
]
mf_direction = [b_left, b_middle, b_right, m_left, m_middle, m_right]
df_direction = [b_left, b_middle, b_right]


class Team:
    def __init__(self, name):
        self.name = name
        self.targets = []
        self.position = [
            "FW", "FW", "FW", "MF", "MF", "MF", "MF", "DF", "DF", "DF", "GK"
        ]

        self.rostor = []

    def player_position(self):

        player_position = random.choice(self.position)
        self.rostor.append(player_position)
        self.position.remove(player_position)

        if self.position == []:
            self.position = self.rostor
        if player_position == "FW":
            print(self.name + "'S " + player_position, " is about to shoot")
            self.targets = any_direction
        elif player_position == "MF":
            print(self.name + "'S " + player_position, " is about to shoot")
            self.targets = mf_direction
        else:
            print(self.name + "'S " + player_position, " is about to shoot")
            self.targets = df_direction
        print("player left to shoot ", self.position)
        return self.targets


def keeper(save):

    if save == u_left:
        print(keeper_u_left)
    elif save == u_middle:
        print(keeper_u_middle)
    elif save == u_right:
        print(keeper_u_right)
    elif save == b_left:
        print(keeper_b_left)
    elif save == b_right:
        print(keeper_b_right)
    elif save == b_middle:
        print(keeper_b_middle)
    elif save == m_left:
        print(keeper_m_left)
    elif save == m_right:
        print(keeper_m_right)
    elif save == m_middle:
        print(keeper_m_middle)
    return save


def goal(shoot, save, player_direction):
    if shoot in player_direction:
        if shoot == save:
            print(" No Goal")
            return 0
        else:
            print("Goal!")
            return 1
    else:
        print("No Goal!")
        return 0


def clean_table_sheet(sheet):

    for i in range(5):
        sheet[i] = ' '
        sheet[i] = ' '


x = 0


def table_sheet(score, sheet):
    global x
    global your_sheet
    global cpu_sheet
    if x == 5:
        clean_table_sheet(your_sheet)
        clean_table_sheet(cpu_sheet)
        x = 0

    if x < 5:
        if score == 1:
            sheet[x] = "O"

        else:
            sheet[x] = "X"


while True:
    print('''\nWelcome to Penalty kick game!\nInstructions are the following:
    
  _______________
||ul    um     ur||
||ml    mm     mr||
||bl    bm     br||

Press u for upper, b for bottom and m for middle
Press l for left, r for right and m for middle
Example for upper left shoot or save you press ul
Forward players can shoot in all targets (u_left, u_middle, u_right, b_left,b_middle, b_right, m_left, m_middle, m_right)
Midfielder players can shoot in the following targets (b_left, b_middle, b_right, m_left, m_middle, m_right)
Defender players and Kepper can shoot in the follwoing targets(b_left, b_middle, b_right)\n'''
          )

    your_score = cpu_score = 0
    kick_set = 1

    while True:
        print(" 1)France\n", "2)Brazil\n", "3)USA\n", "4)Tunisia\n",
              "5)Japan\n")
        choice = input("Choose your team: ")
        if choice == "1":
            your_team = "France "
            break
        elif choice == "2":
            your_team = "Brazil "
            break
        elif choice == "3":
            your_team = "USA    "
            break
        elif choice == "4":
            your_team = "Tunisia"
            break
        elif choice == "5":
            your_team = "Japan  "
            break
        else:
            print("wrong input! Please try again")

    teams = ["France ", "Brazil ", "USA    ", "Tunisia", "Japan  "]

    teams.remove(your_team)
    cpu_team = random.choice(teams)
    your_team = Team(your_team)
    cpu_team = Team(cpu_team)
    print(your_team.name, "VS", cpu_team.name)

    while True:

        print("\nSet", kick_set, "\n")
        player_direction = your_team.player_position()
        shoot = input("\nkick the ball ")
        save = random.choice(player_direction)
        cpu_goalie = keeper(save)
        score = goal(shoot, cpu_goalie, player_direction)
        table_sheet(score, your_sheet)
        your_score = your_score + score
        player_direction = cpu_team.player_position()
        cpu_shoot = random.choice(player_direction)
        save = input('\nSave the ball  ')
        print(cpu_shoot)
        goalie = keeper(save)
        score = goal(goalie, cpu_shoot, any_direction)
        table_sheet(score, cpu_sheet)
        x += 1
        cpu_score = cpu_score + score
        print(f'''
Score Table
== == == == == == == == == ==
|{your_team.name} | {your_sheet[0]} | {your_sheet[1]} | {your_sheet[2]} | {your_sheet[3]} | {your_sheet[4]} |  {your_score}
|{cpu_team.name} | {cpu_sheet[0]} | {cpu_sheet[1]} | {cpu_sheet[2]} | {cpu_sheet[3]} | {cpu_sheet[4]} |  {cpu_score}
== == == == == == == == == ==''')
        kick_set += 1
        if kick_set == 5:
            if your_score - cpu_score == 2:
                print("You Won!!")
                break
            elif cpu_score - your_score == 2:
                print("You Lost!!")
                break
        elif kick_set < 6:

            if your_score - cpu_score == 3:
                print("You Won!!")
                break
            elif cpu_score - your_score == 3:
                print("You Lost!!")
                break
        elif kick_set >= 6:
            if your_score > cpu_score:
                print("You Won!!")
                break
            elif your_score < cpu_score:
                print("You lost!!")
                break

    play_again = input("Do you want to play again? Press Y for yes: ")
    if play_again.lower() == "y":
        clean_table_sheet(your_sheet)
        clean_table_sheet(cpu_sheet)
        x = 0
        continue
    else:
        print("See You Next Time!!")
        break
