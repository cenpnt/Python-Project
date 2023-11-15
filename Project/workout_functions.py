from tkinter import *
from tkinter import messagebox
try:
    from PIL import ImageTk, Image
except ImportError:
    messagebox.showerror("Error", "Pillow module is not installed\nPlease install it by typing 'pip/pip3 install pillow' in the terminal")
    exit()
import webbrowser

class Page(Toplevel):
    def __init__(self, parent, title):
        Toplevel.__init__(self, parent) # Initialize the toplevel
        self.title(title) 
        self.parent = parent # Save the reference to the parent window
        self.font_title = ("TKDefaultFont", 26, "bold")
        self.font_text = ("TKDefaultFont", 18, "bold")
        self.font_text2 = ("TKDefaultFont", 16)
        self.geometry("1000x450+0+0")

    def show(self):
        self.lift() # Show the window

### 1 Day FullBody ###

class Day1Beginner(Frame):
    def __init__(self, second_window):
        super().__init__() # Initialize the frame
        self.second_window = second_window # Save the reference to the second window
        self.window4 = None # No window yet
        
        menubar = Menu(self.second_window.window2)
        self.second_window.window2.config(menu=menubar)

        workouts_menu = Menu(menubar)
        menubar.add_cascade(label="Chest", menu=workouts_menu, command=self.open_chest_workout)
        menubar.add_cascade(label="Shoulders", menu=workouts_menu, command=self.open_shoulders_workout)
        menubar.add_cascade(label="Back", menu=workouts_menu, command=self.open_back_workout)
        menubar.add_cascade(label="Arms", menu=workouts_menu, command=self.open_arms_workout)
        menubar.add_cascade(label="Legs", menu=workouts_menu, command=self.open_legs_workout)
        menubar.add_cascade(label = "Back to Previous Page", menu = workouts_menu, command = self.back)

        self.open_chest_workout()

    def open_chest_workout(self):
        if self.window4:
            self.window4.destroy() 
        self.window4 = Chest1Begin(self.second_window.window2)

    def open_shoulders_workout(self):
        if self.window4:
            self.window4.destroy() 
        self.window4 = Shoulder1Begin(self.second_window.window2)

    def open_back_workout(self):
        if self.window4:
            self.window4.destroy()
        self.window4 = Back1Begin(self.second_window.window2)

    def open_arms_workout(self):
        if self.window4:
            self.window4.destroy()
        self.window4 = Arms1Begin(self.second_window.window2)
    
    def open_legs_workout(self):
        if self.window4:
            self.window4.destroy()
        self.window4 = Legs1Begin(self.second_window.window2)

    def back(self):
        self.window4.destroy()
        self.second_window.window2.deiconify()

class Chest1Begin(Page):
    def __init__(self, parent):
        super().__init__(parent, "Chest") # Initialize the page
        self.geometry("1000x400+0+0")
        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Chest Workout For Beginner", font= self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Push Ups", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text= "3x10 reps", font= self.font_text2).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text= "Incline Push Ups", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "3x10 reps", font= self.font_text2).grid(row=2, column=2, sticky=NSEW)

        img1 = Image.open("picture/pushup.png").resize((400, 200))
        img2 = Image.open("picture/inclinepushup.png").resize((433, 216))
        self.photo1, self.photo2 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, text= "Pushup focusing on middle chest", font= self.font_text2).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Incline Pushup focusing on upper chest", font= self.font_text2).grid(row=4, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=IODxDxX7oi4")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=cfns5VDVVvk")

class Shoulder1Begin(Page):
    def __init__(self, parent):
        super().__init__(parent, "Shoulders")
        self.geometry("1000x550+0+0")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Shoulder Workout For Beginner", font= self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Dumbbell Shoulder Press", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text= "3x10 reps", font= self.font_text2).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text= "Lateral Raise", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "3x to failure", font= self.font_text2).grid(row=2, column=2, sticky=NSEW)

        img1 = Image.open("picture/shoulderpress.png").resize((333, 333))
        img2 = Image.open("picture/lateralraise.png").resize((333, 333))
        self.photo1, self.photo2 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, text= "Dumbbell Shoulder Press focusing on front shoulder", font= self.font_text2).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Lateral Raise focusing on middle shoulder", font= self.font_text2).grid(row=4, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=qEwKCR5JCog")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/shorts/xyK8UiC-BUw")

class Back1Begin(Page):
    def __init__(self, parent):
        super().__init__(parent, "Back")
        self.geometry("1000x550+0+0")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Back Workout For Beginner", font= self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Dumbbell Row", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "3x10 reps", font= self.font_text2).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text= "Dumbbell Over Row", font= self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text= "3x10 reps", font= self.font_text2).grid(row=2, column=3, sticky=NSEW)

        img2 = Image.open("picture/dumbbellrow.png").resize((333, 333))
        img3 = Image.open("picture/dumbbelloverrow.png").resize((333, 333))
        self.photo2, self.photo3 = ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, text= "Dumbbell Row focusing on Lat", font= self.font_text2).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text= "Dumbbell Over Row focusing the whole back", font= self.font_text2).grid(row=4, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=3, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=pYcpY20QaE8")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=6TSP1TRMUzs")

class Arms1Begin(Page):
    def __init__(self, parent):
        super().__init__(parent, "Arms")
        self.geometry("1000x550+0+0")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Arms Workout For Beginner", font= self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Dumbbell Curl", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text= "3x10 reps", font= self.font_text2).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text= "Overhead Tricep Extension", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "3x10 reps", font= self.font_text2).grid(row=2, column=2, sticky=NSEW)

        img1 = Image.open("picture/dumbbellcurl.png").resize((333, 333))
        img2 = Image.open("picture/overheadtricepextension.png").resize((222, 220))
        self.photo2, self.photo3 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2)
        Label(frame2, image=self.photo2).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, text= "Dumbbell Curl focusing on Bicep", font= self.font_text2).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Tricep Overhead Extension focusing on Tricep", font= self.font_text2).grid(row=4, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=ykJmrZ5v0Oo")
    
    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=-Vyt2QdsR7E")

class Legs1Begin(Page):
    def __init__(self, parent):
        super().__init__(parent, "Legs")
        self.geometry("1000x550+0+0")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Legs Workout For Beginner", font= self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Goblet Squat", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text= "3x10 reps", font= self.font_text2).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text= "Leg Lunges", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "3x10 reps", font= self.font_text2).grid(row=2, column=2, sticky=NSEW)

        img1 = Image.open("picture/gobletsquat.png").resize((250, 250))
        img2 = Image.open("picture/leglunge.png").resize((364, 329))
        self.photo2, self.photo3 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2)
        Label(frame2, image=self.photo2).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, text= "Goblet Squat focusing on Quadriceps", font= self.font_text2).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Leg Lunges focusing on Quadriceps", font= self.font_text2).grid(row=4, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=MeIiIdhvXT4")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=3frV3RnPfOY")

class Day1Intermediate(Frame):
    def __init__(self, second_window):
        super().__init__()
        self.second_window = second_window
        self.window5 = None

        menubar = Menu(self.second_window.window2)
        self.second_window.window2.config(menu=menubar)

        workouts_menu = Menu(menubar)
        menubar.add_cascade(label="Chest", menu=workouts_menu, command=self.open_chest_workout)
        menubar.add_cascade(label="Shoulders", menu=workouts_menu, command=self.open_shoulders_workout)
        menubar.add_cascade(label="Back", menu=workouts_menu, command=self.open_back_workout)
        menubar.add_cascade(label="Arms", menu=workouts_menu, command=self.open_arms_workout)
        menubar.add_cascade(label="Legs", menu=workouts_menu, command=self.open_legs_workout)
        menubar.add_cascade(label = "Back to Previous Page", menu = workouts_menu, command = self.back)

        self.open_chest_workout()

    def open_chest_workout(self):
        if self.window5:
            self.window5.destroy()  # Close the previous page
        self.window5 = Chest1Inter(self.second_window.window2)

    def open_shoulders_workout(self):
        if self.window5:
            self.window5.destroy()
        self.window5 = Shoulder1Inter(self.second_window.window2)

    def open_back_workout(self):
        if self.window5:
            self.window5.destroy()
        self.window5 = Back1Inter(self.second_window.window2)

    def open_arms_workout(self):
        if self.window5:
            self.window5.destroy()
        self.window5 = Arms1Inter(self.second_window.window2)

    def open_legs_workout(self):
        if self.window5:
            self.window5.destroy()
        self.window5 = Legs1Inter(self.second_window.window2)
        
    def back(self):
        self.window5.destroy()
        self.second_window.window2.deiconify()

class Chest1Inter(Page):
    def __init__(self, parent):
        super().__init__(parent, "Chest")
        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Chest Workout For Intermediate", font= self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Dumbbell Bench Press", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text= "3x10-12 reps", font= self.font_text2).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text= "Incline Dumbbell Bench Press", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "3x10-12 reps", font= self.font_text2).grid(row=2, column=2, sticky=NSEW)

        img1 = Image.open("picture/dumbbellbenchpress.png").resize((250, 250))
        img2 = Image.open("picture/inclinedumbbellbench.png").resize((250, 250))
        self.photo1, self.photo2 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, text= "Dumbbell Bench Press focusing on middle chest", font= self.font_text2).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Incline Dumbbell Bench Press focusing on upper chest", font= self.font_text2).grid(row=4, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=QsYre__-aro")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=8iPEnn-ltC8")

class Shoulder1Inter(Page):
    def __init__(self, parent):
        super().__init__(parent, "Shoulders")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Shoulder Workout For Intermediate", font= self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Dumbbell Shoulder Press", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text= "3x10-12 reps", font= self.font_text2).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text= "Dumbbell Lateral Raise", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "3x to failure", font= self.font_text2).grid(row=2, column=2, sticky=NSEW)

        img1 = Image.open("picture/shoulderpress.png").resize((250, 250))
        img2 = Image.open("picture/lateralraise.png").resize((250, 250))
        self.photo1, self.photo2 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, text= "Dumbbell Shoulder Press focusing on front shoulder", font= self.font_text2).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Dumbbell Lateral Raise focusing on middle shoulder", font= self.font_text2).grid(row=4, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=qEwKCR5JCog")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/shorts/JIhbYYA1Q90")

class Back1Inter(Page):
    def __init__(self, parent):
        super().__init__(parent, "Back")
        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Back Workout For Intermediate", font= self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Lat Pulldown", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text= "3x10-12 reps", font= self.font_text2).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text= "Seated Cable Row", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "3x10-12 reps", font= self.font_text2).grid(row=2, column=2, sticky=NSEW)

        img1 = Image.open("picture/latpulldown.png").resize((250, 250))
        img2 = Image.open("picture/seatedcablerow.png").resize((250, 250))
        self.photo1, self.photo2 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, text= "Lat Pulldown focusing on Lat", font= self.font_text2).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Seated Cable Row focusing on Middle Back", font= self.font_text2).grid(row=4, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=CAwf7n6Luuc&t=262s")
    
    def open_video2(self):
        webbrowser.open("https://www.youtube.com/shorts/fPbfYDgzIgA")

class Arms1Inter(Page):
    def __init__(self, parent):
        super().__init__(parent, "Arms")
        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Arms Workout For Intermediate", font= self.font_title).grid(row=1, column=0, sticky=NSEW)
        
        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Cable Curl", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text= "3x10-12 reps", font= self.font_text2).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text= "Tricep Rope Pushdown", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "3x10-12 reps", font= self.font_text2).grid(row=2, column=2, sticky=NSEW)

        img1 = Image.open("picture/cablecurl.png").resize((250, 250))
        img2 = Image.open("picture/tricepropepushdown.png").resize((250, 250))
        self.photo1, self.photo2 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, text= "Cable Curl focusing on Bicep", font= self.font_text2).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Tricep Rope Pushdown focusing on Tricep", font= self.font_text2).grid(row=4, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=NFzTWp2qpiE")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=-xa-6cQaZKY")

