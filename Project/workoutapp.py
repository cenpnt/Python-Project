from tkinter import *
from PIL import ImageTk, Image
from explain_plan import Explain
from workout_functions import *
import json
from tkinter import messagebox
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class FirstWindow:
    def __init__(self):
        self.first_window = self
        self.window = Tk()
        self.window.title("Workout App")
        self.window.geometry("600x850+0+0")
        self.font_title = ("TKDefaultFont", 20, "bold")
        self.font = ("TKDefaultFont", 16, "bold")

        menubar = Menu(self.window)
        self.window.config(menu=menubar)

        list_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=list_menu)
        list_menu.add_command(label="Exit", command=self.window.quit)

        frame1 = Frame(self.window)
        frame1.pack(padx=10, pady=10)
        Label(frame1, text= "Welcome to Workout App", font= self.font_title).grid(row=1, column=1, sticky= NSEW)

        #first step
        Label(frame1, text= "First Step: TDEE Calculator", font= self.font).grid(row=2, column=1, sticky= NSEW)
        Label(frame1, text= "Learn How Many Calories You Burn Every Day").grid(row=3, column=1, sticky= NSEW)

        self.button1 = StringVar()
        self.button1.set("Male") #default value

        frame2 = Frame(self.window)
        frame2.pack(padx=10, pady=10)
        #choose gender
        Label(frame2, text= "Gender").grid(row=4, column=1, sticky= NSEW)
        Radiobutton(frame2, variable= self.button1, value = "Male").grid(row=4, column=2, sticky= NSEW)
        Label(frame2, text="Male").grid(row=4, column=3, sticky= NSEW)
        Radiobutton(frame2, variable= self.button1, value= "Female").grid(row=4, column=4, sticky= NSEW)
        Label(frame2, text= "Female").grid(row=4, column=5, sticky= NSEW)

        self.age = IntVar()
        self.weight = DoubleVar()
        self.height = DoubleVar()

        frame3 = Frame(self.window)
        frame3.pack(padx=10, pady=10)
        #enter age, weight, height
        Label(frame3, text= "Age").grid(row=5, column=1, sticky= NSEW)
        Entry(frame3, textvariable= self.age, justify= RIGHT).grid(row=5, column=2, sticky= NSEW)
        Label(frame3, text= "Weight (KG)").grid(row=6, column=1, sticky= NSEW)
        Entry(frame3, textvariable= self.weight, justify= RIGHT).grid(row=6, column=2, sticky= NSEW)
        Label(frame3, text= "Height (CM)").grid(row=7, column=1, sticky= NSEW)
        Entry(frame3, textvariable= self.height, justify= RIGHT).grid(row=7, column=2, sticky= NSEW)
        Label(frame3, text= "Activity").grid(row=8, column=1, sticky= NSEW)

        #dropdown menu
        self.activity_levels = {
            "Sedentary (Office Job)": 1.2,
            "Lightly Active (1-2 days/week)": 1.375,
            "Moderately Active (3-5 days/week)": 1.55,
            "Very Active (6-7 days/week)": 1.725,
            "Athlete (2x per day)": 1.9
        }

        self.activity_option = list(self.activity_levels.keys())
        self.activity = StringVar() #return key
        self.activity.set(self.activity_option[0]) #default value
        self.activity_menu = OptionMenu(frame3, self.activity, *self.activity_option).grid(row=8, column=2, sticky= NSEW)

        self.tdee = DoubleVar()
        self.tdee_result = DoubleVar()

        #tdee
        Button(frame3, text= "Calculate!", command= self.calculate_tdee_bmi).grid(row=8, column=3, sticky= NSEW)
        Label(frame3, text= "Your TDEE is:").grid(row=9, column=1, sticky= NSEW)
        Label(frame3, textvariable=self.tdee_result).grid(row=9, column=2, sticky= NSEW)

        #bmi
        self.bmi = DoubleVar()
        self.bmi_list = ["Underweight", "Normal Weight", "Overweight", "Obese"]
        self.bmi_classification = StringVar()
        Label(frame3, text= "Your BMI is:").grid(row=10, column=1, sticky= NSEW)
        Label(frame3, textvariable=self.bmi).grid(row=10, column=2, sticky= NSEW)

        #second step
        frame4 = Frame(self.window)
        frame4.pack(padx=10, pady=10)
        Label(frame4, text= "Second Step: Choose to Bulk, Cut or Maintain", font= self.font).grid(row=1, column=1, sticky= NSEW)
        Label(frame4, text= "Bulk is to gain weight").grid(row=2, column=1, sticky= NSEW)
        Label(frame4, text= "Cut is to lose weight").grid(row=3, column=1, sticky= NSEW)
        Label(frame4, text= "Maintain is to maintain your weight").grid(row=4, column=1, sticky= NSEW)

        self.button2 = StringVar()
        self.button2.set("Bulk") #default value

        frame5 = Frame(self.window)
        frame5.pack(padx=10, pady=10)
        Radiobutton(frame5, variable= self.button2, value= "Bulk", command= self.calculate_all).grid(row=5, column=1, sticky= NSEW)
        Label(frame5, text= "Bulk").grid(row=5, column=2, sticky= NSEW)
        Radiobutton(frame5, variable= self.button2, value= "Cut", command=self.calculate_all).grid(row=5, column=3, sticky= NSEW)
        Label(frame5, text= "Cut").grid(row=5, column=4, sticky= NSEW)
        Radiobutton(frame5, variable= self.button2, value= "Maintain", command=self.calculate_all).grid(row=5, column=5, sticky= NSEW)
        Label(frame5, text= "Maintain").grid(row=5, column=6, sticky= NSEW)

        self.button3 = StringVar()
        self.button3.set("Low Carb")

        Radiobutton(frame5, variable= self.button3, value= "Low Carb", command= self.calculate_all).grid(row=6, column=1, sticky= NSEW)
        Label(frame5, text= "Low Carb").grid(row=6, column=2, sticky= NSEW)
        Radiobutton(frame5, variable= self.button3, value= "Moderate Carb", command= self.calculate_all).grid(row=6, column=3, sticky= NSEW)
        Label(frame5, text= "Moderate Carb").grid(row=6, column=4, sticky= NSEW)
        Radiobutton(frame5, variable= self.button3, value= "High Carb", command= self.calculate_all).grid(row=6, column=5, sticky= NSEW)
        Label(frame5, text= "High Carb").grid(row=6, column=6, sticky= NSEW)
        # Button(frame5, text= "Calculate!", command= self.calculate_all).grid(row=6, column=7, sticky= NSEW)

        self.recommended_calories = DoubleVar()
        self.recommended_protein = DoubleVar()
        self.recommended_fat = DoubleVar()
        self.recommeneded_carb = DoubleVar()

        frame6 = Frame(self.window)
        frame6.pack(padx=10, pady=10)

        Label(frame6, text= "Recommended Calories :").grid(row=7, column=1, sticky= NSEW)
        Label(frame6, textvariable= self.recommended_calories).grid(row=7, column=2, sticky= NSEW)
        Label(frame6, text= "Recommended Protein :").grid(row=8, column=1, sticky= NSEW)
        Label(frame6, textvariable= self.recommended_protein).grid(row=8, column=2, sticky= NSEW)
        Label(frame6, text= "Recommended Fat :").grid(row=9, column=1, sticky= NSEW)
        Label(frame6, textvariable= self.recommended_fat).grid(row=9, column=2, sticky= NSEW)
        Label(frame6, text= "Recommened Carbs :").grid(row=10, column=1, sticky= NSEW)
        Label(frame6, textvariable= self.recommeneded_carb).grid(row=10, column=2, sticky= NSEW)

        #Next page
        frame7  = Frame(self.window)
        frame7.pack(padx=10, pady=10)
        
        image = Image.open("picture/dumbbell.png")
        image = image.resize((100, 100))
        self.photo = ImageTk.PhotoImage(image)
        Label(frame7, image= self.photo).pack(padx=10, pady=10, side= LEFT)
        
        frame8 = Frame(self.window)
        frame8.pack(padx=10, pady=10)

        Button(frame8, text= "Next Step", command= self.open_second_window).pack(padx=10, pady=10, side= RIGHT ,anchor= SE)
        self.window.mainloop()

    def calculate_tdee_bmi(self):
        if self.button1.get() == "Male":
            bmr = 88.362 + (13.397 * self.weight.get()) + (4.799 * self.height.get()) - (5.677 * self.age.get())
        else:
            bmr = 447.593 + (9.247 * self.weight.get()) + (3.098 * self.height.get()) - (4.330 * self.age.get())

        self.tdee = bmr * self.activity_levels[self.activity.get()] #return the value of the key
        formatted_tdee = "{:.0f} Calories per day".format(self.tdee)
        self.tdee_result.set(formatted_tdee)

        bmi = self.weight.get() / (self.height.get() / 100) ** 2 #self.height.get() is in cm / 100 to convert to m

        if bmi < 18.5:
            self.bmi_classification.set(self.bmi_list[0])
        elif 18.5 <= bmi < 25:
            self.bmi_classification.set(self.bmi_list[1])
        elif 25 <= bmi < 30:
            self.bmi_classification.set(self.bmi_list[2])
        elif bmi >= 30:
            self.bmi_classification.set(self.bmi_list[3])

        formatted_bmi = "{:.2f} {}".format(bmi, self.bmi_classification.get())
        self.bmi.set(formatted_bmi)

    def calculate_all(self):
        if self.button2.get() == "Bulk":
                tdee = self.tdee
                tdee += 500
                formatted_tdee = "Around {:.0f} Calories per day".format(tdee)
                self.recommended_calories.set(formatted_tdee)

                if self.button3.get() == "Low Carb":

                    protein = self.weight.get() * 2.8
                    formatted_protein = "{:.0f} grams per day".format(protein)
                    self.recommended_protein.set(formatted_protein)

                    fat = self.weight.get() * 0.9
                    formatted_fat = "{:.0f} grams per day".format(fat)
                    self.recommended_fat.set(formatted_fat)

                    carbs = (tdee - (protein * 4) - (fat * 9)) / 8
                    formatted_carbs = "{:.0f} grams per day".format(carbs)
                    self.recommeneded_carb.set(formatted_carbs)

                if self.button3.get() == "Moderate Carb":

                    protein = self.weight.get() * 2.5
                    formatted_protein = "{:.0f} grams per day".format(protein)
                    self.recommended_protein.set(formatted_protein)

                    fat = self.weight.get() * 0.7
                    formatted_fat = "{:.0f} grams per day".format(fat)
                    self.recommended_fat.set(formatted_fat)
                    
                    carbs = (tdee - (protein * 4) - (fat * 9)) / 7
                    formatted_carbs = "{:.0f} grams per day".format(carbs)
                    self.recommeneded_carb.set(formatted_carbs)

                if self.button3.get() == "High Carb":

                    protein = self.weight.get() * 2
                    formatted_protein = "{:.0f} grams per day".format(protein)
                    self.recommended_protein.set(formatted_protein)

                    fat = self.weight.get() * 0.4
                    formatted_fat = "{:.0f} grams per day".format(fat)
                    self.recommended_fat.set(formatted_fat)

                    carbs = (tdee - (protein * 4) - (fat * 9)) / 6
                    formatted_carbs = "{:.0f} grams per day".format(carbs)
                    self.recommeneded_carb.set(formatted_carbs)

        if self.button2.get() == "Cut":
                tdee = self.tdee
                tdee -= 500
                formatted_tdee = "Around {:.0f} Calories per day".format(tdee)
                self.recommended_calories.set(formatted_tdee)

                if self.button3.get() == "Low Carb":

                    protein = self.weight.get() * 2.5
                    formatted_protein = "{:.0f} grams per day".format(protein)
                    self.recommended_protein.set(formatted_protein)

                    fat = self.weight.get() * 0.5
                    formatted_fat = "{:.0f} grams per day".format(fat)
                    self.recommended_fat.set(formatted_fat)

                    carbs = (tdee - (protein * 4) - (fat * 9)) / 10
                    formatted_carbs = "{:.0f} grams per day".format(carbs)
                    self.recommeneded_carb.set(formatted_carbs)

                if self.button3.get() == "Moderate Carb":
                    
                    protein = self.weight.get() * 2.2
                    formatted_protein = "{:.0f} grams per day".format(protein)
                    self.recommended_protein.set(formatted_protein)

                    fat = self.weight.get() * 0.3
                    formatted_fat = "{:.0f} grams per day".format(fat)
                    self.recommended_fat.set(formatted_fat)

                    carbs = (tdee - (protein * 4) - (fat * 9)) / 9
                    formatted_carbs = "{:.0f} grams per day".format(carbs)
                    self.recommeneded_carb.set(formatted_carbs)

                if self.button3.get() == "High Carb":
                        
                    protein = self.weight.get() * 2
                    formatted_protein = "{:.0f} grams per day".format(protein)
                    self.recommended_protein.set(formatted_protein)

                    fat = self.weight.get() * 0.1
                    formatted_fat = "{:.0f} grams per day".format(fat)
                    self.recommended_fat.set(formatted_fat)

                    carbs = (tdee - (protein * 4) - (fat * 9)) / 8
                    formatted_carbs = "{:.0f} grams per day".format(carbs)
                    self.recommeneded_carb.set(formatted_carbs)

        if self.button2.get() == "Maintain":
            tdee = self.tdee
            formatted_tdee = "Around {:.0f} Calories per day".format(tdee)
            self.recommended_calories.set(formatted_tdee)

            if self.button3.get() == "Low Carb":

                protein = self.weight.get() * 2
                formatted_protein = "{:.0f} grams per day".format(protein)
                self.recommended_protein.set(formatted_protein)

                fat = self.weight.get() * 0.5
                formatted_fat = "{:.0f} grams per day".format(fat)
                self.recommended_fat.set(formatted_fat)

                carbs = (tdee - (protein * 4) - (fat * 9)) / 9
                formatted_carbs = "{:.0f} grams per day".format(carbs)
                self.recommeneded_carb.set(formatted_carbs)

            if self.button3.get() == "Moderate Carb":
                    
                protein = self.weight.get() * 1.6
                formatted_protein = "{:.0f} grams per day".format(protein)
                self.recommended_protein.set(formatted_protein)

                fat = self.weight.get() * 0.4
                formatted_fat = "{:.0f} grams per day".format(fat)
                self.recommended_fat.set(formatted_fat)

                carbs = (tdee - (protein * 4) - (fat * 9)) / 8
                formatted_carbs = "{:.0f} grams per day".format(carbs)
                self.recommeneded_carb.set(formatted_carbs)
            
            if self.button3.get() == "High Carb":
                            
                protein = self.weight.get() * 1.2
                formatted_protein = "{:.0f} grams per day".format(protein)
                self.recommended_protein.set(formatted_protein)

                fat = self.weight.get() * 0.3
                formatted_fat = "{:.0f} grams per day".format(fat)
                self.recommended_fat.set(formatted_fat)

                carbs = (tdee - (protein * 4) - (fat * 9)) / 7
                formatted_carbs = "{:.0f} grams per day".format(carbs)
                self.recommeneded_carb.set(formatted_carbs)

    def open_second_window(self):
        self.window.withdraw()
        SecondWindow(self.first_window)

