#main.py
from creature import Creature
from environment import Environment
from board_space import BoardSpace
import random

def main():
    diamensions = input("Diamensions: ").split(" ")
    diamensions = tuple([int(diamension) for diamension in diamensions])
    print(f"Diamensions: {diamensions}")
    hospitality = int(input("Hospitality Level 1-5 (1=Inhospitable)"))
    environment = Environment(diamensions=diamensions, hospitality=hospitality)
    base_creature = Creature(id=0, name=random.choice(["John", "Jane"]), spawn=(random.randrange(0,diamensions[0]), random.randrange(0,diamensions[0])))
    environment[base_creature.spawn] = base_creature
    print(environment)

if __name__ == "__main__":
    main()