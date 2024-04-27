import tkinter
import random
import time

# создаем окно
window = tkinter.Tk()

window.title("не парься!")

canvas = tkinter.Canvas(window, width=900, height=700)
canvas.pack()

colors = ("blue", "black", "coral", "cyan", "red", "green", "gold")

while True:
    x, y = random.randint(0, 700), random.randint(0, 700)
    for i, e in enumerate(range(150, 185, 5)):
        canvas.create_oval(x - e, y - e, x + e, y + e, outline=colors[i])
        window.update()
        time.sleep(0.05)

window.mainloop()


