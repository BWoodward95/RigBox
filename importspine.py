import maya.cmds as cmds

from rigbox import labels

class ImportSpine():
    
    def __init__(self):
        
        self.hips = None
        self.spine = None
        self.spine1 = None
        self.spine2 = None
        
        self.hips_pos = (0,100,0)
        self.spine_pos = (0,107,0)
        self.spine1_pos = (0,120,0)
        self.spine2_pos = (0,132,0)
        
    def create_spine(self):
        spine_list = [] # Carries around spine joint variables
        
        self.hips = cmds.createNode("joint", n=labels.JNT[1] + labels.SIDE[0] + labels.SUF[0])   # Create Joints
        self.spine = cmds.createNode("joint", n=labels.JNT[2] + labels.SIDE[0] + labels.SUF[0])  #              |
        self.spine1 = cmds.createNode("joint", n=labels.JNT[3] + labels.SIDE[0] + labels.SUF[0]) #              |
        self.spine2 = cmds.createNode("joint", n=labels.JNT[4] + labels.SIDE[0] + labels.SUF[0]) #              V
       
        cmds.xform(self.hips, ws=True, t=(0,100,0))   # Place Joints
        cmds.xform(self.spine, ws=True, t=(0,107,0))  #             |
        cmds.xform(self.spine1, ws=True, t=(0,120,0)) #             |
        cmds.xform(self.spine2, ws=True, t=(0,132,0)) #             V
        
        spine_list.append(self.hips)   # Append to list
        spine_list.append(self.spine)  #               |
        spine_list.append(self.spine1) #               |
        spine_list.append(self.spine2) #               V
        
        tools.create_joint_chain("X", "Y", spine_list) # Create chain
        
        cmds.parent(self.hips, self.root) # Attach to Root
        
        labels.deformJoint_list.extend(spine_list) # Add to the basket