class SecondWindow(Frame):
    def __init__(self, first_window):
        Frame.__init__(self)
        
        self.first_window = first_window
        self.window = first_window.window
        self.second_window = self
        self.window2 = Toplevel(self.window)
        self.window2.title("Workout App")
        self.window2.geometry("600x800+0+0")


        self.button1 = StringVar()
        self.button1.set("3 Days") #default value

        frame1 = Frame(self.window2)
        frame1.pack(padx=10, pady=10)
        Label(frame1, text= "Third Step: Choose Your Workout Plan", font= self.first_window.font_title).grid(row=1, column=1, sticky= NSEW)
        Label(frame1, text= "How many days can you goto the gym in 1 week").grid(row=2, column=1, sticky= NSEW)

        frame2 = Frame(self.window2)
        frame2.pack(padx=10, pady=10)
        Radiobutton(frame2, variable= self.button1, value= "1 Day", command= self.show_info).grid(row=3, column=1, sticky= NSEW)
        Label(frame2, text= "1 Day").grid(row=3, column=2, sticky= NSEW)
        Radiobutton(frame2, variable= self.button1, value= "2 Days", command= self.show_info).grid(row=3, column=3, sticky= NSEW)
        Label(frame2, text= "2 Days").grid(row=3, column=4, sticky= NSEW)
        Radiobutton(frame2, variable= self.button1, value= "3 Days", command= self.show_info).grid(row=3, column=5, sticky= NSEW)
        Label(frame2, text= "3 Days").grid(row=3, column=6, sticky= NSEW)
        Radiobutton(frame2, variable= self.button1, value= "4 Days", command= self.show_info).grid(row=3, column=7, sticky= NSEW)
        Label(frame2, text= "4 Days").grid(row=3, column=8, sticky= NSEW)
        Radiobutton(frame2, variable= self.button1, value= "5 Days", command= self.show_info).grid(row=3, column=9, sticky= NSEW)
        Label(frame2, text= "5 Days").grid(row=3, column=10, sticky= NSEW)

        self.button2 = StringVar()
        self.button2.set("Beginner") #default value

        frame3 = Frame(self.window2)
        frame3.pack(padx=10, pady=10)
        Radiobutton(frame3, variable= self.button2, value= "Beginner", command= self.show_info).grid(row=4, column=1, sticky= NSEW)
        Label(frame3, text= "Beginner").grid(row=4, column=2, sticky= NSEW)
        Radiobutton(frame3, variable= self.button2, value= "Intermediate", command= self.show_info).grid(row=4, column=3, sticky= NSEW)
        Label(frame3, text= "Intermediate").grid(row=4, column=4, sticky= NSEW)
        Radiobutton(frame3, variable= self.button2, value= "Advanced", command= self.show_info).grid(row=4, column=5, sticky= NSEW)
        Label(frame3, text= "Advanced").grid(row=4, column=6, sticky= NSEW)

        frame4 = Frame(self.window2)
        frame4.pack(padx=10, pady=10)
        Button(frame4, text= "Everything You Need To Know", command= self.explain_plan).grid(row=4, column=1, sticky= NSEW)

        frame5 = Frame(self.window2)
        frame5.pack(padx=10, pady=10)
        self.info = StringVar()
        self.font_label = ("TKDefaultFont", 14, "bold")
        Label(frame5, textvariable= self.info, font=self.font_label).grid(row=5, column=1, sticky= NSEW)

        frame6 = Frame(self.window2)
        frame6.pack(padx=10, pady=10, side= BOTTOM)
        Button(frame6, text= "Back", command= self.back).grid(row=1, column=1, sticky= NSEW)
        Button(frame6, text= "Next Step", command= self.open_third_window).grid(row=1, column=2, sticky= NSEW)


    def show_info(self):
            if self.button1.get() == "1 Day":
                if self.button2.get() == "Beginner":
                    self.info.set("Full Body Workout (Dumbbell or Bodyweight)")
                    self.update_image()

                    if hasattr(self, 'perform'):
                        self.perform.destroy()

                    self.perform = Button(self.window2, text= "Explanation About Full Body Workout Beginner", command= self.open_window_day1_begin)
                    self.perform.pack(padx=10, pady=10, anchor= 'center')

                elif self.button2.get() == "Intermediate":
                    self.info.set("Full Body Workout")
                    self.update_image()

                    if hasattr(self, 'perform'):
                        self.perform.destroy()

                    self.perform = Button(self.window2, text= "Explanation About Full Body Workout Intermediate", command= self.open_window_day1_intermediate)
                    self.perform.pack(padx=10, pady=10, anchor= 'center')

                elif self.button2.get() == "Advanced":
                    self.info.set("Full Body Workout")
                    self.update_image()

                    if hasattr(self, 'perform'):
                        self.perform.destroy()
                    
                    self.perform = Button(self.window2, text= "Explanation About Full Body Workout Advanced", command= self.open_window_day1_advanced)
                    self.perform.pack(padx=10, pady=10, anchor= 'center')

            if self.button1.get() == "2 Days":
                if self.button2.get() == "Beginner":
                    self.info.set("Upper/Lower Split (Dumbbell or Bodyweight)")
                    self.update_image()

                    if hasattr(self, 'perform'):
                        self.perform.destroy()
                    
                    self.perform = Button(self.window2, text= "Explanation About Upper/Lower Split Beginner", command= self.open_window_day2_begin)
                    self.perform.pack(padx=10, pady=10, anchor= 'center')

                elif self.button2.get() == "Intermediate":
                    self.info.set("Upper/Lower Split")
                    self.update_image()

                    if hasattr(self, 'perform'):
                        self.perform.destroy()

                    self.perform = Button(self.window2, text= "Explanation About Upper/Lower Split Intermediate", command= self.open_window_day2_intermediate)
                    self.perform.pack(padx=10, pady=10, anchor= 'center')

                elif self.button2.get() == "Advanced":
                    self.info.set("Upper/Lower Split")
                    self.update_image()

                    if hasattr(self, 'perform'):
                        self.perform.destroy()

                    self.perform = Button(self.window2, text= "Explanation About Upper/Lower Split Advanced", command= self.open_window_day2_advanced)
                    self.perform.pack(padx=10, pady=10, anchor= 'center')

            if self.button1.get() == "3 Days":
                if self.button2.get() == "Beginner":
                    self.info.set("Push Pull Legs (Dumbbell or Bodyweight)")
                    self.update_image()

                    if hasattr(self, 'perform'):
                        self.perform.destroy()

                    self.perform = Button(self.window2, text= "Explanation About Push Pull Legs Beginner", command= self.open_window_day3_begin)
                    self.perform.pack(padx=10, pady=10, anchor= 'center')

                elif self.button2.get() == "Intermediate":
                    self.info.set("Push Pull Legs")
                    self.update_image()

                    if hasattr(self, 'perform'):
                        self.perform.destroy()

                    self.perform = Button(self.window2, text= "Explanation About Push Pull Legs Intermediate", command= self.open_window_day3_intermediate)
                    self.perform.pack(padx=10, pady=10, anchor= 'center')

                elif self.button2.get() == "Advanced":
                    self.info.set("Push Pull Legs")
                    self.update_image()

                    if hasattr(self, 'perform'):
                        self.perform.destroy()

                    self.perform = Button(self.window2, text= "Explanation About Push Pull Legs Advanced", command= self.open_window_day3_advanced)
                    self.perform.pack(padx=10, pady=10, anchor= 'center')
    
            if self.button1.get() == "4 Days":
                if self.button2.get() == "Beginner":
                    self.info.set("Push Pull Legs and Full Body (Dumbbell or Bodyweight)")
                    self.update_image()

                    if hasattr(self, 'perform'):
                        self.perform.destroy()

                    self.perform = Button(self.window2, text= "Explanation About Push Pull Legs and Cardio Beginner", command= self.open_window_day4_begin)
                    self.perform.pack(padx=10, pady=10, anchor= 'center')

                elif self.button2.get() == "Intermediate":
                    self.info.set("Arnold Split (3 Days) or Push Pull Legs and Cardio")
                    self.update_image()

                    if hasattr(self, 'perform'):
                        self.perform.destroy()

                    self.perform = Button(self.window2, text= "Explanation About Arnold Split and Push Pull Legs Intermediate", command= self.open_window_day4_intermediate)
                    self.perform.pack(padx=10, pady=10, anchor= 'center')

                elif self.button2.get() == "Advanced":
                    self.info.set("Arnold Split (3 Days) or Push Pull Legs and Cardio")
                    self.update_image()

                    if hasattr(self, 'perform'):
                        self.perform.destroy()

                    self.perform = Button(self.window2, text= "Explanation About Arnold Split and Push Pull Legs Advanced", command= self.open_window_day4_advanced)
                    self.perform.pack(padx=10, pady=10, anchor= 'center')

            if self.button1.get() == "5 Days":
                if self.button2.get() == "Beginner":
                    self.info.set("Bro Split (Dumbbell or Bodyweight)")
                    self.update_image()

                    if hasattr(self, 'perform'):
                        self.perform.destroy()

                    self.perform = Button(self.window2, text= "Explanation About Bro Split Beginner", command= self.open_window_day5_begin)
                    self.perform.pack(padx=10, pady=10, anchor= 'center')

                elif self.button2.get() == "Intermediate":
                    self.info.set("Bro Split")
                    self.update_image()

                    if hasattr(self, 'perform'):
                        self.perform.destroy()

                    self.perform = Button(self.window2, text= "Explanation About Bro Split Intermediate", command= self.open_window_day5_intermediate)
                    self.perform.pack(padx=10, pady=10, anchor= 'center')

                elif self.button2.get() == "Advanced":
                    self.info.set("Bro Split")
                    self.update_image()

                    if hasattr(self, 'perform'):
                        self.perform.destroy()

                    self.perform = Button(self.window2, text= "Explanation About Bro Split Advanced", command= self.open_window_day5_advanced)
                    self.perform.pack(padx=10, pady=10, anchor= 'center')

    def update_image(self):
        selected_option = self.button1.get() + self.button2.get()
        image = Image.open("picture/" + selected_option + ".png")
        image = image.resize((400, 350))
        self.photo = ImageTk.PhotoImage(image)

        if hasattr(self, 'image_label'):
            self.image_label.configure(image=self.photo)
        else:
            self.image_label = Label(self.window2, image=self.photo)
            self.image_label.pack(padx=10, pady=10, anchor='center')

    def explain_plan(self):
        self.second_window.window2.withdraw()
        Explain(self.second_window)

    def open_third_window(self):
        self.second_window.window2.withdraw()
        tdee = self.first_window.tdee
        first_window = self.first_window
        ThirdWindow(self.second_window, tdee, first_window)
    
    def back(self):
        self.second_window.window2.destroy()
        self.first_window.window.deiconify()

    def open_window_day1_begin(self):
        self.second_window.window2.withdraw()
        Day1Beginner(self.second_window)

    def open_window_day1_intermediate(self):
        self.second_window.window2.withdraw()
        Day1Intermediate(self.second_window)

    def open_window_day1_advanced(self):
        self.second_window.window2.withdraw()
        Day1Advanced(self.second_window)

    def open_window_day2_begin(self):
        self.second_window.window2.withdraw()
        Day2Beginner(self.second_window)

    def open_window_day2_intermediate(self):
        self.second_window.window2.withdraw()
        Day2Intermediate(self.second_window)

    def open_window_day2_advanced(self):
        self.second_window.window2.withdraw()
        Day2Advanced(self.second_window)

    def open_window_day3_begin(self):
        self.second_window.window2.withdraw()
        Day3Beginner(self.second_window)

    def open_window_day3_intermediate(self):
        self.second_window.window2.withdraw()
        Day3Intermediate(self.second_window)

    def open_window_day3_advanced(self):
        self.second_window.window2.withdraw()
        Day3Advanced(self.second_window)

    def open_window_day4_begin(self):
        self.second_window.window2.withdraw()
        Day4Beginner(self.second_window)

    def open_window_day4_intermediate(self):
        self.second_window.window2.withdraw()
        Day4Intermediate(self.second_window)

    def open_window_day4_advanced(self):
        self.second_window.window2.withdraw()
        Day4Advanced(self.second_window)

    def open_window_day5_begin(self):
        self.second_window.window2.withdraw()
        Day5Beginner(self.second_window)

    def open_window_day5_intermediate(self):
        self.second_window.window2.withdraw()
        Day5Intermediate(self.second_window)

    def open_window_day5_advanced(self):
        self.second_window.window2.withdraw()
        Day5Advanced(self.second_window)

