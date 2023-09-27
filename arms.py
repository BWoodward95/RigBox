import maya.cmds as cmds

from rigbox import tools, labels, spine, hands

class ImportArms():
    
    def __init__(self):
        # Declare variables
        self.clavicle_L = None
        self.upperArm_L = None
        self.lowerArm_L = None
        self.wrist_L = None
        
        self.clavicle_R = None
        self.upperArm_R = None
        self.lowerArm_R = None
        self.wrist_R = None
        
        # Initialize joint positions
        self.clavicle_L_pos = (7,147,0)
        self.upperArm_L_pos = (17,147,0)
        self.lowerArm_L_pos = (45,147,0)
        self.wrist_L_pos = (72,147,0)    
    
        self.clavicle_R_pos = (-7,147,0)
        self.upperArm_R_pos = (-17,147,0)
        self.lowerArm_R_pos = (-45,147,0)
        self.wrist_R_pos = (-72,147,0)    
            
    def create_leftArm(self):
        arm_list = []
        
        self.clavicle_L = cmds.createNode("joint", n=labels.JNT[9] + labels.SIDE[1] + labels.SUF[0])
        self.upperArm_L = cmds.createNode("joint", n=labels.JNT[10] + labels.SIDE[1] + labels.SUF[0])
        self.lowerArm_L = cmds.createNode("joint", n=labels.JNT[11] + labels.SIDE[1] + labels.SUF[0])
        self.wrist_L = cmds.createNode("joint", n=labels.JNT[12] + labels.SIDE[1] + labels.SUF[0])
            
        cmds.xform(self.clavicle_L, ws=True, t=self.clavicle_L_pos)
        cmds.xform(self.upperArm_L, ws=True, t=self.upperArm_L_pos)
        cmds.xform(self.lowerArm_L, ws=True, t=self.lowerArm_L_pos)
        cmds.xform(self.wrist_L, ws=True, t=self.wrist_L_pos)
                
        arm_list.append(self.clavicle_L)
        arm_list.append(self.upperArm_L)
        arm_list.append(self.lowerArm_L)
        arm_list.append(self.wrist_L)
        
        tools.create_joint_chain("X", "Y", arm_list)
        
        lowerArm_rot = tools.query_rotation(self.lowerArm_L)
        cmds.xform(self.wrist_L, ro=lowerArm_rot)        
        
        # if hand:
        #     self.create_leftHand()
               
        # cmds.parent(self.clavicle_L, self.spine2)
    
        labels.deformJoint_list.extend(arm_list)
        
    def create_rightArm(self):
        arm_list = []
        
        self.clavicle_R = cmds.createNode("joint", n=labels.JNT[9] + labels.SIDE[2] + labels.SUF[0])
        self.upperArm_R = cmds.createNode("joint", n=labels.JNT[10] + labels.SIDE[2] + labels.SUF[0])
        self.lowerArm_R = cmds.createNode("joint", n=labels.JNT[11] + labels.SIDE[2] + labels.SUF[0])
        self.wrist_R = cmds.createNode("joint", n=labels.JNT[12] + labels.SIDE[2] + labels.SUF[0])
            
        cmds.xform(self.clavicle_R, ws=True, t=self.clavicle_R_pos)
        cmds.xform(self.upperArm_R, ws=True, t=self.upperArm_R_pos)
        cmds.xform(self.lowerArm_R, ws=True, t=self.lowerArm_R_pos)
        cmds.xform(self.wrist_R, ws=True, t=self.wrist_R_pos)
                
        arm_list.append(self.clavicle_R)
        arm_list.append(self.upperArm_R)
        arm_list.append(self.lowerArm_R)
        arm_list.append(self.wrist_R)
        
        tools.create_joint_chain("-X", "-Y", arm_list)
        
        lowerArm_rot = tools.query_rotation(self.lowerArm_R)
        cmds.xform(self.wrist_R, ro=lowerArm_rot)        
        
        # if hand:
        #     self.create_rightHand()
               
        # cmds.parent(self.clavicle_R, self.spine2)
    
        labels.deformJoint_list.extend(arm_list)