import random as rand

class Exercise:
    def __init__(self, words: list):
        self.exercise = words


class ExercisesList:
    def __init__(self):
        self.Exercises = []
        with open("src/exercises.txt") as file:
            for line in file.readlines():
                self.Exercises.append(Exercise(line.split()))

    def clear(self):
        with open("src/exercises.txt", "wb"):
            pass
        self.Exercises.clear()

    def pick(self):
        index = rand.randint(0, len(self.Exercises) - 1)
        return self.Exercises[index]

    def add(self, exer: Exercise):
        with open("src/exercises.txt", "a") as file:
            for elem in exer.exercise:
                file.write(elem)
                file.write(" ")
            file.write("\n")
            self.Exercises.append(Exercise(exer.exercise))
