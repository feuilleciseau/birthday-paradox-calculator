import tkinter as tk
from tkinter import ttk, messagebox
import birthday_paradox


class BirthdayParadoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Birthday Paradox Calculator")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # Title
        ttk.Label(self.root, text="Birthday Paradox Calculator", font=("Arial", 16)).pack(pady=10)

        # Main Frame
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(pady=10)

        # --- Row 1: From people → probability ---
        ttk.Label(frame, text="Number of people:").grid(column=0, row=0, sticky="w")
        self.people_entry = ttk.Entry(frame, width=10)
        self.people_entry.grid(column=1, row=0)

        ttk.Button(frame, text="Calculate Probability", command=self.compute_probability).grid(column=2, row=0, padx=5)
        self.prob_result_label = ttk.Label(frame, text="Probability: ---")
        self.prob_result_label.grid(column=3, row=0, padx=5)

        # --- Row 2: From probability → people ---
        ttk.Label(frame, text="Target probability (%):").grid(column=0, row=1, sticky="w", pady=10)
        self.prob_entry = ttk.Entry(frame, width=10)
        self.prob_entry.grid(column=1, row=1)

        ttk.Button(frame, text="Calculate People", command=self.compute_people_count).grid(column=2, row=1, padx=5)
        self.people_result_label = ttk.Label(frame, text="Required people: ---")
        self.people_result_label.grid(column=3, row=1, padx=5)

        # --- Graph Button ---
        ttk.Button(self.root, text="Show Graph", command=birthday_paradox.show_graph).pack(pady=20)

    def compute_probability(self):
        try:
            n = int(self.people_entry.get())
            if n < 1:
                raise ValueError
            prob = birthday_paradox.calculate_shared_birthday_probability(n) * 100
            self.prob_result_label.config(text=f"Probability: {prob:.2f} %")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive integer.")

    def compute_people_count(self):
        try:
            p = float(self.prob_entry.get())
            if not (0 < p < 100):
                raise ValueError
            group_size = birthday_paradox.calculate_group_size_from_probability(p / 100)
            self.people_result_label.config(text=f"Required people: {group_size}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter a valid probability between 0 and 100.")


if __name__ == "__main__":
    root = tk.Tk()
    app = BirthdayParadoxApp(root)
    root.mainloop()