class Legs1Inter(Page):
    def __init__(self, parent):
        super().__init__(parent, "Legs")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Legs Workout For Intermediate", font= self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Barbell Squat", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text= "3x10-12 reps", font= self.font_text2).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text= "Leg Curl", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "3x10-12 reps", font= self.font_text2).grid(row=2, column=2, sticky=NSEW)

        img1 = Image.open("picture/barbellsquat.png").resize((250, 250))
        img2 = Image.open("picture/legcurl.png").resize((250, 250))
        self.photo1, self.photo2 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, text= "Barbell Squat focusing on Quadriceps", font= self.font_text2).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Leg Curl focusing on Hamstring", font= self.font_text2).grid(row=4, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/shorts/9v3ySm-m8lI")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=1Tq3QdYUuHs")

class Day1Advanced(Frame):
    def __init__(self, second_window):
        super().__init__()
        self.second_window = second_window
        self.window6 = None

        menubar = Menu(self.second_window.window2)
        self.second_window.window2.config(menu=menubar)

        workouts_menu = Menu(menubar)
        menubar.add_cascade(label="Chest", menu=workouts_menu, command=self.open_chest_workout)
        menubar.add_cascade(label="Shoulders", menu=workouts_menu, command=self.open_shoulders_workout)
        menubar.add_cascade(label="Back", menu=workouts_menu, command=self.open_back_workout)
        menubar.add_cascade(label="Arms", menu=workouts_menu, command=self.open_arms_workout)
        menubar.add_cascade(label="Legs", menu=workouts_menu, command=self.open_legs_workout)
        menubar.add_cascade(label = "Back to Previous Page", menu = workouts_menu, command = self.back)

        self.open_chest_workout()

    def open_chest_workout(self):
        if self.window6:
            self.window6.destroy()
        self.window6 = Chest1Adv(self.second_window.window2)

    def open_shoulders_workout(self):
        if self.window6:
            self.window6.destroy()
        self.window6 = Shoulder1Adv(self.second_window.window2)

    def open_back_workout(self):
        if self.window6:
            self.window6.destroy()
        self.window6 = Back1Adv(self.second_window.window2)

    def open_arms_workout(self):
        if self.window6:
            self.window6.destroy()
        self.window6 = Arms1Adv(self.second_window.window2)

    def open_legs_workout(self):
        if self.window6:
            self.window6.destroy()
        self.window6 = Legs1Adv(self.second_window.window2)

    def back(self):
        self.window6.destroy()
        self.second_window.window2.deiconify()

class Chest1Adv(Page):
    def __init__(self, parent):
        super().__init__(parent, "Chest")
        
        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Chest Workout For Advanced", font= self.font_title).grid(row=1, column=0, sticky=NSEW)
        
        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Barbell Bench Press", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text= "2x10-12 reps", font= self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text= "Incline Barbell Bench Press", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "2x10-12 reps", font= self.font_text).grid(row=2, column=2, sticky=NSEW)

        img1 = Image.open("picture/barbellbench.png").resize((250, 250))
        img2 = Image.open("picture/inclinebarbellbench.png").resize((250, 250))
        self.photo1, self.photo2 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, text= "Barbell Bench Press focusing on middle chest", font= self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Incline Barbell Bench Press focusing on upper chest", font= self.font_text).grid(row=4, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=rT7DgCr-3pg")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=SrqOu55lrYU")

class Shoulder1Adv(Page):
    def __init__(self, parent):
        super().__init__(parent, "Shoulders")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Shoulder Workout For Advanced", font= self.font_title).grid(row=1, column=0, sticky=NSEW)
        
        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Barbell Shoulder Press", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text= "2x10-12 reps", font= self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text= "Cable Lateral Raise", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "3x to failure", font= self.font_text).grid(row=2, column=2, sticky=NSEW)

        img1 = Image.open("picture/barbellshoulderpress.png").resize((250, 250))
        img2 = Image.open("picture/cablelateralraise.png").resize((250, 250))
        self.photo1, self.photo2 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, text= "Barbell Shoulder Press focusing on front shoulder", font= self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Cable Lateral Raise focusing on middle shoulder", font= self.font_text).grid(row=4, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=QAQ64hK4Xxs&t=233s")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/shorts/EZSAOY7b3g4")

class Back1Adv(Page):
    def __init__(self, parent):
        super().__init__(parent, "Back")
        
        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Back Workout For Advanced", font= self.font_title).grid(row=1, column=0, sticky=NSEW)
        
        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Lat Pulldown", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text= "3x10-12 reps", font= self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text= "Deadlift", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "2x10-12 reps", font= self.font_text).grid(row=2, column=2, sticky=NSEW)

        img1 = Image.open("picture/latpulldown.png").resize((250, 250))
        img2 = Image.open("picture/deadlift.png").resize((250, 250))
        self.photo1, self.photo2 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, text= "Lat Pulldown focusing on Lat", font= self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Deadlift focusing on the whole back, mainly Inner Back", font= self.font_text).grid(row=4, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=CAwf7n6Luuc&t=262s")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=XxWcirHIwVo")

class Arms1Adv(Page):
    def __init__(self, parent):
        super().__init__(parent, "Arms")
        
        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Arms Workout For Advanced", font= self.font_title).grid(row=1, column=0, sticky=NSEW)
        
        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Preacher Curl", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text= "3x10-12 reps", font= self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text= "Tricep Rope Pushdown", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "3x10-12 reps", font= self.font_text).grid(row=2, column=2, sticky=NSEW)

        img1 = Image.open("picture/preachercurl.png").resize((250, 250))
        img2 = Image.open("picture/tricepropepushdown.png").resize((250, 250))
        self.photo1, self.photo2 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, text= "Barbell Curl focusing on Bicep", font= self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Tricep Rope Pushdown focusing on Tricep", font= self.font_text).grid(row=4, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=fIWP-FRFNU0")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=-xa-6cQaZKY")

class Legs1Adv(Page):
    def __init__(self, parent):
        super().__init__(parent, "Legs")
        
        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Legs Workout For Advanced", font= self.font_title).grid(row=1, column=0, sticky=NSEW)
        
        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Barbell Squat", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text= "4x6-8 reps", font= self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text= "Leg Curl", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "4x10-12 reps", font= self.font_text).grid(row=2, column=2, sticky=NSEW)

        img1 = Image.open("picture/barbellsquat.png").resize((250, 250))
        img2 = Image.open("picture/legcurl.png").resize((250, 250))
        self.photo1, self.photo2 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, text= "Barbell Squat focusing on Quadriceps", font= self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Leg Curl focusing on Hamstring", font= self.font_text).grid(row=4, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/shorts/9v3ySm-m8lI")
    
    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=1Tq3QdYUuHs")

### 2 Day Upper Lower ###

class Day2Beginner(Frame):
    def __init__(self, second_window):
        super().__init__()
        self.second_window = second_window
        self.window7 = None

        menubar = Menu(self.second_window.window2)
        self.second_window.window2.config(menu=menubar)

        workouts_menu = Menu(menubar)
        menubar.add_cascade(label="Upper1", menu=workouts_menu, command=self.open_upper_workout)
        menubar.add_cascade(label="Upper2", menu=workouts_menu, command=self.open_upper_workout2)
        menubar.add_cascade(label="Lower", menu=workouts_menu, command=self.open_lower_workout)
        menubar.add_cascade(label = "Back to Previous Page", menu = workouts_menu, command = self.back)

        self.open_upper_workout()

    def open_upper_workout(self):
        if self.window7:
            self.window7.destroy()
        self.window7 = Upper2Begin1(self.second_window.window2)

    def open_upper_workout2(self):
        if self.window7:
            self.window7.destroy()
        self.window7 = Upper2Begin2(self.second_window.window2)

    def open_lower_workout(self):
        if self.window7:
            self.window7.destroy()
        self.window7 = Lower2Begin(self.second_window.window2)

    def back(self):
        self.window7.destroy()
        self.second_window.window2.deiconify()

class Upper2Begin1(Page):
    def __init__(self, parent):
        super().__init__(parent, "Upper")
        self.geometry("1710x500")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Upper Workout For Beginner", font= self.font_title).grid(row=1, column=0, sticky=NSEW)
        Label(frame1, text= "Upper Workout Contains Chest, Shoulders, Back and Arms", font= self.font_text).grid(row=2, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text="Push Up", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="3x10 reps or to failure", font= self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Incline Push Up", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="2x10 reps or to failure", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Dumbbell Shoulder Press", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="3x10 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Dumbbell Lateral Raise", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="3x to failure", font=self.font_text).grid(row=2, column=4, sticky=NSEW)

        img1 = Image.open("picture/pushup.png").resize((370, 200))
        img2 = Image.open("picture/inclinepushup.png").resize((400, 216))
        img3 = Image.open("picture/shoulderpress.png").resize((250, 250))
        img4 = Image.open("picture/lateralraise.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, text= "Push Up focusing on Chest", font= self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Incline Push Up focusing on Upper Chest", font= self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text= "Dumbbell Shoulder Press focusing on Front Shoulder", font= self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text= "Dumbbell Lateral Raise focusing on Middle Shoulder", font= self.font_text).grid(row=4, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=IODxDxX7oi4")
    
    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=cfns5VDVVvk")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=qEwKCR5JCog")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/shorts/xyK8UiC-BUw")

class Upper2Begin2(Page):
    def __init__(self, parent):
        super().__init__(parent, "Upper")
        self.geometry("1500x500")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Upper Workout For Beginner", font= self.font_title).grid(row=1, column=0, sticky=NSEW)
        Label(frame1, text= "Upper Workout Contains Chest, Shoulders, Back and Arms", font= self.font_text).grid(row=2, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text="Dumbbell Row", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="3x10 reps", font= self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Dumbbell Shrugs", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="3x10 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Dumbbell Curl", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="3x10 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Overhead Tricep Extension", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="3x10 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)

        img1 = Image.open("picture/dumbbellrow.png").resize((250, 250))
        img2 = Image.open("picture/dumbbellshrugs.png").resize((250, 250))
        img3 = Image.open("picture/dumbbellcurl.png").resize((250, 250))
        img4 = Image.open("picture/overheadtricepextension.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, text= "Dumbbell Row focusing on Lat", font= self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Dumbbell Shrugs focusing on Upper Back", font= self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text= "Dumbbell Curl focusing on Bicep", font= self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text= "Overhead Tricep Extension focusing on Tricep", font= self.font_text).grid(row=4, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=pYcpY20QaE8")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=cJRVVxmytaM")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=ykJmrZ5v0Oo")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=-Vyt2QdsR7E")

class Lower2Begin(Page):
    def __init__(self, parent):
        super().__init__(parent, "Lower")
        self.geometry("1500x500")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Lower Workout For Beginner", font= self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Goblet Squat", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text= "3x10 reps", font= self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text= "Lunge", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "3x10 reps", font= self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text= "Sumo Squat", font= self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text= "3x10 reps", font= self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text= "Stiff Leg Deadlift", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text= "3x10 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)

        img1 = Image.open("picture/gobletsquat.png").resize((250, 250))
        img2 = Image.open("picture/leglunge.png").resize((250, 250))
        img3 = Image.open("picture/sumosquat.png").resize((250, 250))
        img4 = Image.open("picture/stifflegdeadlift.png").resize((350, 250))
        self.photo1, self.photo2, self.photo3, self.photo4 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, text= "Squat focusing on Quadriceps", font= self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Lunge focusing on Hamstring", font= self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text= "Sumo Squat focusing on Inner Thigh", font= self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text= "Stiff Leg Deadlift focusing on Hamstring", font= self.font_text).grid(row=4, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=MeIiIdhvXT4")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=3frV3RnPfOY")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/shorts/BrNH9Sekcd8")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=cYKYGwcg0U8&pp=ygUSc3RpZmYgbGVnIGRlYWRsaWZ0")

