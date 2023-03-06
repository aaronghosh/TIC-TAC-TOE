from tkinter import *

class TicTacToe:

    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        self.current_player = 'X'
        self.board = [''] * 9

        self.buttons = []
        for i in range(9):
            button = Button(master, text='', width=3, height=1, command=lambda i=i: self.move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        self.message = Label(master, text='Player ' + self.current_player + ' to move')
        self.message.grid(row=3, column=0, columnspan=3)

    def move(self, index):
        if self.board[index] == '':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'
            self.message.config(text='Player ' + self.current_player + ' to move')
            self.check_win()

    def check_win(self):
        for i in range(3):
            if self.board[i*3] == self.board[i*3+1] == self.board[i*3+2] != '':
                self.message.config(text='Player ' + self.current_player + ' wins')
                self.disable_buttons()
                return
            if self.board[i] == self.board[i+3] == self.board[i+6] != '':
                self.message.config(text='Player ' + self.current_player + ' wins')
                self.disable_buttons()
                return
        if self.board[0] == self.board[4] == self.board[8] != '':
            self.message.config(text='Player ' + self.current_player + ' wins')
            self.disable_buttons()
            return
        if self.board[2] == self.board[4] == self.board[6] != '':
            self.message.config(text='Player ' + self.current_player + ' wins')
            self.disable_buttons()
            return
        if '' not in self.board:
            self.message.config(text='Draw')
            self.disable_buttons()
            return

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=DISABLED)

root = Tk()
game = TicTacToe(root)
root.mainloop()
