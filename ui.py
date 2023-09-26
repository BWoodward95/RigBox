"""
RigBox 2.0

To-Do:
    Connect Curve Library
    Connect Movement System
"""

from PySide2 import QtCore, QtGui, QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui
import maya.cmds as cmds

from rigbox import createskeleton

def getMayaMainWindow():
    return [obj for obj in QtWidgets.QApplication.topLevelWidgets() if obj.objectName() == 'MayaWindow'][0]    
    
class RigBox(QtWidgets.QDialog):
    
    dlg_instance=None
    
    @classmethod
    def show_dialog(cls):
        if not cls.dlg_instance:
            cls.dlg_instance = RigBox()
            
        if cls.dlg_instance.isHidden():
            cls.dlg_instance.show()
        else:
            cls.dlg_instance.raise_()
            cls.dlg_instance.activateWindow()
            
    def __init__(self, parent=None):
        super(RigBox, self).__init__(parent or getMayaMainWindow())
        self.setWindowTitle("RigBox v2.0")
        self.setMinimumSize(300, 100)
        
        self.skeleton_creator = createskeleton.CreateBaseSkeleton()
        
        self.createWidgets()
        self.createLayout()
        self.createConnections()
        
    def createWidgets(self):
        self.importSkeleton_btn = QtWidgets.QPushButton("Import Skeleton")
        self.setup_deformSystem_btn = QtWidgets.QPushButton("Create Deform System")
        self.setup_movementSystem_btn = QtWidgets.QPushButton("Create Movement System")
        self.setup_controlSystem_btn = QtWidgets.QPushButton("Create Control System")
        
    def createLayout(self):
        button_layout = QtWidgets.QVBoxLayout()
        button_layout.addWidget(self.importSkeleton_btn)
        button_layout.addWidget(self.setup_deformSystem_btn)
        button_layout.addWidget(self.setup_movementSystem_btn)
        button_layout.addWidget(self.setup_controlSystem_btn)
        
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(button_layout)
     
    def createConnections(self):
        self.importSkeleton_btn.clicked.connect(self.import_skeleton)
        self.setup_deformSystem_btn.clicked.connect(self.create_deform)
   
    def import_skeleton(self):
        self.skeleton_creator.create_root()
        self.skeleton_creator.create_spine()
        self.skeleton_creator.create_neck()
        self.skeleton_creator.create_leftLeg()
        self.skeleton_creator.create_rightLeg()
        self.skeleton_creator.create_leftArm(hand=True)
        self.skeleton_creator.create_rightArm(hand=True)
        self.skeleton_creator.finalize()
  
    def create_deform(self):
        self.skeleton_creator.apply_roll_jnts(mirror=True)
        self.skeleton_creator.setup_roll_sys(mirror=True)
        
if __name__ == "__main__":
    
    try:
        RigBox.close()
        RigBox.deleteLater()
    except:
        pass
    
    RigBox = RigBox()
    RigBox.show()    
        