---
title: "Hide or Show First Row in Bill of Materials Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Hide_or_Show_First_Row_in_Bill_of_Materials_Example_VB.htm"
---

# Hide or Show First Row in Bill of Materials Example (VBA)

This example shows how to hide the first row in a Bill of Materials if it is visible, or show the first row in a Bill of Materials if it is hidden.

```vb
'-----------------------------------------------------
'
' Preconditions: Drawing document is open and contains
'                a Bill of Materials with at least one
'                row. Any row in the Bill of Materials is
'                selected.
'
' Postconditions: The first row in the Bill of Materials
'                is hidden if it was visible or the first
'                row in the Bill of Materials is visible
'                if it was hidden.
'
'-----------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swBomTable As SldWorks.BomTableAnnotation
Dim swAnnotationTable As SldWorks.TableAnnotation

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager
Set swBomTable = swSelMgr.GetSelectedObject6(1, -1)
Set swAnnotationTable = swBomTable
If swBomTable.RowHidden(1) Then
    swBomTable.RowHidden(1) = False
Else
    swBomTable.RowHidden(1) = True
End If

End Sub
```
