from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class EmbankmentDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'SASLEF V1.0',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            
        GroupBox_4 = FXGroupBox(p=self, text='embankment', opts=FRAME_GROOVE)
        fileName = os.path.join(thisDir, 'rsg.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=GroupBox_4, text='', ic=icon)
        HFrame_1 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=15, pr=0, pt=0, pb=0)
        GroupBox_3 = FXGroupBox(p=HFrame_1, text='Parameters', opts=FRAME_GROOVE)
        VAligner_9 = AFXVerticalAligner(p=GroupBox_3, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=VAligner_9, ncols=12, labelText='Jobname:', tgt=form.IDKw, sel=0)
        AFXTextField(p=VAligner_9, ncols=12, labelText='L(m):', tgt=form.LKw, sel=0)
        AFXTextField(p=VAligner_9, ncols=12, labelText='h1(m):', tgt=form.h1Kw, sel=0)
        AFXTextField(p=VAligner_9, ncols=12, labelText='i1:', tgt=form.i1Kw, sel=0)
        AFXTextField(p=VAligner_9, ncols=12, labelText='H(m):', tgt=form.HKw, sel=0)
        AFXTextField(p=VAligner_9, ncols=12, labelText='L0(m):', tgt=form.L0Kw, sel=0)
        AFXTextField(p=VAligner_9, ncols=12, labelText='d0(m):', tgt=form.d0Kw, sel=0)
        AFXTextField(p=VAligner_9, ncols=12, labelText='g(m/s2):', tgt=form.load1Kw, sel=0)
        VFrame_3 = FXVerticalFrame(p=HFrame_1, opts=0, x=0, y=0, w=0, h=0,
            pl=10, pr=0, pt=0, pb=0)
        GroupBox_1 = FXGroupBox(p=HFrame_1, text='Duncan-Chang EB model', opts=FRAME_GROOVE)
        HFrame_3 = FXHorizontalFrame(p=GroupBox_1, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_6 = FXGroupBox(p=HFrame_3, text='Embankment', opts=FRAME_GROOVE)
        VAligner_3 = AFXVerticalAligner(p=GroupBox_6, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='Density1:', tgt=form.Density1Kw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='AK:', tgt=form.AKKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='AN:', tgt=form.ANKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='RF:', tgt=form.RFKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='C:', tgt=form.CKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='FA:', tgt=form.FAKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='PA:', tgt=form.PAKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='VKB:', tgt=form.VKBKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='VNB:', tgt=form.VNBKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='AUR:', tgt=form.AURKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='pc:', tgt=form.stress2Kw, sel=0)
        GroupBox_5 = FXGroupBox(p=HFrame_3, text='Underlying foundation', opts=FRAME_GROOVE)
        VAligner_4 = AFXVerticalAligner(p=GroupBox_5, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Density2:', tgt=form.Density2Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='AK2:', tgt=form.AK2Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='AN2:', tgt=form.AN2Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='RF2:', tgt=form.RF2Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='C2:', tgt=form.C2Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='FA2:', tgt=form.FA2Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='PA2:', tgt=form.PA2Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='VKB2:', tgt=form.VKB2Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='VNB2:', tgt=form.VNB2Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='AUR2:', tgt=form.AUR2Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='pc:', tgt=form.stress22Kw, sel=0)
