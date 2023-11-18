import time
from tkinter import *
import random
from tkinter import colorchooser


def next_players_turn(row, column):
    global player
    if buttons[row][column]['text'] == '' and check_winner() is False:
        if player == players[0]:

            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]

                label.config(text=((players[1]) + ' turn'))

            elif check_winner() is True:
                label1.pack_forget()
                label.config(text=(players[0] + ' won'), font=('comic sans', 20))
            elif check_winner() == 'Tie!':
                label1.pack_forget()
                label.config(text=('Tie!'), font=('comic sans', 20))
        else:

            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]

                label.config(text=(players[0] + ' turn'))

            elif check_winner() is True:
                label1.pack_forget()
                label.config(text=(players[1] + ' won'), font=('comic sans', 20))
            elif check_winner() == 'Tie!':
                label1.pack_forget()
                label.config(text='Tie!', font=('comic sans', 20))


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg='cyan')
            buttons[row][1].config(bg='cyan')
            buttons[row][2].config(bg='cyan')
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg='cyan')
            buttons[1][column].config(bg='cyan')
            buttons[2][column].config(bg='cyan')
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg='cyan')
        buttons[1][1].config(bg='cyan')
        buttons[2][2].config(bg='cyan')
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg='cyan')
        buttons[1][1].config(bg='cyan')
        buttons[2][0].config(bg='cyan')
        return True
    elif check_spaces() is False:
        buttons[0][0].config(bg='cyan')
        buttons[0][1].config(bg='lime')
        buttons[0][2].config(bg='purple')
        buttons[1][0].config(bg='pink')
        buttons[1][1].config(bg='grey')
        buttons[1][2].config(bg='gold')
        buttons[2][0].config(bg='blue')
        buttons[2][1].config(bg='yellow')
        buttons[2][2].config(bg='orange')
        return 'Tie!'







    else:
        return False


def check_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != '':
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


def restart():
    global player

    player = random.choice(players)

    label.config(text=player + ' turn')
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text='', bg='#F0F0F0')


def change_color():
    color = colorchooser.askcolor()
    window.config(background=color[1])


window = Tk()
window.title('Tic Tac Toe')
icon = PhotoImage(file = 'tic-tac-toe.png')
window.iconphoto(True,icon)
label1 = Label(window, text='tic-tac-toe', font=('comic sans', 20))
label1.pack()

players = ['O', 'X']
player = random.choice(players)

label = Label(window, text=str(player) + ' turn', font=('comic sans', 30))
label.pack()

button = Button(window, text='RESTART', command=restart, font=('comic sans', 20, 'bold'), fg='red', bg='yellow')
button.pack()

change_color = Button(window, text='Change background color', command=change_color, font=('comic sans', 10, 'bold'),
                      fg='blue', bg='light yellow')
change_color.place(x=500, y=0)

frame = Frame(window)
frame.pack()

print(player)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text='', font=('comic sans', 40), width=8, height=3,
                                      command=lambda row=row, column=column: next_players_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()