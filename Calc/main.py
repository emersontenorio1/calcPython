from tkinter import *


class Calc:

    def __init__(self):
        self.window = Tk()
        self.window.title("Calc")
        self.window.resizable(width=False, height=False)
        self.screen_numbers = Entry(self.window, font="arial 20 bold", bg="#080003", fg="white", width=20)
        self.screen_numbers.pack()
        self.frame = Frame(self.window)
        self.frame.pack()
        self.create_buttons()
        self.create_operator_buttons()
        self.create_clear_button()
        self.create_equal_button()

        self.window.mainloop()

    def create_buttons(self):
        button_texts = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']

        row, col = 0, 0
        for text in button_texts:
            button = Button(self.frame, bg="orange", bd=0, text=text, width=5, height=2, command=lambda
                            t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col == 3:
                col = 0
                row += 1

    def create_operator_buttons(self):
        operator_texts = ['+', '-', '*', '/']

        row, col = 0, 3
        for text in operator_texts:
            button = Button(self.frame, bg="lightblue", bd=0, text=text, width=5, height=2,
                            command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

            row += 1

    def create_clear_button(self):
        clear_button = Button(self.frame, bg="lightblue", bd=0, text="C", width=5, height=2, command=self.clear_display)
        clear_button.grid(row=3, column=1, columnspan=3, padx=5, pady=5)

    def create_equal_button(self):
        equal_button = Button(self.frame, bg="lightblue", bd=0, text="=", width=5, height=2, command=self.calculate)
        equal_button.grid(row=3, column=1, padx=5, pady=5)

    def on_button_click(self, value):
        current_text = self.screen_numbers.get()

        if current_text == "0":
            self.screen_numbers.delete(0, 'end')
            self.screen_numbers.insert('end', value)
        else:
            self.screen_numbers.insert('end', value)

    def calculate(self):
        result = eval(self.screen_numbers.get())
        self.screen_numbers.delete(0, END)
        self.screen_numbers.insert(0, str(result))

    def clear_display(self):
        self.screen_numbers.delete(0, 'end')
        self.screen_numbers.insert('end', '')


if __name__ == "__main__":
    Calc()
