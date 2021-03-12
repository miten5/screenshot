import time
import pyautogui
import tkinter as tk


def takescreenshot():
    name = int(round(time.time() * 1000))
    name = "./screenshots/{}.png".format(name)
    time.sleep(1)
    img = pyautogui.screenshot(name)
    img.show()


root = tk.Tk()
root.title("Take screenshot")

# Tkinter windows size
app_width = 300
app_height = 250

# screen size for centralize application window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find center of screen application
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

# set application center to screen
root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

frame = tk.Frame(root)
frame.pack()

ssbutton = tk.Button(
    frame,
    text="Minimize and Take Screenshot",
    command=lambda: [root.wm_state("iconic"), takescreenshot()],
).pack(side=tk.LEFT)

close = tk.Button(frame, text="QUIT", command=quit).pack(side=tk.LEFT)

root.mainloop()
