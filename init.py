import pandas as pd
import random

BALLOONS = ['redBalloon', 'greenBalloon', 'blueBalloon']
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
        {'randomBalloon': colors,
         'maxPumps': max_pumps},
        columns=['randomBalloon', 'maxPumps'])
    df.to_excel('trialTypes.xlsx', index=False, encoding='utf8')
    return


def generate_balloon_colors():
    colors = []
    red_counter = 0
    green_counter = 0
    blue_counter = 0
    balloons = BALLOONS
    while len(balloons) != 0:
        random_balloon = random.choice(balloons)
        if random_balloon is RED:
            red_counter += 1
            if red_counter == 10:
                balloons.remove(RED)
        elif random_balloon is GREEN:
            green_counter += 1
            if green_counter == 10:
                balloons.remove(GREEN)
        elif random_balloon is BLUE:
            blue_counter += 1
            if blue_counter == 10:
                balloons.remove(BLUE)
        colors.append(random_balloon)

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
        if colors[trial] == RED:
            max_pumps = random.randint(1, RED_MAX_PUMPS - 1)
        elif colors[trial] == GREEN:
            max_pumps = random.randint(1, GREEN_MAX_PUMPS - 1)
        elif colors[trial] == BLUE:
            max_pumps = random.randint(1, BLUE_MAX_PUMPS - 1)
        else:
            raise Exception("[Error] Balloon '{}' not identified.".format(colors[trial]))
        trials.append(max_pumps)

    for pumps in range(0, NUM_TRIALS_COLOR):
        red_trials.append(random.randint(1, RED_MAX_PUMPS - 1))
        green_trials.append(random.randint(1, GREEN_MAX_PUMPS - 1))
        blue_trials.append(random.randint(1, BLUE_MAX_PUMPS - 1))
    trials += red_trials + green_trials + blue_trials
    if len(trials) != NUM_TRIALS:
        raise Exception("[Error] Trials generated '{}' does not match {} ".format(len(trials), NUM_TRIALS))
    return trials
