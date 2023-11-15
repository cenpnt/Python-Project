# # # # # # import tkinter as tk
# # # # # # from tkinter import ttk
# # # # # # from matplotlib.figure import Figure
# # # # # # from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# # # # # # def compare_expense_income():
# # # # # #     # Sample data for the bar chart
# # # # # #     categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
# # # # # #     expenses = [10, 25, 15, 30, 20]
# # # # # #     income = [25, 20, 30, 15, 40]  # Adjusted income values for demonstration

# # # # # #     # Calculate the maximum value between income and expenses
# # # # # #     max_value = max(max(expenses), max(income))

# # # # # #     # Create a Figure instance
# # # # # #     fig = Figure(figsize=(8, 5), dpi=100)
    
# # # # # #     # Add a subplot to the Figure
# # # # # #     plot = fig.add_subplot(1, 1, 1)

# # # # # #     # Create a bar chart with two sets of data (expenses and income)
# # # # # #     width = 0.4
# # # # # #     x = range(len(categories))
# # # # # #     bars1 = plot.bar(x, expenses, width=width, customtkinter.CTkLabel='Expenses', align='center')
# # # # # #     bars2 = plot.bar([i + width for i in x], income, width=width, customtkinter.CTkLabel='Income', align='center')

# # # # # #     # Set customtkinter.CTkLabels and title
# # # # # #     plot.set_xcustomtkinter.CTkLabel('Categories')
# # # # # #     plot.set_ycustomtkinter.CTkLabel('Amount')
# # # # # #     plot.set_title('Expense and Income Comparison')
# # # # # #     plot.set_xticks([i + width / 2 for i in x])
# # # # # #     plot.set_xtickcustomtkinter.CTkLabels(categories)
# # # # # #     plot.legend()

# # # # # #     # Dynamic scaling of the Y-axis
# # # # # #     if max_value > 100:
# # # # # #         plot.set_ylim(0, max_value + 10)  # Adjust the Y-axis limit based on the max value

# # # # # #     # Display amount numbers above the bars
# # # # # #     for bar1, bar2 in zip(bars1, bars2):
# # # # # #         height1 = bar1.get_height()
# # # # # #         height2 = bar2.get_height()
# # # # # #         plot.annotate(f'{height1:.2f}', xy=(bar1.get_x() + bar1.get_width() / 2, height1),
# # # # # #                       xytext=(0, 3), textcoords='offset points', ha='center')
# # # # # #         plot.annotate(f'{height2:.2f}', xy=(bar2.get_x() + bar2.get_width() / 2, height2),
# # # # # #                       xytext=(0, 3), textcoords='offset points', ha='center')

# # # # # #     # Create a canvas to display the Figure
# # # # # #     canvas = FigureCanvasTkAgg(fig, master=root)
# # # # # #     canvas.get_tk_widget().pack()

# # # # # #     # Show the chart
# # # # # #     canvas.draw()

# # # # # # root = tk.Tk()
# # # # # # root.title("Dynamic Y-axis Scale Bar Chart")

# # # # # # plot_button = ttk.Button(root, text="Compare Expense and Income", command=compare_expense_income)
# # # # # # plot_button.pack()

# # # # # # root.mainloop()

# # # # # import tkinter as tk
# # # # # from tkinter import ttk

# # # # # def show_graph_window():
# # # # #     # Hide the main window
# # # # #     main_window.withdraw()
    
# # # # #     # Create a new window for the graph
# # # # #     graph_window = tk.Toplevel(main_window)
# # # # #     graph_window.title("Graph Window")

# # # # #     # Add widgets and functionality for the graph window here
    
# # # # #     # Create a button to go back to the main window
# # # # #     back_button = ttk.Button(graph_window, text="Back to Main", command=lambda: close_window(graph_window))
# # # # #     back_button.pack()

# # # # # def close_window(window):
# # # # #     # Close the given window and show the main window
# # # # #     window.destroy()
# # # # #     main_window.deiconify()

# # # # # main_window = tk.Tk()
# # # # # main_window.title("Main Window")

# # # # # show_graph_button = ttk.Button(main_window, text="Show Graph Window", command=show_graph_window)
# # # # # show_graph_button.pack()

# # # # # main_window.mainloop()
# # # # import tkinter as tk
# # # # from tkinter import ttk

# # # # def on_check1():
# # # #     if check_var1.get():
# # # #         customtkinter.CTkLabel1.config(text="Checkbutton 1 is checked")
# # # #     else:
# # # #         customtkinter.CTkLabel1.config(text="Checkbutton 1 is unchecked")

# # # # def on_check2():
# # # #     if check_var2.get():
# # # #         customtkinter.CTkLabel2.config(text="Checkbutton 2 is checked")
# # # #     else:
# # # #         customtkinter.CTkLabel2.config(text="Checkbutton 2 is unchecked")

# # # # root = tk.Tk()
# # # # root.title("Multiple Checkbuttons Example")

# # # # # Create variables for the two Checkbuttons
# # # # check_var1 = tk.BooleanVar()
# # # # check_var2 = tk.BooleanVar()

# # # # # Create the first Checkbutton and associate it with check_var1
# # # # check_button1 = ttk.Checkbutton(root, text="Check me 1", variable=check_var1, command=on_check1)
# # # # check_button1.pack()

# # # # # Create the second Checkbutton and associate it with check_var2
# # # # check_button2 = ttk.Checkbutton(root, text="Check me 2", variable=check_var2, command=on_check2)
# # # # check_button2.pack()

# # # # # Create customtkinter.CTkLabels to display the status of the Checkbuttons
# # # # customtkinter.CTkLabel1 = ttk.customtkinter.CTkLabel(root, text="")
# # # # customtkinter.CTkLabel1.pack()

# # # # customtkinter.CTkLabel2 = ttk.customtkinter.CTkLabel(root, text="")
# # # # customtkinter.CTkLabel2.pack()

# # # # root.mainloop()

# # # import tkinter as tk
# # # import psutil

# # # def update_cpu_usage_customtkinter.CTkLabel():
# # #     cpu_usage = psutil.cpu_percent(interval=1)
# # #     cpu_customtkinter.CTkLabel.config(text=f'CPU Usage: {cpu_usage}%')
# # #     root.after(1000, update_cpu_usage_customtkinter.CTkLabel)

