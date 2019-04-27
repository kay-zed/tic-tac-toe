from tkinter import *
from tkinter import messagebox

class Application(Frame):
    
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.clicked = True

    def create_widgets(self):
        Label(self, text="Tic Tac Toe").grid(row=0, sticky=W)
        Label(self, text="Player 1").grid(row=1, sticky=W)
        self.player1 = Entry(self)
        self.player1.grid(row=2, sticky=W)

        Label(self, text="Player 2").grid(row=3, sticky=W)
        self.player2 = Entry(self)
        self.player2.grid(row=4, sticky=W)

        Button(self, text="Start Game", command=self.start_game).grid(row=5, sticky=W)
    
    def start_game(self):
        self.game = Tk()
        self.game.title("Tic Tac Toe")
        buttons = StringVar()

        self.btn_1 = Button(self.game, relief=SUNKEN, font=('arial',10),
                            command=lambda: self.show_x_o(self.btn_1), text="", width=9, height=6)
        self.btn_1.grid(row=0, column=0, sticky=W)
        self.btn_2 = Button(self.game, relief=SUNKEN, font=('arial',10),
                            command=lambda: self.show_x_o(self.btn_2), text="", width=9, height=6)
        self.btn_2.grid(row=0, column=1, sticky=W)
        self.btn_3 = Button(self.game, relief=SUNKEN, font=('arial',10),
                            command=lambda: self.show_x_o(self.btn_3), text="", width=9, height=6)
        self.btn_3.grid(row=0, column=2, sticky=W)
        self.btn_4 = Button(self.game, relief=SUNKEN, font=('arial',10),
                            command=lambda: self.show_x_o(self.btn_4), text="", width=9, height=6)
        self.btn_4.grid(row=1, column=0, sticky=W)
        self.btn_5 = Button(self.game, relief=SUNKEN, font=('arial',10),
                            command=lambda: self.show_x_o(self.btn_5), text="", width=9, height=6)
        self.btn_5.grid(row=1, column=1, sticky=W)
        self.btn_6 = Button(self.game, relief=SUNKEN, font=('arial',10),
                            command=lambda: self.show_x_o(self.btn_6), text="", width=9, height=6)
        self.btn_6.grid(row=1, column=2, sticky=W)
        self.btn_7 = Button(self.game, relief=SUNKEN, font=('arial',10),
                            command=lambda: self.show_x_o(self.btn_7), text="", width=9, height=6)
        self.btn_7.grid(row=2, column=0, sticky=W)
        self.btn_8 = Button(self.game, relief=SUNKEN, font=('arial',10),
                            command=lambda: self.show_x_o(self.btn_8), text="", width=9, height=6)
        self.btn_8.grid(row=2, column=1, sticky=W)
        self.btn_9 = Button(self.game, relief=SUNKEN, font=('arial',10),
                            command=lambda: self.show_x_o(self.btn_9), text="", width=9, height=6)
        self.btn_9.grid(row=2, column=2, sticky=W)

    def show_x_o(self, btn):
        if btn['text'] == "" and self.clicked == True:
            btn['text'] = 'X'
            self.clicked = False
        elif btn['text'] == "" and self.clicked == False:
            btn['text'] = 'O'
            self.clicked = True
        self.check_win()
    
    def check_win(self):
        btns = [self.btn_1, self.btn_2, self.btn_3,
                self.btn_4, self.btn_5, self.btn_6,
                self.btn_7, self.btn_8, self.btn_9,]
        
        for i, j, k in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
            if btns[i]['text'] == btns[j]['text'] == btns[k]['text'] == 'X':
                self.show_win(self.player1.get())
            if btns[i]['text'] == btns[j]['text'] == btns[k]['text'] == 'O':
                self.show_win(self.player2.get())
            
    def show_win(self, player):
        self.win = Tk()
        t = player + " wins!"
        Label(self.win, text=t, font=(50)).grid(row=0)
        self.game.destroy()

        Button(self.win, text='Play Again', command=self.start_game).grid(row=1, column=0)
        Button(self.win, text="End Game", command=exit).grid(row=1, column=1)


root = Tk()
root.title("Tic Tac Toe")
app = Application(root)
root.mainloop()