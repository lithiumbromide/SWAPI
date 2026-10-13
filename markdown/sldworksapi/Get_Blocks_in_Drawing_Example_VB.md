---
title: "Get Blocks in Drawing Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Blocks_in_Drawing_Example_VB.htm"
---

# Get Blocks in Drawing Example (VBA)

This example shows how to get a block definition and its block instances in a drawing.

```vb
'---------------------------------------------------
'
' Precondition:
'          (1) Drawing is open that contains at least
'              one block definition with at least one
'              block instance.
'          (2) The block definition is selected in the
'              FeatureManager design tree.
'
' Postconditions: None
'
'----------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat As SldWorks.Feature
Dim swBlockDef As SldWorks.SketchBlockDefinition
Dim swBlockInst As SldWorks.SketchBlockInstance
Dim nbrBlockInst As Integer
Dim vBlockInst As Variant
Dim itr As Integer

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager
Set swFeat = swSelMgr.GetSelectedObject6(1, 0)
Set swBlockDef = swFeat.GetSpecificFeature2

Debug.Print "Feature type: " & swFeat.GetTypeName
nbrBlockInst = swBlockDef.GetInstanceCount
Debug.Print "Number of instances of selected block: " & nbrBlockInst

If nbrBlockInst > 0 Then
        vBlockInst = swBlockDef.GetInstances
    For itr = 0 To (nbrBlockInst - 1)
        Set swBlockInst = vBlockInst(itr)
        Debug.Print "Name of block instances: " & swBlockInst.Name
    Next itr
End If

End Sub
```