# # # root = tk.Tk()
# # # root.title("CPU Usage Monitor")

# # # cpu_customtkinter.CTkLabel = tk.customtkinter.CTkLabel(root, text="CPU Usage: ")
# # # cpu_customtkinter.CTkLabel.pack()

# # # update_cpu_usage_customtkinter.CTkLabel()

# # # root.mainloop()

# # # import tkinter as tk
# # # from tkinter import filedialog

# # # def open_file():
# # #     file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
# # #     if file_path:
# # #         # Do something with the selected file, e.g., read its contents
# # #         with open(file_path, 'r') as file:
# # #             file_contents = file.read()
# # #             # Display or process the file contents as needed
# # #             print("File Contents:\n", file_contents)

# # # root = tk.Tk()
# # # root.title("Open File Example")

# # # open_button = tk.Button(root, text="Open File", command=open_file)
# # # open_button.pack(padx=20, pady=20)

# # # root.mainloop()

# # # import tkinter as tk

# # # def display_selected_option():
# # #     selected_option = var.get()
# # #     print("Selected option:", selected_option)

# # # root = tk.Tk()
# # # root.title("Mutually Exclusive Check Buttons")

# # # var = tk.StringVar()

# # # # Create Radiobuttons
# # # option1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1", command=display_selected_option)
# # # option2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2", command=display_selected_option)
# # # option3 = tk.Radiobutton(root, text="Option 3", variable=var, value="Option 3", command=display_selected_option)

# # # # Set the initial selection
# # # var.set("Option 1")

# # # # Place Radiobuttons in the GUI
# # # option1.pack()
# # # option2.pack()
# # # option3.pack()

# # # root.mainloop()

# # # import tkinter as tk
# # # import re

# # # def get_entry_value():
# # #     entry_value = entry.get()
# # #     print("Entry Value:", entry_value)
    
# # #     # Clear the text in the Entry widget
# # #     entry.delete(0, 'end')

# # # root = tk.Tk()
# # # root.title("Get and Clear Entry Value")

# # # entry = tk.Entry(root)
# # # entry.pack()

# # # button = tk.Button(root, text="Get Entry Value", command=get_entry_value)
# # # button.pack()


# # # root.mainloop()

# # # import tkinter as tk
# # # from tkcalendar import Calendar

# # # class Main:
# # #     def __init__(self):
# # #         window = tk.Tk()
# # #         window.title("Date Picker Example")

# # #         # Create a Calendar widget
# # #         self.cal = Calendar(window, selectmode='day', year=2023, month=9, day=1, showweeknumbers=False)

# # #         self.cal.pack(padx=10, pady=10)

# # #         # Create a button to get the selected date
# # #         tk.Button(window, text="Get Date", command=self.get_selected_date).pack()

# # #         self.selected_date = ""

# # #         window.mainloop()

# # #     def get_selected_date(self):
# # #         self.selected_date = self.cal.get_date()
# # #         print("Selected Date:", self.selected_date)

# # # Main()

# # # import tkinter as tk
# # # from tkcalendar import Calendar

# # # class Main:
# # #     def __init__(self):
# # #         window = tk.Tk()
# # #         window.title("Income and Expense Tracker")

# # #         # Create a Calendar widget for selecting dates
# # #         self.date_picker = Calendar(window, selectmode='day', year=2023, month=9, day=1)
# # #         self.date_picker.pack(padx=10, pady=10)

# # #         # Create entry fields for income and expense
# # #         tk.customtkinter.CTkLabel(window, text="Income:").pack()
# # #         self.income_entry = tk.Entry(window)
# # #         self.income_entry.pack()

# # #         tk.customtkinter.CTkLabel(window, text="Expense:").pack()
# # #         self.expense_entry = tk.Entry(window)
# # #         self.expense_entry.pack()

# # #         # Create a button to submit data
# # #         tk.Button(window, text="Submit", command=self.submit_data).pack()

# # #         self.selected_date = ""

# # #         window.mainloop()

# # #     def submit_data(self):
# # #         # Get the selected date from the Calendar widget
# # #         self.selected_date = self.date_picker.get_date()

# # #         # Get the income and expense values from the entry fields
# # #         income_value = self.income_entry.get()
# # #         expense_value = self.expense_entry.get()

# # #         # Here, you can work with the selected date, income, and expense data as needed.
# # #         # For example, you can display or store them in your income and expense records.

# # #         print("Selected Date:", self.selected_date)
# # #         print("Income:", income_value)
# # #         print("Expense:", expense_value)

# # # Main()

# # # import tkinter as tk
# # # from tkinter import Toplevel, customtkinter.CTkLabel, Button
# # # from tkcalendar import Calendar

# # # class Main:
# # #     def __init__(self):
# # #         self.window = tk.Tk()
# # #         self.window.title("Income and Expense Tracker")

# # #         # Create a button to open the calendar
# # #         tk.Button(self.window, text="Select Date", command=self.open_calendar).pack()

# # #         self.selected_date = ""

# # #     def open_calendar(self):
# # #         # Create a separate window for the calendar
# # #         calendar_window = Toplevel(self.window)
# # #         calendar_window.title("Calendar")

# # #         # Create a Calendar widget in the calendar window
# # #         calendar = Calendar(calendar_window, selectmode='day', year=2023, month=9, day=1)
# # #         calendar.pack(padx=10, pady=10)

# # #         # Create a customtkinter.CTkLabel to display the selected date
# # #         self.date_customtkinter.CTkLabel = customtkinter.CTkLabel(calendar_window, text="Selected Date: ")
# # #         self.date_customtkinter.CTkLabel.pack()

# # #         # Create a button to confirm the selected date
# # #         tk.Button(calendar_window, text="Confirm", command=lambda: self.get_selected_date(calendar)).pack()

# # #     def get_selected_date(self, calendar):
# # #         # Retrieve the selected date from the Calendar widget
# # #         self.selected_date = calendar.get_date()

