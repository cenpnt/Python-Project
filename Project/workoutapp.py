from tkinter import *
from tkinter import messagebox
from explain_plan import Explain
from workout_functions import *
import json
import numpy as np
from datetime import datetime
try:
    from PIL import ImageTk, Image
except ImportError:
    messagebox.showerror("Error", "Pillow not installed. Please install Pillow to use this application.\npip install Pillow")
    exit()
try:
    from matplotlib import pyplot as plt
except ImportError:
    messagebox.showerror("Error", "Matplotlib not installed. Please install Matplotlib to use this application.\npip install matplotlib")
    exit()
try:
    from tkmacosx import Button
except ImportError:
    messagebox.showerror("Error", "tkmacosx not installed. Please install tkmacosx to use this application.\npip install tkmacosx")
    exit()

class Login(object):
    def __init__(self):
        self.window = Tk()
        self.window.title("FitnessPal")
        self.window.geometry("925x500+0+0")
        self.window.resizable(False, False)
        self.window.configure(bg="#fff")
        self.login = self

        img = Image.open("picture/login2.png")
        img = img.resize((400, 400))
        img = ImageTk.PhotoImage(img)
        Label(self.window, image=img, bg="white").place(x=50, y=50)

        frame1 = Frame(self.window, width=350, height=350, bg='white')
        frame1.place(x=480, y=70)
        Label(frame1, text="Sign in", font=('Microsoft YaHei UI Light', 26, 'bold'), fg='#57a1f8', bg='white').place(x=130, y=5)

        self.username = StringVar()
        self.username_entry = Entry(frame1, width=25, bg='white', borderwidth=0, highlightthickness=0, font=('Microsoft YaHei UI Light', 14), textvariable=self.username)
        self.username_entry.place(x=30, y=80)
        self.username_entry.insert(0, "Username")  # Placeholder
        self.username_entry.bind("<FocusIn>", self.on_username_entry_focusin) #when the user click on the entry
        self.username_entry.bind("<FocusOut>", self.on_username_entry_focusout) #when the user click out of the entry
        Frame(frame1, width=295, height=2, bg='black').place(x=25, y=107)

        self.password = StringVar()
        self.password_entry = Entry(frame1, textvariable=self.password, show="*", borderwidth=0, highlightthickness=0, font=('Microsoft YaHei UI Light', 14), bg='white')
        self.password_entry.place(x=30, y=150)
        self.password_entry.insert(0, "Password")  # Placeholder
        self.password_entry.bind("<FocusIn>", self.on_password_entry_focusin)
        self.password_entry.bind("<FocusOut>", self.on_password_entry_focusout)
        Frame(frame1, width=295, height=2, bg='black').place(x=25, y=177)

        but = Button(frame1, text="Sign in", command=self.login_action, fg='white', pady=7, bg= "#57a1f8", width= 280, borderless= True)
        but.place(x=35, y=204)
        Label(frame1, text="Don't have an account?", font=('Microsoft YaHei UI Light', 12), bg='white', fg='black').place(x=75, y=270)
        Button(frame1, text="Sign up", command=self.register, bg='white', font=("Microsoft YaHei UI Light", 11), fg= "#57a1f8", pady= 3, borderless = True, bd= 0).place(x=215, y=268)

        self.window.mainloop()

    def login_action(self):
        try:
            with open("json/user.json", "r") as f:
                users = json.load(f)

            username = self.username.get()
            password = self.password.get()

            if username in users:
                if password == users[username]["password"]:
                    print("Successful login. Opening FirstWindow.")
                    self.window.destroy()
                    FirstWindow(self.login)  # open first window
                else:
                    messagebox.showerror("Error", "Incorrect Password")
            else:
                messagebox.showerror("Error", "User Not Found")

        except FileNotFoundError:
            messagebox.showerror("Error", "Username Not Found")
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
            messagebox.showerror("Error", "Error decoding JSON")
        except Exception as e:
            print(f"Unexpected Error: {e}")
            messagebox.showerror("Error", "An unexpected error occurred. Check the console for details.")

    def register(self):
        self.window.destroy()
        Register()

    def on_username_entry_focusin(self, event):
        if self.username_entry.get() == "Username":
            self.username_entry.delete(0, "end")
            self.username_entry.config(fg="black")

    def on_username_entry_focusout(self, event):
        if not self.username_entry.get():
            self.username_entry.insert(0, "Username")
            self.username_entry.config(fg="gray")

    def on_password_entry_focusin(self, event):
        if self.password_entry.get() == "Password":
            self.password_entry.delete(0, "end")
            self.password_entry.config(fg="black")

    def on_password_entry_focusout(self, event):
        if not self.password_entry.get():
            self.password_entry.insert(0, "Password")
            self.password_entry.config(fg="gray")

