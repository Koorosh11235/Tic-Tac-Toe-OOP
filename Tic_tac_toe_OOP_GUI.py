import random # imprting random for creating a random integer latar for calling random player
import tkinter as tk # imprting tkinter obviously know for what

class Game_Board(): # our program must be object oriented so we desfine our classes, starting with Game Board
    def __init__(self): # calling the constructor for the gameboard
        self.root = tk.Tk() # creating a tk inter object\application\gui window
        self.frame1 = tk.Frame(self.root) # we use frame 1 for buttons
        self.frame2 = tk.Frame(self.root) # we use frame 2 for labels
        self.status = tk.Label(self.frame2, text='', font=("Arial", 12), bg = "white", fg= "black") # now creating GAME STATUS
        self.constant = tk.Label(self.frame2, text="", font=("Arial", 12), bg = "white", fg= "black") # setting up a label for the start of the 
        self.q_but = tk.Button(self.frame2, text="Quit", height = 4, width=10,bg= "black", fg= "white", 
            command = self.on_closing, font=("Arial", 13)) # creating quti button
        self.value = True if random.randint(0, 1001)%2 == 0 else False # setting up a boolean value and a random integer 
        self.var = "var" # setting up an important variable
        self.houses = [ # we need to set houses of the board as button with commands for the user to click
            tk.Button(self.frame1, text="0", height=6, width=12, bg= "light blue", fg = "black", command=lambda: self.quit_mainloop(0)),
            tk.Button(self.frame1, text="1", height=6, width=12, bg= "light blue", fg = "black", command=lambda: self.quit_mainloop(1)),
            tk.Button(self.frame1, text="2", height=6, width=12, bg= "light blue", fg = "black", command=lambda: self.quit_mainloop(2)),
            tk.Button(self.frame1, text="3", height=6, width=12, bg= "light blue", fg = "black", command=lambda: self.quit_mainloop(3)),
            tk.Button(self.frame1, text="4", height=6, width=12, bg= "light blue", fg = "black", command=lambda: self.quit_mainloop(4)),
            tk.Button(self.frame1, text="5", height=6, width=12, bg= "light blue", fg = "black", command=lambda: self.quit_mainloop(5)),
            tk.Button(self.frame1, text="6", height=6, width=12, bg= "light blue", fg = "black", command=lambda: self.quit_mainloop(6)),
            tk.Button(self.frame1, text="7", height=6, width=12, bg= "light blue", fg = "black", command=lambda: self.quit_mainloop(7)),
            tk.Button(self.frame1, text="8", height=6, width=12, bg= "light blue", fg = "black", command=lambda: self.quit_mainloop(8))
            ]
        self.cells = [None,None,None,None,None,None,None,None,None,] # i still need this for the simple ai to do everything in oop edition
        
    def print_board(self): # we need a method for the board to show it, it will grid every button in the frame 2 horizental and vertiacl
        self.root.geometry("600x600") # setting up the size of that window
        self.root.title("Tic Tac Toe") # giving a title to the tkinter application
        self.titl_label = tk.Label(self.root, text="Tic Tac Toe", font=("Times New Roman", 25), bg = "purple", fg= "yellow") 
        self.titl_label.pack() # making and customizing a game title
        self.frame1.pack() # packing frame 1
        self.frame2.pack() # packing frame 2
        self.constant.grid(row = 1, column=0) # grdding and placing the constant
        self.status.grid(row = 2, column=0) # gridding the status
        self.q_but.grid(row = 3, column= 0,) # setted up a quiting button now dressing and gridding it
        
        for i in self.houses :
            i.grid(row = int((self.houses.index(i))/3), column=int((self.houses.index(i))%3))
            
    def is_winner(self,state): # becaue the main code is coming from oop edition and needs it for simple ai
        tmp = [[0,1,2],[0,3,6],[2,5,8],[6,7,8],[0,4,8],[2,4,6],[3,4,5],[1,4,7]]
        for i in tmp:
            if((state[i[0]] == state[i[1]] and state[i[1]] == state[i[2]] and state[i[2]] != None)):
                return state[i[0]] # if anybody won give me the letter of the winner
        return "equal" if state.count(None) == 0 else "not_finished" # obvious
    
    def make_a_move(self, number, player) :
        self.cells[number] = player.letter
        self.houses[number].config(text=player.letter)
    
    def is_position_valid(self, number) :
        if self.cells[number] != None : # if user clicked on an ocupied house :
            self.status.config(text="GAME STATUS :\ncan not choose a \nnone-empty house\n click AN UNOCUPIED HOUSE !! ") # change status 
            return True
        
    def give_color(self,state, color) :  # this function is just a dreessing
        tmp = [[0,1,2],[0,3,6],[2,5,8],[6,7,8],[0,4,8],[2,4,6],[3,4,5],[1,4,7]]
        for i in tmp: # it does exactly what check for winner does 
            if((state[i[0]] == state[i[1]] and state[i[1]] == state[i[2]] and state[i[2]] != None)):
                 for j in i : # set the colors of the buttons(Houses) to red
                        self.houses[j].config(bg= color)
            
    def quit_mainloop(self,i): # we need this for quiting the mainloop in line 65,69,160 with an inner value of button (index of button)
        self.root.quit()  # this will caues the program to leave the loop after user clicks on button
        self.var = i #  var is a tkinter INTVARobject which we assign the value of button to it
   
    def on_closing(self): # this function will later be used for the QUIT button
        self.root.destroy() # first it closes the gui wundow and ,,,,
        exit() # than it will exit the whole loop