# # #         # Update the customtkinter.CTkLabel to display the selected date
# # #         self.date_customtkinter.CTkLabel.config(text="Selected Date: " + self.selected_date)

# # #     def run(self):
# # #         self.window.mainloop()

# # # if __name__ == "__main__":
# # #     app = Main()
# # #     app.run()

# # # import tkinter as tk
# # # from tkinter import ttk
# # # import csv

# # # # Create the main window
# # # root = tk.Tk()
# # # root.title("Food Calorie Calculator")

# # # # Create a frame for displaying the data
# # # frame = ttk.Frame(root)
# # # frame.pack(padx=10, pady=10)

# # # food_data = []

# # # with open('food_data.csv', newline='') as csvfile:
# # #     reader = csv.DictReader(csvfile)
# # #     for row in reader:
# # #         food_data.append(row)
        
# # # tree = ttk.Treeview(frame, columns=('Food Item', 'Calories'))
# # # tree.heading('#1', text='Food Item')
# # # tree.heading('#2', text='Calories (kcal)')
# # # tree.column('#1', width=200)
# # # tree.column('#2', width=100)

# # # for food in food_data:
# # #     tree.insert('', 'end', values=(food['Food Item'], food['Calories']))

# # # tree.pack()
# # # root.mainloop()

# # # import tkinter as tk

# # # def on_option_select(selected_item):
# # #     customtkinter.CTkLabel.config(text=f"Selected: {selected_item}")

# # # root = tk.Tk()
# # # root.title("Dropdown Selection")

# # # options = ["Option 1", "Option 2", "Option 3", "Option 4"]
# # # selected_option = tk.StringVar()
# # # selected_option.set(options[0])

# # # customtkinter.CTkLabel = tk.customtkinter.CTkLabel(root, text="")
# # # customtkinter.CTkLabel.pack(padx=10, pady=10)

# # # option_menu = tk.OptionMenu(root, selected_option, *options, command=on_option_select)
# # # option_menu.pack(padx=10, pady=10)

# # # root.mainloop()

# # # import tkinter as tk

# # # class MyApp:
# # #     def __init__(self, root):
# # #         self.root = root
# # #         self.root.title("Dropdown Selection")

# # #         self.options = ["Option 1", "Option 2", "Option 3", "Option 4"]
# # #         self.selected_option = tk.StringVar()
# # #         self.selected_option.set(self.options[0])

# # #         self.customtkinter.CTkLabel = tk.customtkinter.CTkLabel(root, text="")
# # #         self.customtkinter.CTkLabel.pack(padx=10, pady=10)

# # #         self.option_menu = tk.OptionMenu(root, self.selected_option, *self.options, command=self.activity_option)
# # #         self.option_menu.pack(padx=10, pady=10)

# # #     def activity_option(self, selected_item):
# # #         self.customtkinter.CTkLabel.config(text=f"Selected: {selected_item}")

# # # if __name__ == "__main__":
# # #     root = tk.Tk()
# # #     app = MyApp(root)
# # #     root.mainloop()

# # # def calculate_tdee(gender, age, weight_kg, height_cm, activity_level):
# # #     if gender == "Male":
# # #         bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
# # #     elif gender == "Female":
# # #         bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
# # #     else:
# # #         raise ValueError("Invalid gender")

# # #     activity_factors = {
# # #         "Sedentary": 1.2,
# # #         "Lightly Active": 1.375,
# # #         "Moderately Active": 1.55,
# # #         "Very Active": 1.725,
# # #         "Extremely Active": 1.9,
# # #     }

# # #     if activity_level not in activity_factors:
# # #         raise ValueError("Invalid activity level")

# # #     tdee = bmr * activity_factors[activity_level]
# # #     return tdee

# # # # Example usage:
# # # gender = "Female"  # Change to "Female" for females
# # # age = 30
# # # weight_kg = 70
# # # height_cm = 175
# # # activity_level = "Moderately Active"  # Choose the appropriate activity level
# # # result = calculate_tdee(gender, age, weight_kg, height_cm, activity_level)
# # # print(f"TDEE for {gender}: {result:.0f} calories per day")

# # # import tkinter as tk
# # # from tkinter import ttk

# # # class FirstWindow:
# # #     def __init__(self, root):
# # #         self.root = root
# # #         self.root.title("Workout App")
# # #         self.root.geometry("400x300")
        
# # #         self.customtkinter.CTkLabel = ttk.customtkinter.CTkLabel(root, text="First Window")
# # #         self.customtkinter.CTkLabel.pack(pady=20)

# # #         self.value_to_pass = "Hello from FirstWindow"

# # #         self.next_button = ttk.Button(root, text="Next", command=self.open_second_window)
# # #         self.next_button.pack()

# # #     def open_second_window(self):
# # #         # Destroy the first window
# # #         self.root.destroy()
        
# # #         # Create and show the second window, passing the value
# # #         SecondWindow(self.value_to_pass)

# # # class SecondWindow:
# # #     def __init__(self, value_from_first):
# # #         self.root = tk.Tk()
# # #         self.root.title("Second Window")
# # #         self.root.geometry("400x300")
        
# # #         self.customtkinter.CTkLabel = ttk.customtkinter.CTkLabel(self.root, text="Second Window")
# # #         self.customtkinter.CTkLabel.pack(pady=20)

# # #         self.value_customtkinter.CTkLabel = ttk.customtkinter.CTkLabel(self.root, text="Value from FirstWindow:")
# # #         self.value_customtkinter.CTkLabel.pack()
        
# # #         self.value_display = ttk.customtkinter.CTkLabel(self.root, text=value_from_first)
# # #         self.value_display.pack()

# # #         self.back_button = ttk.Button(self.root, text="Back", command=self.open_first_window)
# # #         self.back_button.pack()

# # #         self.root.mainloop()

# # #     def open_first_window(self):
# # #         # Close the second window
# # #         self.root.destroy()
        
# # #         # Recreate and show the first window
# # #         root = tk.Tk()
# # #         FirstWindow(root)

# # # if __name__ == "__main__":
# # #     root = tk.Tk()
# # #     app = FirstWindow(root)
# # #     root.mainloop()

# # # # 
# # # import tkinter as tk
# # # from tkinter import ttk

