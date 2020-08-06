"""
Main.py gets the data from the user in an easy to use gui
"""
import tkinter as tk
import math
import solver

root = tk.Tk()

root.title("Sliding Number Puzzle Solver")
root.geometry("500x700")
grid_frames = []
grid_entries = []
root.resizable(0,0)

def main():
    board = get_inputs()
    if board:
        solution = solver.find_solution(board)
        formatted_solution = " -> ".join(solution)
        create_solution_box(formatted_solution)
def clear_grid():
    for entry in grid_entries:
        entry.delete(0, 1000)

def create_solution_box(solution):
    box = tk.Toplevel(bg="#4ca1c3")
    box.title("Solution")
    box.geometry("300x300")

    solution_label = tk.Label(box,text=solution,fg="white",font="Fixedsys 15 bold",bg="#4ca1c3",pady=10,wraplength=250)
    solution_label.pack()

    dismiss_button = tk.Button(box,text="Dismiss",relief="flat",bg="#5a4c67",activebackground="#540101",fg="white",activeforeground="white",cursor="hand1",bd=0,highlightthickness=0,width=12,height=2,font="Fixedsys 10 bold",command=box.destroy)
    dismiss_button.pack()

def get_inputs():
    # Put inputs into a list
    values = []
    duplicate_check = []
    for i in range(3):
        values.append([])
    a = 0
    for entry in grid_entries:
        value = entry.get()
        if value == "":
            value = "0"
        values[a].append(value)
        duplicate_check.append(value)
        a+=1
        if a == 3:
            a = 0

    # Check for duplicate values
    for value in duplicate_check:
        if duplicate_check.count(value) > 1:
            return None
    return values


def validate_function(input):
    # Test if number is in the range of acceptable values
    acceptable = [""]
    for i in range(9):
        acceptable.append(str(i))
    if input in acceptable:
        return True
    else:
        return False

validation = root.register(validate_function)




def setup_gui():
    #Create widgets
    board_area = tk.Frame(root, height = 500, width = 500, bg="#517796")

    input_area = tk.Frame(root, height = 200, width = 500, bg="#4ca1c3")


    reset_button = tk.Button(input_area,text="Clear Spaces",relief="flat",bg="#b72b3d",activebackground="#540101",fg="white",activeforeground="white",cursor="hand1",bd=0,highlightthickness=0,width=12,height=2,font="Fixedsys 10 bold",command=clear_grid)

    find_button = tk.Button(input_area,text="Find Solution",relief="flat",bg="#5a4c67",activebackground="#540101",fg="white",activeforeground="white",cursor="hand1",bd=0,highlightthickness=0,width=12,height=2,font="Fixedsys 10 bold",command=main)

    #Add each widget to its layout position
    board_area.grid(column=0,row=0)
    board_area.grid_propagate(False)
    input_area.grid(column=0,row=1)
    input_area.grid_propagate(False)
    reset_button.place(relx=.5,rely=.3,anchor="center")
    find_button.place(relx=.5,rely=.6,anchor="center")


    setup_grid(board_area)

def setup_grid(board_area):
    global grid_frames
    global grid_entries
    for i in grid_frames:
        i.destroy()
    grid_frames = []
    grid_entries = []
    for i in range(3):
        for j in range(3):
            frame = tk.Frame(board_area,height=500/3,width=500/3,bg="#517796",highlightbackground="white",highlightthickness=2,highlightcolor="white")
            frame.grid(column=i,row=j)
            grid_frames.append(frame)
            entry = tk.Entry(frame,bg="#517796",font="Fixedsys 50 bold",fg="white",width=2,highlightcolor="white",insertbackground="white",justify="center",validate="key",vcmd=(validation, '%P'))
            entry.place(relx=.5,rely=.5,anchor="center")
            grid_entries.append(entry)

setup_gui()
root.mainloop()
