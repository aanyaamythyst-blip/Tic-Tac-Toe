import tkinter as tk
from tkinter import messagebox, simpledialog
Board = [""]*9
CurrentPlayer = "X"
Player1 = simpledialog.askstring("Player1","Enter your name: ")
Player2 = simpledialog.askstring("Player2","Enter your name: ")
Number = simpledialog.askinteger("Answer","How many games would you like to play (Best of how many..)")
WinNumber = messagebox.showinfo("TicTacToe",f"The total number of rounds will be {Number}\nFirst to reach {Number//2+1} is the winner!")
Score = {"X":0, "O":0}
roundover = False
def CheckWinner():
    WinCombos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in WinCombos:
        if Board[a]==Board[b]==Board[c]!="":
          return True
    return False

def ResetBoard():
   global Board, CurrentPlayer
   Board = [""]*9
   CurrentPlayer = "X"
   for i in Buttons:
      i.config(text="")


def click(i):
   global CurrentPlayer,Score,roundover
   if Board[i]=="" and not CheckWinner():
      Board[i]=CurrentPlayer
      Buttons[i].config(text=CurrentPlayer)
      Winner = CheckWinner()
      roundover=True
      if Winner:
         messagebox.showinfo("GameOver",f"Player {CurrentPlayer} Wins!")
         Score[CurrentPlayer]+=1
      elif "" not in Board:
         messagebox.showinfo("Gameover","it's a draw")
      else:
         CurrentPlayer="O" if CurrentPlayer == "X" else "X"




root = tk.Tk()
root.title("TicTacToe ❌⭕❌⭕")


Buttons = []


for i in range(9):
   button = tk.Button(root,text="",font=("Abril Fatface",20),width = 8, height = 3,command=lambda  i = i:click(i))
   button.grid(row=i//3,column=i%3)
   Buttons.append(button)
info = tk.Label(root,text=f"Total Number of Games:{Number}",font=("Abril Fatface",20))
info.grid(row=4,column=0,columnspan=3,pady=5)
info1 = tk.Label(root,text=f"{Player1} (X): 0    |    {Player2} (O): 0",font=("Abril Fatface",20))
info1.grid(row=6,column=0,columnspan=3,pady=5) #Pad means padding meaning space and y is the y-axis, x s the x-axis. So the pady means spacing of y-axis. 
Reset = tk.Button(root,text="Reset Now",font=("Abril Fatface",20),command=ResetBoard) #no need to give width and height 
Reset.grid(row=8,column=0,columnspan = 3) 
feedback = tk.Label(root,text="feedback",font=("Abril Fatface",20))
feedback.grid(row=10,column=0,pady=5,padx=9)
feedbackEntry = tk.Entry(root,font=("Abril Fatface",20)).grid(row=10,column=1,pady=5,padx=11)

root.mainloop()

















# A=50
# def Demo():
#     A = 50
#     A+=1
#     print(A)
# Demo()
# Demo()
# print(A)


# A=50
# def Demo():
#     global A
#     A+=1
#     print(A)
# Demo()
# Demo()
# print(A)


