---
title: "Insert Hole Wizard Slot and Hole Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Hole_Wizard_Slot_and_Hole_Example_VB.htm"
---

# Insert Hole Wizard Slot and Hole Example (VBA)

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
' 4. To verify steps 2 and 3, examine the part
'    in the graphics area, the FeatureManager
'    design tree, and the Immediate window.
'
' NOTE: Because the part document is used elsewhere,
' do not save changes.
'------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swFeatureMgr As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim fileName As String
Dim errors As Long
Dim warnings As Long
Dim status As Boolean
Dim SlotType As Long
Dim HoleType As Long
Dim StandardIndex As Long
Dim FastenerTypeIndex As Long
Dim SSize As String
Dim EndType As Long
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
Dim swWizardHoleFeatData As SldWorks.WizardHoleFeatureData2
```

```
Sub main()

    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2020\samples\tutorial\api\block20.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swFeatureMgr = swModel.FeatureManager
    Set swModelDocExt = swModel.Extension
```

```
    'Create a slot
```

```
    'Select the face where to create the slot
    status = swModelDocExt.SelectByID2("", "FACE", -6.09805077203873E-04, 3.96239999998897E-02, -8.30387834611201E-03, False, 0, Nothing, 0)
```

```
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
```

```
     'Value1 to Value7 arguments; SOLIDWORKS Design ignores parameters set to -1
```

```
     ScrewFit = -1                       'Value1
    DrillAngle = 100 * ConvFactorAngle  'Value2
    NearCsinkDiameter = -1              'Value3
    NearCsinkAngle = -1                 'Value4
    FarCsinkDiameter = -1               'Value5
    FarCsinkAngle = -1                  'Value6
    Offset = -1                         'Value7
    'Value8 - Value12 are all -1
```

```
     ThreadClass = ""
```

```
     Set swFeature = swFeatureMgr.HoleWizard5(SlotType, StandardIndex, FastenerTypeIndex, _
        SSize, EndType, Diameter, Depth, Length, ScrewFit, DrillAngle, _
        NearCsinkDiameter, NearCsinkAngle, FarCsinkDiameter, FarCsinkAngle, Offset, -1, -1, -1, _
        -1, -1, ThreadClass, False, False, False, False, False, False)

    'Print length of slot to Immediate window
    Set swWizardHoleFeatData = swFeature.GetDefinition
    Debug.Print "Length of slot: " & swWizardHoleFeatData.Length & " inches"
```

```
     'Create a counterbore hole
```

```
     'Select the face where to create the hole
    status = swModelDocExt.SelectByID2("", "FACE", -6.0197480091233E-03, 3.96239999998329E-02, 2.70812377555103E-02, False, 0, Nothing, 0)
```

```
     HoleType = swWzdGeneralHoleTypes_e.swWzdCounterBore
    StandardIndex = swWzdHoleStandards_e.swStandardAnsiInch
    FastenerTypeIndex = swWzdHoleStandardFastenerTypes_e.swStandardAnsiInchBinding
    SSize = "#12"
    EndType = swEndConditions_e.swEndCondThroughAll
    ConvFactorLength = 25.4 / 1000      'Convert inches to meters
    ConvFactorAngle = (22 / 7) / 180    'Convert degrees to radians
    Diameter = 0.5 * ConvFactorLength
    Depth = -1
    Length = -1    ' Holes do not have length
```

```
     'Value1 to Value12 arguments; SOLIDWORKS Design ignores parameters set to -1
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
```

```
     ThreadClass = ""
```

```
     Set swFeature = swFeatureMgr.HoleWizard5(HoleType, StandardIndex, FastenerTypeIndex, SSize, EndType, _
         Diameter, Depth, Length, CounterBoreDiameter, CounterBoreDepth, HeadClearance, ScrewFit, DrillAngle, _
         NearCsinkDiameter, NearCsinkAngle, BotCsinkDiameter, BotCsinkAngle, FarCsinkDiameter, FarCsinkAngle, _
         Offset, ThreadClass, False, False, False, False, False, False)
```

```
End Sub
```
