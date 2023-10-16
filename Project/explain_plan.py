from tkinter import *
from PIL import ImageTk, Image
import webbrowser

class Explain:
    def __init__(self, second_window):
        self.second_window = second_window
        self.window3 = Toplevel(self.second_window.window2)
        self.third_window = self
        self.window3.title("Workout App")
        self.window3.geometry("900x700+0+0")
        self.font_title = ("TKDefaultFont", 18, "bold")
        self.font_label = ("TKDefaultFont", 14, "bold")

        frame1 = Frame(self.window3)
        frame1.pack(padx=10, pady=10)
        Label(frame1, text="Explanation For Each Workout", font=self.font_title).grid(row=1, column=1, sticky=NSEW)
        Label(frame1, text="Choose one of the workout you want to know about").grid(row=2, column=1, sticky=NSEW)

        frame2 = Frame(self.window3)
        frame2.pack(padx=10, pady=10)
        self.button1 = StringVar()
        self.button1.set("Full Body Workout")  # default value

        Radiobutton(frame2, variable=self.button1, value="Full Body Workout", command=self.update_content).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, text="Full Body Workout").grid(row=3, column=2, sticky=NSEW)
        Radiobutton(frame2, variable=self.button1, value="Upper/Lower Split", command=self.update_content).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, text="Upper/Lower Split").grid(row=3, column=4, sticky=NSEW)
        Radiobutton(frame2, variable=self.button1, value="Push Pull Legs", command=self.update_content).grid(row=3, column=5, sticky=NSEW)
        Label(frame2, text="Push Pull Legs").grid(row=3, column=6, sticky=NSEW)
        Radiobutton(frame2, variable=self.button1, value="Arnold Split", command=self.update_content).grid(row=3, column=7, sticky=NSEW)
        Label(frame2, text="Arnold Split").grid(row=3, column=8, sticky=NSEW)
        Radiobutton(frame2, variable=self.button1, value="Bro Split", command=self.update_content).grid(row=3, column=9, sticky=NSEW)
        Label(frame2, text="Chest, Back, Shoulders, Arms, Legs or called Bro Split").grid(row=3, column=10, sticky=NSEW)

        frame3 = Frame(self.window3)
        frame3.pack(padx=10, pady=10)
        self.info = StringVar()
        # default value
        self.info.set("Full Body Workout is a workout that you do all the exercises for your whole body in one day.\nThis workout is good for beginners because it is easy to follow.\nThis workout is also good for people who want to maintain their muscle mass.\n You can do this workout with dumbbells or bodyweight only.")

        self.font_label = ("TKDefaultFont", 14, "bold")

        frame4 = Frame(self.window3)
        frame4.pack(padx=10, pady=10)
        Label(frame4, textvariable=self.info, font=self.font_label).grid(row=4, column=1, sticky=NSEW)

        frame5 = Frame(self.window3)
        frame5.pack(padx=10, pady=10)
        Button(frame5, text="More information", command=self.open_link).grid(row=5, column=1, sticky=NSEW)

        frame7 = Frame(self.window3)
        frame7.pack(padx=10, pady=10, side= BOTTOM)
        Button(frame7, text="Back", command=self.back).grid(row=1, column= 1, sticky=NSEW)
        Button(frame7, text="Next", command= self.open_chest_explain).grid(row=1, column= 2, sticky=NSEW)

        frame6 = Frame(self.window3)
        frame6.pack(padx=10, pady=10)
        image = Image.open("picture/arnold.png")
        image = image.resize((600, 500))
        self.photo = ImageTk.PhotoImage(image)
        Label(frame6, image=self.photo).grid(row=6, column=1, sticky=NSEW)

        self.window3.mainloop()
    
    def back(self):
        self.window3.destroy()
        self.second_window.window2.deiconify()

    def update_content(self):
        if self.button1.get() == "Full Body Workout":
            self.info.set("Full Body Workout is a workout that you do all the exercises for your whole body in one day.\nThis workout is good for beginners because it is easy to follow.\nThis workout is also good for people who want to maintain their muscle mass.\n You can do this workout with dumbbells or bodyweight only.")

        if self.button1.get() == "Upper/Lower Split":
            self.info.set("Upper/Lower Split is a workout that you do all the exercises for your upper body in one day and lower body in another day.\n This workout is good for intermediate and advanced people because it is more challenging than Full Body Workout. \nYou can do this workout with dumbbells or barbells.")
        
        if self.button1.get() == "Push Pull Legs":
            self.info.set("Push Pull Legs is a workout that you do all the exercises for your push muscles in one day, pull muscles in another day\n and legs in another day. This workout is good for intermediate and advanced people\n because it is more challenging than Full Body Workout.\n You can do this workout with dumbbells or barbells.")
        
        if self.button1.get() == "Arnold Split":
            self.info.set("Arnold Split is a workout that you do all the exercises for your chest and back in one day, shoulders and arms in another day\n and legs in another day. This workout is good for advanced people because it is more challenging than Full Body Workout.\n You can do this workout with dumbbells or barbells.")
        
        if self.button1.get() == "Bro Split":
            self.info.set("Chest, Back, Shoulders, Arms, Legs is a workout that you do all the exercises\n for your chest in one day, back in another day, shoulders in another day, arms in another day and legs in another day.\n This workout is good for advanced people because it is more challenging than Full Body Workout. \nYou can do this workout with dumbbells or barbells.")

    def open_link(self):
        
        if self.button1.get() == "Full Body Workout":
            webbrowser.open("https://www.youtube.com/shorts/bVrj4pIPEqg")

        if self.button1.get() == "Upper/Lower Split":
            webbrowser.open("https://youtu.be/eWPj3ikAExk?t=44")
        
        if self.button1.get() == "Push Pull Legs":
            webbrowser.open("https://www.youtube.com/watch?v=k_JvRZLXMj4")
        
        if self.button1.get() == "Arnold Split":
            webbrowser.open("https://www.youtube.com/watch?v=7ZPzeGnb2uI")
        
        if self.button1.get() == "Bro Split":
            webbrowser.open("https://www.youtube.com/watch?v=1vh7wLrFLW8")

    def open_chest_explain(self):
        self.third_window.window3.withdraw()
        ExplainChest(self.third_window)

