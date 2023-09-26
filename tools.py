'''
RigBox Tools

'''

import maya.cmds as cmds

def query_location(name):
    result = cmds.xform(name, q=True, t=True)
        
    return result

def query_rotation(name):
    result = cmds.xform(name, q=True, ws=True, ro=True)
        
    return result
    
def average_location(primaryAxis, lastJoint):
    lastJoint_pos = cmds.xform(lastJoint, q=True, t=True)
    
    if primaryAxis == "X":
        result = lastJoint_pos[0]/2 
        finalResult = (result, 0,0)     
    if primaryAxis == "Y":
        result = lastJoint_pos[1]/2
        finalResult = (0,result,0)        
    if primaryAxis == "Z":
        result = lastJoint_pos[2]/2
        finalResult = (0,0,result)
        
    if primaryAxis == "-X":
        result = lastJoint_pos[0]/2 
        finalResult = ((result*-1), 0,0)     
    if primaryAxis == "-Y":
        result = lastJoint_pos[1]/2
        finalResult = (0,(result*-1),0)        
    if primaryAxis == "-Z":
        result = lastJoint_pos[2]/2
        finalResult = (0,0,(result*-1))            
        
    return finalResult
    
def create_joint_chain(primaryAxis, upAxis, jointList):
    if primaryAxis == "X":
        aim = (1,0,0)            
    if primaryAxis == "Y":
        aim = (0,1,0)
    if primaryAxis == "Z":
        aim = (0,0,1)
    if primaryAxis == "-X":
        aim = (-1,0,0)
    if primaryAxis == "-Y":
        aim = (0,-1,0)
    if primaryAxis == "-Z":
        aim = (0,0,-1)
    
    if upAxis == "X":
        up = (1,0,0)
    if upAxis == "Y":
        up = (0,1,0)
    if upAxis == "Z":
        up = (0,0,1)
    if upAxis == "-X":
        up = (-1,0,0)
    if upAxis == "-Y":
        up = (0,-1,0)
    if upAxis == "-Z":
        up = (0,0,-1)
    
    for i in range(len(jointList)-1):
        aim_joint = cmds.aimConstraint(jointList[i+1], jointList[i], aim=aim, wu=up) # Aim parent at child (X-forward, Z-up)
        cmds.delete(aim_joint) # Delete aim constraint
        cmds.makeIdentity(apply=True, r=True) # Zero joint rotations
        cmds.parent(jointList[i+1], jointList[i]) # Make parent relationship