from array import *
from queue import Queue
from matplotlib import pyplot as plt
import time
import  os
import numpy as nmp

from BfsNode import BfsNode


class BFS:
    #def __init__(self):


        def printMaze(self, maze):
            for i in maze:
                for j in i:
                    print(j, end=" ")
                print()


        def findPath(self, maze):
            self.printMaze(maze)

            goalI=len(maze)-1
            goalJ=len(maze[0])-1
            hasBeenVisitedToke=7

            print("goal j=")
            print(goalJ)
            distance =0

            tempNode = BfsNode(0,0,0)

            q = Queue(maxsize=0)
            q.put(tempNode)

            visited = []
            counter = 0
            for r in range(len(maze)):
                row = []
                for c in range(len(maze[0])):
                    row.append(counter)

                visited.append(row)


            while not q.empty():
                print()
                print()
                currentNode = q.get()
                #print("current node is: " + str(currentNode))
                #print(currentNode)
                i=currentNode.i
                j=currentNode.j
                maze[i][j]=hasBeenVisitedToke


                self.printMaze(maze)
                #plt.imshow(maze, interpolation='none')
                #plt.show()
                print()
                #self.printMaze(visited)


                #check for exit
                if(i==goalI and j==goalJ):
                    print("######## Exit Reached ##########")
                    print('total steps: ['+str(currentNode.distance)+']')
                    #plt.imshow(visited, interpolation='none')
                    #plt.show()
                    break

                #check visited
                if(visited[i][j]==1):
                    continue

                visited[i][j] = 1

                #down
                if(i< len(maze)-1 and maze[i+1][j]!=1):
                    if(visited[i+1][j]==0):
                        #print("can go down!!")
                        visited[i+1][j]=2
                        downNode = BfsNode(i + 1, j, currentNode.distance + 1)
                        q.put(downNode)

                #right
                if(j<len(maze)-1 and maze[i][j+1]!=1):
                    if(visited[i][j+1]==0):
                        #print("can go right!!")
                        visited[i][j+1] = 2
                        rightNode = BfsNode(i, j+1, currentNode.distance+1)
                        q.put(rightNode)
                #left
                if(j>0 and maze[i][j-1]!= 1):
                    if(visited[i][j-1]==0):
                        #print("can go left!!")
                        visited[i][j-1] = 2
                        leftNode = BfsNode(i, j - 1, currentNode.distance + 1)
                        q.put(leftNode)

                #up
                if(i>0 and maze[i-1][j]!=1):
                    if(visited[i-1][j]==0):
                        #print("can go up!!")
                        visited[i-1][j] = 2
                        upNode = BfsNode(i - 1, j, currentNode.distance + 1)
                        q.put(upNode)


            print()
            self.printMaze(maze)
            plt.imshow(maze, interpolation='none')
            plt.show()