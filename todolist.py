import tkinter as tk
from tkinter import ttk, messagebox

# Function to add a task
def add_task():
    task_text = task_entry.get()
    if task_text != "":
        task_number = len(tasks_treeview.get_children()) + 1
        tasks_treeview.insert("", tk.END, values=(task_number, task_text, "Pending"))
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task
def delete_task():
    selected_task = tasks_treeview.selection()
    if selected_task:
        tasks_treeview.delete(selected_task)
        update_task_numbers()
    else:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to update task numbers after deletion
def update_task_numbers():
    for index, item in enumerate(tasks_treeview.get_children(), start=1):
        tasks_treeview.item(item, values=(index, tasks_treeview.item(item, "values")[1], tasks_treeview.item(item, "values")[2]))

# Function to mark a task as completed or pending
def toggle_task_status():
    selected_task = tasks_treeview.selection()
    if selected_task:
        current_status = tasks_treeview.item(selected_task, "values")[2]
        new_status = "Completed" if current_status == "Pending" else "Pending"
        tasks_treeview.item(selected_task, values=(tasks_treeview.item(selected_task, "values")[0], tasks_treeview.item(selected_task, "values")[1], new_status))
    else:
        messagebox.showwarning("Warning", "You must select a task to change its status.")

# Initialize main window
root = tk.Tk()
root.title("TO DO LIST")

# Set background color
root.configure(bg="LIGHT BLUE")

# Treeview to display tasks with task number and status
columns = ("Number", "Task", "Status")
tasks_treeview = ttk.Treeview(root, columns = columns, show = "headings")
tasks_treeview.heading("Number", text = "Sl No.")
tasks_treeview.heading("Task", text = "Task")
tasks_treeview.heading("Status", text = "Status")
tasks_treeview.column("Number", width = 70)
tasks_treeview.column("Task", width = 300)
tasks_treeview.column("Status", width = 100)
tasks_treeview.pack(pady = 20)

# Entry box to add tasks
task_entry = tk.Entry(root, width = 40)
task_entry.pack(pady = 10)

# Buttons
add_button = tk.Button(root, text="Add Task", width=15, command=add_task, bg="#5d737e", fg="white")
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task, bg="#5d737e", fg="white")
delete_button.pack(pady=5)

toggle_button = tk.Button(root, text="Toggle Status", width=15, command=toggle_task_status, bg="#5d737e", fg="white")
toggle_button.pack(pady=5)

# Run the main loop
root.mainloop()