# # # window = tk.Tk()

# # # style = ttk.Style()
# # # style.configure("TRadiobutton", foreground="green")

# # # radio_button = ttk.Radiobutton(window, text="Option 1", value=1)
# # # radio_button.pack()

# # # window.mainloop()


# # # import tkinter as tk
# # # from tkinter import PhotoImage

# # # # Create a Tkinter window
# # # window = tk.Tk()
# # # window.title("Workout App")
# # # window.geometry("720x1080")

# # # # Load the background image
# # # bg_image = PhotoImage(file="background.png")

# # # # Create a customtkinter.CTkLabel widget to display the image as the background
# # # bg_customtkinter.CTkLabel = tk.customtkinter.CTkLabel(window, image=bg_image)
# # # bg_customtkinter.CTkLabel.place(relwidth=1, relheight=1)  # Make the customtkinter.CTkLabel cover the entire window

# # # # Add your workout app widgets on top of the background
# # # bg_customtkinter.CTkLabel = tk.customtkinter.CTkLabel(window, text="Workout App", font=("Arial", 30), background="black", foreground="red")
# # # bg_customtkinter.CTkLabel.pack(pady=20)
# # # # For example, buttons, customtkinter.CTkLabels, etc.

# # # # Start the Tkinter main loop
# # # window.mainloop()
# # # 

# # # import tkinter as tk

# # # def change_content():
# # #     # Clear the existing content of the container
# # #     for widget in container.winfo_children():
# # #         widget.destroy()

# # #     # Create and add new widgets to the container
# # #     customtkinter.CTkLabel = tk.customtkinter.CTkLabel(container, text="New Content")
# # #     customtkinter.CTkLabel.pack()

# # # root = tk.Tk()
# # # root.title("Dynamic Content Example")

# # # container = tk.Frame(root)
# # # container.pack(padx=10, pady=10)

# # # button = tk.Button(root, text="Change Content", command=change_content)
# # # button.pack()

# # # # Initial content of the container
# # # customtkinter.CTkLabel = tk.customtkinter.CTkLabel(container, text="Initial Content")
# # # customtkinter.CTkLabel.pack()

# # # root.mainloop()

# # # import tkinter as tk
# # # from tkinter import PhotoImage
# # # from PIL import Image, ImageTk

# # # Function to change the displayed image and update the customtkinter.CTkLabel text based on the selected option
# # # def change_image():
# # #     selected_option = var.get()
# # #     if selected_option == 1:
# # #         image_customtkinter.CTkLabel.config(image=image1)
# # #         image_name_customtkinter.CTkLabel.config(text="Image 1")
# # #     elif selected_option == 2:
# # #         image_customtkinter.CTkLabel.config(image=image2)
# # #         image_name_customtkinter.CTkLabel.config(text="Image 2")
# # #     # elif selected_option == 3:
# # #     #     image_customtkinter.CTkLabel.config(image=image3)
# # #     #     image_name_customtkinter.CTkLabel.config(text="Image 3")

# # # # Create the main window
# # # root = tk.Tk()
# # # root.title("Image Viewer")

# # # # Create radio buttons
# # # var = tk.IntVar()
# # # radio1 = tk.Radiobutton(root, text="Image 1", variable=var, value=1, command=change_image)
# # # radio2 = tk.Radiobutton(root, text="Image 2", variable=var, value=2, command=change_image)
# # # # radio3 = tk.Radiobutton(root, text="Image 3", variable=var, value=3, command=change_image)

# # # # Load and convert PNG images using Pillow
# # # image1 = Image.open("arnold.png")
# # # image1 = ImageTk.PhotoImage(image1)
# # # image2 = Image.open("dumbbell.png")
# # # image2 = ImageTk.PhotoImage(image2)
# # # # image3 = Image.open("image3.png")
# # # # image3 = ImageTk.PhotoImage(image3)

# # # # Create a customtkinter.CTkLabel to display the image
# # # image_customtkinter.CTkLabel = tk.customtkinter.CTkLabel(root, image=image1)

# # # # Text customtkinter.CTkLabel to display the image name
# # # image_name_customtkinter.CTkLabel = tk.customtkinter.CTkLabel(root, text="Image 1")

# # # # Pack the widgets
# # # radio1.grid(row=1, column=1)
# # # radio2.grid(row=1, column=2)
# # # # radio3.pack()
# # # image_customtkinter.CTkLabel.grid(row=2, column=1, columnspan=2)
# # # image_name_customtkinter.CTkLabel.grid(row=3, column=1, columnspan=2)

# # # # Set an initial selection
# # # var.set(1)
# # # change_image()

# # # # Start the Tkinter main loop
# # # root.mainloop()


# # import tkinter as tk
# # from PIL import ImageTk, Image

# # class WorkoutApp:
# #     def __init__(self, window):
# #         self.window = window
# #         self.window.title("Workout App")
        
# #         self.image_paths = {
# #             "1 Day Beginner": "fullbody.png",
# #             "2 Days Beginner": "arnold.png",
# #             # Add more image paths for different options here
# #         }

# #         self.selected_option = tk.StringVar()
# #         self.selected_option.set("1 Day Beginner")  # Set a default option

# #         # Create radio buttons
# #         options = ["1 Day Beginner", "2 Days Beginner"]  # Add more options here
# #         for option in options:
# #             tk.Radiobutton(window, text=option, variable=self.selected_option, value=option, command=self.update_image).pack()

# #         # Initialize the image
# #         self.image = None
# #         self.update_image()
            
# #     def update_image(self):
# #         selected_option = self.selected_option.get()
# #         if selected_option == "1 Day Beginner":
# #             image_path = "fullbody.png"
# #         elif selected_option == "2 Days Beginner":
# #             image_path = "arnold.png"
# #         # Add more conditions for other options as needed
# #         else:
# #             image_path = "dumbbell.png"  # Use a default image path

# #         image = Image.open(image_path)
# #         image = image.resize((300, 300))
# #         self.photo = ImageTk.PhotoImage(image)

# #         # Update the image customtkinter.CTkLabel
# #         self.image_customtkinter.CTkLabel.configure(image=self.photo)


# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     app = WorkoutApp(root)
# #     root.mainloop()


# from tkinter import *
# from PIL import ImageTk, Image
# import webbrowser

# class Explain:
#     def __init__(self, second_window):
#         self.second_window = second_window
#         self.window3 = Toplevel(self.second_window.window2)
#         self.third_window = self
#         self.window3.title("Workout App")
#         self.window3.geometry("900x700")
#         self.font_title = ("TKDefaultFont", 20, "bold")

#         Button(self.window3, text="Back", command=self.back).pack(padx=10, pady=10, side=BOTTOM)
#         Button(self.window3, text="Next", command= self.open_chest_explain).pack(padx=10, pady=10, side=BOTTOM)

#         frame1 = Frame(self.window3)
#         frame1.pack(padx=10, pady=10)
#         customtkinter.CTkLabel(frame1, text="Explanation For Each Workout", font=self.font_title).grid(row=1, column=1, sticky=NSEW)
#         customtkinter.CTkLabel(frame1, text="Choose one of the workout you want to know about").grid(row=2, column=1, sticky=NSEW)

#         frame2 = Frame(self.window3)
#         frame2.pack(padx=10, pady=10)
#         self.button1 = StringVar()
#         self.button1.set("Full Body Workout")  # default value

#         Radiobutton(frame2, variable=self.button1, value="Full Body Workout", command=self.update_content).grid(row=3, column=1, sticky=NSEW)
#         customtkinter.CTkLabel(frame2, text="Full Body Workout").grid(row=3, column=2, sticky=NSEW)
#         Radiobutton(frame2, variable=self.button1, value="Upper/Lower Split", command=self.update_content).grid(row=3, column=3, sticky=NSEW)
#         customtkinter.CTkLabel(frame2, text="Upper/Lower Split").grid(row=3, column=4, sticky=NSEW)
#         Radiobutton(frame2, variable=self.button1, value="Push Pull Legs", command=self.update_content).grid(row=3, column=5, sticky=NSEW)
#         customtkinter.CTkLabel(frame2, text="Push Pull Legs").grid(row=3, column=6, sticky=NSEW)
#         Radiobutton(frame2, variable=self.button1, value="Arnold Split", command=self.update_content).grid(row=3, column=7, sticky=NSEW)
#         customtkinter.CTkLabel(frame2, text="Arnold Split").grid(row=3, column=8, sticky=NSEW)
#         Radiobutton(frame2, variable=self.button1, value="Bro Split", command=self.update_content).grid(row=3, column=9, sticky=NSEW)
#         customtkinter.CTkLabel(frame2, text="Chest, Back, Shoulders, Arms, Legs or called Bro Split").grid(row=3, column=10, sticky=NSEW)

#         frame3 = Frame(self.window3)
#         frame3.pack(padx=10, pady=10)
#         self.info = StringVar()
#         # default value
#         self.info.set("Full Body Workout is a workout that you do all the exercises for your whole body in one day.\nThis workout is good for beginners because it is easy to follow.\nThis workout is also good for people who want to maintain their muscle mass.\n You can do this workout with dumbbells or bodyweight only.")

#         self.font_customtkinter.CTkLabel = ("TKDefaultFont", 14, "bold")

#         frame4 = Frame(self.window3)
#         frame4.pack(padx=10, pady=10)
#         customtkinter.CTkLabel(frame4, textvariable=self.info, font=self.font_customtkinter.CTkLabel).grid(row=4, column=1, sticky=NSEW)

#         frame5 = Frame(self.window3)
#         frame5.pack(padx=10, pady=10)
#         Button(frame5, text="More information", command=self.open_link).grid(row=5, column=1, sticky=NSEW)

#         frame6 = Frame(self.window3)
#         frame6.pack(padx=10, pady=10)
#         image = Image.open("picture/arnold.png")
#         image = image.resize((600, 500))
#         self.photo = ImageTk.PhotoImage(image)
#         customtkinter.CTkLabel(frame6, image=self.photo).grid(row=6, column=1, sticky=NSEW)

#         self.window3.mainloop()
    
#     def back(self):
#         self.window3.destroy()
#         self.second_window.window2.deiconify()

#     def update_content(self):
#         if self.button1.get() == "Full Body Workout":
#             self.info.set("Full Body Workout is a workout that you do all the exercises for your whole body in one day.\nThis workout is good for beginners because it is easy to follow.\nThis workout is also good for people who want to maintain their muscle mass.\n You can do this workout with dumbbells or bodyweight only.")

#         if self.button1.get() == "Upper/Lower Split":
#             self.info.set("Upper/Lower Split is a workout that you do all the exercises for your upper body in one day and lower body in another day.\n This workout is good for intermediate and advanced people because it is more challenging than Full Body Workout. \nYou can do this workout with dumbbells or barbells.")
        
#         if self.button1.get() == "Push Pull Legs":
#             self.info.set("Push Pull Legs is a workout that you do all the exercises for your push muscles in one day, pull muscles in another day\n and legs in another day. This workout is good for intermediate and advanced people\n because it is more challenging than Full Body Workout.\n You can do this workout with dumbbells or barbells.")
        
#         if self.button1.get() == "Arnold Split":
#             self.info.set("Arnold Split is a workout that you do all the exercises for your chest and back in one day, shoulders and arms in another day\n and legs in another day. This workout is good for advanced people because it is more challenging than Full Body Workout.\n You can do this workout with dumbbells or barbells.")
        
#         if self.button1.get() == "Bro Split":
#             self.info.set("Chest, Back, Shoulders, Arms, Legs is a workout that you do all the exercises\n for your chest in one day, back in another day, shoulders in another day, arms in another day and legs in another day.\n This workout is good for advanced people because it is more challenging than Full Body Workout. \nYou can do this workout with dumbbells or barbells.")

#     def open_link(self):
        
#         if self.button1.get() == "Full Body Workout":
#             webbrowser.open("https://www.youtube.com/shorts/bVrj4pIPEqg")

#         if self.button1.get() == "Upper/Lower Split":
#             webbrowser.open("https://youtu.be/eWPj3ikAExk?t=44")
        
