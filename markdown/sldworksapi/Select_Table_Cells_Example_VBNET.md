---
title: "Select Table Cells Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Table_Cells_Example_VBNET.htm"
---

# Select Table Cells Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swSelectionMgr As SelectionMgr
        Dim swDrawing As DrawingDoc
        Dim swAnnotation As Annotation
        Dim swTableAnnotation As TableAnnotation
        Dim firstRow As Integer
        Dim lastRow As Integer
        Dim firstColumn As Integer
        Dim lastColumn As Integer
        Dim idx As Integer

        swModel = swApp.ActiveDoc
        swSelectionMgr = swModel.SelectionManager
        swDrawing = swModel

        For idx = 1 To swSelectionMgr.GetSelectedObjectCount2(-1)

            swTableAnnotation = swSelectionMgr.GetSelectedObject6(idx, -1)
            swAnnotation = swTableAnnotation.GetAnnotation

            swTableAnnotation.GetCellRange(firstRow, lastRow, firstColumn, lastColumn)

            Debug.Print("First selected cell's row     = " & firstRow)
            Debug.Print("Last selected cell's row      = " & lastRow)
            Debug.Print("First selected cell's column  = " & firstColumn)
            Debug.Print("Last selected cell's column   = " & lastColumn)
            Debug.Print("")

        Next idx

        If (firstRow = -1) Then
            Debug.Print("Selected entire table!")
        End If

        swModel.ClearSelection2(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
