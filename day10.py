import re
from abc import ABC, abstractmethod


class ChipContainer(ABC):
    def __init__(self, id):
        self.id = id

    @abstractmethod
    def add_chip(self, chip_id):
        pass


class Bot(ChipContainer):
    def __init__(self, id):
        super(Bot, self).__init__(id)
        self.low_target = None # Bot or Output
        self.high_target = None # Bot or Output
        self.chips = () # tuple of chip_id

    def can_process(self):
        return len(self.chips) == 2

    def process(self):
        assert(self.can_process())
        self.low_target.add_chip(min(self.chips))
        self.high_target.add_chip(max(self.chips))
        self.chips = ()

    def add_chip(self, chip_id):
        self.chips += (chip_id,)
        if 61 in self.chips and 17 in self.chips:
            print("Part1: {}".format(self.id))


class Output(ChipContainer):
    def __init__(self, id):
        super(Output, self).__init__(id)
        self.chip = None

    def add_chip(self, chip_id):
        assert(self.chip is None)
        self.chip = chip_id


bots = [Bot(i) for i in range(0,1000)]
outputs = [Output(i) for i in range(0,100)]


def read_input(filepath):
    with open(filepath) as f:
        return [line.strip() for line in f]


def preprocess_input(input):
    goes_regex = re.compile("value (\d+) goes to bot (\d+)")
    gives_regex = re.compile("bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)")

    for line in input:
        if goes_regex.match(line):
            chip_id, bot_id = goes_regex.match(line).groups()
            bots[int(bot_id)].add_chip(int(chip_id))
        elif gives_regex.match(line):
            bot_id, low_target, low_target_id, high_target, high_target_id = gives_regex.match(line).groups()
            bot = bots[int(bot_id)]
            if low_target == "bot":
                bot.low_target = bots[int(low_target_id)]
            else:
                bot.low_target = outputs[int(low_target_id)]
            
            if high_target == "bot":
                bot.high_target = bots[int(high_target_id)]
            else:
                bot.high_target = outputs[int(high_target_id)]
        else:
            assert(0)


def process():
    do_continue = True
    while do_continue:
        do_continue = False
        for b in [b for b in bots if b.can_process()]:
            b.process()
            do_continue = True


if __name__ == "__main__":
    input = read_input("day10.txt")
    
    preprocess_input(input)
    process()

    outputs_product = 1
    for i in range(0,3):
        outputs_product *= outputs[i].chip

    print("Part2: {}".format(outputs_product))
