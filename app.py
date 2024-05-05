import time

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import *

from data import *

exercise_data = ExercisesList()

class Menu:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu")
        self.root.geometry("600x200+670+380")

        ToKeyboardExercise = ttk.Button(
            text="Start exercise", command=self.to_keyboard_exercise
        )
        ToUploadExerciseFromFile = ttk.Button(
            text="Upload exercise from file", command=self.upload_from_file
        )
        ToUploadExerciseManually = ttk.Button(
            text="Upload exercise manually", command=self.to_upload_manually
        )
        ClearExerciseList = ttk.Button(
            text="Delete all exercises", command=self.clear_exercises_list
        )   
        Exit = ttk.Button(text="Exit", command=self.root.destroy)
        ToKeyboardExercise.pack()
        ToUploadExerciseFromFile.pack()
        ToUploadExerciseManually.pack()
        ClearExerciseList.pack()
        Exit.pack()

        self.root.mainloop()

    def to_keyboard_exercise(self):
        self.root.destroy()
        global current_section
        current_section = KeyboardExercise()
        global section_name
        section_name = "KeyboardExercise"

    def upload_from_file(self):
        filepath = filedialog.askopenfilename()
        if filepath == None:
            return
        with open(filepath, "r") as file:
            current = Exercise([])
            for line in file.readlines():
                for elem in line.split():
                    current.exercise.append(elem)
            exercise_data.add(current)

    def to_upload_manually(self):
        self.root.destroy()
        current_section = UploadExerciseManually()

    def clear_exercises_list(self):
        exercise_data.clear()


class KeyboardExercise:

    def end_exercise(self):
        end_time = time.time()
        duration = round(end_time - self.start_time, 3)
        if self.mistake_count == 0:
            Result = ttk.Label(
                text="Exercise done in " + str(duration) + "s with no mistakes!"
            )
            Result.pack()
        elif self.mistake_count == 1:
            Result = ttk.Label(
                text="Exercise done in "
                + str(duration)
                + "s with "
                + str(self.mistake_count)
                + " mistake"
            )
            Result.pack()
        else:
            Result = ttk.Label(
                text="Exercise done in "
                + str(duration)
                + "s with "
                + str(self.mistake_count)
                + " mistakes"
            )
            Result.pack()
        speed = round(len(self.current_exercise_str) / duration, 1)
        Speed = ttk.Label(text="Your typing speed is " + str(speed) + " symb/sec")
        Speed.pack()

    def is_valid(self, input):
        if len(input) > len(self.current_exercise_str):
            return 1 == 0
        if input[len(input) - 1] != self.current_exercise_str[len(input) - 1]:
            self.mistake_count += 1
            self.MistakeCounter.configure(
                text="Mistakes: " + str(self.mistake_count), foreground="red"
            )
            return 1 == 0

        if len(input) == len(self.current_exercise_str):
            self.end_exercise()
        return 1 != 0

    def __init__(self):
        self.start_time = time.time()
        self.root = tk.Tk()
        self.root.title("Exercise")
        self.root.geometry("600x200+670+380")
        self.mistake_count = 0

        self.current_exercise = exercise_data.pick()
        self.current_exercise_str = " ".join(self.current_exercise.exercise)

        self.MistakeCounter = ttk.Label(
            text="Mistakes: " + str(self.mistake_count), foreground="green"
        )
        self.MistakeCounter.pack(anchor=NE, pady=0)

        Answer = ttk.Label(text=self.current_exercise_str)
        Answer.pack()

        check = (self.root.register(self.is_valid), "%P")

        Input = ttk.Entry(validate="key", validatecommand=check, width=50)
        Input.pack(anchor=CENTER)
        Input.focus_set()

        ToMenu = ttk.Button(text="Back to menu", command=self.to_menu)
        ToMenu.pack()

        self.root.mainloop()

    def to_menu(self):
        self.root.destroy()
        current_section = Menu()


class UploadExerciseManually:

    def add_manually(self):
        exercise_data.add(Exercise(self.Input.get().split()))
        self.to_menu()

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Upload exercise manually") 
        self.root.geometry("600x200+670+380")

        self.Input = ttk.Entry()
        self.Input.pack()
        self.Input.focus_set()
        Confirm = ttk.Button(text="Confirm the input", command=self.add_manually)
        Confirm.pack()

        ToMenu = ttk.Button(text="Back to menu", command=self.to_menu)
        ToMenu.pack()

    def to_menu(self):
        self.root.destroy()
        current_section = Menu()


class KeyboardTrainingApp:

    def __init__(self):
        current_section = Menu()