class Register(object):
    def __init__(self):
        self.window = Tk()
        self.window.title("FitnessPal")
        self.window.geometry("925x500+0+0")
        self.window.resizable(False, False)
        self.window.configure(bg="#fff")

        img = PhotoImage(file="picture/login.png")
        Label(self.window, image=img, bg="white").place(x=50, y=50)

        frame1 = Frame(self.window, width=350, height=350, bg='white')
        frame1.place(x=480, y=70)
        Label(frame1, text="Sign up", font=('Microsoft YaHei UI Light', 26, 'bold'), fg='#57a1f8', bg='white').place(x=130, y=5)

        self.username = StringVar()
        self.username_entry = Entry(frame1, width=25, bg='white', borderwidth=0, highlightthickness=0, font=('Microsoft YaHei UI Light', 14), textvariable=self.username)
        self.username_entry.place(x=30, y=80)
        self.username_entry.insert(0, "Username")  # Placeholder
        self.username_entry.bind("<FocusIn>", self.on_username_entry_focusin)
        self.username_entry.bind("<FocusOut>", self.on_username_entry_focusout)
        Frame(frame1, width=295, height=2, bg='black').place(x=25, y=107)

        self.password = StringVar()
        self.password_entry = Entry(frame1, textvariable=self.password, show="*", borderwidth=0, highlightthickness=0, font=('Microsoft YaHei UI Light', 14), bg='white')
        self.password_entry.place(x=30, y=150)
        self.password_entry.insert(0, "Password")  # Placeholder
        self.password_entry.bind("<FocusIn>", self.on_password_entry_focusin)
        self.password_entry.bind("<FocusOut>", self.on_password_entry_focusout)
        Frame(frame1, width=295, height=2, bg='black').place(x=25, y=177)

        self.confirm_password = StringVar()
        self.confirm_password_entry = Entry(frame1, textvariable=self.confirm_password, show="*", borderwidth=0, highlightthickness=0, font=('Microsoft YaHei UI Light', 14), bg='white')
        self.confirm_password_entry.place(x=30, y=220)
        self.confirm_password_entry.insert(0, "Password")  # Placeholder
        self.confirm_password_entry.bind("<FocusIn>", self.on_confirm_password_entry_focusin)
        self.confirm_password_entry.bind("<FocusOut>", self.on_confirm_password_entry_focusout)
        Frame(frame1, width=295, height=2, bg='black').place(x=25, y=247)

        but = Button(frame1, text="Sign up", command=self.register, fg='white', pady=7, bg= "#57a1f8", width= 280, borderless= True)
        but.place(x=35, y=274)

        Label(frame1, text="Already have an account?", font=('Microsoft YaHei UI Light', 12), bg='white', fg='black').place(x=65, y=324)
        Button(frame1, text="Sign in", command=self.back, bg='white', font=("Microsoft YaHei UI Light", 11), fg= "#57a1f8", pady= 2, borderless = True, bd= 0).place(x=215, y=322)

        self.window.mainloop()

    def register(self):
        try:
            with open("json/user.json", "r") as f:
                users = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            # If the file is not found or not valid JSON, create an empty dictionary
            users = {}

        username = self.username.get() #get the username
        password = self.password.get() #get the password
        confirm_password = self.confirm_password.get()

        if username in users: #check if username already exists
            messagebox.showerror("Error", "Username Already Exists")
        elif password != confirm_password: #check if password match
            messagebox.showerror("Error", "Password Does Not Match")
        elif self.username.get() == "Username" or self.password.get() == "Password" or self.confirm_password.get() == "Password":
            messagebox.showerror("Error", "Please Enter Username and Password")
        else:
            users[username] = {"password": password} #add username and password to dictionary
            with open("json/user.json", "w") as f:
                json.dump(users, f)
            self.window.destroy()
            messagebox.showinfo("Success", "Account Created")
            Login()

    def back(self):
        self.window.destroy()
        Login()

    def on_username_entry_focusin(self, event):
        if self.username_entry.get() == "Username":
            self.username_entry.delete(0, "end")
            self.username_entry.config(fg="black")

    def on_username_entry_focusout(self, event):
        if not self.username_entry.get():
            self.username_entry.insert(0, "Username")
            self.username_entry.config(fg="gray")

    def on_password_entry_focusin(self, event):
        if self.password_entry.get() == "Password":
            self.password_entry.delete(0, "end")
            self.password_entry.config(fg="black")

    def on_password_entry_focusout(self, event):
        if not self.password_entry.get():
            self.password_entry.insert(0, "Password")
            self.password_entry.config(fg="gray")

    def on_confirm_password_entry_focusin(self, event):
        if self.confirm_password_entry.get() == "Password":
            self.confirm_password_entry.delete(0, "end")
            self.confirm_password_entry.config(fg="black")

    def on_confirm_password_entry_focusout(self, event):
        if not self.confirm_password_entry.get():
            self.confirm_password_entry.insert(0, "Password")
            self.confirm_password_entry.config(fg="gray")

