from die import Die

ROLLS = 10
dice = [Die(), Die(12), Die(20)]

for die in dice:
    print(f"\nRolling die with {die.sides} sides:")
    for _ in range(ROLLS):
        die.roll_die()

