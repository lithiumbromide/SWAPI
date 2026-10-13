---
title: "Get Block Definitions in Part or Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Block_Definitions_in_Part_or_Assembly_Example_VB.htm"
---

# Get Block Definitions in Part or Assembly Example (VBA)

This example shows how to get all of the block definitions and their block instances in a part or assembly.

```vb
'-----------------------------
'
' Preconditions: Part document is open and contains at least
'               one block definition and block instance.
'
' Postconditions: All of the block instances in the part are selected.
'
'-----------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim skMgr As SldWorks.SketchManager
Dim swSelMgr As SldWorks.SelectionMgr
Dim selBlockInst As SldWorks.SketchBlockInstance
Dim pBlock As SldWorks.SketchBlockDefinition
Dim pInst As Object
Dim vBlocks As Variant
Dim vInstances As Variant
Dim itr As Long
Dim jtr As Long
Dim retval As Boolean

Sub main()
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager

    Set skMgr = swModel.SketchManager

    vBlocks = skMgr.GetSketchBlockDefinitions

    ' Exit if no block definitions
    If IsEmpty(vBlocks) Then
        Exit Sub
    End If

    ' Process blocks instances
    For itr = 0 To UBound(vBlocks)
        Set pBlock = vBlocks(itr)
        vInstances = pBlock.GetInstances
        If False = IsEmpty(vInstances) Then
            For jtr = 0 To UBound(vInstances)
                Set pInst = vInstances(jtr)
                retval = pInst.Select(True, Nothing)
                Set selBlockInst = swSelMgr.GetSelectedObject6(1, -1)
            Next jtr
        End If
    Next itr
End Sub
```
