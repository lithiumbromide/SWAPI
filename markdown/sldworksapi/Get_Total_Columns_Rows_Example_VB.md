---
title: "Get the Total Number of Columns and Rows in a Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Total_Columns_Rows_Example_VB.htm"
---

# Get the Total Number of Columns and Rows in a Table Example (VBA)

This example shows how to get the total number of columns and rows (visible and hidden) in a table annotation.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a drawing that contains a hole table
 ' with multiple columns and rows.
 '
 ' Postconditions: Inspect the Immediate Window.
 '----------------------------------------------------------------------------
Option Explicit
Sub ProcessTable( _
     swApp As SldWorks.SldWorks, _
     swModel As SldWorks.ModelDoc2, _
     swTable As SldWorks.TableAnnotation _
 )
    Dim swAnn                   As SldWorks.Annotation
     Dim nNumCol                 As Long
     Dim nNumRow                 As Long
     Dim nTotalNumCol            As Long
     Dim nTotalNumRow            As Long
     Set swAnn = swTable.GetAnnotation

    ' Show the name and type of table
     Debug.Print "    " & swAnn.GetName & " <" & swTable.Type & ">"
    ' Get the visible counts
     nNumCol = swTable.ColumnCount
     Debug.Print "      Number of visible columns: " & nNumCol
     nNumRow = swTable.RowCount
     Debug.Print "      Number of visible rows: " & nNumRow

    ' Get the total (hidden + visible) counts
     nTotalNumCol = swTable.TotalColumnCount
     Debug.Print "      Total number of visible + hidden columns: " & nTotalNumCol
     nTotalNumRow = swTable.TotalRowCount
     Debug.Print "      Total number of visible + hidden rows: " & nTotalNumRow
    ' Hide the first row and column
     Debug.Print ""
     Debug.Print "      First row and column are now hidden"
     Debug.Print ""
     swTable.RowHidden(0) = True
     swTable.ColumnHidden(0) = True
    ' Get the visible counts
     nNumCol = swTable.ColumnCount
     Debug.Print "      Number of visible columns: " & nNumCol
     nNumRow = swTable.RowCount
     Debug.Print "      Number of visible rows: " & nNumRow

    ' Get the total (hidden + visible) counts
     nTotalNumCol = swTable.TotalColumnCount
     Debug.Print "      Total number of visible + hidden columns: " & nTotalNumCol
     nTotalNumRow = swTable.TotalRowCount
     Debug.Print "      Total number of visible + hidden rows: " & nTotalNumRow
End Sub
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swDraw                  As SldWorks.DrawingDoc
     Dim swView                  As SldWorks.View
     Dim swTable                 As SldWorks.TableAnnotation
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swDraw = swModel
    Debug.Print "File = " & swModel.GetPathName
    ' Get the first view
     Set swView = swDraw.GetFirstView
     Do While Not swView Is Nothing
        ' Show the name of the view
         Debug.Print "View =  " & swView.Name
        ' Get the first table annotation for this view
         Set swTable = swView.GetFirstTableAnnotation
        Do While Not swTable Is Nothing
             ProcessTable swApp, swModel, swTable
            ' Get next table annotation for this view
             Set swTable = swTable.GetNext
        Loop
        ' Get the next view
         Set swView = swView.GetNextView
    Loop
End Sub
```