class FirstWindow(object):
    def __init__(self, login):
        self.login = login
        self.first_window = self
        self.window = Tk()
        self.window.title("FitnessPal")
        self.window.geometry("600x810+0+0")
        self.font_title = ("TKDefaultFont", 26, "bold")
        self.font = ("TKDefaultFont", 20, "bold")

        menubar = Menu(self.window)
        self.window.config(menu=menubar)

        list_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=list_menu)
        list_menu.add_command(label="Back to Login Page", command=self.back_login)
        list_menu.add_command(label="Exit", command=self.window.quit)

        frame1 = Frame(self.window)
        frame1.pack(padx=10, pady=10)
        Label(frame1, text= "Welcome to FitnessPal", font= self.font_title, fg="#57a1f8").grid(row=1, column=1, sticky= NSEW)

        #first step
        Label(frame1, text= "First Step: TDEE Calculator", font= self.font, fg="#57a1f8").grid(row=2, column=1, sticky= NSEW)
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
        Button(frame3, text= "Calculate!", command= self.calculate_tdee_bmi, fg="white", bg= "#57a1f8",borderless=True, bd=0).grid(row=8, column=3, sticky= NSEW)
        Label(frame3, text= "Your TDEE is:").grid(row=9, column=1, sticky= NSEW)
        Label(frame3, textvariable=self.tdee_result).grid(row=9, column=2, sticky= NSEW)

        #bmi
        self.bmi = DoubleVar()
        self.bmi_list = ["Underweight", "Normal Weight", "Overweight", "Obese"]
        self.bmi_classification = StringVar()
        Label(frame3, text= "Your BMI is:").grid(row=10, column=1, sticky= NSEW)
        Label(frame3, textvariable=self.bmi).grid(row=10, column=2, sticky= NSEW)
