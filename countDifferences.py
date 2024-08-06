import customtkinter as ctk
from tkinter import filedialog, messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class StringDifferenceCalculator:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("String Difference Calculator")
        self.root.geometry("500x600")
        self.strings = []
        self.checkboxes = []
        self.selected_strings = []

        self.create_widgets()

    def create_widgets(self):
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(self.main_frame, text="String Difference Calculator", font=("Roboto", 24)).pack(pady=10)

        self.input_frame = ctk.CTkFrame(self.main_frame)
        self.input_frame.pack(pady=10, fill="x")

        ctk.CTkButton(self.input_frame, text="Direct Input", command=self.get_input_directly).pack(side="left", padx=10, expand=True)
        ctk.CTkButton(self.input_frame, text="Read from File", command=self.get_input_from_file).pack(side="right", padx=10, expand=True)

        self.strings_frame = ctk.CTkScrollableFrame(self.main_frame, height=300)
        self.strings_frame.pack(pady=10, fill="both", expand=True)

        self.compare_button = ctk.CTkButton(self.main_frame, text="Compare Strings", command=self.compare_selected_strings, state="disabled")
        self.compare_button.pack(pady=10)

        self.theme_switch = ctk.CTkSwitch(self.main_frame, text="Dark Mode", command=self.toggle_theme)
        self.theme_switch.pack(pady=10)

    def toggle_theme(self):
        ctk.set_appearance_mode("Dark" if self.theme_switch.get() == 1 else "Light")

    def get_input_directly(self):
        num_strings = ctk.CTkInputDialog(text="How many strings do you want to enter?", title="Input").get_input()
        if num_strings and num_strings.isdigit() and int(num_strings) >= 2:
            self.strings = []
            for i in range(int(num_strings)):
                string = ctk.CTkInputDialog(text=f"Enter string {i+1}:", title="Input").get_input()
                if string:
                    self.strings.append(string)
            self.update_string_list()

    def get_input_from_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.strings = [line.strip() for line in file if line.strip()]
            self.update_string_list()

    def update_string_list(self):
        for widget in self.strings_frame.winfo_children():
            widget.destroy()
        self.checkboxes = []
        self.selected_strings = []

        for i, string in enumerate(self.strings):
            checkbox = ctk.CTkCheckBox(self.strings_frame, text=f"{i+1}: {string[:30]}...", command=self.update_selection)
            checkbox.pack(anchor="w", pady=2)
            self.checkboxes.append(checkbox)

        self.compare_button.configure(state="normal" if len(self.strings) >= 2 else "disabled")

    def update_selection(self):
        self.selected_strings = [i for i, cb in enumerate(self.checkboxes) if cb.get() == 1]
        
        if len(self.selected_strings) > 2:
            for i, cb in enumerate(self.checkboxes):
                if i not in self.selected_strings[:2]:
                    cb.deselect()
            self.selected_strings = self.selected_strings[:2]

        self.compare_button.configure(state="normal" if len(self.selected_strings) == 2 else "disabled")

    def compare_selected_strings(self):
        if len(self.selected_strings) != 2:
            messagebox.showerror("Error", "Please select exactly two strings.")
            return

        string1 = self.strings[self.selected_strings[0]]
        string2 = self.strings[self.selected_strings[1]]
        self.calculate_differences(string1, string2)

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

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = StringDifferenceCalculator()
    app.run()