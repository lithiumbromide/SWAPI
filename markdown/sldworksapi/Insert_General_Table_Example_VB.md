---
title: "Insert General Table (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_General_Table_Example_VB.htm"
---

# Insert General Table (VBA)

This example shows how to insert a general table in a drawing document and how to hide and show a row in that table.

```vb
'---------------------------------
' Preconditions: Drawing document is open.
'
' Postconditions: The third row of the general table is
'                 hidden and shown.
'----------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawing As SldWorks.DrawingDoc
Dim swTable As SldWorks.TableAnnotation

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swDrawing = swModel

' Insert general table with four rows
Set swTable = swDrawing.InsertTableAnnotation2(True, 0, 0, swBOMConfigurationAnchor_TopLeft, "", 4, 2)
Debug.Print "Nbr of rows before hiding third third row: " & swTable.RowCount
' Hide the third row
swTable.RowHidden(2) = True
Debug.Print "Nbr of rows after hiding third row: " & swTable.RowCount
' Show the third row
swTable.RowHidden(2) = False
Debug.Print "Nbr of rows after showing third row: " & swTable.RowCount

End Sub
```