class ExplainChest:
    def __init__(self, third_window):
        self.third_window = third_window
        self.window4 = Toplevel(self.third_window.window3)
        self.fourth_window = self
        self.window4.title("Workout App")
        self.window4.geometry("900x700+0+0")
        self.font_title = ("TKDefaultFont", 18, "bold")
        self.font_label = ("TKDefaultFont", 14, "bold")

        frame1 = Frame(self.window4)
        frame1.pack(padx=10, pady=10)
        Label(frame1, text="Explanation For Each Muscle", font=self.font_title).grid(row=1, column=1, sticky=NSEW)
        Label(frame1, text="First Muscle Group", font= self.font_title).grid(row=2, column=1, sticky=NSEW)
        Label(frame1, text= "Chest", font= self.font_title).grid(row=3, column=1, sticky=NSEW)

        frame2 = Frame(self.window4)
        frame2.pack(padx=10, pady=10)
        Label(frame2, text="Chest consist of three main muscles\nwhich is\n Upper Chest, Middle Chest and Lower Chest", font= self.font_label).grid(row=3, column=1, sticky=NSEW)
        
        frame4 = Frame(self.window4)
        frame4.pack(padx=10, pady=10, side= BOTTOM)
        Button(frame4, text="Back", command=self.back).grid(row=1, column= 1, sticky=NSEW)
        Button(frame4, text="Next", command= self.open_shoulders_explain).grid(row=1, column= 2, sticky=NSEW)

        frame3 = Frame(self.window4)
        frame3.pack(padx=10, pady=10)
        image = Image.open("picture/chestanatomy.png")
        image = image.resize((600, 400))
        self.photo = ImageTk.PhotoImage(image)
        Label(frame3, image=self.photo).grid(row=4, column=1, sticky=NSEW)

    def back(self):
        self.window4.destroy()
        self.third_window.window3.deiconify()

    def open_shoulders_explain(self):
        self.fourth_window.window4.withdraw()
        ExplainShoulders(self.fourth_window)