class Day2Intermediate(Frame):
    def __init__(self, second_window):
        super().__init__()
        self.second_window = second_window
        self.window8 = None

        menubar = Menu(self.second_window.window2)
        self.second_window.window2.config(menu=menubar)

        workouts_menu = Menu(menubar)
        menubar.add_cascade(label="Upper1", menu=workouts_menu, command=self.open_upper_workout)
        menubar.add_cascade(label="Upper2", menu=workouts_menu, command=self.open_upper_workout2)
        menubar.add_cascade(label="Lower", menu=workouts_menu, command=self.open_lower_workout)
        menubar.add_cascade(label = "Back to Previous Page", menu = workouts_menu, command = self.back)

        self.open_upper_workout()

    def open_upper_workout(self):
        if self.window8:
            self.window8.destroy()
        self.window8 = Upper2Inter1(self.second_window.window2)

    def open_upper_workout2(self):
        if self.window8:
            self.window8.destroy()
        self.window8 = Upper2Inter2(self.second_window.window2)

    def open_lower_workout(self):
        if self.window8:
            self.window8.destroy()
        self.window8 = Lower2Inter(self.second_window.window2)

    def back(self):
        self.window8.destroy()
        self.second_window.window2.deiconify()

class Upper2Inter1(Page):
    def __init__(self, parent):
        super().__init__(parent, "Upper")
        self.geometry("1200x450")
        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Upper Workout For Intermediate", font= self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text="Dumbbell Bench Press", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="4x8-10 reps", font= self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Incline Dumbbell Bench Press", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="3x8-10 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Dumbbell Shoulder Press", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="3x8-10 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Dumbbell Lateral Raise", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="3x to failure", font=self.font_text).grid(row=2, column=4, sticky=NSEW)

        img1 = Image.open("picture/dumbbellbenchpress.png").resize((250, 250))
        img2 = Image.open("picture/inclinedumbbellbench.png").resize((250, 250))
        img3 = Image.open("picture/shoulderpress.png").resize((250, 250))
        img4 = Image.open("picture/lateralraise.png").resize((250, 250))
        self.photo1 = ImageTk.PhotoImage(img1)
        self.photo2 = ImageTk.PhotoImage(img2)
        self.photo3 = ImageTk.PhotoImage(img3)
        self.photo4 = ImageTk.PhotoImage(img4)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, text= "Focusing on Chest", font= self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Focusing on Upper Chest", font= self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text= "Focusing on Front Shoulder", font= self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text= "Focusing on Middle Shoulder", font= self.font_text).grid(row=4, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=QsYre__-aro")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=8iPEnn-ltC8")
    
    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=qEwKCR5JCog")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/shorts/JIhbYYA1Q90")

class Upper2Inter2(Page):
    def __init__(self, parent):
        super().__init__(parent, "Upper")
        self.geometry("1200x450")
        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Upper Workout For Intermediate", font= self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text="Lat Pulldown", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="3x10-12 reps", font= self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Seated Cable Row", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="3x10-12 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Cable Curl", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="3x10-12 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Tricep Rope Pushdown", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)

        img1 = Image.open("picture/latpulldown.png").resize((250, 250))
        img2 = Image.open("picture/seatedcablerow.png").resize((250, 250))
        img3 = Image.open("picture/cablecurl.png").resize((250, 250))
        img4 = Image.open("picture/tricepropepushdown.png").resize((250, 250))
        self.photo1 = ImageTk.PhotoImage(img1)
        self.photo2 = ImageTk.PhotoImage(img2)
        self.photo3 = ImageTk.PhotoImage(img3)
        self.photo4 = ImageTk.PhotoImage(img4)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)

        Label(frame2, text= "Focusing on Lat", font= self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Focusing on Upper Back", font= self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text= "Focusing on Bicep", font= self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text= "Focusing on Tricep", font= self.font_text).grid(row=4, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)
    
    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=CAwf7n6Luuc&t=262s")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/shorts/fPbfYDgzIgA")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=NFzTWp2qpiE")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=-xa-6cQaZKY")

class Lower2Inter(Page):
    def __init__(self, parent):
        super().__init__(parent, "Lower")
        self.geometry("1200x450")
        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Lower Workout For Intermediate", font= self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Barbell Squat", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text= "4x6-8 reps", font= self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text= "Romanian Deadlift", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "4x8-10 reps", font= self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text= "Leg Extension", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text= "3x10-12 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text= "Leg Curl", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text= "3x10-12 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)

        img1 = Image.open("picture/barbellsquat.png").resize((250, 250))
        img2 = Image.open("picture/romaniandeadlift.png").resize((400, 250))
        img3 = Image.open("picture/legextension.png").resize((250, 250))
        img4 = Image.open("picture/legcurl.png").resize((250, 250))
        self.photo1 = ImageTk.PhotoImage(img1)
        self.photo2 = ImageTk.PhotoImage(img2)
        self.photo3 = ImageTk.PhotoImage(img3)
        self.photo4 = ImageTk.PhotoImage(img4)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, text= "Focusing on Quadriceps", font= self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Focusing on Hamstring", font= self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text= "Focusing on Quadriceps", font= self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text= "Focusing on Hamstring", font= self.font_text).grid(row=4, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/shorts/9v3ySm-m8lI")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=FUwsp0OVyVM&pp=ygURcm9tYW5pYW4gZGVhZGxpZnQ%3D")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=swZQC689o9U&pp=ygUNbGVnIGV4dGVuc2lvbg%3D%3D")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=1Tq3QdYUuHs")

class Day2Advanced(Frame):
    def __init__(self, second_window):
        super().__init__()
        self.second_window = second_window
        self.window9 = None

        menubar = Menu(self.second_window.window2)
        self.second_window.window2.config(menu=menubar)

        workouts_menu = Menu(menubar)
        menubar.add_cascade(label="Upper1", menu=workouts_menu, command=self.open_upper_workout)
        menubar.add_cascade(label="Upper2", menu=workouts_menu, command=self.open_upper_workout2)
        menubar.add_cascade(label="Lower", menu=workouts_menu, command=self.open_lower_workout)
        menubar.add_cascade(label = "Back to Previous Page", menu = workouts_menu, command = self.back)

        self.open_upper_workout()

    def open_upper_workout(self):
        if self.window9:
            self.window9.destroy()
        self.window9 = Upper2Adv1(self.second_window.window2)

    def open_upper_workout2(self):
        if self.window9:
            self.window9.destroy()
        self.window9 = Upper2Adv2(self.second_window.window2)

    def open_lower_workout(self):
        if self.window9:
            self.window9.destroy()
        self.window9 = Lower2Adv(self.second_window.window2)

    def back(self):
        self.window9.destroy()
        self.second_window.window2.deiconify()

