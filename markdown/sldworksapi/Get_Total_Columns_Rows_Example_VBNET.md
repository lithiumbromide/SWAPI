---
title: "Get the Total Number of Columns and Rows in a Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Total_Columns_Rows_Example_VBNET.htm"
---

# Get the Total Number of Columns and Rows in a Table Example (VB.NET)

This example shows how to get the total number of columns and rows (visible and hidden) in a table annotation.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a drawing that contains a hole table
 ' with multiple columns and rows.
 '
 ' Postconditions: Inspect the Immediate Window.
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub ProcessTable(ByVal swApp As SldWorks, _
     ByVal swModel As ModelDoc2, _
     ByVal swTable As TableAnnotation _
     )

         Dim swAnn As Annotation
         Dim nNumCol As Long
         Dim nNumRow As Long
         Dim nTotalNumCol As Long
         Dim nTotalNumRow As Long
         swAnn = swTable.GetAnnotation

         ' Show the name and type of table
         Debug.Print("    " & swAnn.GetName & " <" & swTable.Type & ">")

         ' Get the visible counts
         nNumCol = swTable.ColumnCount
         Debug.Print("      Number of visible columns: " & nNumCol)
         nNumRow = swTable.RowCount
         Debug.Print("      Number of visible rows: " & nNumRow)

         ' Get the total (hidden + visible) counts
         nTotalNumCol = swTable.TotalColumnCount
         Debug.Print("      Total number of visible + hidden columns: " & nTotalNumCol)
         nTotalNumRow = swTable.TotalRowCount
         Debug.Print("      Total number of visible + hidden rows: " & nTotalNumRow)

         ' Hide the first row and column
         Debug.Print("")
         Debug.Print("      First row and column are now hidden")
         Debug.Print("")
         swTable.RowHidden(0) = True
         swTable.ColumnHidden(0) =  True

         ' Get the visible counts
         nNumCol = swTable.ColumnCount
         Debug.Print("      Number of visible columns: " & nNumCol)
         nNumRow = swTable.RowCount
         Debug.Print("      Number of visible rows: " & nNumRow)

         ' Get the total (hidden + visible) counts
         nTotalNumCol = swTable.TotalColumnCount
         Debug.Print("      Total number of visible + hidden columns: " & nTotalNumCol)
         nTotalNumRow = swTable.TotalRowCount
         Debug.Print("      Total number of visible + hidden rows: " & nTotalNumRow)

     End Sub

     Sub main()

         Dim swModel As ModelDoc2
         Dim swDraw As DrawingDoc
         Dim swView As View
         Dim swTable As TableAnnotation

         swModel = swApp.ActiveDoc
         swDraw = swModel

         Debug.Print("File = " & swModel.GetPathName)

         ' Get the first view
         swView = swDraw.GetFirstView
         Do While Not swView Is  Nothing

             ' Show the name of the view
             Debug.Print("View =  " & swView.Name)

             ' Get the first table annotation for this view
             swTable = swView.GetFirstTableAnnotation

             Do While Not swTable Is  Nothing
                 ProcessTable(swApp, swModel, swTable)

                 ' Get next table annotation for this view
                 swTable = swTable.GetNext

             Loop

             ' Get the next view
             swView = swView.GetNextView

         Loop

     End Sub

     Public swApp As SldWorks

 End  Class
```
