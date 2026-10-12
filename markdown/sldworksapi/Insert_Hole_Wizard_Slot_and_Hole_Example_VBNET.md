---
title: "Insert Hole Wizard Slot and Hole Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Hole_Wizard_Slot_and_Hole_Example_VBNET.htm"
---

# Insert Hole Wizard Slot and Hole Example (VB.NET)

This example shows how to use [IFeatureManager::HoleWizard5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~HoleWizard5.html) to insert a straight slot and a counterbore hole in a part.

```
'-----------------------------------------------
' Preconditions:
' 1. Verify that the specified part document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Creates a straight slot and a counterbore hole.
' 3. Prints the length of the slot to the Immediate
'    window.
' 4. To verify steps 2 and 3, examine the part in the
'    graphics area, the FeatureManager design tree,
'    and the Immediate window.
'
' NOTE: Because the part document is used elsewhere,
' do not save changes.
'------------------------------------------------

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swFeatureMgr As FeatureManager
        Dim swFeature As Feature
        Dim swModelDocExt As ModelDocExtension
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer
        Dim status As Boolean
        Dim SlotType As Integer
        Dim HoleType As Integer
        Dim StandardIndex As Integer
        Dim FastenerTypeIndex As Integer
        Dim SSize As String
        Dim EndType As Integer
        Dim ConvFactorLength As Double
        Dim ConvFactorAngle As Double
        Dim Diameter As Double
        Dim Depth As Double
        Dim Length As Double
        Dim ScrewFit As Double
        Dim DrillAngle As Double
        Dim NearCsinkDiameter As Double
        Dim NearCsinkAngle As Double
        Dim FarCsinkDiameter As Double
        Dim FarCsinkAngle As Double
        Dim Offset As Double
        Dim ThreadClass As String
        Dim CounterBoreDiameter As Double
        Dim CounterBoreDepth As Double
        Dim HeadClearance As Double
        Dim BotCsinkDiameter As Double
        Dim BotCsinkAngle As Double
        Dim swWizardHoleFeatData As WizardHoleFeatureData2

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2020\samples\tutorial\api\block20.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swFeatureMgr = swModel.FeatureManager
        swModelDocExt = swModel.Extension

        'Create a slot

        'Select the face where to create the slot
        status = swModelDocExt.SelectByID2("", "FACE", -0.000609805077203873, 0.0396239999998897, -0.00830387834611201, False, 0, Nothing, 0)

        SlotType = swWzdGeneralHoleTypes_e.swWzdHoleSlot
        StandardIndex = swWzdHoleStandards_e.swStandardAnsiInch
        FastenerTypeIndex = swWzdHoleStandardFastenerTypes_e.swStandardAnsiInchAllDrillSizes
        SSize = "#97"
        EndType = swEndConditions_e.swEndCondBlind
        ConvFactorLength = 25.4 / 1000     'Convert inches to meters
        ConvFactorAngle = (22 / 7) / 180   'Convert degrees to radians
        Diameter = 0.5 * ConvFactorLength
        Depth = 2 * ConvFactorLength
        Length = 3 * ConvFactorLength

        'Value1 to Value12 arguments; SOLIDWORKS Design
        'ignores parameters set to -1
        ScrewFit = -1                       'Value1
        DrillAngle = 100 * ConvFactorAngle  'Value2
        NearCsinkDiameter = -1              'Value3
        NearCsinkAngle = -1                 'Value4
        FarCsinkDiameter = -1               'Value5
        FarCsinkAngle = -1                  'Value6
        Offset = -1                         'Value7
        'Value8 - Value12 all set to -1

        ThreadClass = ""

        swFeature = swFeatureMgr.HoleWizard5(SlotType, StandardIndex, FastenerTypeIndex, SSize, EndType, _
           Diameter, Depth, Length, ScrewFit, DrillAngle, NearCsinkDiameter, NearCsinkAngle, _
           FarCsinkDiameter, FarCsinkAngle, Offset, -1, -1, -1, -1, -1, ThreadClass, _
           False, False, False, False, False, False)

        'Print length of slot to Immediate window
        swWizardHoleFeatData = swFeature.GetDefinition
        Debug.Print("Length of slot: " & swWizardHoleFeatData.Length & " inches")

        'Create a counterbore hole

        'Select the face where to create the hole
        status = swModelDocExt.SelectByID2("", "FACE", -0.0060197480091233, 0.0396239999998329, 0.0270812377555103, False, 0, Nothing, 0)

        HoleType = swWzdGeneralHoleTypes_e.swWzdCounterBore
        StandardIndex = swWzdHoleStandards_e.swStandardAnsiInch
        FastenerTypeIndex = swWzdHoleStandardFastenerTypes_e.swStandardAnsiInchBinding
        SSize = "#12"
        EndType = swEndConditions_e.swEndCondThroughAll
        ConvFactorLength = 25.4 / 1000      'Convert inches to meters
        ConvFactorAngle = (22 / 7) / 180    'Convert degrees to radians
        Diameter = 0.5 * ConvFactorLength
        Depth = -1
        Length = -1

        'Value1 to Value12 arguments; SOLIDWORKS Design
        'ignores parameters set to -1
        CounterBoreDiameter = 0.6 * ConvFactorLength    'Value1
        CounterBoreDepth = 0.2 * ConvFactorLength       'Value2
        HeadClearance = -1                              'Value3
        ScrewFit = -1                                   'Value4
        DrillAngle = -1                                 'Value5
        NearCsinkDiameter = -1                          'Value6
        NearCsinkAngle = -1                             'Value7
        BotCsinkDiameter = -1                           'Value8
        BotCsinkAngle = -1                              'Value9
        FarCsinkDiameter = -1                           'Value10
        FarCsinkAngle = -1                              'Value11
        Offset = -1                                     'Value12

        ThreadClass = ""

        swFeature = swFeatureMgr.HoleWizard5(HoleType, StandardIndex, FastenerTypeIndex, SSize, EndType, _
            Diameter, Depth, Length, CounterBoreDiameter, CounterBoreDepth, HeadClearance, ScrewFit, DrillAngle, _
            NearCsinkDiameter, NearCsinkAngle, BotCsinkDiameter, BotCsinkAngle, FarCsinkDiameter, FarCsinkAngle, Offset, _
            ThreadClass, False, False, False, False, False, False)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