class ThirdWindow:
    def __init__(self, second_window, tdee, first_window):
        self.second_window = second_window
        self.tdee = tdee
        self.first_window = first_window
        self.window3 = Toplevel(self.second_window.window2)
        self.window3.title("Workout App")
        self.window3.geometry("600x800+0+0")
        self.font = ("TKDefaultFont", 20, "bold")

        frame1 = Frame(self.window3)
        frame1.pack(padx=10, pady=10)
        Label(frame1, text="Fourth Step: Calories Tracker", font=self.font).grid(row=1, column=1, sticky=NSEW)
        Label(frame1, text="Select what you ate today").grid(row=2, column=1, sticky=NSEW)

        frame2 = Frame(self.window3)
        frame2.pack(padx=10, pady=10)
        Label(frame2, text="Search Food:").grid(row=3, column=1, sticky=NSEW)
        self.search_food = StringVar()
        self.search_food.trace("w", self.search_food_callback)
        Entry(frame2, textvariable=self.search_food).grid(row=3, column=2, sticky=NSEW)
        #create sort by dropdown menu
        self.sort = StringVar()
        self.sort.set("Sort By")
        self.sort.trace("w", self.sort_callback)
        self.sort_menu = OptionMenu(frame2, self.sort, "Sort By", "Calories (Low to High)", "Calories (High to Low)", "Alphabetical (A-Z)", "Alphabetical (Z-A)")
        self.sort_menu.grid(row=3, column=3, sticky=NSEW)

        self.food_list = []
        frame3 = Frame(self.window3)
        frame3.pack(padx=10, pady=10)
        self.list_box = Listbox(frame3, height=10, width=50)
        self.list_box.grid(row=4, column=1, sticky=NSEW)
        self.list_box.bind("<Button-1>", self.selected_food)
        
        self.load_data()

        frame4 = Frame(self.window3)
        frame4.pack(padx=10, pady=10)
        Label(frame4, text="Calories:").grid(row=5, column=1, sticky=NSEW)
        self.calories = IntVar()
        self.calories.set(0)
        Label(frame4, textvariable=self.calories).grid(row=5, column=2, sticky=NSEW)

        self.calorie_list = []
        self.graph_shown = False

        frame5 = Frame(self.window3)
        frame5.pack(padx=10, pady=10)
        Button(frame5, text="Graph Compare", command=self.bar_graph).pack(padx=10, pady=10, side=LEFT)


        Button(self.window3, text="Back", command=self.back).pack(padx=10, pady=10, side=BOTTOM)

        self.window3.mainloop()

    def back(self):
        self.window3.destroy()
        self.second_window.window2.deiconify()

    def selected_food(self, event):
        selected_index = self.list_box.curselection()
        if selected_index:
            selected_item = self.list_box.get(selected_index)
            calories = int(selected_item.split('-')[1].strip().split(' ')[0])

            self.calories.set(self.calories.get() + calories)
            self.calorie_list.append(calories)

    def search_food_callback(self, *args):
        search_term = self.search_food.get()
        self.list_box.delete(0, END)
        for food_name, calories in self.food_list:
            if search_term.lower() in food_name.lower():
                self.list_box.insert(END, f"{food_name} - {calories} calories")

    def bar_graph(self):
        total_calories = sum(self.calorie_list)
        tdee_calories = self.tdee
        bar_width = 0.35
        x = np.arange(2)  # Two bars: total calories and tdee calories

        plt.bar(x, [total_calories, tdee_calories], bar_width, color=["orange", "blue"], label=["Total Calories", "TDEE Calories"])
        plt.title("Total Calories vs TDEE Calories")
        plt.xticks(x, ["Total Calories", "TDEE Calories"])
        plt.ylabel("Calories")
        plt.legend()
        plt.tight_layout()
        plt.show() 

    def load_data(self):
        try:
            with open("foods.json", "r") as file:
                data = json.load(file)
                for entry in data:
                    food_items = entry["foodItems"]
                    for item in food_items:
                        food_name = item["foodName"]
                        calories = item["calories"]
                        self.food_list.append((food_name, calories))
                        self.list_box.insert(END, f"{food_name} - {calories} calories")

        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")
        except json.JSONDecodeError as e:
            messagebox.showerror("JSON decoding error:", e)
        except Exception as e:
            messagebox.showerror("An error occurred:", e)

        try:
            with open("drinks.json", "r") as drink_file:
                data = json.load(drink_file)
                for entry in data:
                    drink_name = entry["drinkName"]
                    calories = entry["calories"]
                    self.food_list.append((drink_name, calories))
                    self.list_box.insert(END, f"{drink_name} - {calories} calories")

        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")
        except json.JSONDecodeError as e:
            messagebox.showerror("JSON decoding error:", e)
        except Exception as e:
            messagebox.showerror("An error occurred:", e)

    def sort_callback(self, *args):
        sort_option = self.sort.get()
        if sort_option == "Calories (Low to High)":
            self.food_list.sort(key=lambda x: x[1]) #sort by calories ascending
            self.list_box.delete(0, END)
            for food_name, calories in self.food_list:
                self.list_box.insert(END, f"{food_name} - {calories} calories")
        elif sort_option == "Calories (High to Low)":
            self.food_list.sort(key=lambda x: x[1], reverse=True) #reverse=True means descending order
            self.list_box.delete(0, END)
            for food_name, calories in self.food_list:
                self.list_box.insert(END, f"{food_name} - {calories} calories")
        elif sort_option == "Alphabetical (A-Z)":
            self.food_list.sort(key=lambda x: x[0]) #sort by food name ascending
            self.list_box.delete(0, END)
            for food_name, calories in self.food_list:
                self.list_box.insert(END, f"{food_name} - {calories} calories")
        elif sort_option == "Alphabetical (Z-A)":
            self.food_list.sort(key=lambda x: x[0], reverse=True)
            self.list_box.delete(0, END)
            for food_name, calories in self.food_list:
                self.list_box.insert(END, f"{food_name} - {calories} calories")

if __name__ == "__main__":
    FirstWindow()
