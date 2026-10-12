---
title: "Get Block Instance in Part or Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Block_Instance_in_Part_or_Assembly_Example_VB.htm"
---

# Get Block Instance in Part or Assembly Example (VBA)

This example shows how to get a block instance and its block definition.

```vb
'-------------------------------------------------
'
' Precondition:
'          (1) Part or assembly document is open
'              that has at least one block instance.
'          (2) Block instance is selected.
'
' Postconditions: None
'
'--------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat As SldWorks.Feature
Dim swBlockInst As SldWorks.SketchBlockInstance
Dim swBlockDef As SldWorks.SketchBlockDefinition

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager
Set swBlockInst = swSelMgr.GetSelectedObject6(1, 0)

Debug.Print "BLOCK INSTANCE: "
Debug.Print "Number of attributes: " & swBlockInst.GetAttributeCount
Debug.Print "Scale: " & swBlockInst.Scale
Debug.Print "Name: " & swBlockInst.Name

Set swBlockDef = swBlockInst.Definition
Debug.Print " "
Debug.Print "BLOCK DEFINITION: "
Debug.Print "Number of arcs: " & swBlockDef.GetArcCount
Debug.Print "Number of dimensions: " & swBlockDef.GetDisplayDimensionCount
Debug.Print "Number of lines: " & swBlockDef.GetLineCount
End Sub
```
