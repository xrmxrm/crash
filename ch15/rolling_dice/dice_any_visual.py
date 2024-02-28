import plotly.express as px

from die import Die

def roll_dice(rolls, sides=[6,6]):

    # Create dice
    dice = []

    for side in sides:
        dice.append(Die(side))

    # Make some rolls, and store results in a list.
    results = []

    for _ in range(rolls):
        result = 0
        for i in range(len(dice)):
            result += dice[i].roll()
        results.append(result)

    # Analyze the results.
    frequencies = []
    max_result = 0
    for i in range(len(dice)):
        max_result += dice[i].num_sides

    min_result = len(dice)

    poss_results = range(min_result, max_result+1)
    for value in poss_results:
        frequency = results.count(value)
        frequencies.append(frequency)

    # Visualize the results.
    title = f"Rolling Dice of sides {sides} -- {rolls} Times"
    labels = {'x': 'Result', 'y': 'Frequency of Result'}
    fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

    # Further customize chart.
    fig.update_layout(xaxis_dtick=1)
                
    fig.show()

if __name__ == "__main__":
    NUM_ROLLS = 10000
    SIDES = [6, 10, 6, 20]

    roll_dice(NUM_ROLLS, SIDES)
