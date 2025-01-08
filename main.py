import random
from itertools import combinations
from collections import Counter

def roll_dice(n: int) -> list[int]:
    return [random.randint(1, 6) for _ in range(n)]

def is_valid(dice: list[int]) -> bool:
    if 1 in dice or 5 in dice:
        return True
    for value in Counter(dice).values():
        if value >= 3:
            return True
    return False

def score(dice: tuple[int, ...]) -> int:
    hashmap = Counter(dice)

    # straight
    if len(dice) == 6 and len(set(hashmap.keys())) == 6:
        return 1500

    # partial straight
    if len(dice) == 5 and len(set(hashmap.keys())) == 5:
        if hashmap[1]and not hashmap[6]:
            return 500
        elif not hashmap[1] and hashmap[6]:
            return 750

    # x of a kind
    for v, n in hashmap.items():
        if n >= 3:
            if v == 1:
                v = 10
            return 100 * v * (2 ** (n - 3))

    if len(dice) == 1:
        if 1 in dice:
            return 100
        if 5 in dice:
            return 50
    return 0


def get_selections(dice: list[int]):
    out = [0] * len(dice)
    for i in range(len(dice)):
        for combination in set(combinations(dice, i+1)):
            combination_score = score(combination)
            if combination_score > out[i]:
                out[i] = combination_score
                print(combination_score, combination)
        if out[i]:
            print(f"for {i+1} dice the best score is {out[i]}")



def main():
    dice = roll_dice(6)
    # dice = [1,2,3,4,5,6]
    # dice = [2,3,2,2,2,4]
    # dice = [2,2,2,2,2,2]
    # dice = [1,1,1,1,1,1]
    dice = [1,2,3,4,5,5]
    print(f"Dice: {dice}")
    if not is_valid(dice):
        print("Invalid dice")
        return
    get_selections(dice)



if __name__ == "__main__":
    main()

# print(get_possiblities(roll_dice(6)))