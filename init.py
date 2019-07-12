import pandas as pd
import random

BALLOONS = ['red', 'green', 'blue']
BALLOONS_COLORS = 3
RED = BALLOONS[0]
RED_MAX_PUMPS = 8
GREEN = BALLOONS[1]
GREEN_MAX_PUMPS = 32
BLUE = BALLOONS[2]
BLUE_MAX_PUMPS = 64
NUM_TRIALS = 90
NUM_TRIALS_RANDOM = 30
NUM_TRIALS_COLOR = 20


def generate_excel():
    colors = generate_balloon_colors()
    max_pumps = generate_trials(colors)
    df = pd.DataFrame(
        {'imageFile': colors,
         'maxPump': max_pumps})
    df.to_excel('trialTypes.xlsx', index=False, encoding='utf8')
    return


def generate_balloon_colors():
    colors = []
    for color in range(0, NUM_TRIALS_RANDOM):
        colors.append(random.choice(BALLOONS))

    red = [RED] * NUM_TRIALS_COLOR
    green = [GREEN] * NUM_TRIALS_COLOR
    blue = [BLUE] * NUM_TRIALS_COLOR

    colors += red
    colors += green
    colors += blue

    if len(colors) != NUM_TRIALS:
        raise Exception("[Error] Generated {} balloons colors did not match {}.".format(len(colors), NUM_TRIALS))
    return colors


def generate_trials(colors):
    trials = []
    red_trials = []
    green_trials = []
    blue_trials = []
    for trial in range(0, NUM_TRIALS_RANDOM):
        if colors[trial] == 'red':
            max_pumps = random.randint(1, RED_MAX_PUMPS-1)
        elif colors[trial] == 'green':
            max_pumps = random.randint(1, GREEN_MAX_PUMPS-1)
        elif colors[trial] == 'blue':
            max_pumps = random.randint(1, BLUE_MAX_PUMPS-1)
        else:
            raise Exception("[Error] Balloon not identified")
        trials.append(max_pumps)

    for pumps in range(0, NUM_TRIALS_COLOR):
        red_trials.append(random.randint(1, RED_MAX_PUMPS-1))
        green_trials.append(random.randint(1, GREEN_MAX_PUMPS-1))
        blue_trials.append(random.randint(1, BLUE_MAX_PUMPS-1))
    trials += red_trials + green_trials + blue_trials
    if len(trials) != 90:
        raise Exception("[Error] Trials generated does not match " + str(NUM_TRIALS) + '.' )
    return trials











