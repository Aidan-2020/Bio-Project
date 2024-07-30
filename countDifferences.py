import tkinter as tk
from tkinter import filedialog, messagebox

def GetInputDirectlyFromUser():
    window = tk.Toplevel(root)
    window.title("Enter Strings")
    
    tk.Label(window, text="Enter the first string:").pack()
    entry1 = tk.Entry(window, width=50)
    entry1.pack()
    
    tk.Label(window, text="Enter the second string:").pack()
    entry2 = tk.Entry(window, width=50)
    entry2.pack()
    
    def submit():
        global string1, string2
        string1 = entry1.get()
        string2 = entry2.get()
        window.destroy()
        calculate_differences()
    
    tk.Button(window, text="Submit", command=submit).pack()

def GetInputFromFile():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            global string1, string2
            string1 = file.readline().strip()
            string2 = file.readline().strip()
        calculate_differences()

def calculate_differences():
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

root = tk.Tk()
root.title("String Difference Calculator")

tk.Button(root, text="Direct Input", command=GetInputDirectlyFromUser).pack(pady=10)
tk.Button(root, text="Read from File", command=GetInputFromFile).pack(pady=10)

root.mainloop()