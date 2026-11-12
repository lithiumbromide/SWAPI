---
title: "Create Countersink Slot Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Countersink_Slot_Example_VB.htm"
---

# Create Countersink Slot Example (VBA)

This example shows how to create a countersink slot using the hole wizard.

```
'---------------------------------
' Preconditions:
' 1. SOLIDWORKS Design is running.
' 2. Open the Immediate window.
' 3. Run the macro.
'
' Postconditions:
' 1. Creates a model and a countersink
'    slot in the model using the hole wizard.
' 2. Examine the Immediate window.
'-----------------------------------
```

```vb
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatMgr As SldWorks.FeatureManager
Dim swFeat As SldWorks.Feature
Dim swSketchMgr As SldWorks.SketchManager

 Dim swWizardHoleFeatData As SldWorks.WizardHoleFeatureData2
Dim sketchLines As Variant
Dim longstatus As Long
Dim boolstatus As Boolean
Dim P1(2) As Double
Dim P2(2) As Double
Dim P3(2) As Double

Sub main()
```

```vb
Set swApp = Application.SldWorks

' Create the model for the countersink slot
swApp.ResetUntitledCount 0, 0, 0
Set swModel = swApp.NewDocument("C:\Documents and Settings\All Users\Application Data\SOLIDWORKS\SOLIDWORKS 2014\templates\Part.prtdot", 0, 0, 0)
swApp.ActivateDoc2 "Part1", False, longstatus
Set swModel = swApp.ActiveDoc
Set swSketchMgr = swModel.SketchManager
Set swModelDocExt = swModel.Extension
Set swFeatMgr = swModel.FeatureManager
sketchLines = swSketchMgr.CreateCornerRectangle(-0.05096498314664, 0.05060941349678, 0, 0.1021670127265, -0.05037236706354, 0)
boolstatus = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
boolstatus = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
boolstatus = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
boolstatus = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
Set swFeat = swFeatMgr.FeatureExtrusion2(True, False, False, 0, 0, 0.381, 0.381, False, False, False, False, 0.01745329251994, 0.01745329251994, False, False, False, False, True, True, True, 0, 0, False)

'Create three points for the reference plane
P1(0) = -1.41556764402858E-02
P1(1) = 1.94061273859598E-03
P1(2) = 0
P2(0) = -1.41556764402858E-02
P2(1) = 1.94061273859598E-03
P2(2) = 1
P3(0) = -0.149976101832345
P3(1) = -0.988792859011662
P3(2) = 0

'Create the reference plane
swModel.CreatePlaneFixed2 P1, P2, P3, False

'Select reference plane
boolstatus = swModelDocExt.SelectByID2("Plane1", "PLANE", -1.56784487003801E-02, -9.16715285390111E-03, 5.58270998665543E-02, False, 0, Nothing, 0)

' Create the hole countersink slot
Set swFeat = swFeatMgr.HoleWizard5(swWzdCounterSinkSlot, swStandardAnsiMetric, swStandardAnsiMetricFlatHead82, "M2", swEndCondThroughAll, 0.0102, 0.010312189893273, _
                                   1, 0.0044, 1.57079632679489, 1.52189893272978E-04, 0, 2.05948851735331, 0, 0, 0, 1, 0, 0, 0, "", False, True, True, True, True, False)
```

```vb
     Set swWizardHoleFeatData = swFeat.GetDefinition
      Debug.Print ("Length of countersink slot: " & swWizardHoleFeatData.Length)

End Sub
```
