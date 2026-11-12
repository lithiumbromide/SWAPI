---
title: "Change Weld Bead Faces Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Weld_Bead_Faces_Example_VB.htm"
---

# Change Weld Bead Faces Example (VBA)

This example shows how to change the faces of an existing fillet weld bead.

```vb
'-----------------------------------
'
' Preconditions: Fillet weld bead exists and is selected in
'                the open part document.
'
' Postconditions: Fillet weld bead is recreated on the
'                the selected faces.
'
'------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim SwFeat As SldWorks.Feature
Dim swWeldBead As WeldmentBeadFeatureData
Dim SwModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swComp As SldWorks.Component2
Dim f1 As Variant
Dim f2 As Variant
Dim fa1(0) As Object
Dim fa2(0) As Object
Dim boolstatus As Boolean

Sub main()

Set swApp = Application.SldWorks
Set SwModel = swApp.ActiveDoc
Set swSelMgr = SwModel.SelectionManager

'Select the fillet weld bead feature
Set SwFeat = swSelMgr.GetSelectedObject5(1)
Set swWeldBead = SwFeat.GetDefinition

'Roll back the model to the feature just above the weld bead feature
boolstatus = swWeldBead.AccessSelections(SwModel, swComp)

'Use both sides of the fillet weld bead
swWeldBead.UseOtherSide = True

'Set the type of weld bead to intermittent
swWeldBead.BeadType(swWeldBeadOtherSide) = swWeldBeadTypeIntermittent

'Select the two faces to which you want to apply the weld bead
Set fa1(0) = swSelMgr.GetSelectedObject5(1)
Set fa2(0) = swSelMgr.GetSelectedObject5(2)
f1 = fa1
f2 = fa2

'Use the selected faces for the weld bead
boolstatus = swWeldBead.SetFaces(swWeldBeadOtherSide, (f1), (f2))
'Modify the weld bead using the just selected faces
boolstatus = SwFeat.ModifyDefinition(swWeldBead, SwModel, swComp)

End Sub
```