class Upper2Adv1(Page):
    def __init__(self, parent):
        super().__init__(parent, "Upper")
        self.geometry("1200x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Upper Workout For Advanced", font= self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text="Barbell Bench Press", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="4x6-8 reps", font= self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Incline Barbell Bench Press", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="3x6-8 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Military Press", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="3x6-8 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Cable Lateral Raise", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="3x to failure", font=self.font_text).grid(row=2, column=4, sticky=NSEW)

        img1 = Image.open("picture/barbellbench.png").resize((250, 250))
        img2 = Image.open("picture/inclinebarbellbench.png").resize((250, 250))
        img3 = Image.open("picture/militarypress.png").resize((250, 250))
        img4 = Image.open("picture/cablelateralraise.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, text= "Focusing on Chest", font= self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Focusing on Upper Chest", font= self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text= "Focusing on Front Shoulder", font= self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text= "Focusing on Middle Shoulder", font= self.font_text).grid(row=4, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=rT7DgCr-3pg")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=SrqOu55lrYU")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=2yjwXTZQDDI")
    
    def open_video4(self):
        webbrowser.open("https://www.youtube.com/shorts/EZSAOY7b3g4")

class Upper2Adv2(Page):
    def __init__(self, parent):
        super().__init__(parent, "Upper")
        self.geometry("1200x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Upper Workout For Advanced", font= self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text="Lat Pulldown", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="3x10-12", font= self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Deadlift", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="3x6-8 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Preacher Curl", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Close Grip Bench Press", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="3x6-8 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)

        img1 = Image.open("picture/latpulldown.png").resize((250, 250))
        img2 = Image.open("picture/deadlift.png").resize((250, 250))
        img3 = Image.open("picture/preachercurl.png").resize((250, 250))
        img4 = Image.open("picture/closegripbenchpress.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, text= "Focusing on Lat", font= self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Focusing on Back", font= self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text= "Focusing on Bicep", font= self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text= "Focusing on Tricep", font= self.font_text).grid(row=4, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=CAwf7n6Luuc&t=262s")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=XxWcirHIwVo")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=fIWP-FRFNU0")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=wxVRe9pmJdk&pp=ygUWY2xvc2UgZ3JpcCBiZW5jaCBwcmVzcw%3D%3D")

class Lower2Adv(Page):
    def __init__(self, parent):
        super().__init__(parent, "Lower")
        self.geometry("1500x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text= "Lower Workout For Advanced", font= self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text= "Barbell Squat", font= self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text= "4x6-8 reps", font= self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text= "Romanian Deadlift", font= self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text= "4x6-8 reps", font= self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text= "Leg Extension", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text= "3x8-12 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text= "Leg Curl", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text= "3x8-12 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)
        Label(frame2, text= "Calf Raise", font=self.font_text).grid(row=1, column=5, sticky=NSEW)
        Label(frame2, text= "3x8-12 reps", font=self.font_text).grid(row=2, column=5, sticky=NSEW)

        img1 = Image.open("picture/barbellsquat.png").resize((250, 250))
        img2 = Image.open("picture/romaniandeadlift.png").resize((400, 250))
        img3 = Image.open("picture/legextension.png").resize((250, 250))
        img4 = Image.open("picture/legcurl.png").resize((250, 250))
        img5 = Image.open("picture/calfraise.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4, self.photo5 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4), ImageTk.PhotoImage(img5)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, image=self.photo5).grid(row=3, column=5, sticky=NSEW)
        Label(frame2, text= "Focusing on Quadriceps", font= self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text= "Focusing on Hamstring", font= self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text= "Focusing on Quadriceps", font= self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text= "Focusing on Hamstring", font= self.font_text).grid(row=4, column=4, sticky=NSEW)
        Label(frame2, text= "Focusing on Calf", font= self.font_text).grid(row=4, column=5, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video5).grid(row=5, column=5, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/shorts/9v3ySm-m8lI")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=FUwsp0OVyVM&pp=ygURcm9tYW5pYW4gZGVhZGxpZnQ%3D")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=swZQC689o9U&pp=ygUNbGVnIGV4dGVuc2lvbg%3D%3D")
    
    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=1Tq3QdYUuHs")

    def open_video5(self):
        webbrowser.open("https://www.youtube.com/watch?v=d2GgSoHvIXo&pp=ygULY2FsZiByYWlzZXM%3D")

### 3 Day PPL ###

class Day3Beginner(Frame):
    def __init__(self, second_window):
        super().__init__()
        self.second_window = second_window
        self.window10 = None

        menubar = Menu(self.second_window.window2)
        self.second_window.window2.config(menu=menubar)

        workouts_menu = Menu(menubar)
        menubar.add_cascade(label="Push", menu=workouts_menu, command=self.open_fullbody_workout)
        menubar.add_cascade(label="Pull", menu=workouts_menu, command=self.open_fullbody_workout2)
        menubar.add_cascade(label="Leg", menu=workouts_menu, command=self.open_fullbody_workout3)
        menubar.add_cascade(label = "Back to Previous Page", menu = workouts_menu, command = self.back)

        self.open_fullbody_workout()

    def open_fullbody_workout(self):
        if self.window10:
            self.window10.destroy()
        self.window10 = Push3Begin(self.second_window.window2)

    def open_fullbody_workout2(self):
        if self.window10:
            self.window10.destroy()
        self.window10 = Pull3Begin(self.second_window.window2)

    def open_fullbody_workout3(self):
        if self.window10:
            self.window10.destroy()
        self.window10 = Leg3Begin(self.second_window.window2)

    def back(self):
        self.window10.destroy()
        self.second_window.window2.deiconify()

class Push3Begin(Page):
    def __init__(self, parent):
        super().__init__(parent, "Push")
        self.geometry("1580x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Push Workout For Beginner", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text="Push up", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Incline Push up", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Tricep Dips", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)
        Label(frame2, text="Dumbbell Shoulder Press", font=self.font_text).grid(row=1, column=5, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=5, sticky=NSEW)
        Label(frame2, text="Dumbbell Lateral Raise", font=self.font_text).grid(row=1, column=6, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=6, sticky=NSEW)
        Label(frame2, text="Dumbbell Rear Delt Fly", font=self.font_text).grid(row=1, column=7, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=7, sticky=NSEW)

        img1 = Image.open("picture/pushup.png").resize((250, 250))
        img2 = Image.open("picture/inclinepushup.png").resize((250, 250))
        img4 = Image.open("picture/tricepdips.png").resize((250, 250))
        img5 = Image.open("picture/shoulderpress.png").resize((250, 250))
        img6 = Image.open("picture/lateralraise.png").resize((250, 250))
        img7 = Image.open("picture/reardeltfly.png").resize((250, 250))
        self.photo1, self.photo2, self.photo4, self.photo5, self.photo6, self.photo7 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img4), ImageTk.PhotoImage(img5), ImageTk.PhotoImage(img6), ImageTk.PhotoImage(img7)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, image=self.photo5).grid(row=3, column=5, sticky=NSEW)
        Label(frame2, image=self.photo6).grid(row=3, column=6, sticky=NSEW)
        Label(frame2, image=self.photo7).grid(row=3, column=7, sticky=NSEW)
        Label(frame2, text="Focusing on Chest", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Upper Chest", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Tricep", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Front Shoulder", font=self.font_text).grid(row=4, column=5, sticky=NSEW)
        Label(frame2, text="Focusing on Middle Shoulder", font=self.font_text).grid(row=4, column=6, sticky=NSEW)
        Label(frame2, text="Focusing on Rear Shoulder", font=self.font_text).grid(row=4, column=7, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video5).grid(row=5, column=5, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video6).grid(row=5, column=6, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video7).grid(row=5, column=7, sticky=NSEW)

    def open_video1(self):  
        webbrowser.open("https://www.youtube.com/watch?v=IODxDxX7oi4")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=cfns5VDVVvk")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/shorts/Qz39qVt6NGA")

    def open_video5(self):
        webbrowser.open("https://www.youtube.com/watch?v=qEwKCR5JCog")

    def open_video6(self):
        webbrowser.open("https://www.youtube.com/watch?v=EA7u4Q_8HQ0&t=7s&pp=ygUNcmVhciBkZWx0IGZseQ%3D%3D")

    def open_video7(self):
        webbrowser.open("https://www.youtube.com/watch?v=EA7u4Q_8HQ0&t=7s&pp=ygUNcmVhciBkZWx0IGZseQ%3D%3D")

class Pull3Begin(Page):
    def __init__(self, parent):
        super().__init__(parent, "Pull")
        self.geometry("1350x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Pull Workout For Beginner", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text="Dumbbell Row", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Pull up", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Dumbbell Over Row", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Dumbbell Bicep Curl", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)
        Label(frame2, text="Dumbbell Hammer Curl", font=self.font_text).grid(row=1, column=5, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=5, sticky=NSEW)

        img1 = Image.open("picture/dumbbellrow.png").resize((250, 250))
        img2 = Image.open("picture/pullup.png").resize((250, 250))
        img3 = Image.open("picture/dumbbelloverrow.png").resize((250, 250))
        img4 = Image.open("picture/dumbbellcurl.png").resize((250, 250))
        img5 = Image.open("picture/hammercurl.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4, self.photo5 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4), ImageTk.PhotoImage(img5)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, image=self.photo5).grid(row=3, column=5, sticky=NSEW)
        Label(frame2, text="Focusing on Back", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Lat", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Back", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Bicep", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Bicep", font=self.font_text).grid(row=4, column=5, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video5).grid(row=5, column=5, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=pYcpY20QaE8")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=p40iUjf02j0&pp=ygUHcHVsbCB1cA%3D%3D")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=6TSP1TRMUzs")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=ykJmrZ5v0Oo")

    def open_video5(self):
        webbrowser.open("https://www.youtube.com/watch?v=TwD-YGVP4Bk&pp=ygULaGFtbWVyIGN1cms%3D")

class Leg3Begin(Page):
    def __init__(self, parent):
        super().__init__(parent, "Leg")
        self.geometry("1350x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Leg Workout For Beginner", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text="Goblet Squat", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Leg Lunge", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Sumo Squat", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Dumbbell Stiff Leg Deadlift", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)
        Label(frame2, text="Standing Calf Raise", font=self.font_text).grid(row=1, column=5, sticky=NSEW)
        Label(frame2, text="3x8-12 reps", font=self.font_text).grid(row=2, column=5, sticky=NSEW)

        img1 = Image.open("picture/gobletsquat.png").resize((250, 250))
        img2 = Image.open("picture/leglunge.png").resize((250, 250))
        img3 = Image.open("picture/sumosquat.png").resize((250, 250))
        img4 = Image.open("picture/stifflegdeadlift.png").resize((250, 250))
        img5 = Image.open("picture/calfraise.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4, self.photo5 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4), ImageTk.PhotoImage(img5)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, image=self.photo5).grid(row=3, column=5, sticky=NSEW)
        Label(frame2, text="Focusing on Quadriceps", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Quadriceps", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Quadriceps", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Hamstring", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Calf", font=self.font_text).grid(row=4, column=5, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video5).grid(row=5, column=5, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=MeIiIdhvXT4")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=3frV3RnPfOY")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=kjlfpqXnyL8&pp=ygUKc3VtbyBzcXVhdA%3D%3D")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=cYKYGwcg0U8&pp=ygUSc3RpZmYgbGVnIGRlYWRsaWZ0")

    def open_video5(self):
        webbrowser.open("https://www.youtube.com/watch?v=d2GgSoHvIXo&pp=ygULY2FsZiByYWlzZXM%3D")

class Day3Intermediate(Frame):
    def __init__(self, second_window):
        super().__init__()
        self.second_window = second_window
        self.window11 = None

        menubar = Menu(self.second_window.window2)
        self.second_window.window2.config(menu=menubar)

        workouts_menu = Menu(menubar)
        menubar.add_cascade(label="Push", menu=workouts_menu, command=self.open_push_workout)
        menubar.add_cascade(label="Pull", menu=workouts_menu, command=self.open_pull_workout)
        menubar.add_cascade(label="Leg", menu=workouts_menu, command=self.open_leg_workout)
        menubar.add_cascade(label = "Back to Previous Page", menu = workouts_menu, command = self.back)

        self.open_push_workout()

    def open_push_workout(self):
        if self.window11:
            self.window11.destroy()
        self.window11 = Push3Inter(self.second_window.window2)

    def open_pull_workout(self):
        if self.window11:
            self.window11.destroy()
        self.window11 = Pull3Inter(self.second_window.window2)

    def open_leg_workout(self):
        if self.window11:
            self.window11.destroy()
        self.window11 = Leg3Inter(self.second_window.window2)

    def back(self):
        self.window11.destroy()
        self.second_window.window2.deiconify()

class Push3Inter(Page):
    def __init__(self, parent):
        super().__init__(parent, "Push")
        self.geometry("1580x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Push Workout For Intermediate", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text="Dumbbell Bench Press", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="4x8-10 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Incline Dumbbell Bench Press", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="4x8-10 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Tricep Rope Pushdown", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="4x8-10 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)
        Label(frame2, text="Dumbbell Shoulder Press", font=self.font_text).grid(row=1, column=5, sticky=NSEW)
        Label(frame2, text="4x8-10 reps", font=self.font_text).grid(row=2, column=5, sticky=NSEW)
        Label(frame2, text="Dumbbell Lateral Raise", font=self.font_text).grid(row=1, column=6, sticky=NSEW)
        Label(frame2, text="4x8-10 reps", font=self.font_text).grid(row=2, column=6, sticky=NSEW)
        Label(frame2, text="Tricep Pushdown", font=self.font_text).grid(row=1, column=7, sticky=NSEW)
        Label(frame2, text="4x8-10 reps", font=self.font_text).grid(row=2, column=7, sticky=NSEW)

        img1 = Image.open("picture/dumbbellbenchpress.png").resize((250, 250))
        img2 = Image.open("picture/inclinedumbbellbench.png").resize((250, 250))
        img4 = Image.open("picture/tricepropepushdown.png").resize((250, 250))
        img5 = Image.open("picture/shoulderpress.png").resize((250, 250))
        img6 = Image.open("picture/lateralraise.png").resize((250, 250))
        img7 = Image.open("picture/triceppushdown.png").resize((250, 250))
        self.photo1, self.photo2, self.photo4, self.photo5, self.photo6, self.photo7 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img4), ImageTk.PhotoImage(img5), ImageTk.PhotoImage(img6), ImageTk.PhotoImage(img7)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, image=self.photo5).grid(row=3, column=5, sticky=NSEW)
        Label(frame2, image=self.photo6).grid(row=3, column=6, sticky=NSEW)
        Label(frame2, image=self.photo7).grid(row=3, column=7, sticky=NSEW)
        Label(frame2, text="Focusing on Chest", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Upper Chest", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Tricep", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Front Shoulder", font=self.font_text).grid(row=4, column=5, sticky=NSEW)
        Label(frame2, text="Focusing on Middle Shoulder", font=self.font_text).grid(row=4, column=6, sticky=NSEW)
        Label(frame2, text="Focusing on Tricep", font=self.font_text).grid(row=4, column=7, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video5).grid(row=5, column=5, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video6).grid(row=5, column=6, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video7).grid(row=5, column=7, sticky=NSEW)
        
    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=QsYre__-aro")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=8iPEnn-ltC8")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=-xa-6cQaZKY")

    def open_video5(self):
        webbrowser.open("https://www.youtube.com/watch?v=qEwKCR5JCog")

    def open_video6(self):
        webbrowser.open("https://www.youtube.com/shorts/JIhbYYA1Q90")

    def open_video7(self):
        webbrowser.open("https://www.youtube.com/shorts/WjLJ7zIppXQ")

class Pull3Inter(Page):
    def __init__(self, parent):
        super().__init__(parent, "Pull")
        self.geometry("1350x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Pull Workout For Intermediate", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text="Lat Pulldown", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="4x8-10 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Cable Row", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="4x8-10 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Close Grip Lat Pulldown", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="4x8-10 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Cable Bicep Curl", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="4x8-10 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)
        Label(frame2, text="Dumbbell Hammer Curl", font=self.font_text).grid(row=1, column=5, sticky=NSEW)
        Label(frame2, text="4x8-10 reps", font=self.font_text).grid(row=2, column=5, sticky=NSEW)

        img1 = Image.open("picture/latpulldown.png").resize((250, 250))
        img2 = Image.open("picture/seatedcablerow.png").resize((250, 250))
        img3 = Image.open("picture/closegrippulldown.png").resize((250, 250))
        img4 = Image.open("picture/cablecurl.png").resize((250, 250))
        img5 = Image.open("picture/hammercurl.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4, self.photo5 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4), ImageTk.PhotoImage(img5)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, image=self.photo5).grid(row=3, column=5, sticky=NSEW)
        Label(frame2, text="Focusing on Lat", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Back", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Lat", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Bicep", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Bicep", font=self.font_text).grid(row=4, column=5, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video5).grid(row=5, column=5, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=CAwf7n6Luuc&t=262s")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/shorts/fPbfYDgzIgA")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=8hzVLzu-RJk&pp=ygUXY2xvc2UgZ3JpcCBsYXQgcHVsbGRvd24%3D")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=NFzTWp2qpiE")

    def open_video5(self):
        webbrowser.open("https://www.youtube.com/watch?v=TwD-YGVP4Bk&pp=ygULaGFtbWVyIGN1cms%3D")

class Leg3Inter(Page):
    def __init__(self, parent):
        super().__init__(parent, "Leg")
        self.geometry("1450x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Leg Workout For Intermediate", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text="Barbell Squat", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="4x8-10 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Leg Press", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="4x8-10 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Leg Extension", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="4x8-10 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Leg Curl", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="4x8-10 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)
        Label(frame2, text="Standing Calf Raise", font=self.font_text).grid(row=1, column=5, sticky=NSEW)
        Label(frame2, text="4x8-10 reps", font=self.font_text).grid(row=2, column=5, sticky=NSEW)

        img1 = Image.open("picture/barbellsquat.png").resize((250, 250))
        img2 = Image.open("picture/legpress.png").resize((250, 250))
        img3 = Image.open("picture/legextension.png").resize((250, 250))
        img4 = Image.open("picture/legcurl.png").resize((250, 250))
        img5 = Image.open("picture/calfraise.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4, self.photo5 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4), ImageTk.PhotoImage(img5)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, image=self.photo5).grid(row=3, column=5, sticky=NSEW)
        Label(frame2, text="Focusing on Quadriceps", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Quadriceps", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Quadriceps", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Hamstring", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Calf", font=self.font_text).grid(row=4, column=5, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video5).grid(row=5, column=5, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/shorts/9v3ySm-m8lI")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/shorts/wa9UCsNWVo0")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=swZQC689o9U&pp=ygUNbGVnIGV4dGVuc2lvbg%3D%3D")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=1Tq3QdYUuHs")

    def open_video5(self):
        webbrowser.open("https://www.youtube.com/watch?v=d2GgSoHvIXo&pp=ygULY2FsZiByYWlzZXM%3D")

class Day3Advanced(Frame):
    def __init__(self, second_window):
        super().__init__()
        self.second_window = second_window
        self.window12 = None

        menubar = Menu(self.second_window.window2)
        self.second_window.window2.config(menu=menubar)

        workouts_menu = Menu(menubar)
        menubar.add_cascade(label="Push", menu=workouts_menu, command=self.open_push_workout)
        menubar.add_cascade(label="Pull", menu=workouts_menu, command=self.open_pull_workout)
        menubar.add_cascade(label="Leg", menu=workouts_menu, command=self.open_leg_workout)
        menubar.add_cascade(label = "Back to Previous Page", menu = workouts_menu, command = self.back)

        self.open_push_workout()

    def open_push_workout(self):
        if self.window12:
            self.window12.destroy()
        self.window12 = Push3Adv(self.second_window.window2)

    def open_pull_workout(self):
        if self.window12:
            self.window12.destroy()
        self.window12 = Pull3Adv(self.second_window.window2)

    def open_leg_workout(self):
        if self.window12:
            self.window12.destroy()
        self.window12 = Leg3Adv(self.second_window.window2)

    def back(self):
        self.window12.destroy()
        self.second_window.window2.deiconify()

class Push3Adv(Page):
    def __init__(self, parent):
        super().__init__(parent, "Push")
        self.geometry("1580x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Push Workout For Advanced", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text="Barbell Bench Press", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="4x6-8 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Incline Barbell Bench Press", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="4x6-8 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Dumbbell Shoulder Press", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="4x6-8 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Cable Lateral Raise", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="4x12-15 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)
        Label(frame2, text="Tricep Rope Pushdown", font=self.font_text).grid(row=1, column=5, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=5, sticky=NSEW)
        Label(frame2, text="Tricep Pushdown", font=self.font_text).grid(row=1, column=6, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=6, sticky=NSEW)

        img1 = Image.open("picture/barbellbench.png").resize((250, 250))
        img2 = Image.open("picture/inclinebarbellbench.png").resize((250, 250))
        img3 = Image.open("picture/shoulderpress.png").resize((250, 250))
        img4 = Image.open("picture/cablelateralraise.png").resize((250, 250))
        img5 = Image.open("picture/tricepropepushdown.png").resize((250, 250))
        img6 = Image.open("picture/triceppushdown.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4, self.photo5, self.photo6 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4), ImageTk.PhotoImage(img5), ImageTk.PhotoImage(img6)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, image=self.photo5).grid(row=3, column=5, sticky=NSEW)
        Label(frame2, image=self.photo6).grid(row=3, column=6, sticky=NSEW)
        Label(frame2, text="Focusing on Chest", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Upper Chest", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Front Shoulder", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Middle Shoulder", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Tricep", font=self.font_text).grid(row=4, column=5, sticky=NSEW)
        Label(frame2, text="Focusing on Tricep", font=self.font_text).grid(row=4, column=6, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)    
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video5).grid(row=5, column=5, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video6).grid(row=5, column=6, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=rT7DgCr-3pg")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=SrqOu55lrYU")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=qEwKCR5JCog")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/shorts/EZSAOY7b3g4")

    def open_video5(self):
        webbrowser.open("https://www.youtube.com/watch?v=-xa-6cQaZKY")

    def open_video6(self):
        webbrowser.open("https://www.youtube.com/shorts/WjLJ7zIppXQ")

class Pull3Adv(Page):
    def __init__(self, parent):
        super().__init__(parent, "Pull")
        self.geometry("1580x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Pull Workout For Advanced", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text="Weighted Pull Up", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="4xto failure reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Lat Pulldown", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="T-Bar Row", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="4x6-8 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Close Grip Lat Pulldown", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)
        Label(frame2, text="Cable Bicep Curl", font=self.font_text).grid(row=1, column=5, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=5, sticky=NSEW)
        Label(frame2, text="Dumbbell Hammer Curl", font=self.font_text).grid(row=1, column=6, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=6, sticky=NSEW)

        img1 = Image.open("picture/weightedpullup.png").resize((250, 250))
        img2 = Image.open("picture/latpulldown.png").resize((250, 250))
        img3 = Image.open("picture/tbarrow.png").resize((250, 250))
        img4 = Image.open("picture/closegrippulldown.png").resize((250, 250))
        img5 = Image.open("picture/cablecurl.png").resize((250, 250))
        img6 = Image.open("picture/hammercurl.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4, self.photo5, self.photo6 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4), ImageTk.PhotoImage(img5), ImageTk.PhotoImage(img6)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, image=self.photo5).grid(row=3, column=5, sticky=NSEW)
        Label(frame2, image=self.photo6).grid(row=3, column=6, sticky=NSEW)
        Label(frame2, text="Focusing on Lat", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Lat", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Middle Back", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Upper Back", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Bicep", font=self.font_text).grid(row=4, column=5, sticky=NSEW)
        Label(frame2, text="Focusing on Bicep", font=self.font_text).grid(row=4, column=6, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video5).grid(row=5, column=5, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video6).grid(row=5, column=6, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=C0I0gb76yaA&pp=ygUQd2VpZ2h0ZWQgcHVsbCB1cA%3D%3D")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=CAwf7n6Luuc&t=262s")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/shorts/MIulz5576AY")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=8hzVLzu-RJk&pp=ygUXY2xvc2UgZ3JpcCBsYXQgcHVsbGRvd24%3D")

    def open_video5(self):
        webbrowser.open("https://www.youtube.com/watch?v=NFzTWp2qpiE")

    def open_video6(self):
        webbrowser.open("https://www.youtube.com/watch?v=TwD-YGVP4Bk&pp=ygULaGFtbWVyIGN1cms%3D")

class Leg3Adv(Page):
    def __init__(self, parent):
        super().__init__(parent, "Leg")
        self.geometry("1580x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Leg Workout For Advanced", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text="Barbell Squat", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="4x6-8 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Leg Press", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="4x6-8 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Leg Extension", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="4x6-8 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Leg Curl", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="4x6-8 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)
        Label(frame2, text="Stiffleg Deadlift", font=self.font_text).grid(row=1, column=5, sticky=NSEW)
        Label(frame2, text="4x6-8 reps", font=self.font_text).grid(row=2, column=5, sticky=NSEW)
        Label(frame2, text="Standing Calf Raise", font=self.font_text).grid(row=1, column=6, sticky=NSEW)
        Label(frame2, text="4x6-8 reps", font=self.font_text).grid(row=2, column=6, sticky=NSEW)

        img1 = Image.open("picture/barbellsquat.png").resize((250, 250))
        img2 = Image.open("picture/legpress.png").resize((250, 250))
        img3 = Image.open("picture/legextension.png").resize((250, 250))
        img4 = Image.open("picture/legcurl.png").resize((250, 250))
        img5 = Image.open("picture/barbellstifflegdeadlift.png").resize((250, 250))
        img6 = Image.open("picture/calfraise.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4, self.photo5, self.photo6 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4), ImageTk.PhotoImage(img5), ImageTk.PhotoImage(img6)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, image=self.photo5).grid(row=3, column=5, sticky=NSEW)
        Label(frame2, image=self.photo6).grid(row=3, column=6, sticky=NSEW)
        Label(frame2, text="Focusing on Quadriceps", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Quadriceps", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Quadriceps", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Hamstring", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Hamstring", font=self.font_text).grid(row=4, column=5, sticky=NSEW)
        Label(frame2, text="Focusing on Calf", font=self.font_text).grid(row=4, column=6, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video5).grid(row=5, column=5, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video6).grid(row=5, column=6, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/shorts/9v3ySm-m8lI")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/shorts/wa9UCsNWVo0")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=swZQC689o9U&pp=ygUNbGVnIGV4dGVuc2lvbg%3D%3D")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=1Tq3QdYUuHs")

    def open_video5(self):
        webbrowser.open("https://www.youtube.com/watch?v=CN_7cz3P-1U&pp=ygUSc3RpZmYgbGVnIGRlYWRsaWZ0")

    def open_video6(self):
        webbrowser.open("https://www.youtube.com/watch?v=d2GgSoHvIXo&pp=ygULY2FsZiByYWlzZXM%3D")

### 4 Days Workout ###

class Day4Beginner(Frame):
    def __init__(self, second_window):
        super().__init__()
        self.second_window = second_window
        self.window13 = None

        menubar = Menu(self.second_window.window2)
        self.second_window.window2.config(menu=menubar)

        workouts_menu = Menu(menubar)
        menubar.add_cascade(label="Push", menu=workouts_menu, command=self.open_push_workout)
        menubar.add_cascade(label="Pull", menu=workouts_menu, command=self.open_pull_workout)
        menubar.add_cascade(label="Leg", menu=workouts_menu, command=self.open_leg_workout)
        menubar.add_cascade(label="Cardio", menu=workouts_menu, command=self.open_cardio)
        menubar.add_cascade(label = "Back to Previous Page", menu = workouts_menu, command = self.back)

        self.open_push_workout()

    def open_push_workout(self):
        if self.window13:
            self.window13.destroy()
        self.window13 = Push3Begin(self.second_window.window2)

    def open_pull_workout(self):
        if self.window13:
            self.window13.destroy()
        self.window13 = Pull3Begin(self.second_window.window2)

    def open_leg_workout(self):
        if self.window13:
            self.window13.destroy()
        self.window13 = Leg3Begin(self.second_window.window2)

    def open_cardio(self):
        if self.window13:
            self.window13.destroy()
        self.window13 = Cardio4Begin(self.second_window.window2)

    def back(self):
        self.window13.destroy()
        self.second_window.window2.deiconify()

class Cardio4Begin(Page):
    def __init__(self, parent):
        super().__init__(parent, "Cardio")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Cardio Workout For Beginner", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack()
        Label(frame2, text="Treadmill", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="30 minutes", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Bicycle", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="30 minutes", font=self.font_text).grid(row=2, column=2, sticky=NSEW)

        img1 = Image.open("picture/treadmill.png").resize((250, 250))
        img2 = Image.open("picture/bicycle.png").resize((250, 250))
        self.photo1, self.photo2 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, text="Cardio to lose some fat", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Cardio to lose some fat", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=8i3Vrd95o2k&pp=ygUJdHJlYWRtaWxs")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=ewrf_rCHUdA&pp=ygUOYmljeWNsZSBjYXJkaW8%3D")

class Day4Intermediate(Frame):
    def __init__(self, second_window):
        super().__init__()
        self.second_window = second_window
        self.window14 = None

        menubar = Menu(self.second_window.window2)
        self.second_window.window2.config(menu=menubar)

        workouts_menu = Menu(menubar)
        menubar.add_cascade(label="Push", menu=workouts_menu, command=self.open_push_workout)
        menubar.add_cascade(label="Pull", menu=workouts_menu, command=self.open_pull_workout)
        menubar.add_cascade(label="Leg", menu=workouts_menu, command=self.open_leg_workout)
        menubar.add_cascade(label="Cardio", menu=workouts_menu, command=self.open_cardio)
        menubar.add_cascade(label = "Back to Previous Page", menu = workouts_menu, command = self.back)

        self.open_push_workout()
    
    def open_push_workout(self):
        if self.window14:
            self.window14.destroy()
        self.window14 = Push3Inter(self.second_window.window2)

    def open_pull_workout(self):
        if self.window14:
            self.window14.destroy()
        self.window14 = Pull3Inter(self.second_window.window2)

    def open_leg_workout(self):
        if self.window14:
            self.window14.destroy()
        self.window14 = Leg3Inter(self.second_window.window2)

    def open_cardio(self):
        if self.window14:
            self.window14.destroy()
        self.window14 = Cardio4Begin(self.second_window.window2)

    def back(self):
        self.window14.destroy()
        self.second_window.window2.deiconify()

class Day4Advanced(Frame):
    def __init__(self, second_window):
        super().__init__()
        self.second_window = second_window
        self.window15 = None

        menubar = Menu(self.second_window.window2)
        self.second_window.window2.config(menu=menubar)

        workouts_menu = Menu(menubar)
        menubar.add_cascade(label="Chest and Back", menu=workouts_menu, command=self.open_chestandback_workout)
        menubar.add_cascade(label="Arms and Shoulders", menu=workouts_menu, command=self.open_armsandshoulders_workout)
        menubar.add_cascade(label="Leg", menu=workouts_menu, command=self.open_leg_workout)
        menubar.add_cascade(label="Cardio", menu=workouts_menu, command=self.open_cardio)
        menubar.add_cascade(label = "Back to Previous Page", menu = workouts_menu, command = self.back)

        self.open_chestandback_workout()

    def open_chestandback_workout(self):
        if self.window15:
            self.window15.destroy()
        self.window15 = ChestBack4Adv(self.second_window.window2)

    def open_armsandshoulders_workout(self):
        if self.window15:
            self.window15.destroy()
        self.window15 = ArmsShoulders4Adv(self.second_window.window2)

    def open_leg_workout(self):
        if self.window15:
            self.window15.destroy()
        self.window15 = Leg3Adv(self.second_window.window2)

    def open_cardio(self):
        if self.window15:
            self.window15.destroy()
        self.window15 = Cardio4Begin(self.second_window.window2)

    def back(self):
        self.window15.destroy()
        self.second_window.window2.deiconify()

class ChestBack4Adv(Page):
    def __init__(self, parent):
        super().__init__(parent, "Chest and Back")
        self.geometry("1580x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Chest and Back Workout For Advanced", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack()
        Label(frame2, text="Barbell Bench Press", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="4x6-8 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Incline Barbell Bench Press", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="4x6-8 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Cable Fly", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Lat Pulldown", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)
        Label(frame2, text="T-Bar Row", font=self.font_text).grid(row=1, column=5, sticky=NSEW)
        Label(frame2, text="4x6-8 reps", font=self.font_text).grid(row=2, column=5, sticky=NSEW)
        Label(frame2, text="Close Grip Lat Pulldown", font=self.font_text).grid(row=1, column=6, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=6, sticky=NSEW)

        img1 = Image.open("picture/barbellbench.png").resize((250, 250))
        img2 = Image.open("picture/inclinebarbellbench.png").resize((250, 250))
        img3 = Image.open("picture/cablefly.png").resize((250, 250))
        img4 = Image.open("picture/latpulldown.png").resize((250, 250))
        img5 = Image.open("picture/tbarrow.png").resize((250, 250))
        img6 = Image.open("picture/closegrippulldown.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4, self.photo5, self.photo6 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4), ImageTk.PhotoImage(img5), ImageTk.PhotoImage(img6)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, image=self.photo5).grid(row=3, column=5, sticky=NSEW)
        Label(frame2, image=self.photo6).grid(row=3, column=6, sticky=NSEW)
        Label(frame2, text="Focusing on Middle Chest", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Upper Chest", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Lower Chest", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Lat", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Middle Back", font=self.font_text).grid(row=4, column=5, sticky=NSEW)
        Label(frame2, text="Focusing on Upper Back", font=self.font_text).grid(row=4, column=6, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video5).grid(row=5, column=5, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video6).grid(row=5, column=6, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=BYKScL2sgCs")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=0GIgVpY2hAE")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=4Jz9v8YjqiI")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=CAwf7n6Luuc&t=262s")

    def open_video5(self):
        webbrowser.open("https://www.youtube.com/shorts/MIulz5576AY")

    def open_video6(self):
        webbrowser.open("https://www.youtube.com/watch?v=8hzVLzu-RJk&pp=ygUXY2xvc2UgZ3JpcCBsYXQgcHVsbGRvd24%3D")

class ArmsShoulders4Adv(Page):
    def __init__(self, parent):
        super().__init__(parent, "Arms and Shoulders")
        self.geometry("1710x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Arms and Shoulders Workout For Advanced", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack(padx=10, pady=20)
        Label(frame2, text="Barbell Shoulder Press", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="4x6-8 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Cable Lateral Raise", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Rear Delt Fly", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Cable Curl", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="4x6-8 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)
        Label(frame2, text="Close Grip Bench Press", font=self.font_text).grid(row=1, column=5, sticky=NSEW)
        Label(frame2, text="4x6-8 reps", font=self.font_text).grid(row=2, column=5, sticky=NSEW)
        Label(frame2, text="Tricep Rope Pushdown", font=self.font_text).grid(row=1, column=6, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=6, sticky=NSEW)
        Label(frame2, text="Dumbbell Hammer Curl", font=self.font_text).grid(row=1, column=7, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=7, sticky=NSEW)

        img1 = Image.open("picture/barbellshoulderpress.png").resize((250, 250))
        img2 = Image.open("picture/cablelateralraise.png").resize((250, 250))
        img3 = Image.open("picture/reardeltfly.png").resize((250, 250))
        img4 = Image.open("picture/cablecurl.png").resize((250, 250))
        img5 = Image.open("picture/closegripbenchpress.png").resize((250, 250))
        img6 = Image.open("picture/tricepropepushdown.png").resize((250, 250))
        img7 = Image.open("picture/hammercurl.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4, self.photo5, self.photo6, self.photo7 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4), ImageTk.PhotoImage(img5), ImageTk.PhotoImage(img6), ImageTk.PhotoImage(img7)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, image=self.photo5).grid(row=3, column=5, sticky=NSEW)
        Label(frame2, image=self.photo6).grid(row=3, column=6, sticky=NSEW)
        Label(frame2, image=self.photo7).grid(row=3, column=7, sticky=NSEW)
        Label(frame2, text="Focusing on Front Delt", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Side Delt", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Rear Delt", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Bicep", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Tricep", font=self.font_text).grid(row=4, column=5, sticky=NSEW)
        Label(frame2, text="Focusing on Tricep", font=self.font_text).grid(row=4, column=6, sticky=NSEW)
        Label(frame2, text="Focusing on Bicep", font=self.font_text).grid(row=4, column=7, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video5).grid(row=5, column=5, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video6).grid(row=5, column=6, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video7).grid(row=5, column=7, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=oBGeXxnigsQ&pp=ygUWYmFyYmVsbCBzaG91bGRlciBwcmVzcw%3D%3D")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/shorts/1AmmsXlf8MU")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=EA7u4Q_8HQ0&t=8s&pp=ygUNcmVhciBkZWx0IGZseQ%3D%3D")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=kwG2ipFRgfo&pp=ygUMYmFyYmVsbCBjdXJs")

    def open_video5(self):
        webbrowser.open("https://www.youtube.com/watch?v=nEF0bv2FW94&pp=ygUWY2xvc2UgZ3JpcCBiZW5jaCBwcmVzcw%3D%3D")

    def open_video6(self):
        webbrowser.open("https://www.youtube.com/watch?v=-xa-6cQaZKY&pp=ygUUdHJpY2VwIHJvcGUgcHVzaGRvd24%3D")

    def open_video7(self):
        webbrowser.open("https://www.youtube.com/watch?v=TwD-YGVP4Bk&t=1s&pp=ygULaGFtbWVyIGN1cmw%3D")

### 5 Days Workout ###

class Day5Beginner(Frame):
    def __init__(self, second_window):
        super().__init__()
        self.second_window = second_window
        self.window16 = None

        menubar = Menu(self.second_window.window2)
        self.second_window.window2.config(menu=menubar)

        workouts_menu = Menu(menubar) 
        menubar.add_cascade(label="Chest", menu=workouts_menu, command=self.open_chest_workout)
        menubar.add_cascade(label="Shoulders", menu=workouts_menu, command=self.open_shoulders_workout)
        menubar.add_cascade(label="Back", menu=workouts_menu, command=self.open_back_workout)
        menubar.add_cascade(label="Arms", menu=workouts_menu, command=self.open_arms_workout)
        menubar.add_cascade(label="Leg", menu=workouts_menu, command=self.open_leg_workout)
        menubar.add_cascade(label="Back", menu=workouts_menu, command=self.back)

        self.open_chest_workout()

    def open_chest_workout(self):
        if self.window16:
            self.window16.destroy()
        self.window16 = Chest5Begin(self.second_window.window2)

    def open_shoulders_workout(self):
        if self.window16:
            self.window16.destroy()
        self.window16 = Shoulders5Begin(self.second_window.window2)

    def open_back_workout(self):
        if self.window16:
            self.window16.destroy()
        self.window16 = Back5Begin(self.second_window.window2)
    
    def open_arms_workout(self):
        if self.window16:
            self.window16.destroy()
        self.window16 = Arms5Begin(self.second_window.window2)

    def open_leg_workout(self):
        if self.window16:
            self.window16.destroy()
        self.window16 = Leg5Begin(self.second_window.window2)

    def back(self):
        self.window16.destroy()
        self.second_window.window2.deiconify()

class Chest5Begin(Page):
    def __init__(self, parent):
        super().__init__(parent, "Chest")
        self.geometry("1300x450")

        frame1 = Frame(self)
        frame1.pack(padx=10, pady=20)
        Label(frame1, text="Chest Workout For Beginner", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack()
        Label(frame2, text="Push up", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Incline Push up", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Decline Pushup", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Dumbbell Fly", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)

        img1 = Image.open("picture/pushup.png").resize((300, 250))
        img2 = Image.open("picture/inclinepushup.png").resize((300, 250))
        img3 = Image.open("picture/declinepushup.png").resize((300, 250))
        img4 = Image.open("picture/dumbbellfly.png").resize((300, 250))
        self.photo1, self.photo2, self.photo3, self.photo4 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Middle Chest", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Upper Chest", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Lower Chest", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Middle Chest", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=IODxDxX7oi4")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=cfns5VDVVvk")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/shorts/dcV-ATSeryA")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=QENKPHhQVi4&pp=ygUMZHVtYmJlbGwgZmx5")

class Shoulders5Begin(Page):
    def __init__(self, parent):
        super().__init__(parent, "Shoulders")
        self.geometry("1300x450")

        frame1 = Frame(self)
        frame1.pack(padx=10, pady=20)
        Label(frame1, text="Shoulders Workout For Beginner", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack()
        Label(frame2, text="Dumbbell Shoulder Press", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Dumbbell Lateral Raise", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Dumbbell Front Raise", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Dumbbell Rear Delt Fly", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)

        img1 = Image.open("picture/shoulderpress.png").resize((300, 250))
        img2 = Image.open("picture/lateralraise.png").resize((300, 250))
        img3 = Image.open("picture/frontraise.png").resize((300, 250))
        img4 = Image.open("picture/reardeltfly.png").resize((300, 250))
        self.photo1, self.photo2, self.photo3, self.photo4 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Front Delt", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Side Delt", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Front Delt", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Rear Delt", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=qEwKCR5JCog")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/shorts/xyK8UiC-BUw")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=-t7fuZ0KhDA&t=11s&pp=ygULZnJvbnQgcmFpc2U%3D")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=EA7u4Q_8HQ0&t=7s&pp=ygUNcmVhciBkZWx0IGZseQ%3D%3D")

class Back5Begin(Page):
    def __init__(self, parent):
        super().__init__(parent, "Back")

        frame1 = Frame(self)
        frame1.pack(padx=10, pady=20)  
        Label(frame1, text="Back Workout For Beginner", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack()
        Label(frame2, text="Dumbbell Row", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Dumbbel Overrow", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Dumbbell Pullover", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)

        img1 = Image.open("picture/dumbbellrow.png").resize((300, 250))
        img2 = Image.open("picture/dumbbelloverrow.png").resize((300, 250))
        img3 = Image.open("picture/pullover.png").resize((300, 250))
        self.photo1, self.photo2, self.photo3 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Middle Back", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Upper Back", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Lower Back", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=pYcpY20QaE")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=6TSP1TRMUzs")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=FK4rHfWKEac&pp=ygURZHVtYmJlbGwgcHVsbG92ZXI%3D")

class Arms5Begin(Page):
    def __init__(self, parent):
        super().__init__(parent, "Arms")
        self.geometry("1300x450")

        frame1 = Frame(self)
        frame1.pack(padx=10, pady=20)
        Label(frame1, text="Arms Workout For Beginner", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack()
        Label(frame2, text="Dumbbell Curl", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Dumbbell Hammer Curl", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Dumbbell Tricep Extension", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Dumbbell Skull Crusher", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)

        img1 = Image.open("picture/dumbbellcurl.png").resize((300, 250))
        img2 = Image.open("picture/hammercurl.png").resize((300, 250))
        img3 = Image.open("picture/overheadtricepextension.png").resize((300, 250))
        img4 = Image.open("picture/skullcrusher.png").resize((300, 250))
        self.photo1, self.photo2, self.photo3, self.photo4 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Bicep", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Bicep", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Tricep", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Tricep", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=ykJmrZ5v0Oo")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=TwD-YGVP4Bk&pp=ygULaGFtbWVyIGN1cms%3D")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=-Vyt2QdsR7E")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/shorts/D1y1-sXZDA0")

class Leg5Begin(Page):
    def __init__(self, parent):
        super().__init__(parent, "Leg")
        self.geometry("1300x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Leg Workout For Beginner", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack()
        Label(frame2, text="Goblet Squat", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Leg Lunge", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Calf Raise", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Stiff Leg Deadlift", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="3x12 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)

        img1 = Image.open("picture/gobletsquat.png").resize((300, 250))
        img2 = Image.open("picture/leglunge.png").resize((300, 250))
        img3 = Image.open("picture/calfraise.png").resize((300, 250))
        img4 = Image.open("picture/stifflegdeadlift.png").resize((300, 250))
        self.photo1, self.photo2, self.photo3, self.photo4 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Quads", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Quads", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Calves", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Hamstring", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=MeIiIdhvXT4")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=3frV3RnPfOY")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=d2GgSoHvIXo&pp=ygULY2FsZiByYWlzZXM%3D")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=cYKYGwcg0U8&pp=ygUSc3RpZmYgbGVnIGRlYWRsaWZ0")

class Day5Intermediate(Frame):
    def __init__(self, second_window):
        super().__init__()
        self.second_window = second_window
        self.window17 = None

        menubar = Menu(self.second_window.window2)
        self.second_window.window2.config(menu=menubar)

        workotus_menu = Menu(menubar)
        menubar.add_cascade(label="Chest", menu=workotus_menu, command=self.open_chest_workout)
        menubar.add_cascade(label="Shoulders", menu=workotus_menu, command=self.open_shoulders_workout)
        menubar.add_cascade(label="Back", menu=workotus_menu, command=self.open_back_workout)
        menubar.add_cascade(label="Arms", menu=workotus_menu, command=self.open_arms_workout)
        menubar.add_cascade(label="Leg", menu=workotus_menu, command=self.open_leg_workout)
        menubar.add_cascade(label="Back", menu=workotus_menu, command=self.back)

        self.open_chest_workout()

    def open_chest_workout(self):
        if self.window17:
            self.window17.destroy()
        self.window17 = Chest5Inter(self.second_window.window2)

    def open_shoulders_workout(self):
        if self.window17:
            self.window17.destroy()
        self.window17 = Shoulders5Inter(self.second_window.window2)

    def open_back_workout(self):
        if self.window17:
            self.window17.destroy()
        self.window17 = Back5Inter(self.second_window.window2)

    def open_arms_workout(self):
        if self.window17:
            self.window17.destroy()
        self.window17 = Arms5Inter(self.second_window.window2)

    def open_leg_workout(self):
        if self.window17:
            self.window17.destroy()
        self.window17 = Leg3Inter(self.second_window.window2)

    def back(self):
        self.window17.destroy()
        self.second_window.window2.deiconify()

class Chest5Inter(Page):
    def __init__(self, parent):
        super().__init__(parent, "Chest")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Chest Workout For Intermediate", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack()
        Label(frame2, text="Dumbbell Bench Press", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="5x10 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Incline Dumbbell Bench Press", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="5x10 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Cable Fly", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="5x10 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
    
        img1 = Image.open("picture/dumbbellbenchpress.png").resize((300, 250))
        img2 = Image.open("picture/inclinedumbbellbench.png").resize((300, 250))
        img3 = Image.open("picture/cablefly.png").resize((300, 250))
        self.photo1, self.photo2, self.photo3 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Middle Chest", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Upper Chest", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Lower Chest", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=QsYre__-aro")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=8iPEnn-ltC8")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=4Jz9v8YjqiI")

class Back5Inter(Page):
    def __init__(self, parent):
        super().__init__(parent, "Back")
        self.geometry("1300x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Back Workout For Intermediate", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack()
        Label(frame2, text="Pull Up", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="3x10 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Lat Pulldown", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="3x10 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Seated Cable Row", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="3x10 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Bent Overrow", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="3x10 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)

        img1 = Image.open("picture/pullup.png").resize((300, 250))
        img2 = Image.open("picture/latpulldown.png").resize((300, 250))
        img3 = Image.open("picture/seatedcablerow.png").resize((300, 250))
        img4 = Image.open("picture/dumbbelloverrow.png").resize((300, 250))
        self.photo1, self.photo2, self.photo3, self.photo4 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Lat", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Lat", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Middle Back", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Middle Back", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=p40iUjf02j0&pp=ygUGcHVsbHVw")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=CAwf7n6Luuc&t=262s")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/shorts/fPbfYDgzIgA")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=8hzVLzu-RJk&pp=ygUYY2xvc2UgZ3JpcCBsYXQgcHVsbGRvd24g")

class Shoulders5Inter(Page):
    def __init__(self, parent):
        super().__init__(parent, "Shoulders")
        self.geometry("1300x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Shoulders Workout For Intermediate", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack()
        Label(frame2, text="Dumbbell Shoulder Press", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="5x10 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Dumbbell Lateral Raise", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="5x10 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Dumbbell Front Raise", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="5x10 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Machine Rear Delt Fly", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="5x10 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)

        img1 = Image.open("picture/shoulderpress.png").resize((300, 250))
        img2 = Image.open("picture/lateralraise.png").resize((300, 250))
        img3 = Image.open("picture/frontraise.png").resize((300, 250))
        img4 = Image.open("picture/machinereardeltfly.png").resize((300, 250))
        self.photo1, self.photo2, self.photo3, self.photo4 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Front Delt", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Side Delt", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Front Delt", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Rear Delt", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=qEwKCR5JCog")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/shorts/JIhbYYA1Q90")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=-t7fuZ0KhDA&t=11s&pp=ygULZnJvbnQgcmFpc2U%3D")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=1FNDEePWTLc&pp=ygUVbWFjaGluZSByZWFyIGRlbHQgZmx5D")

class Arms5Inter(Page):
    def __init__(self, parent):
        super().__init__(parent, "Arms")
        self.geometry("1350x450")

        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Arms Workout For Intermediate", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack()
        Label(frame2, text="Cable Curl", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="5x10 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Dumbbell Hammer Curl", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="5x10 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Tricep Rope Pushdown", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="5x10 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Dumbbell Skull Crusher", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="5x10 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)
        Label(frame2, text="Tripcep Pushdown", font=self.font_text).grid(row=1, column=5, sticky=NSEW)
        Label(frame2, text="5x10 reps", font=self.font_text).grid(row=2, column=5, sticky=NSEW)

        img1 = Image.open("picture/cablecurl.png").resize((250, 250))
        img2 = Image.open("picture/hammercurl.png").resize((250, 250))
        img3 = Image.open("picture/tricepropepushdown.png").resize((250, 250))
        img4 = Image.open("picture/skullcrusher.png").resize((250, 250))
        img5 = Image.open("picture/triceppushdown.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4, self.photo5 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4), ImageTk.PhotoImage(img5)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, image=self.photo5).grid(row=3, column=5, sticky=NSEW)
        Label(frame2, text="Focusing on Bicep", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Bicep", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Tricep", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Tricep", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Tricep", font=self.font_text).grid(row=4, column=5, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video5).grid(row=5, column=5, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=NFzTWp2qpiE")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=TwD-YGVP4Bk&t=1s&pp=ygULaGFtbWVyIGN1cmw%3D")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=-xa-6cQaZKY&pp=ygUUdHJpY2VwIHJvcGUgcHVzaGRvd24%3D")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/shorts/D1y1-sXZDA0")

    def open_video5(self):
        webbrowser.open("https://www.youtube.com/watch?v=2-LAMcpzODU&pp=ygUPdHJpY2VwIHB1c2hkb3du")

class Day5Advanced(Frame):
    def __init__(self, second_window):
        super().__init__()
        self.second_window = second_window
        self.window18 = None

        menubar = Menu(self.second_window.window2)
        self.second_window.window2.config(menu=menubar)

        workotus_menu = Menu(menubar)
        menubar.add_cascade(label="Chest", menu=workotus_menu, command=self.open_chest_workout)
        menubar.add_cascade(label="Shoulders", menu=workotus_menu, command=self.open_shoulders_workout)
        menubar.add_cascade(label="Back", menu=workotus_menu, command=self.open_back_workout)
        menubar.add_cascade(label="Arms", menu=workotus_menu, command=self.open_arms_workout)
        menubar.add_cascade(label="Leg", menu=workotus_menu, command=self.open_leg_workout)
        menubar.add_cascade(label="Back to Previous Page", menu=workotus_menu, command=self.back)

        self.open_chest_workout()

    def open_chest_workout(self):
        if self.window18:
            self.window18.destroy()
        self.window18 = Chest5Adv(self.second_window.window2)

    def open_shoulders_workout(self):
        if self.window18:
            self.window18.destroy()
        self.window18 = Shoulders5Adv(self.second_window.window2)

    def open_back_workout(self):
        if self.window18:
            self.window18.destroy()
        self.window18 = Back5Adv(self.second_window.window2)

    def open_arms_workout(self):
        if self.window18:
            self.window18.destroy()
        self.window18 = Arms5Adv(self.second_window.window2)

    def open_leg_workout(self):
        if self.window18:
            self.window18.destroy()
        self.window18 = Leg3Adv(self.second_window.window2)

    def back(self):
        self.window18.destroy()
        self.second_window.window2.deiconify()

class Chest5Adv(Page):
    def __init__(self, parent):
        super().__init__(parent, "Chest")
        self.geometry("1400x450")
        
        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Chest Workout For Advanced", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack()
        Label(frame2, text="Barbell Bench Press", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="4x4-8 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Incline Barbell Bench Press", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="4x4-8 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Cable Fly", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="4x12 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Dumbbell Incline Bench Press", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)

        img1 = Image.open("picture/barbellbench.png").resize((250, 250))
        img2 = Image.open("picture/inclinebarbellbench.png").resize((250, 250))
        img3 = Image.open("picture/cablefly.png").resize((250, 250))
        img4 = Image.open("picture/inclinedumbbellbench.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Middle Chest", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Upper Chest", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Lower Chest", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Upper Chest", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=rT7DgCr-3pg")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=SrqOu55lrYU")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=4Jz9v8YjqiI")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=8iPEnn-ltC8")

class Back5Adv(Page):
    def __init__(self, parent):
        super().__init__(parent, "Back")
        self.geometry("1710x450")
        
        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Back Workout For Advanced", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack()
        Label(frame2, text="Weighted Pull Up", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Lat Pulldown", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Seated Cable Row", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Bent Overrow", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="4x4-8 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)
        Label(frame2, text="Deadlift", font=self.font_text).grid(row=1, column=5, sticky=NSEW)
        Label(frame2, text="4x4-8 reps", font=self.font_text).grid(row=2, column=5, sticky=NSEW)
        Label(frame2, text="Close Grip Lat Pulldown", font=self.font_text).grid(row=1, column=6, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=6, sticky=NSEW)

        img1 = Image.open("picture/weightedpullup.png").resize((250, 250))
        img2 = Image.open("picture/latpulldown.png").resize((250, 250))
        img3 = Image.open("picture/seatedcablerow.png").resize((250, 250))
        img4 = Image.open("picture/dumbbelloverrow.png").resize((250, 250))
        img5 = Image.open("picture/deadlift.png").resize((250, 250))
        img6 = Image.open("picture/closegrippulldown.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4, self.photo5, self.photo6 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4), ImageTk.PhotoImage(img5), ImageTk.PhotoImage(img6)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, image=self.photo5).grid(row=3, column=5, sticky=NSEW)
        Label(frame2, image=self.photo6).grid(row=3, column=6, sticky=NSEW)
        Label(frame2, text="Focusing on Lat", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Lat", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Middle Back", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Upper Back", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Upper Back", font=self.font_text).grid(row=4, column=5, sticky=NSEW)
        Label(frame2, text="Focusing on Lat", font=self.font_text).grid(row=4, column=6, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video5).grid(row=5, column=5, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video6).grid(row=5, column=6, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=C0I0gb76yaA&pp=ygUQd2VpZ2h0ZWQgcHVsbCB1cA%3D%3D")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=CAwf7n6Luuc&t=262s")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/shorts/fPbfYDgzIgA")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=knB5Q4FN4ck&pp=ygUSZHVtYmJlbGwgb3ZlciByb3cg")

    def open_video5(self):
        webbrowser.open("https://www.youtube.com/watch?v=XxWcirHIwVo")

    def open_video6(self):
        webbrowser.open("https://www.youtube.com/watch?v=8hzVLzu-RJk&pp=ygUXY2xvc2UgZ3JpcCBsYXQgcHVsbGRvd24%3D")

class Shoulders5Adv(Page):
    def __init__(self, parent):
        super().__init__(parent, "Shoulders")
        self.geometry("1300x450")
        
        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Shoulders Workout For Advanced", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack()
        Label(frame2, text="Dumbbell Shoulder Press", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="4x6-12 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Cable Lateral Raise", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Dumbbell Front Raise", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Machine Rear Delt Fly", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)
        Label(frame2, text="Dumbbell Reverse Fly", font=self.font_text).grid(row=1, column=5, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=5, sticky=NSEW)

        img1 = Image.open("picture/shoulderpress.png").resize((250, 250))
        img2 = Image.open("picture/cablelateralraise.png").resize((250, 250))
        img3 = Image.open("picture/frontraise.png").resize((250, 250))
        img4 = Image.open("picture/machinereardeltfly.png").resize((250, 250))
        img5 = Image.open("picture/reardeltfly.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4, self.photo5 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4), ImageTk.PhotoImage(img5)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, image=self.photo5).grid(row=3, column=5, sticky=NSEW)
        Label(frame2, text="Focusing on Front Delt", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Side Delt", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Front Delt", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Rear Delt", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Rear Delt", font=self.font_text).grid(row=4, column=5, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video5).grid(row=5, column=5, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=qEwKCR5JCog")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/shorts/EZSAOY7b3g4")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=-t7fuZ0KhDA&t=11s&pp=ygUdHJpY2VwIHJvcGUgcHVzaGRvd24%3D")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/watch?v=1FNDEePWTLc&pp=ygUdHJpY2VwIHJvcGUgcHVzaGRvd24%3D")

    def open_video5(self):
        webbrowser.open("https://www.youtube.com/watch?v=EA7u4Q_8HQ0&t=8s&pp=ygUNcmVhciBkZWx0IGZseQ%3D%3D")

class Arms5Adv(Page):
    def __init__(self, parent):
        super().__init__(parent, "Arms")
        self.geometry("1350x450")
        
        frame1 = Frame(self)
        frame1.pack()
        Label(frame1, text="Arms Workout For Advanced", font=self.font_title).grid(row=1, column=0, sticky=NSEW)

        frame2 = Frame(self)
        frame2.pack()
        Label(frame2, text="Dumbbell Curl", font=self.font_text).grid(row=1, column=1, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=1, sticky=NSEW)
        Label(frame2, text="Dumbbell Hammer Curl", font=self.font_text).grid(row=1, column=2, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=2, sticky=NSEW)
        Label(frame2, text="Tricep Rope Pushdown", font=self.font_text).grid(row=1, column=3, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=3, sticky=NSEW)
        Label(frame2, text="Cable Curl", font=self.font_text).grid(row=1, column=4, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=4, sticky=NSEW)
        Label(frame2, text="Tripcep Pushdown", font=self.font_text).grid(row=1, column=5, sticky=NSEW)
        Label(frame2, text="4x8-12 reps", font=self.font_text).grid(row=2, column=5, sticky=NSEW)

        img1 = Image.open("picture/dumbbellcurl.png").resize((250, 250))
        img2 = Image.open("picture/hammercurl.png").resize((250, 250))
        img3 = Image.open("picture/tricepropepushdown.png").resize((250, 250))
        img4 = Image.open("picture/cablecurl.png").resize((250, 250))
        img5 = Image.open("picture/triceppushdown.png").resize((250, 250))
        self.photo1, self.photo2, self.photo3, self.photo4, self.photo5 = ImageTk.PhotoImage(img1), ImageTk.PhotoImage(img2), ImageTk.PhotoImage(img3), ImageTk.PhotoImage(img4), ImageTk.PhotoImage(img5)
        Label(frame2, image=self.photo1).grid(row=3, column=1, sticky=NSEW)
        Label(frame2, image=self.photo2).grid(row=3, column=2, sticky=NSEW)
        Label(frame2, image=self.photo3).grid(row=3, column=3, sticky=NSEW)
        Label(frame2, image=self.photo4).grid(row=3, column=4, sticky=NSEW)
        Label(frame2, image=self.photo5).grid(row=3, column=5, sticky=NSEW)
        Label(frame2, text="Focusing on Bicep", font=self.font_text).grid(row=4, column=1, sticky=NSEW)
        Label(frame2, text="Focusing on Bicep", font=self.font_text).grid(row=4, column=2, sticky=NSEW)
        Label(frame2, text="Focusing on Tricep", font=self.font_text).grid(row=4, column=3, sticky=NSEW)
        Label(frame2, text="Focusing on Bicep", font=self.font_text).grid(row=4, column=4, sticky=NSEW)
        Label(frame2, text="Focusing on Tricep", font=self.font_text).grid(row=4, column=5, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video1).grid(row=5, column=1, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video2).grid(row=5, column=2, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video3).grid(row=5, column=3, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video4).grid(row=5, column=4, sticky=NSEW)
        Button(frame2, text="Watch Video Tutorial", command=self.open_video5).grid(row=5, column=5, sticky=NSEW)

    def open_video1(self):
        webbrowser.open("https://www.youtube.com/watch?v=ykJmrZ5v0Oo&t=1s&pp=ygUNZHVtYmJlbGwgY3VybA%3D%3D")

    def open_video2(self):
        webbrowser.open("https://www.youtube.com/watch?v=TwD-YGVP4Bk&t=1s&pp=ygUUZHVtYmJlbGwgaGFtbWVyIGN1cmw%3D")

    def open_video3(self):
        webbrowser.open("https://www.youtube.com/watch?v=-xa-6cQaZKY&pp=ygUdHJpY2VwIHJvcGUgcHVzaGRvd24%3D")

    def open_video4(self):
        webbrowser.open("https://www.youtube.com/shorts/Krkjb73ZuAU")

    def open_video5(self):
        webbrowser.open("https://www.youtube.com/shorts/Rc7-euA8FDI")
