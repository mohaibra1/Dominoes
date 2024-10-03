# Write your code here
from itertools import combinations_with_replacement
import random, copy

comb = []
computer_pieces = []
player_pieces = []
domino_snake_1 = []


def make_random_combination():
    global comb
    comb = list(combinations_with_replacement([0, 1, 2, 3, 4, 5, 6], 2))
    return comb


def shuffle_list():
    global comb
    random.shuffle(comb)


def generate_pieces():
    global comb
    generate_pieces = []
    for i in range(0, 7):
        shuffle_list()
        num = generate_random_num(7)
        generate_pieces.append(comb[num])
        comb.pop(num)
    return generate_pieces


def start_combination():
    global computer_pieces, player_pieces
    c = generate_pieces()
    computer_pieces = copy.deepcopy(c)
    p = generate_pieces()
    player_pieces = copy.deepcopy(p)


def domino_snake():
    global domino_snake_1
    c_max = max(computer_pieces)
    p_max = max(player_pieces)
    if c_max == (6, 6):
        status = 'player'
        domino_snake_1.append(c_max)
        computer_pieces.remove(c_max)
        return status
    elif p_max == (6, 6):
        status = 'computer'
        domino_snake_1.append(p_max)
        player_pieces.remove(p_max)
        return status
    elif c_max == (5, 5):
        status = 'player'
        domino_snake_1.append(c_max)
        computer_pieces.remove(c_max)
        return status
    elif p_max == (5, 5):
        status = 'computer'
        domino_snake_1.append(p_max)
        player_pieces.remove(p_max)
        return status

    return ''


def generate_random_num(index, num=0):
    random_num = random.randint(num, index)
    return random_num


def tuple_to_list(data):
    t_to_l = []  # Tuple to list
    for l in data:
        t_to_l.append(list(l))
    return t_to_l


def first_instance_of_game():
    global comb, computer_pieces, player_pieces, domino_snake_1
    while True:
        make_random_combination()
        start_combination()
        status = domino_snake()
        if status != '':
            comb = tuple_to_list(comb)
            computer_pieces = tuple_to_list(computer_pieces)
            player_pieces = tuple_to_list(player_pieces)
            domino_snake_1 = [list(domino_snake_1[0])]
            return status
        else:
            continue


def domino_snake_effect(num, random_list):
    m = num
    if num > 0:
        index = num - 1
        # domino_snake_1.append(random_list[index])
        # random_list.pop(index)
        move_domino_player(m,index, random_list)
    elif num < 0:
        num = abs(num)
        index = num - 1
        # domino_snake_1.insert(0, random_list[index])
        # random_list.pop(index)
        move_domino_player(m,index, random_list)
    else:
        length = len(comb) - 1
        if length != 0:
            insert_random = generate_random_num(length)
            random_list.append(comb[insert_random])
            comb.pop(insert_random)


def move_domino_player(num,index, random_list):
    i = domino_snake_1[0][0]
    j = domino_snake_1[- 1][-1]
    temp = random_list[index]
    reversed_temp = copy.deepcopy(temp)
    reversed_temp.reverse()
    if num < 0:
        if i == temp[1]:
            domino_snake_1.insert(0, temp)
            random_list.pop(index)
        elif i == temp[0]:
            domino_snake_1.insert(0, reversed_temp)
            random_list.pop(index)
        elif j == temp[0]:
            domino_snake_1.append(temp)
            random_list.pop(index)
        elif j == temp[1]:
            domino_snake_1.append(reversed_temp)
            random_list.pop(index)
        else:
            raise Exception('Illegal move. Please try again.')
    elif num > 0:
        if j == temp[0]:
            domino_snake_1.append(temp)
            random_list.pop(index)
        elif j == temp[1]:
            domino_snake_1.append(reversed_temp)
            random_list.pop(index)
        elif i == temp[1]:
            domino_snake_1.insert(0, temp)
            random_list.pop(index)
        elif i == temp[0]:
            domino_snake_1.insert(0, reversed_temp)
            random_list.pop(index)
        else:
            raise Exception('Illegal move. Please try again.')
    else:
        raise Exception('Illegal move. Please try again.')
