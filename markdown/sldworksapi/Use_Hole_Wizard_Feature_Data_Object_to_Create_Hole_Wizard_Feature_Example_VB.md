---
title: "Use Hole Wizard Feature Data Object to Create Hole Wizard Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Use_Hole_Wizard_Feature_Data_Object_to_Create_Hole_Wizard_Feature_Example_VB.htm"
---

# Use Hole Wizard Feature Data Object to Create Hole Wizard Feature Example (VBA)

This example shows how to use an existing hole wizard feature data object to create another hole wizard feature.

```
'--------------------------------------------------------------
' Preconditions: Verify that the specified part to open exists.
'
' Postconditions:
' 1. Opens the part.
' 2. Creates a hole wizard feature.
' 3. Creates another hole wizard feature
'    based on the existing hole wizard feature
'    and selected entities.
' 4. Examine the graphics area and FeatureManager design tree.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat As SldWorks.Feature
Dim swWzdHole As SldWorks.WizardHoleFeatureData2
Dim swFeatMgr As SldWorks.FeatureManager
Dim boolstatus As Boolean
Dim longstatus As Long
Dim longwarnings As Long
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
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt", 1, 0, "", longstatus, longwarnings)
    Set swModelDocExt = swModel.Extension
    Set swFeatMgr = swModel.FeatureManager
    Set swSelMgr = swModel.SelectionManager
```

```
    ' Create hole wizard feature
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 2.21497493083689E-03, 3.96239999998897E-02, -4.21939153824269E-03, False, 0, Nothing, 0)
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
    ' Value1 to Value12 arguments; SOLIDWORKS Design
    ' ignores parameters set to -1
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
    Set swFeat = swFeatMgr.HoleWizard5(HoleType, StandardIndex, FastenerTypeIndex, SSize, EndType, Diameter, Depth, Length, CounterBoreDiameter, CounterBoreDepth, HeadClearance, ScrewFit, DrillAngle, NearCsinkDiameter, NearCsinkAngle, BotCsinkDiameter, BotCsinkAngle, FarCsinkDiameter, FarCsinkAngle, Offset, ThreadClass, False, False, False, False, False, False)
```

```
    ' Get the hole wizard feature data object
    boolstatus = swModelDocExt.SelectByID2("CBORE for #12 Binding Head Machine Screw1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set swWzdHole = swFeat.GetDefinition
    swModel.ClearSelection2 True
```

```
    Set swFeat = Nothing
```

```
    ' Select the reference entities to use to create another hole wizard feature
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 4.31776836886115E-02, 3.96239999998897E-02, -4.15372044423066E-02, False, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("", "VERTEX", 6.46002912861796E-02, 0.039624, -0.063937043942379, True, 2, Nothing, 0)
```

```
    ' Create the new hole wizard feature
    Set swFeat = swFeatMgr.CreateFeature(swWzdHole)
```

```
End Sub
```
