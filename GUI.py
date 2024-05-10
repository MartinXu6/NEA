import tkinter as tk


def main_game_window():
    start_window.destroy()
    game_window = tk.Tk()
    game_window.iconbitmap("Images/game_icon.ico")
    game_window.geometry("1000x600")
    game_window.title("Zero Point One")
    game_window.mainloop()


def settings_window():
    settings = tk.Tk()
    settings.geometry("500x300")
    settings.title("settings")
    settings.iconbitmap("Images/setting_icon.ico")
    settings.mainloop()


start_window = tk.Tk()
start_window.geometry("1000x600")
start_window.title("MENU")
start_window.iconbitmap("Images/game_icon.ico")
start = tk.Button(start_window, text="START", bg="red", height="10", width="20", command=main_game_window)
Quit = tk.Button(start_window, text="QUIT", bg="blue", height="10", width="20", command=start_window.destroy)
setting = tk.Button(start_window,text="SETTINGS", bg="green", height="10", width="20", command=settings_window)
start.pack()
setting.pack()
Quit.pack()
start_window.mainloop()
