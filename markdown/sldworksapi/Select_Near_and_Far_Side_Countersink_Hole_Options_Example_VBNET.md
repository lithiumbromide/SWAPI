---
title: "Select Near and Far Side Hole Wizard Countersink Features Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Near_and_Far_Side_Countersink_Hole_Options_Example_VBNET.htm"
---

# Select Near and Far Side Hole Wizard Countersink Features Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim FeatureData As WizardHoleFeatureData2
     Dim Feature As Feature
     Dim swModelDocExt As ModelDocExtension
     Dim swSelMgr As SelectionMgr
     Dim boolstatus As Boolean

     Sub main()

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension
         swSelMgr = swModel.SelectionManager

         swModel.ClearSelection2(True)

         boolstatus = swModelDocExt.SelectByID2("Hole1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, swSelectOption_e.swSelectOptionDefault)
         Feature = swSelMgr.GetSelectedObject6(1, -1)
         FeatureData = Feature.GetDefinition

         Debug.Print("Near side countersink option is selected: " & FeatureData.NearSideCounterSink)

         If (FeatureData.NearSideCounterSink)  Then
             FeatureData.NearSideCounterSink = False
         Else
             FeatureData.NearSideCounterSink = True ' near side countersink option is selected
             FeatureData.NearCounterSinkDiameter = 0.0061 ' meters
             FeatureData.NearCounterSinkAngle = 1.57 ' radians
         End If

         Debug.Print("Far side countersink option is selected: " & FeatureData.FarSideCounterSink)

         If (FeatureData.FarSideCounterSink) Then
             FeatureData.FarSideCounterSink = False
         Else
             FeatureData.FarSideCounterSink = True ' far side countersink option is selected
             FeatureData.FarCounterSinkDiameter = 0.0061 ' meters
             FeatureData.FarCounterSinkAngle = 1.57 ' radians
         End If

         boolstatus = Feature.ModifyDefinition(FeatureData, swModel,  Nothing)
         FeatureData = Feature.GetDefinition

         Debug.Print("Near side countersink option is selected: " & FeatureData.NearSideCounterSink)
         Debug.Print("Far side countersink option is selected: " & FeatureData.FarSideCounterSink)

     End Sub

     Public swApp As SldWorks

 End  Class
```
