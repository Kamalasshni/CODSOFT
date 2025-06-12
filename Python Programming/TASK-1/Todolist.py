import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple To-Do List")

        self.tasks = []

        # Frame to hold everything
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Task entry box
        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.grid(row=0, column=0)

        # Button to add task
        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1)

        # Listbox to show tasks
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, pady=10)

        # Buttons for actions
        self.complete_button = tk.Button(self.frame, text="Mark Done", command=self.mark_done)
        self.complete_button.grid(row=2, column=0, sticky='w')

        self.delete_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, sticky='e')

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.task_entry.delete(0, tk.END)
            self.update_listbox()
        else:
            messagebox.showwarning("Wait!", "You forgot to type a task.")

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            self.update_listbox()
        else:
            messagebox.showinfo("Hmm", "Click on a task to mark it done.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            del self.tasks[selected[0]]
            self.update_listbox()
        else:
            messagebox.showinfo("Oops", "Pick a task to delete.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["done"] else "✗"
            self.task_listbox.insert(tk.END, f"[{status}] {task['task']}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
