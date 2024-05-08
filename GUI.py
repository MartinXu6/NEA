import tkinter as tk

window = tk.Tk()
window.geometry("400x500")
start = tk.Button(text="start", bg="red",height="5",width="10")
quit = tk.Button(window, text="quit",bg="blue",height="5",width="10",command=window.destroy)
start.pack()
quit.pack()
window.mainloop()