############################################################################################################################################################################
        #second step
        frame4 = Frame(self.window)
        frame4.pack(padx=10, pady=10)
        Label(frame4, text= "Second Step: Choose to Bulk, Cut or Maintain", font= self.font, fg="#57a1f8").grid(row=1, column=1, sticky= NSEW)
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
        Button(frame8, text= "Next Step", command= self.open_second_window).pack(side= RIGHT ,anchor= SE)
        self.window.mainloop()

    def calculate_tdee_bmi(self):
        if self.age.get() == 0 or self.weight.get() == 0 or self.height.get() == 0:
            messagebox.showerror("Error", "Please Enter Age, Weight and Height")
            self.tdee_result.set("0 Calories per day")
            return
        
        if self.age.get() > 100 or self.weight.get() > 500 or self.height.get() > 300:
            messagebox.showerror("Error", "Please Enter Valid Age, Weight and Height")
            self.tdee_result.set("0 Calories per day")
            return
        
        if self.button1.get() == "Male":
            bmr = 88.362 + (13.397 * self.weight.get()) + (4.799 * self.height.get()) - (5.677 * self.age.get())
        else:
            if self.age.get() == 0 or self.weight.get() == 0 or self.height.get() == 0:
                messagebox.showerror("Error", "Please Enter Age, Weight and Height")
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
        login = self.login
        SecondWindow(self.first_window, login)

    def back_login(self):
        self.window.destroy()
        Login()

class SecondWindow(Frame):
    def __init__(self, first_window, login): #pass in the first window
        super().__init__()
        self.login = login
        self.first_window = first_window
        self.window = first_window.window
        self.second_window = self
        self.window2 = Toplevel(self.window)
        self.window2.title("FitnessPal")
        self.window2.geometry("600x800+0+0")

        menubar = Menu(self.window2)
        self.window2.config(menu=menubar)

        list_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=list_menu)
        list_menu.add_command(label="Exit", command=self.window2.quit)

        self.button1 = StringVar()
        self.button1.set("3 Days") #default value

        frame1 = Frame(self.window2)
        frame1.pack(padx=10, pady=10)
        Label(frame1, text= "Third Step: Choose Your Workout Plan", font= self.first_window.font, fg='#57a1f8').grid(row=1, column=1, sticky= NSEW)
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
        Button(frame4, text= "Everything You Need To Know", command= self.explain_plan, fg="white", bg= "#57a1f8",borderless=True, bd=0).grid(row=4, column=1, sticky= NSEW)

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

                    if hasattr(self, 'perform'): #if the attribute is already there
                        self.perform.destroy() #destroy the attribute

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
        login = self.login
        ThirdWindow(self.second_window, tdee, first_window, login)
    
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

class ThirdWindow(object):
    def __init__(self, second_window, tdee, first_window, login):
        self.login = login
        self.second_window = second_window
        self.tdee = tdee
        self.first_window = first_window
        self.window3 = Toplevel(self.second_window.window2)
        self.third_window = self
        self.window3.title("FitnessPal")
        self.window3.geometry("600x800+0+0")
        self.font = ("TKDefaultFont", 20, "bold")

        frame1 = Frame(self.window3)
        frame1.pack(padx=10, pady=10)
        Label(frame1, text="Fourth Step: Calories Tracker", font=self.font, fg='#57a1f8').grid(row=1, column=1, sticky=NSEW)
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

        frame5 = Frame(self.window3)
        frame5.pack(padx=10, pady=10)
        Button(frame5, text="Graph Compare", command=self.bar_graph, fg="white", bg= "#57a1f8",borderless=True, bd=0).pack(padx=10, pady=10, side=LEFT)

        frame6 = Frame(self.window3)
        frame6.pack(padx=10, pady=10, side=BOTTOM)
        Button(frame6, text="Back", command=self.back).grid(row=1, column=1, sticky=NSEW)
        Button(frame6, text="Next Page", command=self.next).grid(row=1, column=2, sticky=NSEW)

        self.window3.mainloop()

    def back(self):
        self.window3.destroy()
        self.second_window.window2.deiconify()

    def next(self):
        self.window3.withdraw()
        FourthWindow(self.first_window, "json/user_data.json", self.login, self.third_window)

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
        try:
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
        except:
            messagebox.showerror("An error occur: ","Please get tdee first before comparing")

    def load_data(self):
        try:
            with open("json/foods.json", "r") as file:
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
            with open("json/drinks.json", "r") as drink_file:
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