#         if self.button1.get() == "Push Pull Legs":
#             webbrowser.open("https://www.youtube.com/watch?v=k_JvRZLXMj4")
        
#         if self.button1.get() == "Arnold Split":
#             webbrowser.open("https://www.youtube.com/watch?v=7ZPzeGnb2uI")
        
#         if self.button1.get() == "Bro Split":
#             webbrowser.open("https://www.youtube.com/watch?v=1vh7wLrFLW8")

#     def open_chest_explain(self):
#         self.third_window.window3.withdraw()
#         ExplainChest(self.third_window)

# class ExplainChest:
#     def __init__(self, third_window):
#         self.third_window = third_window
#         self.window4 = Toplevel(self.third_window.window3)
#         self.fourth_window = self
#         self.window4.title("Workout App")
#         self.window4.geometry("900x700")
#         self.font_title = ("TKDefaultFont", 18, "bold")
#         self.font_customtkinter.CTkLabel = ("TKDefaultFont", 14, "bold")

#         Button(self.window4, text="Back", command=self.back).pack(padx=10, pady=10, side=BOTTOM)
#         Button(self.window4, text="Next", command=self.open_shoulders_explain).pack(padx=10, pady=10, side=BOTTOM)

#         frame1 = Frame(self.window4)
#         frame1.pack(padx=10, pady=10)
#         customtkinter.CTkLabel(frame1, text="Explanation For Each Muscle", font=self.font_title).grid(row=1, column=1, sticky=NSEW)
#         customtkinter.CTkLabel(frame1, text="First Muscle Group", font= self.font_title).grid(row=2, column=1, sticky=NSEW)
#         customtkinter.CTkLabel(frame1, text= "Chest", font= self.font_title).grid(row=3, column=1, sticky=NSEW)

#         frame2 = Frame(self.window4)
#         frame2.pack(padx=10, pady=10)
#         customtkinter.CTkLabel(frame2, text="Chest consist of three main muscles\nwhich is\n Upper Chest, Middle Chest and Lower Chest", font= self.font_customtkinter.CTkLabel).grid(row=3, column=1, sticky=NSEW)

#         frame3 = Frame(self.window4)
#         frame3.pack(padx=10, pady=10)
#         image = Image.open("picture/chestanatomy.png")
#         image = image.resize((600, 400))
#         self.photo = ImageTk.PhotoImage(image)
#         customtkinter.CTkLabel(frame3, image=self.photo).grid(row=4, column=1, sticky=NSEW)

#     def back(self):
#         self.window4.destroy()
#         self.third_window.window3.deiconify()

#     def open_shoulders_explain(self):
#         self.fourth_window.window4.withdraw()
#         ExplainShoulders(self.fourth_window)

# class ExplainShoulders:
#     def __init__(self, fourth_window):
#         self.fourth_window = fourth_window
#         self.window5 = Toplevel(self.fourth_window.window4)
#         self.fifth_window = self
#         self.window5.title("Workout App")
#         self.window5.geometry("900x700")
#         self.font_title = ("TKDefaultFont", 18, "bold")
#         self.font_customtkinter.CTkLabel = ("TKDefaultFont", 14, "bold")

#         Button(self.window5, text="Back", command=self.back).pack(padx=10, pady=10, side=BOTTOM)
#         Button(self.window5, text="Next", command=self.open_back_explain).pack(padx=10, pady=10, side=BOTTOM)

#         frame1 = Frame(self.window5)
#         frame1.pack(padx=10, pady=10)
#         customtkinter.CTkLabel(frame1, text="Second Muscle Group", font= self.font_title).grid(row=1, column=1, sticky=NSEW)
#         customtkinter.CTkLabel(frame1, text= "Shoulders", font= self.font_title).grid(row=2, column=1, sticky=NSEW)

#         frame2 = Frame(self.window5)
#         frame2.pack(padx=10, pady=10)
#         customtkinter.CTkLabel(frame2, text="Shoulders consist of three main muscles\nwhich is\n Anterior Deltoid, Medial Deltoid and Posterior Deltoid", font= self.font_customtkinter.CTkLabel).grid(row=3, column=1, sticky=NSEW)

#         frame3 = Frame(self.window5)
#         frame3.pack(padx=10, pady=10)
#         image = Image.open("picture/shoulderanatomy.png")
#         image = image.resize((600, 400))
#         self.photo = ImageTk.PhotoImage(image)
#         customtkinter.CTkLabel(frame3, image=self.photo).grid(row=4, column=1, sticky=NSEW)

#     def back(self):
#         self.window4.destroy()
#         self.fourth_window.window3.deiconify()

#     def open_back_explain(self):
#         self.fifth_window.window5.withdraw()
#         ExplainBack(self.fifth_window)

# class ExplainBack:
#     def __init__(self, fifth_window):
#         self.fifth_window = fifth_window
#         self.window6 = Toplevel(self.fifth_window.window5)
#         self.fifth_window = self
#         self.window6.title("Workout App")
#         self.window6.geometry("900x700")
#         self.font_title = ("TKDefaultFont", 18, "bold")
#         self.font_customtkinter.CTkLabel = ("TKDefaultFont", 14, "bold")

#         Button(self.window6, text="Back", command=self.back).pack(padx=10, pady=10, side=BOTTOM)
#         Button(self.window6, text="Next", command=self.open_arms_explain).pack(padx=10, pady=10, side=BOTTOM)

#         frame1 = Frame(self.window6)
#         frame1.pack(padx=10, pady=10)
#         customtkinter.CTkLabel(frame1, text="Third Muscle Group", font= self.font_title).grid(row=1, column=1, sticky=NSEW)
#         customtkinter.CTkLabel(frame1, text= "Back", font= self.font_title).grid(row=2, column=1, sticky=NSEW)

#         frame2 = Frame(self.window6)
#         frame2.pack(padx=10, pady=10)
#         customtkinter.CTkLabel(frame2, text="Back consist of many muscles\nwhich is\n Trapezius, Latissimus Dorsi, Rhomboids, Teres Major, Teres Minor and Erector Spinae", font= self.font_customtkinter.CTkLabel).grid(row=3, column=1, sticky=NSEW)

