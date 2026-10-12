---
title: "Set New End Condition for Simple Hole Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_New_End_Condition_for_Simple_Hole_Feature_Example_VB.htm"
---

# Set New End Condition for Simple Hole Feature Example (VBA)

This example shows how to set a new end condition for a simple hole feature.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part document containing a block with a simple hole feature named
 '    Hole1.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Select the bottom face of the block at Stop, then press F5.
 ' 2. Sets the bottom face of the block as the new end condition
 '    of the simple hole feature.
 ' 3. Examine the Immediate window.
 '----------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Model As SldWorks.ModelDoc2
 Dim SelMgr As SldWorks.SelectionMgr
 Dim SimpleHoleFeature As SldWorks.Feature
 Dim SimpleHoleFeature_DEF As SldWorks.SimpleHoleFeatureData2
 Dim bottomFace As SldWorks.Face2
 Dim SimpleHoleEndCondition As SldWorks.Face2
 Dim boolstatus As Boolean
Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set Model = swApp.ActiveDoc
     Set SelMgr = Model.SelectionManager

    boolstatus = Model.Extension.SelectByID2("Hole1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
     Set SimpleHoleFeature = SelMgr.GetSelectedObject6(1, -1)

    Stop 'Select the bottom face of the block, then press F5
     Set bottomFace = SelMgr.GetSelectedObject6(1, -1)

    Set SimpleHoleFeature_DEF = SimpleHoleFeature.GetDefinition
     SimpleHoleFeature_DEF.AccessSelections Model, Nothing

    Dim SimpleHoleType As Long

    ' Print the type of hole
     SimpleHoleType = SimpleHoleFeature_DEF.Type
     Debug.Print "Hole type: " & SimpleHoleType

    ' If the end condition is blind, no reference is returned
     Set SimpleHoleEndCondition = SimpleHoleFeature_DEF.GetEndConditionReference(SimpleHoleType)

    SimpleHoleFeature_DEF.Type = swEndCondUpToSurface
     SimpleHoleFeature_DEF.SetEndConditionReference bottomFace
     SimpleHoleFeature.ModifyDefinition SimpleHoleFeature_DEF, Model, Nothing
     SimpleHoleFeature_DEF.AccessSelections Model, Nothing

    ' Print the type of hole
     SimpleHoleType = SimpleHoleFeature_DEF.Type
     Debug.Print "Hole type after setting end condition: " & SimpleHoleType

    ' The end condition is not blind, so a reference is returned
     Set SimpleHoleEndCondition = SimpleHoleFeature_DEF.GetEndConditionReference(SimpleHoleType)

     SimpleHoleFeature_DEF.ReleaseSelectionAccess

End Sub
```
