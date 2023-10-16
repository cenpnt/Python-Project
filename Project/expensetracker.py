#pip3 install tkcalendar
#pip3 install matplotlib
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkcalendar import Calendar
import numpy as np

class Main:
    def __init__(self):
        self.window = Tk()
        self.window.title("Expense Tracker")

        menubar = Menu(self.window)
        self.window.config(menu=menubar)

        list_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=list_menu)
        list_menu.add_command(label="Open")
        list_menu.add_command(label="Save")
        list_menu.add_separator()
        list_menu.add_command(label="Exit", command=self.window.quit)

        self.button = StringVar()
        
        self.frame0 = Frame(self.window)
        self.frame0.pack(padx=10, pady=10)
        Label(self.frame0, text="Please select income or expense").grid(row=1, column=1, sticky="nswe")
        income = Radiobutton(self.frame0, variable=self.button, value="Income")
        income.grid(row=1, column=2)
        Label(self.frame0, text="Income").grid(row=1, column=3, sticky="nswe")
        expense = Radiobutton(self.frame0, variable=self.button, value="Expense")
        expense.grid(row=1, column=4)
        Label(self.frame0, text="Expense").grid(row=1, column=5, sticky="nswe")
        Button(self.frame0, text= "Select Date", command=self.open_calendar).grid(row=1, column=6, sticky="nswe")

        self.enter = StringVar()
        self.selected_date = StringVar()

        frame1 = Frame(self.window)
        frame1.pack(padx=10, pady=10)
        Label(frame1, text="Enter the amount of money").grid(row=1, column=1)
        Entry(frame1, textvariable=self.enter, justify= RIGHT).grid(row=1, column=2, sticky="nswe")
        Button(frame1, text="Submit", command=self.check_type).grid(row=1, column=3, sticky="nswe")
        self.button.set("Income") #default value
        Label(frame1, text="Date").grid(row=5, column=1, sticky="nswe")
        Label(frame1, textvariable= self.selected_date).grid(row=5, column=2, sticky="nswe")
        Button(frame1, text= "Stored Data", command= self.stored_data).grid(row=5, column=3, sticky="nswe")

        self.income = DoubleVar()
        self.expense = DoubleVar()
        # self.income.set(2000) #assuming that when opening the bank account, the initial amount is 2000
        self.income_all = 0.0
        self.expense_all = 0.0
        self.income_list = []
        self.expense_list = []
        self.month = ""
        self.month_list = []

        Label(frame1, text= "Income amount").grid(row=2, column=1, sticky="nswe")
        Label(frame1, textvariable=self.income).grid(row=2, column=2, sticky="nswe")
        Label(frame1, text="Expense amount").grid(row=3, column=1, sticky="nswe")
        Label(frame1, textvariable=self.expense).grid(row=3, column=2, sticky="nswe")
        Button(frame1, text="Clear", command= self.clear).grid(row=3, column=3, sticky="nswe")

        frame2 = Frame(self.window)
        frame2.pack(padx=10, pady=10)
        Button(frame2, text= "Bar Graph", command= self.bar_graph).grid(row=4, column=1, sticky="nswe")
        Button(frame2, text= "Pie Chart").grid(row=4, column=2, sticky="nswe")
        Button(frame2, text= "Line Graph").grid(row=4, column=3, sticky="nswe")

        self.window.mainloop()

    def check_type(self):
        try:
            self.value = float(self.enter.get())
            if self.button.get() == "Income":
                self.income_all = self.income.get() + self.value
                self.income.set(self.income_all)
            elif self.button.get() == "Expense":
                self.expense_all = self.expense.get() + self.value
                self.expense.set(self.expense_all)
            self.enter.set("")  # Clear the input Entry
        except ValueError:
            self.enter.set("")

    def clear(self):
        self.income.set(0.0)
        self.expense.set(0.0)
        self.selected_date.set("")

    def open_calendar(self):
        self.calendar_window = Toplevel(self.window) #create a new window for picking date
        self.calendar_window.title("Calendar")

        calendar = Calendar(self.calendar_window, font= "Arial 14", selectmode="day", year=2023, month=9, day=1, showweeknumbers=False, firstweekday="sunday")
        calendar.pack(padx=10, pady=10)
        Button(self.calendar_window, text="Get Date", command= lambda: self.get_month(calendar)).pack()

    def get_month(self, calendar):
        self.selected_date.set(calendar.get_date())
        month_number = calendar.get_date().split("/")[0]
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        self.month = months[int(month_number) - 1]
        self.calendar_window.destroy()

    def stored_data(self):
        self.income_list.append(self.income_all)
        self.expense_list.append(self.expense_all)
        self.month_list.append(self.month)

    def bar_graph(self):
            bar_width = 0.35
            x = np.arange(len(self.month_list))
            fig, ax = plt.subplots(figsize=(8, 5), dpi=100)
            ax.bar(x - bar_width / 2, self.expense_list, bar_width, color= "orange", label="Expense")
            ax.bar(x + bar_width / 2, self.income_list, bar_width, label="Income")
            ax.set_title("Income and Expense")
            ax.set_xlabel("Month")
            ax.set_xticks(x)
            ax.set_xticklabels(self.month_list)
            ax.set_ylabel("Amount")
            ax.legend()
            ax.autoscale()
            plt.tight_layout()
            plt.show()

Main()