#         frame3 = Frame(self.window6)
#         frame3.pack(padx=10, pady=10)
#         image = Image.open("picture/backanatomy.png")
#         image = image.resize((600, 550))
#         self.photo = ImageTk.PhotoImage(image)
#         customtkinter.CTkLabel(frame3, image=self.photo).grid(row=4, column=1, sticky=NSEW)

#     def back(self):
#         self.window6.destroy()
#         self.fifth_window.window2.deiconify()

#     def open_arms_explain(self):
#         self.fifth_window.window6.withdraw()
#         ExplainArms(self.fifth_window)

# class ExplainArms:
#     def __init__(self, sixth_window):
#         self.sixth_window = sixth_window
#         self.window7 = Toplevel(self.sixth_window.window6)
#         self.sixth_window = self
#         self.window7.title("Workout App")
#         self.window7.geometry("900x700")
#         self.font_title = ("TKDefaultFont", 18, "bold")
#         self.font_customtkinter.CTkLabel = ("TKDefaultFont", 14, "bold")

#         Button(self.window7, text="Back", command=self.back).pack(padx=10, pady=10, side=BOTTOM)
#         Button(self.window7, text="Next", command=self.open_legs_explain).pack(padx=10, pady=10, side=BOTTOM)

#         frame1 = Frame(self.window7)
#         frame1.pack(padx=10, pady=10)
#         customtkinter.CTkLabel(frame1, text="Fourth Muscle Group", font= self.font_title).grid(row=1, column=1, sticky=NSEW)
#         customtkinter.CTkLabel(frame1, text= "Arms", font= self.font_title).grid(row=2, column=1, sticky=NSEW)

#         frame2 = Frame(self.window7)
#         frame2.pack(padx=10, pady=10)
#         customtkinter.CTkLabel(frame2, text="Arms consist of three main muscles\nwhich is\n Biceps, Triceps and Forearms", font= self.font_customtkinter.CTkLabel).grid(row=3, column=1, sticky=NSEW)

#         frame3 = Frame(self.window7)
#         frame3.pack(padx=10, pady=10)
#         image = Image.open("picture/armsanatomy.png")
#         image = image.resize((450, 550))
#         self.photo = ImageTk.PhotoImage(image)
#         customtkinter.CTkLabel(frame3, image=self.photo).grid(row=4, column=1, sticky=NSEW)

#     def back(self):
#         self.window7.destroy()
#         self.sixth_window.window2.deiconify()

#     def open_legs_explain(self):
#         self.sixth_window.window7.withdraw()
#         ExplainLegs(self.sixth_window)


# class ExplainLegs:
#     def __init__(self, seventh_window):
#         self.seventh_window = seventh_window
#         self.window8 = Toplevel(self.seventh_window.window7)
#         self.seventh_window = self
#         self.window8.title("Workout App")
#         self.window8.geometry("900x700")
#         self.font_title = ("TKDefaultFont", 18, "bold")
#         self.font_customtkinter.CTkLabel = ("TKDefaultFont", 14, "bold")

#         Button(self.window8, text="Back", command=self.back).pack(padx=10, pady=10, side=BOTTOM)

#         frame1 = Frame(self.window8)
#         frame1.pack(padx=10, pady=10)
#         customtkinter.CTkLabel(frame1, text="Fifth Muscle Group", font= self.font_title).grid(row=1, column=1, sticky=NSEW)
#         customtkinter.CTkLabel(frame1, text= "Legs", font= self.font_title).grid(row=2, column=1, sticky=NSEW)

#         frame2 = Frame(self.window8)
#         frame2.pack(padx=10, pady=10)
#         customtkinter.CTkLabel(frame2, text="Legs consist of three main muscles\nwhich is\n Quadriceps, Hamstrings and Calves", font= self.font_customtkinter.CTkLabel).grid(row=3, column=1, sticky=NSEW)

#         frame3 = Frame(self.window8)
#         frame3.pack(padx=10, pady=10)
#         image = Image.open("picture/legsanatomy.png")
#         image = image.resize((500, 600))
#         self.photo = ImageTk.PhotoImage(image)
#         customtkinter.CTkLabel(frame3, image=self.photo).grid(row=4, column=1, sticky=NSEW)

#     #back to main
#     def back(self):
#         self.window8.destroy()
#         self.seventh_window.window2.deiconify()

# import tkinter as tk

# class WorkoutApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Workout History")

#         self.workout_history = []

#         # UI elements
#         self.label_history = tk.Label(master, text="Workout History")
#         self.text_history = tk.Text(master, height=10, width=50, state=tk.DISABLED)
#         self.button_log_workout = tk.Button(master, text="Log Workout", command=self.log_workout)

#         # Pack UI elements
#         self.label_history.pack()
#         self.text_history.pack()
#         self.button_log_workout.pack()

#     def log_workout(self):
#         # Add your logic to log workout details (exercise, sets, reps, etc.)
#         workout_details = "Example Workout Details\nExercise: Squats\nSets: 3\nReps: 10"
#         self.workout_history.append(workout_details)

#         # Update the displayed workout history
#         self.update_history()

#     def update_history(self):
#         # Clear the text widget and display updated workout history
#         self.text_history.config(state=tk.NORMAL)
#         self.text_history.delete(1.0, tk.END)
#         for workout in self.workout_history:
#             self.text_history.insert(tk.END, f"{workout}\n\n")
#         self.text_history.config(state=tk.DISABLED)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = WorkoutApp(root)
#     root.mainloop()

# import tkinter as tk
# from tkinter import messagebox

# class WorkoutApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Login or Sign Up")

#         # User credentials (for simplicity; in a real app, use a database)
#         self.valid_username = "user"
#         self.valid_password = "pass"

#         # UI elements for login
#         self.label_username = tk.Label(master, text="Username:")
#         self.label_password = tk.Label(master, text="Password:")

#         self.entry_username = tk.Entry(master)
#         self.entry_password = tk.Entry(master, show="*")  # Show asterisks to hide the password

#         self.button_login = tk.Button(master, text="Login", command=self.authenticate_user)
#         self.button_signup = tk.Button(master, text="Sign Up", command=self.signup)

