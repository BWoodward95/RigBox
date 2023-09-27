import maya.cmds as cmds

from rigbox import labels, arms

class ImportHands():
    
    def __init__(self):
        
        self.index_L = None
        self.index2_L = None
        self.index3_L = None
        self.indexEnd_L = None
        
        self.middle_L = None
        self.middle2_L = None
        self.middle3_L = None
        self.middleEnd_L = None
        
        self.ring_L = None
        self.ring2_L = None
        self.ring3_L = None
        self.ringEnd_L = None
        
        self.pinky_L = None
        self.pinky2_L = None
        self.pinky3_L = None
        self.pinkyEnd_L = None
        
        self.thumb_L = None
        self.thumb2_L = None
        self.thumb3_L = None
        self.thumbEnd_L = None
        
        self.index_R = None
        self.index2_R = None
        self.index3_R = None
        self.indexEnd_R = None
        
        self.middle_R = None
        self.middle2_R = None
        self.middle3_R = None
        self.middleEnd_R = None
        
        self.ring_R = None
        self.ring2_R = None
        self.ring3_R = None
        self.ringEnd_R = None
        
        self.pinky_R = None
        self.pinky2_R = None
        self.pinky3_R = None
        self.pinkyEnd_R = None
        
        self.thumb_R = None
        self.thumb2_R = None
        self.thumb3_R = None
        self.thumbEnd_R = None      
        
    def create_leftHand(self):
        index_list = []
        middle_list = []
        ring_list = []
        pinky_list = []
        thumb_list = []
        
        # Index Finger
        self.index_L = cmds.createNode("joint", n=labels.JNT[17] + labels.SIDE[1] + labels.SUF[0])
        self.index1_L = cmds.createNode("joint", n=labels.JNT[18] + labels.SIDE[1] + labels.SUF[0])
        self.index2_L = cmds.createNode("joint", n=labels.JNT[19] + labels.SIDE[1] + labels.SUF[0])
        self.indexEnd_L = cmds.createNode("joint", n=labels.JNT[20] + labels.SIDE[1] + labels.SUF[0])
        
        cmds.xform(self.index_L, ws=True, t=(80,147,3))
        cmds.xform(self.index1_L, ws=True, t=(85,147,3))
        cmds.xform(self.index2_L, ws=True, t=(88,147,3))
        cmds.xform(self.indexEnd_L, ws=True, t=(90,147,3))
        
        index_list.append(self.index_L)
        index_list.append(self.index1_L)
        index_list.append(self.index2_L)
        index_list.append(self.indexEnd_L)
        
        # Middle Finger
        self.middle_L = cmds.createNode("joint", n=labels.JNT[21] + labels.SIDE[1] + labels.SUF[0])
        self.middle1_L = cmds.createNode("joint", n=labels.JNT[22] + labels.SIDE[1] + labels.SUF[0])
        self.middle2_L = cmds.createNode("joint", n=labels.JNT[23] + labels.SIDE[1] + labels.SUF[0])
        self.middleEnd_L = cmds.createNode("joint", n=labels.JNT[24] + labels.SIDE[1] + labels.SUF[0])
        
        cmds.xform(self.middle_L, ws=True, t=(80,147,1))
        cmds.xform(self.middle1_L, ws=True, t=(85,147,1))
        cmds.xform(self.middle2_L, ws=True, t=(88,147,1))
        cmds.xform(self.middleEnd_L, ws=True, t=(90,147,1))
        
        middle_list.append(self.middle_L)
        middle_list.append(self.middle1_L)
        middle_list.append(self.middle2_L)
        middle_list.append(self.middleEnd_L)
        
        # Ring Finger
        self.ring_L = cmds.createNode("joint", n=labels.JNT[25] + labels.SIDE[1] + labels.SUF[0])
        self.ring1_L = cmds.createNode("joint", n=labels.JNT[26] + labels.SIDE[1] + labels.SUF[0])
        self.ring2_L = cmds.createNode("joint", n=labels.JNT[27] + labels.SIDE[1] + labels.SUF[0])
        self.ringEnd_L = cmds.createNode("joint", n=labels.JNT[28] + labels.SIDE[1] + labels.SUF[0])
        
        cmds.xform(self.ring_L, ws=True, t=(80,147,-1))
        cmds.xform(self.ring1_L, ws=True, t=(85,147,-1))
        cmds.xform(self.ring2_L, ws=True, t=(88,147,-1))
        cmds.xform(self.ringEnd_L, ws=True, t=(90,147,-1))
        
        ring_list.append(self.ring_L)
        ring_list.append(self.ring1_L)
        ring_list.append(self.ring2_L)
        ring_list.append(self.ringEnd_L)
        
        # Pinky Finger
        self.pinky_L = cmds.createNode("joint", n=labels.JNT[29] + labels.SIDE[1] + labels.SUF[0])
        self.pinky1_L = cmds.createNode("joint", n=labels.JNT[30] + labels.SIDE[1] + labels.SUF[0])
        self.pinky2_L = cmds.createNode("joint", n=labels.JNT[31] + labels.SIDE[1] + labels.SUF[0])
        self.pinkyEnd_L = cmds.createNode("joint", n=labels.JNT[32] + labels.SIDE[1] + labels.SUF[0])
        
        cmds.xform(self.pinky_L, ws=True, t=(80,147,-3))
        cmds.xform(self.pinky1_L, ws=True, t=(85,147,-3))
        cmds.xform(self.pinky2_L, ws=True, t=(88,147,-3))
        cmds.xform(self.pinkyEnd_L, ws=True, t=(90,147,-3))
        
        pinky_list.append(self.pinky_L)
        pinky_list.append(self.pinky1_L)
        pinky_list.append(self.pinky2_L)
        pinky_list.append(self.pinkyEnd_L)
        
        # Thumb
        self.thumb_L = cmds.createNode("joint", n=labels.JNT[13] + labels.SIDE[1] + labels.SUF[0])
        self.thumb1_L = cmds.createNode("joint", n=labels.JNT[14] + labels.SIDE[1] + labels.SUF[0])
        self.thumb2_L = cmds.createNode("joint", n=labels.JNT[15] + labels.SIDE[1] + labels.SUF[0])
        self.thumbEnd_L = cmds.createNode("joint", n=labels.JNT[16] + labels.SIDE[1] + labels.SUF[0])
        
        cmds.xform(self.thumb_L, ws=True, t=(76,145,4))
        cmds.xform(self.thumb1_L, ws=True, t=(78,145,5))
        cmds.xform(self.thumb2_L, ws=True, t=(81,145,5))
        cmds.xform(self.thumbEnd_L, ws=True, t=(84,145,5))
        
        thumb_list.append(self.thumb_L)
        thumb_list.append(self.thumb1_L)
        thumb_list.append(self.thumb2_L)
        thumb_list.append(self.thumbEnd_L)
        
        tools.create_joint_chain("X", "Y", index_list)
        tools.create_joint_chain("X", "Y", middle_list)
        tools.create_joint_chain("X", "Y", ring_list)
        tools.create_joint_chain("X", "Y", pinky_list)
        tools.create_joint_chain("X", "Y", thumb_list)
        
        cmds.parent(self.index_L, self.middle_L, self.ring_L, self.pinky_L, self.thumb_L, self.wrist_L)
        
        labels.deformJoint_list.extend(index_list)
        labels.deformJoint_list.extend(middle_list)
        labels.deformJoint_list.extend(ring_list)
        labels.deformJoint_list.extend(pinky_list)
        labels.deformJoint_list.extend(thumb_list)
        
    def create_rightHand(self):
        index_list = []
        middle_list = []
        ring_list = []
        pinky_list = []
        thumb_list = []
        
        # Index Finger
        self.index_R = cmds.createNode("joint", n=labels.JNT[17] + labels.SIDE[2] + labels.SUF[0])
        self.index1_R = cmds.createNode("joint", n=labels.JNT[18] + labels.SIDE[2] + labels.SUF[0])
        self.index2_R = cmds.createNode("joint", n=labels.JNT[19] + labels.SIDE[2] + labels.SUF[0])
        self.indexEnd_R = cmds.createNode("joint", n=labels.JNT[20] + labels.SIDE[2] + labels.SUF[0])
        
        cmds.xform(self.index_R, ws=True, t=(-80,147,3))
        cmds.xform(self.index1_R, ws=True, t=(-85,147,3))
        cmds.xform(self.index2_R, ws=True, t=(-88,147,3))
        cmds.xform(self.indexEnd_R, ws=True, t=(-90,147,3))
        
        index_list.append(self.index_R)
        index_list.append(self.index1_R)
        index_list.append(self.index2_R)
        index_list.append(self.indexEnd_R)
        
        # Middle Finger
        self.middle_R = cmds.createNode("joint", n=labels.JNT[21] + labels.SIDE[2] + labels.SUF[0])
        self.middle1_R = cmds.createNode("joint", n=labels.JNT[22] + labels.SIDE[2] + labels.SUF[0])
        self.middle2_R = cmds.createNode("joint", n=labels.JNT[23] + labels.SIDE[2] + labels.SUF[0])
        self.middleEnd_R = cmds.createNode("joint", n=labels.JNT[24] + labels.SIDE[2] + labels.SUF[0])
        
        cmds.xform(self.middle_R, ws=True, t=(-80,147,1))
        cmds.xform(self.middle1_R, ws=True, t=(-85,147,1))
        cmds.xform(self.middle2_R, ws=True, t=(-88,147,1))
        cmds.xform(self.middleEnd_R, ws=True, t=(-90,147,1))
        
        middle_list.append(self.middle_R)
        middle_list.append(self.middle1_R)
        middle_list.append(self.middle2_R)
        middle_list.append(self.middleEnd_R)
        
        # Ring Finger
        self.ring_R = cmds.createNode("joint", n=labels.JNT[25] + labels.SIDE[2] + labels.SUF[0])
        self.ring1_R = cmds.createNode("joint", n=labels.JNT[26] + labels.SIDE[2] + labels.SUF[0])
        self.ring2_R = cmds.createNode("joint", n=labels.JNT[27] + labels.SIDE[2] + labels.SUF[0])
        self.ringEnd_R = cmds.createNode("joint", n=labels.JNT[28] + labels.SIDE[2] + labels.SUF[0])
        
        cmds.xform(self.ring_R, ws=True, t=(-80,147,-1))
        cmds.xform(self.ring1_R, ws=True, t=(-85,147,-1))
        cmds.xform(self.ring2_R, ws=True, t=(-88,147,-1))
        cmds.xform(self.ringEnd_R, ws=True, t=(-90,147,-1))
        
        ring_list.append(self.ring_R)
        ring_list.append(self.ring1_R)
        ring_list.append(self.ring2_R)
        ring_list.append(self.ringEnd_R)
        
        # Pinky Finger
        self.pinky_R = cmds.createNode("joint", n=labels.JNT[29] + labels.SIDE[2] + labels.SUF[0])
        self.pinky1_R = cmds.createNode("joint", n=labels.JNT[30] + labels.SIDE[2] + labels.SUF[0])
        self.pinky2_R = cmds.createNode("joint", n=labels.JNT[31] + labels.SIDE[2] + labels.SUF[0])
        self.pinkyEnd_R = cmds.createNode("joint", n=labels.JNT[32] + labels.SIDE[2] + labels.SUF[0])
        
        cmds.xform(self.pinky_R, ws=True, t=(-80,147,-3))
        cmds.xform(self.pinky1_R, ws=True, t=(-85,147,-3))
        cmds.xform(self.pinky2_R, ws=True, t=(-88,147,-3))
        cmds.xform(self.pinkyEnd_R, ws=True, t=(-90,147,-3))
        
        pinky_list.append(self.pinky_R)
        pinky_list.append(self.pinky1_R)
        pinky_list.append(self.pinky2_R)
        pinky_list.append(self.pinkyEnd_R)
        
        # Thumb
        self.thumb_R = cmds.createNode("joint", n=labels.JNT[13] + labels.SIDE[2] + labels.SUF[0])
        self.thumb1_R = cmds.createNode("joint", n=labels.JNT[14] + labels.SIDE[2] + labels.SUF[0])
        self.thumb2_R = cmds.createNode("joint", n=labels.JNT[15] + labels.SIDE[2] + labels.SUF[0])
        self.thumbEnd_R = cmds.createNode("joint", n=labels.JNT[16] + labels.SIDE[2] + labels.SUF[0])
        
        cmds.xform(self.thumb_R, ws=True, t=(-76,145,4))
        cmds.xform(self.thumb1_R, ws=True, t=(-78,145,5))
        cmds.xform(self.thumb2_R, ws=True, t=(-81,145,5))
        cmds.xform(self.thumbEnd_R, ws=True, t=(-84,145,5))
        
        thumb_list.append(self.thumb_R)
        thumb_list.append(self.thumb1_R)
        thumb_list.append(self.thumb2_R)
        thumb_list.append(self.thumbEnd_R)
        
        tools.create_joint_chain("-X", "-Y", index_list)
        tools.create_joint_chain("-X", "-Y", middle_list)
        tools.create_joint_chain("-X", "-Y", ring_list)
        tools.create_joint_chain("-X", "-Y", pinky_list)
        tools.create_joint_chain("-X", "-Y", thumb_list)
        
        cmds.parent(self.index_R, self.middle_R, self.ring_R, self.pinky_R, self.thumb_R, arms.wrist_R)
        
        labels.deformJoint_list.extend(index_list)
        labels.deformJoint_list.extend(middle_list)
        labels.deformJoint_list.extend(ring_list)
        labels.deformJoint_list.extend(pinky_list)
        labels.deformJoint_list.extend(thumb_list)               
        
    
        