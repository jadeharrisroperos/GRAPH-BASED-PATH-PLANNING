
import pygame, sys, random, math
from collections import deque
from tkinter import messagebox, Tk

messagebox.showinfo("Information_Message", "Enter your optional size in the console." )
cols, rows = int(input("Column size: ")), int(input("Row size: "))

clock = pygame.time.Clock()
size = (width, height) = 640, 480


w = width//cols
h = height//rows

grid = []
queue, visited = deque(), []
path = []

class Spot:
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.neighbors = []
        self.prev = None
        self.wall = False
        self.visited = False
        if (i+j)%7 == 0:
            self.wall == True
        # if random.randint(0, 100) < 20:
        #     self.wall = True
        
    def show(self, win, col, shape= 1):
        if self.wall == True:
            col = (255,69,0)
        if shape == 1:
            pygame.draw.rect(win, col, (self.x*w, self.y*h, w-1, h-1))
        else:
            pygame.draw.circle(win, col, (self.x*w+w//2, self.y*h+h//2), w//3)
    
    def add_neighbors(self, grid):
        if self.x < cols - 1:
            self.neighbors.append(grid[self.x+1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x-1][self.y])
        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y+1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y-1])


def clickWall(pos, state):
    i = pos[0] // w
    j = pos[1] // h
    grid[i][j].wall = state

def place(pos):
    i = pos[0] // w
    j = pos[1] // h
    return w, h

for i in range(cols):
    arr = []
    for j in range(rows):
        arr.append(Spot(i, j))
    grid.append(arr)

for i in range(cols):
    for j in range(rows):
        grid[i][j].add_neighbors(grid)
startvalue = 0
endvalue = 0
def set_start_end():

    messagebox.showinfo("Click for start flag")
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):
                    startvalue = pygame.mouse.get_pos()
    messagebox.showinfo("Click for end flag")
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):
                    endvalue = pygame.mouse.get_pos()

    
# Change this values on flags
start = grid[int(input("Enter x location for start flag: "))][int(input("Enter y location for start flag: "))]
end = grid[int(input("Enter x location for end flag: "))][int(input("Enter y location for end flag: "))]
start.wall = False
end.wall = False

pygame.init()

win = pygame.display.set_mode(size)
pygame.display.set_caption("SHORTEST PATH")

queue.append(start)
start.visited = True

def main():
    flag = False
    noflag = True
    startflag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (1, 3):  
                    clickWall(pygame.mouse.get_pos(), event.button==1)
            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0] or event.buttons[2]:
                    clickWall(pygame.mouse.get_pos(), event.buttons[0])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    startflag = True

        if startflag:
            if len(queue) > 0:
                current = queue.popleft()
                if current == end:
                    temp = current
                    while temp.prev:
                        path.append(temp.prev)
                        temp = temp.prev 
                    if not flag:
                        flag = True
                        print("Done")
                    elif flag:
                        continue
                if flag == False:
                    for i in current.neighbors:
                        if not i.visited and not i.wall:
                            i.visited = True
                            i.prev = current
                            queue.append(i)
            else:
                if noflag and not flag:
                    Tk().wm_withdraw()
                    messagebox.showinfo("Message", "No route found!" )
                    noflag = False
                else:
                    continue


        win.fill((100, 80, 101))
        for i in range(cols):
            for j in range(rows):
                spot = grid[i][j]
                spot.show(win, (225, 225, 255))

                if spot in path:
                    spot.show(win, ((0,255,255)))
                    spot.show(win, (139,69,19), 0)
                elif spot.visited:
                    #spots visited
                    spot.show(win, (0, 0, 0))
                if spot in queue and not flag:
                    spot.show(win, (75,0,130))
                    spot.show(win, (39, 174, 96), 0)

                if spot == end:
                    spot.show(win, (0,0,255))
                if spot == start:
                    spot.show(win, (46,139,87))

               
                
                
        pygame.display.flip()


main()