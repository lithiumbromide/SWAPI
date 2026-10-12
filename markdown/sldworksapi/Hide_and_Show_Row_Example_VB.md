---
title: "Hide and Show Row(VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_and_Show_Row_Example_VB.htm"
---

# Hide and Show Row(VBA)

## Hide and Show Row (VBA)

This example shows how to hide and show a row in a general table.

```vb
'---------------------------------
' Preconditions: Drawing document is open and
'                contains a general table feature
'                with at least three rows and that
'                feature is selected.
'
' Postconditions: The third row of the general table is
'                 hidden and shown.
'----------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swGeneralTableFeature As SldWorks.GeneralTableFeature
Dim vTables As Variant
Dim swTable As SldWorks.TableAnnotation
Dim boolstatus As Boolean

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager
Set swModelDocExt = swModel.Extension

' Interactively have selected a general table feature
Set swGeneralTableFeature = swSelMgr.GetSelectedObject6(1, -1)

Debug.Print "Nbr of table annotations: " & swGeneralTableFeature.GetTableAnnotationCount
vTables = swGeneralTableFeature.GetTableAnnotations
Set swTable = vTables(0)
Debug.Print "Nbr of rows before hiding third third row: " & swTable.RowCount
' Hide the third row
swTable.RowHidden(2) = True
Debug.Print "Nbr of rows after hiding third row: " & swTable.RowCount
' Show the third row
swTable.RowHidden(2) = False
Debug.Print "Nbr of rows after showing third row: " & swTable.RowCount

End Sub
```
