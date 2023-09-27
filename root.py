import maya.cmds as cmds

from rigbox import labels

class ImportRoot():
    
    def __init__(self):
        
        self.root = None
        
        self.root_pos = (0,0,0)
        
    def create_root(self):
        self.root = cmds.createNode("joint", n=labels.JNT[0] + labels.SUF[0]) # Create root node at world origin        