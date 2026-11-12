---
title: "Change Reference Dimension Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Reference_Dimension_Example_VB.htm"
---

# Change Reference Dimension Example (VBA)

This example shows how to change a reference dimension in a drawing without changing the model.

```vb
'------------------------------------------
'
' Preconditions:
'            (1) Drawing document is open.
'            (2) Reference dimension named RD1@Drawing View1 exists in the drawing.
'
' Postconditions: Value of RD1@Drawing View1 changed to 10.0, but model is not changed.
'
'-------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swDispDim As SldWorks.DisplayDimension
Dim boolstatus As Boolean

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swModelDocExt = swModel.Extension
Set swSelMgr = swModel.SelectionManager
boolstatus = swModelDocExt.SelectByID2("RD1@Drawing View1", "DIMENSION", 0.2765561531303, 0.1334812822687, 0, False, 0, Nothing, 0)

Set swDispDim = swSelMgr.GetSelectedObject6(1, 0)
swDispDim.SetText SwConst.swDimensionTextParts_e.swDimensionTextAll, "10.0"

End Sub
```
