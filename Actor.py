class actor:

    width=30

    height=100

    #pos indicate position of M and C;

    #  0 and 1 indicates left and right shore respectively

    # 2 and 4 indicates left an right of boat at left shore

    # 3 and 5 indicates left an right of boat at right shore



    def __init__(self, x,y,x_change,pos,char,leftright,image1,image2,win):
        self.leftright=leftright
        self.x=x
        self.y=y
        self.x_change=x_change #change in x for movement of missionary or cannibal
        self.pos=pos
        self.char=char #char indicates character i.e M for Missionary and C for cannibal
        self.rect_x = self.x+12
        self.rect_y = self.y
        self.image1=image1
        self.image2=image2
        self.win=win



    def display(self):
            self.win.blit(self.image1, (self.x, self.y))


    def highlight(self):
        self.win.blit(self.image2, (self.x, self.y))