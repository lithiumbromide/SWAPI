---
title: "Clear, Set, and Toggle Selection Filters Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Clear,_Set,_and_Toggle_Selection_Filters_Example_VB.htm"
---

# Clear, Set, and Toggle Selection Filters Example (VBA)

## Set and Toggle Selection Filters Example (VBA)

This example shows how to clear all existing selection filters, set new selection filters, and toggle the selection filters on and off.

```vb
'------------------------------------------------
'
' Preconditions: Model document is open.
'
' Postconditions:
'          (1) Any existing selected selection filters are cleared.
'          (2) The face, edge, and vertex selection filters are selected.
'          (3) The selection filters are turned off.
'
'-------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim SelMgr As Object
Dim boolstatus As Boolean

Sub main()

Dim params As Variant
Dim selfils(2) As Long

Set swApp = Application.SldWorks

Set swModel = swApp.ActiveDoc
Set SelMgr = swModel.SelectionManager

'Clear all existing selection filters
params = swApp.GetSelectionFilters
swApp.SetSelectionFilters params, False
params = swApp.GetSelectionFilters

'Define filters to select
selfils(0) = 1 'Edge
selfils(1) = 2 'Face
selfils(2) = 3 'Vertex
swApp.SetSelectionFilters (selfils), True

'Toggle the selection filter
boolstatus = swApp.GetApplySelectionFilter
If boolstatus = False Then
    swApp.SetApplySelectionFilter True
Else
    swApp.SetApplySelectionFilter False
End If

End Sub
```
