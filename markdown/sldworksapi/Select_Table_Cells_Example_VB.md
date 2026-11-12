---
title: "Select Table Cells Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Table_Cells_Example_VB.htm"
---

# Select Table Cells Example (VBA)

This example shows how to interpret the results of selecting table cells in various ways.

```
'-----------------------------------------------------
' Preconditions:
' 1. A drawing with a table, which has multiple rows
'    and columns, is open.
' 2. Open the Immediate window.
' 3. Select a column.
' 4. Run the macro.
'
' Postconditions:
' 1. The range for all of the cells in the column is
'    printed to the Immediate window. Examine
'    the Immediate window.
' 2. Hold down the Ctrl key and click a cell.
' 3. Repeat step 2 to select additional adjacent cells.
' 4. Run the macro again.
' 5. The range for each selected cell is printed to
'    the Immediate window. Examine the Immediate
'    window.
'--------------------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
```

```
Sub main()
```

```
    Dim swModel             As SldWorks.ModelDoc2
    Dim swSelectionMgr      As SldWorks.SelectionMgr
    Dim swDrawing           As SldWorks.DrawingDoc
    Dim swAnnotation        As SldWorks.Annotation
    Dim swTableAnnotation   As SldWorks.TableAnnotation
    Dim firstRow            As Long
    Dim lastRow             As Long
    Dim firstColumn         As Long
    Dim lastColumn          As Long
    Dim idx                 As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelectionMgr = swModel.SelectionManager
    Set swDrawing = swModel
```

```
    For idx = 1 To swSelectionMgr.GetSelectedObjectCount2(-1)
```

```
        Set swTableAnnotation = swSelectionMgr.GetSelectedObject6(idx, -1)
        Set swAnnotation = swTableAnnotation.GetAnnotation
```

```
        swTableAnnotation.GetCellRange firstRow, lastRow, firstColumn, lastColumn
```

```
        Debug.Print "First selected cell's row     = " & firstRow
        Debug.Print "Last selected cell's row      = " & lastRow
        Debug.Print "First selected cell's column  = " & firstColumn
        Debug.Print "Last selected cell's column   = " & lastColumn
        Debug.Print ""
```

```
    Next idx
```

```
    If (firstRow = -1) Then
            Debug.Print "Selected entire table!"
    End If
```

```
    swModel.ClearSelection2 True
```

```
End Sub
```
