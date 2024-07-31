import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

class StringDifferenceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("String Difference Calculator")
        self.strings = []
        self.compare_again_button = None

        tk.Button(root, text="Direct Input", command=self.get_input_directly).pack(pady=10)
        tk.Button(root, text="Read from File", command=self.get_input_from_file).pack(pady=10)

    def get_input_directly(self):
        num_strings = simpledialog.askinteger("Input", "How many strings do you want to enter?", minvalue=2)
        if num_strings:
            for i in range(num_strings):
                string = simpledialog.askstring("Input", f"Enter string {i+1}:")
                if string:
                    self.strings.append(string)
            self.show_string_selection()

    def get_input_from_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.strings = [line.strip() for line in file if line.strip()]
            self.show_string_selection()

    def show_string_selection(self):
        if len(self.strings) < 2:
            messagebox.showerror("Error", "At least two strings are required.")
            return

        selection_window = tk.Toplevel(self.root)
        selection_window.title("Select Strings")

        tk.Label(selection_window, text="Select two strings to compare:").pack(pady=10)

        listbox = tk.Listbox(selection_window, selectmode=tk.MULTIPLE, height=10)
        for i, string in enumerate(self.strings):
            listbox.insert(tk.END, f"{i+1}: {string[:30]}...")
        listbox.pack(pady=10)

        def on_select():
            selections = listbox.curselection()
            if len(selections) != 2:
                messagebox.showerror("Error", "Please select exactly two strings.")
            else:
                string1 = self.strings[selections[0]]
                string2 = self.strings[selections[1]]
                selection_window.destroy()
                self.calculate_differences(string1, string2)

        tk.Button(selection_window, text="Compare", command=on_select).pack(pady=10)

    def calculate_differences(self, string1, string2):
        count = 0
        min_length = min(len(string1), len(string2))

        for x in range(min_length):
            if string1[x] != string2[x]:
                count += 1

        count += abs(len(string1) - len(string2))

        result = f"There are {count} differences"
        if len(string1) != len(string2):
            result += "\nWarning: The input strings have different lengths."
        
        messagebox.showinfo("Result", result)
        self.show_compare_again_button()

    def show_compare_again_button(self):
        if not self.compare_again_button:
            self.compare_again_button = tk.Button(self.root, text="Compare Again", command=self.show_string_selection)
            self.compare_again_button.pack(pady=10)

root = tk.Tk()
app = StringDifferenceCalculator(root)
root.mainloop()