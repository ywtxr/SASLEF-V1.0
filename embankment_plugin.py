from abaqusGui import *
from abaqusConstants import ALL
import osutils, os


###########################################################################
# Class definition
###########################################################################

class Embankment_plugin(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='bankment',
            objectName='Embankment', registerQuery=False)
        pickedDefault = ''
        self.IDKw = AFXFloatKeyword(self.cmd, 'ID', True, 1)
        self.LKw = AFXFloatKeyword(self.cmd, 'L', True, 30)
        self.h1Kw = AFXFloatKeyword(self.cmd, 'h1', True, 6.0)
        self.i1Kw = AFXFloatKeyword(self.cmd, 'i1', True, 1.45)
        self.HKw = AFXFloatKeyword(self.cmd, 'H', True, 10)
        self.L0Kw = AFXFloatKeyword(self.cmd, 'L0', True, 150)
        self.d0Kw = AFXFloatKeyword(self.cmd, 'd0', True, 0.25)
        self.load1Kw = AFXFloatKeyword(self.cmd, 'load1', True, 9.8)
        self.Density1Kw = AFXFloatKeyword(self.cmd, 'Density1', True, 1.996)
        self.AKKw = AFXFloatKeyword(self.cmd, 'AK', True, 300)
        self.ANKw = AFXFloatKeyword(self.cmd, 'AN', True, 0.4)
        self.RFKw = AFXFloatKeyword(self.cmd, 'RF', True, 0.6)
        self.CKw = AFXFloatKeyword(self.cmd, 'C', True, 84.3)
        self.FAKw = AFXFloatKeyword(self.cmd, 'FA', True, 27.3)
        self.PAKw = AFXFloatKeyword(self.cmd, 'PA', True, 101.3)
        self.VKBKw = AFXFloatKeyword(self.cmd, 'VKB', True, 200)
        self.VNBKw = AFXFloatKeyword(self.cmd, 'VNB', True, 0.5)
        self.AURKw = AFXFloatKeyword(self.cmd, 'AUR', True, 2.3)
        self.stress2Kw = AFXFloatKeyword(self.cmd, 'stress2', True, 338.8)
        self.Density2Kw = AFXFloatKeyword(self.cmd, 'Density2', True, 2.117)
        self.AK2Kw = AFXFloatKeyword(self.cmd, 'AK2', True, 400)
        self.AN2Kw = AFXFloatKeyword(self.cmd, 'AN2', True, 0.3)
        self.RF2Kw = AFXFloatKeyword(self.cmd, 'RF2', True, 0.75)
        self.C2Kw = AFXFloatKeyword(self.cmd, 'C2', True, 35.4)
        self.FA2Kw = AFXFloatKeyword(self.cmd, 'FA2', True, 17.2)
        self.PA2Kw = AFXFloatKeyword(self.cmd, 'PA2', True, 101.3)
        self.VKB2Kw = AFXFloatKeyword(self.cmd, 'VKB2', True, 100)
        self.VNB2Kw = AFXFloatKeyword(self.cmd, 'VNB2', True, 0.5)
        self.AUR2Kw = AFXFloatKeyword(self.cmd, 'AUR2', True, 1)
        self.stress22Kw = AFXFloatKeyword(self.cmd, 'stress22', True, 100)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import embankmentDB
        return embankmentDB.EmbankmentDB(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        #
        for kw1,kw2,d in self.radioButtonGroups.values():
            try:
                value = d[ kw1.getValue() ]
                kw2.setValue(value)
            except:
                pass
        return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Register the plug-in
#
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='Embankment', 
    object=Embankment_plugin(toolset),
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    kernelInitString='import Embankment',
    applicableModules=ALL,
    version='N/A',
    author='N/A',
    description='N/A',
    helpUrl='N/A'
)
