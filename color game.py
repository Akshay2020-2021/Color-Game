import random
import tkinter as tk


class Game:
    def __init__(self, root):
        self.__score = 0
        self.__text = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white"]
        self.__color = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white"]
        self.label_name = tk.Label(root, text="", font=("Helvetica", 50), bg="white")
        self.label_name.place(relx=0.5, rely=0.5, anchor="center")
    
    def updateGame(self):
        self.random_number_for_text = random.randint(0, 5)
        self.random_number_for_color = random.randint(0, 5)
        self.label_name.config(text=self.__text[self.random_number_for_text], fg=self.__color[self.random_number_for_color])

root = tk.Tk()
root.geometry("600x400")
root.config(bg="blue")
root.title("Color Game")


game = Game(root)


start_button = tk.Button(root, text="Start", command=game.updateGame, bg="black", fg="blue", relief="flat", padx=20, pady=10, font=("Helvetica", 20))
start_button.place(relx=0.5, rely=0.8, anchor="center")

root.mainloop()
