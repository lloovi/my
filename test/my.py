import tkinter
import random
import time

# window = tkinter.Tk()
# создаем холст и размещаем его в окне
# canvas = tkinter.Canvas(window, width=800, height=700)
# canvas.pack()
# colors = ("blue", "black", "coral", "cyan", "red", "green", "gold")

number = random.randint(1, 10)
name = input("Как тебя зовут? ")
print(name + ", приветствую!")
time.sleep(2)
print("Отгадай число от 1 до 10:")
time.sleep(2)
print("У тебя есть три попытки!")
for i in range(3):
    num = int(input())
    if number > num:
        print("ммм, принято..")
        time.sleep(3)
        print("Загаданное число больше")
    elif number < num:
        print("ммм, принято..")
        time.sleep(3)
        print("Загаданное число меньше")
    else:
        print("Поздравляю тебя!")
        time.sleep(2)
        print("Вы выиграли!")
        break

        window = tkinter.Tk()
        canvas = tkinter.Canvas(window, width=800, height=700)
        canvas.pack()
        colors = ("blue", "black", "coral", "cyan", "red", "green", "gold")
        while True:
            x, y = random.randint(0, 800), random.randint(0, 700)
            for i, e in enumerate(range(150, 181, 5)):
                canvas.create_oval(x - e, y - e, x + e, y + e, outline=colors[i])
                window.update()
                time.sleep(0.05)

        window.mainloop()

        # break
else:
    print("Ну, не судьба")









