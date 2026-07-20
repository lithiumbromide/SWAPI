---
title: "Get Table Annotation and Contents Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Table_Annotation_and_Contents_Example_VB.htm"
---

# Get Table Annotation and Contents Example (VBA)

This example shows how to get the table annotation and its contents.

```
'-----------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\2012-sm.slddrw.
' 2. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'-----------------------------------------------------
Option Explicit
```

```
Sub ProcessTable(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swTable As SldWorks.TableAnnotation)
```

```
    Dim swAnn As SldWorks.Annotation
    Dim nNumCol As Long
    Dim nNumRow As Long
    Dim sRowStr As String
    Dim i As Long
    Dim j  As Long
```

```
    Set swAnn = swTable.GetAnnotation
    nNumCol = swTable.ColumnCount
    nNumRow = swTable.RowCount
```

```
    ' Show the name and type of table
    Debug.Print "    " & swAnn.GetName & " <" & swTable.Type & ">"
```

```
    ' Get the table contents
    For i = 0 To nNumRow - 1
        sRowStr = "      ["
        For j = 0 To nNumCol - 1
            sRowStr = sRowStr & swTable.DisplayedText2(i, j, True) & ","
        Next j
        ' Show the table contents
        Debug.Print Left(sRowStr, Len(sRowStr) - 1) & "]"
    Next i
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swView As SldWorks.View
    Dim swTable As SldWorks.TableAnnotation
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    ' Get the first view
    Set swView = swDraw.GetFirstView
    Do While Not swView Is Nothing
        ' Show the name of the view
        Debug.Print "  " & swView.Name
        ' Get the first table annotation for this view
        Set swTable = swView.GetFirstTableAnnotation2
        Do While Not swTable Is Nothing
            ProcessTable swApp, swModel, swTable
            ' Get next table annotation for this view
            Set swTable = swTable.GetNext
        Loop
        ' Get the next view
        Set swView = swView.GetNextView
    Loop
```

```
End Sub
```
