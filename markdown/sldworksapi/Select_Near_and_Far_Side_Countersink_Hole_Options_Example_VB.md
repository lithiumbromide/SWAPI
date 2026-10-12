---
title: "Select Near and Far Side Hole Wizard Countersink Features Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Near_and_Far_Side_Countersink_Hole_Options_Example_VB.htm"
---

# Select Near and Far Side Hole Wizard Countersink Features Example (VBA)

This example shows how to select near and far side Hole Wizard countersink features.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part that contains a Hole Wizard hole named, Hole1.
 ' 2. Modify the countersink diameter and angle values as required by Hole1.
 ' 3. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Inspect the Immediate window.
 ' 2. The current near side countersink option is displayed.
 ' 3. The current far side countersink option is displayed.
 ' 4. The near side countersink option is toggled.
 '    If the near side countersink option is selected,
 '    the proper angle and diameter are set.
 ' 5. The far side countersink option is toggled.
 '    If the far side countersink option is selected,
 '    the proper angle and diameter are set.
 ' 6. The new near side countersink option is displayed.
 ' 7. The new far side countersink option is displayed.
 ' ---------------------------------------------------------------------------

 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim FeatureData As SldWorks.WizardHoleFeatureData2
 Dim Feature As SldWorks.Feature
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim boolstatus As Boolean
 Option Explicit
 Sub main()

     Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension
     Set swSelMgr = swModel.SelectionManager

     swModel.ClearSelection2 True

     boolstatus = swModelDocExt.SelectByID2("Hole1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
     Set Feature = swSelMgr.GetSelectedObject6(1, -1)
     Set FeatureData = Feature.GetDefinition

     Debug.Print "Near side countersink option is selected: " & FeatureData.NearSideCounterSink

     If (FeatureData.NearSideCounterSink) Then
         FeatureData.NearSideCounterSink = False
     Else
         FeatureData.NearSideCounterSink = True ' near side countersink option is selected
         FeatureData.NearCounterSinkDiameter = 0.0061 ' meters
         FeatureData.NearCounterSinkAngle = 1.57 ' radians
     End If

     Debug.Print "Far side countersink option is selected: " & FeatureData.FarSideCounterSink

     If (FeatureData.FarSideCounterSink) Then
         FeatureData.FarSideCounterSink = False
     Else
         FeatureData.FarSideCounterSink = True ' far side countersink option is selected
         FeatureData.FarCounterSinkDiameter = 0.0061 ' meters
         FeatureData.FarCounterSinkAngle = 1.57 ' radians
     End If

     boolstatus = Feature.ModifyDefinition(FeatureData, swModel, Nothing)
     Set FeatureData = Feature.GetDefinition

     Debug.Print "Near side countersink option is selected: " & FeatureData.NearSideCounterSink
     Debug.Print "Far side countersink option is selected: " & FeatureData.FarSideCounterSink

 End Sub
```