class ExplainShoulders:
    def __init__(self, fourth_window):
        self.fourth_window = fourth_window
        self.window5 = Toplevel(self.fourth_window.window4)
        self.fifth_window = self
        self.window5.title("Workout App")
        self.window5.geometry("900x700+0+0")
        self.font_title = ("TKDefaultFont", 18, "bold")
        self.font_label = ("TKDefaultFont", 14, "bold")

        frame1 = Frame(self.window5)
        frame1.pack(padx=10, pady=10)
        Label(frame1, text="Second Muscle Group", font= self.font_title).grid(row=1, column=1, sticky=NSEW)
        Label(frame1, text= "Shoulders", font= self.font_title).grid(row=2, column=1, sticky=NSEW)

        frame2 = Frame(self.window5)
        frame2.pack(padx=10, pady=10)
        Label(frame2, text="Shoulders consist of three main muscles\nwhich is\n Anterior Deltoid, Medial Deltoid and Posterior Deltoid", font= self.font_label).grid(row=3, column=1, sticky=NSEW)

        frame4 = Frame(self.window5)
        frame4.pack(padx=10, pady=10, side= BOTTOM)
        Button(frame4, text="Back", command=self.back).grid(row=1, column= 1, sticky=NSEW)
        Button(frame4, text="Next", command= self.open_back_explain).grid(row=1, column= 2, sticky=NSEW)

        frame3 = Frame(self.window5)
        frame3.pack(padx=10, pady=10)
        image = Image.open("picture/shoulderanatomy.png")
        image = image.resize((600, 400))
        self.photo = ImageTk.PhotoImage(image)
        Label(frame3, image=self.photo).grid(row=4, column=1, sticky=NSEW)

    def back(self):
        self.window5.destroy()
        self.fourth_window.window4.deiconify()

    def open_back_explain(self):
        self.fifth_window.window5.withdraw()
        ExplainBack(self.fifth_window)

class ExplainBack:
    def __init__(self, fifth_window):
        self.fifth_window = fifth_window
        self.window6 = Toplevel(self.fifth_window.window5)
        self.sixth_window = self
        self.window6.title("Workout App")
        self.window6.geometry("900x700+0+0")
        self.font_title = ("TKDefaultFont", 18, "bold")
        self.font_label = ("TKDefaultFont", 14, "bold")

        frame1 = Frame(self.window6)
        frame1.pack(padx=10, pady=10)
        Label(frame1, text="Third Muscle Group", font= self.font_title).grid(row=1, column=1, sticky=NSEW)
        Label(frame1, text= "Back", font= self.font_title).grid(row=2, column=1, sticky=NSEW)

        frame2 = Frame(self.window6)
        frame2.pack(padx=10, pady=10)
        Label(frame2, text="Back consist of many muscles\nwhich is\n Trapezius, Latissimus Dorsi, Rhomboids, Teres Major, Teres Minor and Erector Spinae", font= self.font_label).grid(row=3, column=1, sticky=NSEW)

        frame4 = Frame(self.window6)
        frame4.pack(padx=10, pady=10, side= BOTTOM)
        Button(frame4, text="Back", command=self.back).grid(row=1, column= 1, sticky=NSEW)
        Button(frame4, text="Next", command= self.open_arms_explain).grid(row=1, column= 2, sticky=NSEW)

        frame3 = Frame(self.window6)
        frame3.pack(padx=10, pady=10)
        image = Image.open("picture/backanatomy.png")
        image = image.resize((600, 550))
        self.photo = ImageTk.PhotoImage(image)
        Label(frame3, image=self.photo).grid(row=4, column=1, sticky=NSEW)

    def back(self):
        self.window6.destroy()
        self.fifth_window.window5.deiconify()

    def open_arms_explain(self):
        self.sixth_window.window6.withdraw()
        ExplainArms(self.sixth_window)

