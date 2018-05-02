import random

def random_choice(iteration, red_ball=40, black_ball=80):
    if not str(iteration).isdigit():
        raise('Format function random_choice(iterations:int [,count_red:int]  [,count black:int])')

    d = {'red': [i for i in range(1, red_ball+1)], 'black': [i for i in range(red_ball+1, red_ball+ black_ball+1)]}
    for _ in range(iteration):
        if random.choice(d.get('red') + d.get('black')) in d.get('red'):
            print('red')
        else:
            print('black')

random_choice(5, 10, 20)
print('\n')
random_choice(1, 100000, 100000)