#         # Pack UI elements
#         self.label_username.pack()
#         self.entry_username.pack()
#         self.label_password.pack()
#         self.entry_password.pack()
#         self.button_login.pack()
#         self.button_signup.pack()

#     def authenticate_user(self):
#         # Get the entered username and password
#         entered_username = self.entry_username.get()
#         entered_password = self.entry_password.get()

#         # Check against valid credentials
#         if entered_username == self.valid_username and entered_password == self.valid_password:
#             # Successful login
#             messagebox.showinfo("Login Successful", "Welcome back!")

#             # After successful login, you can launch the main workout app
#             self.launch_workout_app()
#         else:
#             # Failed login
#             messagebox.showerror("Login Failed", "Invalid username or password")

#     def signup(self):
#         signup_window = tk.Toplevel(self.master)
#         signup_window.title("Sign Up")

#         # UI elements for sign up
#         label_new_username = tk.Label(signup_window, text="New Username:")
#         label_new_password = tk.Label(signup_window, text="New Password:")

#         entry_new_username = tk.Entry(signup_window)
#         entry_new_password = tk.Entry(signup_window, show="*")

#         button_create_account = tk.Button(signup_window, text="Create Account", command=lambda: self.create_account(entry_new_username.get(), entry_new_password.get(), signup_window))

#         # Pack UI elements for sign up
#         label_new_username.pack()
#         entry_new_username.pack()
#         label_new_password.pack()
#         entry_new_password.pack()
#         button_create_account.pack()

#     def create_account(self, new_username, new_password, signup_window):
#         # Add logic to create a new user account
#         # For simplicity, let's just display the information for now
#         messagebox.showinfo("Account Created", f"New Account Created!\nUsername: {new_username}\nPassword: {new_password}")

#         # You might want to store the new user credentials in a database

#         # Close the signup window
#         signup_window.destroy()

#     def launch_workout_app(self):
#         # Destroy the login window
#         self.master.destroy()

#         # Now, you can create an instance of the WorkoutAppMain and launch it
#         root = tk.Tk()
#         app = WorkoutAppMain(root)
#         root.mainloop()

# class WorkoutAppMain:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Workout App")

#         # Your workout app UI and functionality go here

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = WorkoutApp(root)
#     root.mainloop()


#  frame1 = Frame(self.window, width= 1000, height= 850, bg='white')
#         frame1.place(x=350, y=425, anchor= CENTER)
#         Label(frame1, text= "Welcome to Workout App", font= self.font_title, bg='white', fg="#57a1f8").place(x=500, y= 20)

#         # #first step
#         Label(frame1, text= "First Step: TDEE Calculator", font= self.font, bg='white', fg="#57a1f5").place(x=550, y= 65)
#         Label(frame1, text= "Learn How Many Calories You Burn Every Day", bg= 'white').place(x=525, y=100)

#         self.button1 = StringVar()
#         self.button1.set("Male") #default value

#         #choose gender
#         Label(frame1, text= "Gender", bg='white').place(x= 565, y= 150)
#         Radiobutton(frame1, variable= self.button1, value = "Male", bg='white').place(x= 625, y= 150)
#         Label(frame1, text="Male", bg='white').place(x= 655, y= 150)
#         Radiobutton(frame1, variable= self.button1, value= "Female", bg='white').place(x= 700, y= 150)
#         Label(frame1, text= "Female", bg='white').place(x= 725, y= 150)
#          frame1 = Frame(self.window)
#         frame1 = Frame(self.window, width= 1000, height= 850, bg='white')
#         frame1.place(x=350, y=425, anchor= CENTER)
#         Label(frame1, text= "Welcome to Workout App", font= self.font_title, bg='white', fg="#57a1f8").place(x=500, y= 20)

        # # #first step
        # Label(frame1, text= "First Step: TDEE Calculator", font= self.font, bg='white', fg="#57a1f5").place(x=550, y= 65)
        # Label(frame1, text= "Learn How Many Calories You Burn Every Day", bg= 'white').place(x=525, y=100)

        # self.button1 = StringVar()
        # self.button1.set("Male") #default value

        # #choose gender
        # Label(frame1, text= "Gender", bg='white').place(x= 555, y= 150)
        # Radiobutton(frame1, variable= self.button1, value = "Male", bg='white').place(x= 615, y= 150)
        # Label(frame1, text="Male", bg='white').place(x= 645, y= 150)
        # Radiobutton(frame1, variable= self.button1, value= "Female", bg='white').place(x= 690, y= 150)
        # Label(frame1, text= "Female", bg='white').place(x= 715, y= 150)


        # self.age = StringVar()
        # self.weight = DoubleVar()
        # self.height = DoubleVar()

        # #enter age, weight, height
        # Label(frame1, text= "Age", bg='white').place(x= 555, y= 200)
        # self.age_entry = Entry(frame1, textvariable= self.age, width=25, bg='white', borderwidth=0, highlightthickness=0, font=('Microsoft YaHei UI Light', 14))
        # self.age_entry.place(x= 615, y= 200)
        # self.age_entry.insert(0, "0")
        # self.age_entry.bind("<FocusIn>", self.on_age_entry_focusin)
        # self.age_entry.bind("<FocusOut>", self.on_age_entry_focusout)
        # Frame(frame1, width=200, height=2, bg='black').place(x= 610, y= 227)
        # Entry(frame1, textvariable= self.age, justify= RIGHT).place(x= 615, y= 200)
        
import tkinter as tk
from tkmacosx import Button

def change_border_color(event):
    frame.config(bg="red")  # Change the border color to red

def restore_border_color(event):
    frame.config(bg="black")  # Restore the border color to black

root = tk.Tk()

# Create a frame as a container for the button with border width set to zero
frame = tk.Frame(root, bg="black", bd=0)  # Set the initial border color and border width to zero
frame.pack(padx=10, pady=10)

# Create a button inside the frame
button = Button(frame, text="Click me!", borderless=True)

# Bind events to the button to change and restore the border color
button.bind("<Enter>", change_border_color)  # Hovering over the button
button.bind("<Leave>", restore_border_color)  # Leaving the button

button.pack(padx=20, pady=20)

root.mainloop()
