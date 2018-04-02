from tkinter import *
cut=30
w=600
grid=[[(0,0,w/3,w/3)    ,(w/3,0,2*w/3,w/3)    ,(2*w/3,0,w,w/3)      ],
      [(0,w/3,w/3,2*w/3),(w/3,w/3,2*w/3,2*w/3),(2*w/3,w/3,w,2*w/3)  ],
      [(0,2*w/3,w/3,w)  ,(w/3,2*w/3,2*w/3,w)  ,(2*w/3,2*w/3,w,w)    ]]
fo='Comic Sans MS'

class Tic(Frame):
    
    def __init__(self):
        super().__init__()   
        self.val=[[0,0,0],[0,0,0],[0,0,0]]
        self.canvas = Canvas(self,height=w,width=w,bg='lavender')
        self.pack()
        self.canvas.pack()
        self.main_scr()
        
    def main_scr(self):
        self.canvas.create_text(w/2,w/3,text="Tic Tac Toe",fill ='blue2',font=(fo,60, 'bold'))
        self.canvas.create_text(w/2,1.5*w/3,text="(Two Player Game)",fill ='SlateBlue3',font=(fo,20, 'bold')) 
        self.canvas.create_text(w/2,2*w/3,text="Click to Play",fill ='gray15',font=(fo,30, 'bold'))
        self.text=StringVar()
        self.turn=Label(self,textvariable=self.text,font=(fo,20, 'bold')).pack()
        self.canvas.bind('<Button-1>', self.sel_play)
        
    def sel_play(self,event):
        self.canvas.delete('all')
        self.canvas.configure(bg="ivory")
        self.c=0
        self.draw_grid()
        self.text.set("It is the turn for X to play")
        self.canvas.bind('<Button-1>', self.play)

    def play(self,event):
        x=event.x
        y=event.y
        f=0
        for i in range (3):
            for j in range (3):
                    if (x>grid[i][j][0])&(x<grid[i][j][2])&(y>grid[i][j][1])&(y<grid[i][j][3]):
                        if self.val[i][j]==0:
                            if self.c%2==0:
                                self.draw_x(grid[i][j])
                                self.text.set("It is the turn for O to play")
                                self.val[i][j]='X'
                            else:
                                self.draw_o(grid[i][j])
                                self.text.set("It is the turn for X to play")
                                self.val[i][j]='O'
                            f=1
                            self.c+=1
                            break
            if f==1:
                break
        f=int(w/6)
        for i in range (3):
            if self.val[i][0]==self.val[i][1]==self.val[i][2]!=0:
                self.draw_win((0+cut,f,w-cut,f))
                self.win(self.val[i][0])
            elif self.val[0][i]==self.val[1][i]==self.val[2][i]!=0:
                self.draw_win((f,0+cut,f,w-cut))
                self.win(self.val[0][i])
            f+=int(w/3)
        if (self.val[0][0]==self.val[1][1]==self.val[2][2]!=0):
            self.draw_win((0+cut,0+cut,w-cut,w-cut))
            self.win(self.val[0][0])
        elif (self.val[0][2]==self.val[1][1]==self.val[2][0]!=0):
            self.draw_win((0+cut,w-cut,w-cut,0+cut))
            self.win(self.val[0][2])
        f=0
        for i in range (3):
            for j in range (3):
                if self.val[i][j]==0:
                    f=1
        if f==0:
            self.win("Draw")
        
    def draw_x(self,cord):
        self.canvas.create_line(cord[0]+cut,cord[1]+cut,cord[2]-cut,cord[3]-cut,width=30,fill='red')
        self.canvas.create_line(cord[0]+cut,cord[3]-cut,cord[2]-cut,cord[1]+cut,width=30,fill='red')

    def draw_o(self,cord):
        self.canvas.create_oval(cord[0]+cut,cord[1]+cut,cord[2]-cut,cord[3]-cut,width=30,outline='green')

    def draw_win(self,c):
        self.canvas.create_line(c[0],c[1],c[2],c[3],width=20,fill='gray55')
            
    def draw_grid(self):
        for i in range (4):
            self.canvas.create_line(0,i*w/3,w,i*w/3,width=5)
            self.canvas.create_line(i*w/3,0,i*w/3,w,width=5)
        
    def win(self,s):
        self.st=s
        self.text.set("Click for Match Result")
        self.canvas.bind('<Button-1>', self.win_scr)

    def win_scr(self,event):
        str=self.st
        self.canvas.delete('all')
        self.text.set("")
        if str!="Draw":
            if str=='X':
                t='red'
            else:
                t='green'
            str+=" Won the Match"
        else:
            str="Match "+str
            t='orange red'
        self.canvas.configure(bg="lemon chiffon")
        self.canvas.create_text(w/2,w/2,text=str,fill =t,font=(fo,40, 'bold'))
        self.val=[[0,0,0],[0,0,0],[0,0,0]]
        self.canvas.create_text(w/2,3*w/4,text="Click to Play again",fill ='gray15',font=(fo,15, 'bold'))
        self.canvas.bind('<Button-1>', self.sel_play)
 
root = Tk()
Tic()
root.title("Tic Tac Toe")
root.geometry("+350+20")
root.mainloop()
