import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []

        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def set_contents(self, contents):
        self.contents = list(contents)

    def draw(self, num):
        if len(self.contents) < num:
            return self.contents

        values = []
        samples = random.sample(range(0, len(self.contents)), num)

        for i in samples:
            values.append(self.contents[i])
            self.contents[i] = 0

        while(0 in self.contents):
            self.contents.remove(0)

        return values


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0

    temp_contents = list(hat.contents)

    for i in range(num_experiments):
        samples = hat.draw(num_balls_drawn)
        hat.set_contents(temp_contents)

        found = True

        for key, val in expected_balls.items():
            if samples.count(key) < val:
                found = False
                break

        if found:
            M += 1

    return M / num_experiments


hat = Hat(blue=3, red=2, green=6)
probability = experiment(hat=hat, expected_balls={
                         "blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=1000)

print(probability)