class Player(): # now we need a class named playre for both computer and human
    def __init__(self, board,letter, turn, color): # having the two attributes :
        self.letter = letter
        self.podletter = "X" if self.letter == "O" else  "O"
        self.board = board
        self.turn = turn
        self.color = color
        
    def simple_ai(self,state):
        for i in range(0,9):# it returns index of the best field that computer must select
            cloned_cells = self.board.cells.copy() # making a copy 
            if(cloned_cells[i] == None): # weee need to change and check in a table exepct our real tablke
                cloned_cells[i] = self.letter
                if(self.board.is_winner(cloned_cells) == self.letter):
                    return i
        for i in range(0,9):
            cloned_cells = self.board.cells.copy()
            if(cloned_cells[i] == None):
                cloned_cells[i] = self.podletter
                if(self.board.is_winner(cloned_cells) == self.podletter):
                    return i
        for i in [0,2,6,8,4,1,3,5,7]: # checking if corners are empty? than the middle? than the sides
            if(self.board.cells[i] == None): 
                return i
    
    def get_human_move(self, board, turn) :
        if self.turn :
            board.root.mainloop() # hold the program until the user clicks 
            board.constant.destroy() # destroy the constant label
            new_var = board.var # set the new var
            if board.is_position_valid(new_var) :
                board.root.mainloop()
                new_var = self.board.var
                if self.board.is_position_valid(new_var) : # if again chooses a none empty house break the loop
                    exit()
            board.make_a_move(new_var, self) # now if choosed corretly ....
            tmp = self.simple_ai(board.cells) # this time just tell the config to set status to this and than in 103 set the text of button
            board.status.config(text=(f"GAME STATUS :\n computer turn:\ncomputer decided to select {tmp}\n")
                               + f"user turn, please click on an empty house:")
        self.turn = not self.turn
    
    def get_computer_move(self, board, turn):
        if turn == True:
            tmp = self.simple_ai(board.cells) # give me the best move for computer
            board.make_a_move(tmp, self) # computer chooses the best house for itself
        self.turn = not self.turn
        
    def show_player_info(self) :
        winner = self.board.is_winner(self.board.cells)
        if winner == self.letter :
            self.board.give_color(self.board.cells, self.color)
            self.board.status.config(text=f'GAME STATUS :\n{winner} won the game', fg= self.color, font=("Arial", 15)) 
        elif (winner == "equal"): # if equal
                self.board.status.config(text="GAME STATUS :\ngame ended in TIE", fg= "blue",font=("Arial", 15))

    def starts_first(self) :
        self.board.constant.config(text=f'starting game randomly...,\nyou are "{self.letter}" and playing\nagainst computer("{self.podletter}")') 
        if self.board.value == True : # it it is user to play
           self.board.status.config(text =f'GAME STATUS :\n{self.letter} starts first (User) ',font=("Arial", 12))
        else: # else it is computer and set the game status text to this, if computer starts first, i will always pick 0
            self.board.status.config(text=f'GAME STATUS :\n{self.podletter} starts first :\ncomputer decided to select 0,\nuser turn please click on an empty house: ', font=("Arial", 12))

def play(pl1, pl2, board):

        board.print_board()# # better diplay, showing the board for the fisrst time
        pl2.starts_first()s
        while True: # as long as true. 
            pl1.get_computer_move(board, pl1.turn)# changing the text of that house
            pl2.get_human_move(board, pl2.turn)
            tmp = board.is_winner(board.cells)
            if(tmp == pl2.letter):
                pl2.show_player_info()
                break
            elif(tmp == pl1.letter):
                pl1.show_player_info()
                break
            elif tmp == "equal" :
                pl1.show_player_info()
                break
        board.root.mainloop()
            
if __name__ == "__main__"  :       
    newb = Game_Board() # creating an object of board becaue we are defining function that they need an object with its attributes
    human1 = Player(newb, "X", newb.value, "green") # setting up the human player X
    cpu1 = Player(newb, "O", not newb.value, "indian red") # setting up the computer playing as O
    play(cpu1, human1, newb) # calling the game