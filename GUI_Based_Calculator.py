import tkinter as tk
import math


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.equation = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self.root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="white", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        btns_frame = tk.Frame(self.root, width=400, height=450, bg="grey")
        btns_frame.pack()

        # First row
        tk.Button(btns_frame, text="C", fg="black", width=20, height=3, bd=0, bg="#eee", cursor="hand2", command=self.clear).grid(row=0, column=0, columnspan=2)
        tk.Button(btns_frame, text="DEL", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=self.delete).grid(row=0, column=2)
        tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.click("/")).grid(row=0, column=3)

        # Second row
        tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("7")).grid(row=1, column=0)
        tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("8")).grid(row=1, column=1)
        tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("9")).grid(row=1, column=2)
        tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.click("*")).grid(row=1, column=3)

        # Third row
        tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("4")).grid(row=2, column=0)
        tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("5")).grid(row=2, column=1)
        tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("6")).grid(row=2, column=2)
        tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.click("-")).grid(row=2, column=3)

        # Fourth row
        tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("1")).grid(row=3, column=0)
        tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("2")).grid(row=3, column=1)
        tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("3")).grid(row=3, column=2)
        tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.click("+")).grid(row=3, column=3)

        # Fifth row
        tk.Button(btns_frame, text="0", fg="black", width=22, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("0")).grid(row=4, column=0, columnspan=2)
        tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.click(".")).grid(row=4, column=2)
        tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=self.calculate).grid(row=4, column=3)

        # Scientific Function Buttons
        tk.Button(btns_frame, text="sin", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("math.sin(math.radians(")).grid(row=5, column=0)
        tk.Button(btns_frame, text="cos", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("math.cos(math.radians(")).grid(row=5, column=1)
        tk.Button(btns_frame, text="tan", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("math.tan(math.radians(")).grid(row=5, column=2)
        tk.Button(btns_frame, text="log", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("math.log(")).grid(row=5, column=3)

        # More Scientific Functions
        tk.Button(btns_frame, text="√", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("math.sqrt(")).grid(row=6, column=0)
        tk.Button(btns_frame, text="π", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("math.pi")).grid(row=6, column=1)
        tk.Button(btns_frame, text="e", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("math.e")).grid(row=6, column=2)
        tk.Button(btns_frame, text="^", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click("**")).grid(row=6, column=3)

    def click(self, item):
        """Handle button click and update the input field."""
        self.equation += str(item)
        self.input_text.set(self.equation)

    def delete(self):
        """Delete the last character from the input."""
        self.equation = self.equation[:-1]
        self.input_text.set(self.equation)

    def clear(self):
        """Clear the input field."""
        self.equation = ""
        self.input_text.set("")

    def calculate(self):
        """Evaluate the entered equation."""
        try:
            # Check for incomplete scientific functions and close them
            if 'math.sin(math.radians(' in self.equation or 'math.cos(math.radians(' in self.equation or 'math.tan(math.radians(' in self.equation:
                self.equation += '))'
            elif 'math.log(' in self.equation or 'math.sqrt(' in self.equation:
                self.equation += ')'
            result = str(eval(self.equation))
            self.input_text.set(result)
            self.equation = result
        except:
            self.input_text.set("Error")
            self.equation = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
