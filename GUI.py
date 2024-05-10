import tkinter as tk


def new_window():
    window.destroy()
    window1 = tk.Tk()
    window1.geometry("400x500")
    window1.mainloop()


window = tk.Tk()
window.geometry("400x500")
start = tk.Button(text="START", bg="red", height="5", width="10", command=new_window)
Quit = tk.Button(window, text="QUIT", bg="blue", height="5", width="10", command=window.destroy)
start.pack()
Quit.pack()
window.mainloop()
