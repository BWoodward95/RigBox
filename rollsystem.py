import maya.cmds as cmds

from rigbox import tools, labels, legs, arms

class RollSystem():
    
    def __init__(self):
        self.importlegs = legs.ImportLegs()
        self.importarms = arms.ImportArms()  
    
    # Create Deform System        
    def create_roll_jnt(self, name, first, last):
        cmds.select(first)
        self.roll_jnt = cmds.joint(n=name)

        self.roll_jnt_pos = tools.average_location("X", last)
                        
        cmds.xform(self.roll_jnt, t=self.roll_jnt_pos)
        
        labels.deformJoint_list.append(self.roll_jnt)
        
        return self.roll_jnt    
        
    def apply_roll_jnts(self, mirror=False):
        self.upperLeg_roll_L = self.create_roll_jnt(f"{labels.JNT[33]}labels{labels[1]}{labels.SUF[0]}", self.importlegs.upperLeg_L, self.importlegs.lowerLeg_L)
             
        self.lowerLeg_roll_L = self.create_roll_jnt(f"{labels.JNT[34]}_roll{labels.SIDE[1]}{labels.SUF[0]}", self.importlegs.lowerLeg_L, self.create_skeleton.foot_L)
        
        self.upperArm_roll_L = self.create_roll_jnt(f"{labels.JNT[10]}_roll{labels.SIDE[1]}{labels.SUF[0]}", self.importarms.upperArm_L, self.create_skeleton.lowerArm_L)

        self.lowerArm_roll_L = self.create_roll_jnt(f"{labels.JNT[11]}_roll{labels.SIDE[1]}{labels.SUF[0]}", self.importarms.lowerArm_L, self.create_skeleton.wrist_L)   
        
        if mirror:
            self.upperLeg_roll_R = self.create_roll_jnt(f"{labels.JNT[33]}_roll{labels.SIDE[2]}{labels.SUF[0]}", self.importlegs.upperLeg_R, self.create_skeleton.lowerLeg_R)
                 
            self.lowerLeg_roll_R = self.create_roll_jnt(f"{labels.JNT[34]}_roll{labels.SIDE[2]}{labels.SUF[0]}", self.importlegs.lowerLeg_R, self.create_skeleton.foot_R)
            
            self.upperArm_roll_R = self.create_roll_jnt(f"{labels.JNT[10]}_roll{labels.SIDE[2]}{labels.SUF[0]}", self.importarms.upperArm_R, self.create_skeleton.lowerArm_R)

            self.lowerArm_roll_R = self.create_roll_jnt(f"{labels.JNT[11]}_roll{labels.SIDE[2]}{labels.SUF[0]}", self.importarms.lowerArm_R, self.create_skeleton.wrist_R)       
            
    def create_roll_sys(self, name, inJoint, outJoint, factor):    
        sys_node = cmds.createNode("multiplyDivide", n=name)
        cmds.connectAttr(f"{inJoint}.ry", f"{sys_node}.input1X")
        cmds.connectAttr(f"{sys_node}.outputX", f"{outJoint}.ry")
        cmds.setAttr(f"{sys_node}.input2X", factor)
        labels.node_list.append(sys_node)        
    
    def setup_roll_sys(self, mirror=False):
        # upperArm roll
        self.create_roll_sys(f"{labels.JNT[10]}{labels.SIDE[1]}{labels.SUF[1]}", self.importarms.upperArm_L, self.upperArm_roll_L, -0.5)
    
        # lowerArm roll
        self.create_roll_sys(f"{labels.JNT[11]}{labels.SIDE[1]}{labels.SUF[1]}", self.importarms.lowerArm_L, self.lowerArm_roll_L, 0.5)
        
        # upperLeg roll
        self.create_roll_sys(f"{labels.JNT[33]}{labels.SIDE[1]}{labels.SUF[1]}", self.importlegs.upperLeg_L, self.upperLeg_roll_R, 0.5)
        
        # lowerLeg roll
        self.create_roll_sys(f"{labels.JNT[34]}{labels.SIDE[1]}{labels.SUF[1]}", self.importlegs.lowerLeg_L, self.lowerLeg_roll_L, 0.5)
        
        if mirror:       
            # upperArm roll
            self.create_roll_sys(f"{labels.JNT[10]}{labels.SIDE[2]}{labels.SUF[1]}", self.importarms.upperArm_R, self.upperArm_roll_R, -0.5)
           
            # lowerArm roll
            self.create_roll_sys(f"{labels.JNT[11]}{labels.SIDE[2]}{labels.SUF[1]}", self.importarms.lowerArm_R, self.lowerArm_roll_R, 0.5)

            # upperLeg roll
            self.create_roll_sys(f"{labels.JNT[33]}{labels.SIDE[2]}{labels.SUF[1]}", self.importlegs.upperLeg_R, self.upperLeg_roll_R, 0.5)
            
            # lowerLeg roll
            self.create_roll_sys(f"{labels.JNT[34]}{labels.SIDE[2]}{labels.SUF[1]}", self.importlegs.lowerLeg_R, self.lowerLeg_roll_R, 0.5)                     
    
    def main(self):
        self.apply_roll_jnts(mirror=True)
        self.setup_roll_sys(mirror=True)