class ExplainArms:
    def __init__(self, sixth_window):
        self.sixth_window = sixth_window
        self.window7 = Toplevel(self.sixth_window.window6)
        self.seventh_window = self
        self.window7.title("Workout App")
        self.window7.geometry("900x700+0+0")
        self.font_title = ("TKDefaultFont", 18, "bold")
        self.font_label = ("TKDefaultFont", 14, "bold")

        frame1 = Frame(self.window7)
        frame1.pack(padx=10, pady=10)
        Label(frame1, text="Fourth Muscle Group", font= self.font_title).grid(row=1, column=1, sticky=NSEW)
        Label(frame1, text= "Arms", font= self.font_title).grid(row=2, column=1, sticky=NSEW)

        frame2 = Frame(self.window7)
        frame2.pack(padx=10, pady=10)
        Label(frame2, text="Arms consist of three main muscles\nwhich is\n Biceps, Triceps and Forearms", font= self.font_label).grid(row=3, column=1, sticky=NSEW)
        
        frame4 = Frame(self.window7)
        frame4.pack(padx=10, pady=10, side= BOTTOM)
        Button(frame4, text="Back", command=self.back).grid(row=1, column= 1, sticky=NSEW)
        Button(frame4, text="Next", command= self.open_legs_explain).grid(row=1, column= 2, sticky=NSEW)

        frame3 = Frame(self.window7)
        frame3.pack(padx=10, pady=10)
        image = Image.open("picture/armsanatomy.png")
        image = image.resize((450, 550))
        self.photo = ImageTk.PhotoImage(image)
        Label(frame3, image=self.photo).grid(row=4, column=1, sticky=NSEW)

    def back(self):
        self.window7.destroy()
        self.sixth_window.window6.deiconify()

    def open_legs_explain(self):
        self.seventh_window.window7.withdraw()
        ExplainLegs(self.seventh_window)

class ExplainLegs:
    def __init__(self, seventh_window):
        self.seventh_window = seventh_window
        self.window8 = Toplevel(self.seventh_window.window7)
        self.eight_window = self
        self.window8.title("Workout App")
        self.window8.geometry("900x700+0+0")
        self.font_title = ("TKDefaultFont", 18, "bold")
        self.font_label = ("TKDefaultFont", 14, "bold")

        frame1 = Frame(self.window8)
        frame1.pack(padx=10, pady=10)
        Label(frame1, text="Fifth Muscle Group", font= self.font_title).grid(row=1, column=1, sticky=NSEW)
        Label(frame1, text= "Legs", font= self.font_title).grid(row=2, column=1, sticky=NSEW)

        frame2 = Frame(self.window8)
        frame2.pack(padx=10, pady=10)
        Label(frame2, text="Legs consist of three main muscles\nwhich is\n Quadriceps, Hamstrings and Calves", font= self.font_label).grid(row=3, column=1, sticky=NSEW)

        frame4 = Frame(self.window8)
        frame4.pack(padx=10, pady=10, side= BOTTOM)
        Button(frame4, text="Back", command=self.back).grid(row=1, column= 1, sticky=NSEW)

        frame3 = Frame(self.window8)
        frame3.pack(padx=10, pady=10)
        image = Image.open("picture/legsanatomy.png")
        image = image.resize((500, 600))
        self.photo = ImageTk.PhotoImage(image)
        Label(frame3, image=self.photo).grid(row=4, column=1, sticky=NSEW)

    def back(self):
        self.window8.destroy()
        self.seventh_window.window7.deiconify()