class FourthWindow(object):
    def __init__(self, first_window, json_file, login, third_window):
        self.third_window = third_window
        self.window4 = Toplevel(self.third_window.window3)
        self.window4.title("FitnessPal")
        self.window4.geometry("600x800+0+0")
        self.font = ("TKDefaultFont", 20, "bold")
        self.login = login
        self.json_file = json_file
        self.data = self.load_data()
        self.first_window = first_window

        menubar = Menu(self.window4)
        self.window4.config(menu=menubar)

        frame1 = Frame(self.window4)
        frame1.pack(padx=10, pady=10)
        Label(frame1, text="Fifth Step: Weight/Height History", font=self.font, fg='#57a1f8').grid(row=1, column=1, sticky=NSEW)
        #get weight and height from window1
        #get username from login window
        self.weight = self.first_window.weight
        self.height = self.first_window.height
        self.username = self.login.username

        frame2 = Frame(self.window4)
        frame2.pack(padx=10, pady=10)
        img = Image.open("picture/workoutcartoon.png")
        img = img.resize((400, 350))
        self.photo = ImageTk.PhotoImage(img)
        Label(frame2, image=self.photo).grid(row=2, column=1, sticky=NSEW)

        frame3 = Frame(self.window4)
        frame3.pack(padx=10, pady=10)
        Button(frame3, text="Update Data", command=self.update_data, fg="white", bg= "#57a1f8",borderless=True, bd=0).grid(row=3, column=1, sticky=NSEW)

        frame4 = Frame(self.window4)
        frame4.pack(padx=10, pady=10)
        Button(frame4, text="Weight/Height History Graph", command=self.plot_user_data, fg="white", bg= "#57a1f8",borderless=True, bd=0).grid(row=4, column=1, sticky=NSEW)
        
        frame5 = Frame(self.window4)
        frame5.pack(padx=10, pady=10, side= BOTTOM)
        Button(frame5, text="Back", command=self.back).pack(padx=10, pady=10, side=BOTTOM)

    def load_data(self):
        try:
            with open(self.json_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
        
    def save_data(self):
        try:
            with open(self.json_file, 'w') as f:
                json.dump(self.data, f)
        except Exception as e:
            messagebox.showerror("An error occurred:", e)

    def update_data(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        username = self.username.get()  # Extract the string value from StringVar
        weight_value = self.weight.get()
        height_value = self.height.get()

        print(f"Updating data for {username} at {timestamp}")
        print(f"Current data: {self.data.get(username, {'weight': [], 'height': []})}")

        if username not in self.data:
            self.data[username] = {'weight': [], 'height': []}

        self.data[username]['weight'].append({'timestamp': timestamp, 'value': weight_value})
        self.data[username]['height'].append({'timestamp': timestamp, 'value': height_value})

        print(f"Updated data: {self.data}")

        self.save_data()
        print("Data updated.")

    def get_user_data(self):
        username = self.username.get()
        return self.data.get(username, {'weight': [], 'height': []})
    
    def plot_user_data(self):
        data = self.get_user_data()
        print("Data for plotting:", data)

        weight_data = data['weight']
        height_data = data['height']

        weight_timestamps = [entry['timestamp'] for entry in weight_data]
        weight_values = [entry['value'] for entry in weight_data]

        height_timestamps = [entry['timestamp'] for entry in height_data]
        height_values = [entry['value'] for entry in height_data]

        print("Weight Timestamps:", weight_timestamps)
        print("Weight Values:", weight_values)

        print("Height Timestamps:", height_timestamps)
        print("Height Values:", height_values)

        plt.plot(weight_timestamps, weight_values, label='Weight', marker='o')
        plt.plot(height_timestamps, height_values, label='Height', marker='o')

        plt.title(f"{self.username.get()}'s Weight/Height History")
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.legend()
        plt.tight_layout()
        plt.xticks(rotation=45)
        plt.show()

    def back(self):
        self.window4.destroy()
        self.third_window.window3.deiconify()

    def back_login(self):
        self.window4.destroy()
        Login()

if __name__ == "__main__":
    Login()