def move_domino_computer(lis):
    i = domino_snake_1[0][0]
    j = domino_snake_1[- 1][-1]
    temp = lis
    reversed_temp = copy.deepcopy(temp)
    reversed_temp.reverse()
    if j == temp[0]:
        domino_snake_1.append(temp)
        computer_pieces.remove(lis)
        return True
    elif j == temp[1]:
        domino_snake_1.append(reversed_temp)
        computer_pieces.remove(lis)
        return True
    elif i == temp[1]:
        domino_snake_1.insert(0, temp)
        computer_pieces.remove(lis)
        return True
    elif i == temp[0]:
        domino_snake_1.insert(0, reversed_temp)
        computer_pieces.remove(lis)
        return True
    else:
        #raise Exception('Illegal move. Please try again.')
        return False

def print_game():
    print('=' * 70)

    print(f'Stock size: {len(comb)}')
    print(f'Computer pieces: {len(computer_pieces)}')
    print()
    d = len(domino_snake_1)
    if d < 6:
        for j in domino_snake_1:
            print(j, end='')
        print()
    else:
        print(
            f'{domino_snake_1[0]}{domino_snake_1[1]}{domino_snake_1[2]}...{domino_snake_1[d - 3]}{domino_snake_1[d - 2]}{domino_snake_1[d - 1]}')
    print()
    print('Your pieces:')
    count = 1
    for i in player_pieces:
        print(f'{count}: {list(i)}')
        count = count + 1
    print()


def flat_list():
    flat_l = [element for inn in domino_snake_1 for element in inn]
    return flat_l


def check_winner():
    player = len(player_pieces)
    computer = len(computer_pieces)
    if player == 0:
        print('Status: The game is over. You won!')
        return True
    elif computer == 0:
        print('Status: The game is over. The computer won!')
        return True
    else:
        check = flat_list()
        length = len(check) - 1
        first_el = check[0]
        last_el = check[length]
        if first_el == last_el:
            count = check.count(first_el)
            if count == 8:
                print("Status: The game is over. It's a draw!")
                return True
    return False

def count_domino_snake_and_computer_domino():
    global computer_pieces, domino_snake_1
    dict_count = {0:0,1:0,2:0,3:0,4:0,5:0,6:0}
    joined_list = computer_pieces + domino_snake_1
    for i in joined_list:
        for j in i:
            dict_count[j] += 1
    return dict_count
def scores():
    joined = count_domino_snake_and_computer_domino()
    score_dic = {}
    for i in computer_pieces:
        total = joined[i[0]] + joined[i[1]]
        score_dic[total] = i

    return score_dic

def computer_choice():
    count = scores()
    sorted_dict = dict(sorted(count.items()))
    length = len(sorted_dict) - 1
    nothing_added = True
    for i in reversed(sorted_dict.keys()):
        if move_domino_computer(sorted_dict[i]):
            nothing_added = False
            break
    if nothing_added:
        domino_snake_effect(0, computer_pieces)

def check_user_input():
    while True:
        try:
            user_input = int(input())
            if abs(int(user_input)) > len(player_pieces):
                raise Exception('Something went wrong!')
        except:
            print('Invalid input. Please try again.')
            continue
        else:
            break
    return user_input


def play_domino():
    status = first_instance_of_game()
    game_start = True
    while game_start:
        print_game()
        if check_winner():
            game_start = False
        elif status == 'player':
            if len(comb) != 0:
                print("Status: It's your turn to make a move. Enter your command.")
                # user_input = check_user_input()
                # user_input = int(user_input)
                # domino_snake_effect(user_input, player_pieces)

                while True:
                    try:
                        #user_input = check_user_input()
                        #user_input = int(user_input)
                        comp_ln = len(player_pieces)
                        g_number = random.randrange(-comp_ln, comp_ln)
                        domino_snake_effect(g_number, player_pieces)
                    except:
                        print('Illegal move. Please try again.')
                        continue
                    else:
                        status = '' + 'computer'
                        break
                continue
        else:
            print("Status: Computer is about to make a move. Press Enter to continue...")
            print('>')
            # user_input = input()

            #while True:
             #   try:
                    #comp_ln = len(computer_pieces)
                    #g_number = random.randrange(-comp_ln, comp_ln)
                    #domino_snake_effect(g_number, computer_pieces)
            computer_choice()
              #  except:
               #     continue
                #else:
            status = '' + 'player'
                 #   break
            continue


play_domino()