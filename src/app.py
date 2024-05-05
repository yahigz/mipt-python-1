from data import *
from pages import *

class KeyboardTrainingApp:

    def __init__(self):
        self.exercise_data = ExercisesList()
        current_section = Menu(self.exercise_data)