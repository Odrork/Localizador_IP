from tkinter import *

root = Tk()

label = Label(root, text="Entrada IP")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)


entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right", state="normal")

root.mainloop()
