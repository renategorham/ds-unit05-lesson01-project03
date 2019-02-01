'''
Trees function
'''
import numpy as np
from queue import Queue

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        
    def bfs(self): 
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            self = queue.get()
            print(self.val)

            if self.left:
                queue.put(self.left)

            if self.right:
                queue.put(self.right)
