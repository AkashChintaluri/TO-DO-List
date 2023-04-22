from tkinter import *
from tkinter import ttk
import tkinter.messagebox

window = Tk()
window.title("ODSHACK'23 To-Do List")
window.configure(bg="light blue")

# Style
style = ttk.Style(window)
style.configure("TButton", font=("Helvetica", 12), foreground="black")
style.configure("TLabel", font=("Helvetica", 12))

# Frame
frame_task = Frame(window, bg="grey")
frame_task.pack(padx=20, pady=20)

# Listbox
listbox_task = Listbox(frame_task, bg="white", fg="black", height=15, width=50, font=("Helvetica", 12))
listbox_task.pack(side=LEFT)

scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Functions
def entertask():
    # A new window to pop up to take input
    input_text = ""

    def add():
        input_text = entry_task.get(1.0, "end-1c")
        deadline_text = deadline_entry.get()
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            if deadline_text != "":
                input_text += f" (Deadline: {deadline_text})"
            listbox_task.insert(END, input_text)
            # close the root1 window
            root1.destroy()

    root1 = Tk()
    root1.title("Add task")
    entry_task = Text(root1, width=40, height=4, font=("Helvetica", 12))
    entry_task.pack(pady=10)

    deadline_label = ttk.Label(root1, text="Deadline (optional):")
    deadline_label.pack(pady=5)

    deadline_entry = ttk.Entry(root1, font=("Helvetica", 12))
    deadline_entry.pack(pady=5)

    button_temp = ttk.Button(root1, text="Add task", command=add)
    button_temp.pack(pady=10)
    root1.mainloop()


def deletetask():
    # selects the selected item and then deletes it
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])


def markcompleted():
    marked = listbox_task.curselection()
    temp = marked[0]
    temp_marked = listbox_task.get(marked)
    temp_marked = temp_marked + " ✔"
    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)


# Buttons
entry_button = ttk.Button(window, text="Add task", command=entertask)
entry_button.pack(pady=0)

delete_button = ttk.Button(window, text="Delete selected task", command=deletetask)
delete_button.pack(pady=0)

mark_button = ttk.Button(window, text="Mark as completed", command=markcompleted)
mark_button.pack(pady=10)

# Set anchor parameter to "center" to center the tasks in the listbox
listbox_task.pack(side=LEFT, anchor="center")

window.mainloop()
