---
title: "Insert Swept-cut Feature Using Circular Profile Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Swept-cut_Feature_Using_Circular_Profile_Example_VB.htm"
---

# Insert Swept-cut Feature Using Circular Profile Example (VBA)

This example shows how to create a swept-cut feature using a circular profile and get its properties.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the part exists.
' 2. Open an Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Selects an edge on the part.
' 3. Creates a cut-sweep feature using a circular profile.
' 4. Accesses the cut-sweep feature.
' 5. Changes the diameter of the circular profile.
' 6. Examine the Immediate window, FeatureManager
'    design tree, and graphics area.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swPathFeat As SldWorks.Feature
Dim swFeatureManager As SldWorks.FeatureManager
Dim swSweep As SldWorks.SweepFeatureData
Dim status As Boolean
Dim errors As Long
Dim warnings As Long

Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt", 1, 0, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    'Select an edge for the circular profile
    status = swModelDocExt.SelectByID2("", "EDGE", -3.72983839416747E-02, 3.93904284381961E-02, 4.95042874504179E-02, True, 4, Nothing, 0)
    Set swFeatureManager = swModel.FeatureManager
```

```vb
    Set swSweep = swModel.FeatureManager.CreateDefinition(swFmSweepCut)

     swSweep.TangentPropagation = False
     swSweep.AlignWithEndFaces = True
     swSweep.TwistControlType = 0
     swSweep.MaintainTangency = False
     swSweep.AdvancedSmoothing = False
     swSweep.StartTangencyType = 0
     swSweep.EndTangencyType = 0
     swSweep.PathAlignmentType = 0
     swSweep.FeatureScope = True
     swSweep.AutoSelect = True
     swSweep.MergeSmoothFaces = True
     swSweep.CircularProfile = True
     swSweep.CircularProfileDiameter = 0.008

     Set swPathFeat = swModel.FeatureManager.CreateFeature(swSweep)

     Set swSweep = swPathFeat.GetDefinition
     status = swSweep.AccessSelections(swModel, Nothing)
     Debug.Print "Using a circular profile? " & swSweep.CircularProfile
     Debug.Print "Original size of circular profile = " & swSweep.CircularProfileDiameter
     swSweep.CircularProfileDiameter = 0.003
     Debug.Print "Modified size of circular profile = " & swSweep.CircularProfileDiameter
     swPathFeat.ModifyDefinition swSweep, swModel, Nothing
```

```
End Sub
```
