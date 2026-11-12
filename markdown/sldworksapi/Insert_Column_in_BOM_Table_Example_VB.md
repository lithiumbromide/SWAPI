---
title: "Insert Column in BOM Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Column_in_BOM_Table_Example_VB.htm"
---

# Insert Column in BOM Table Example (VBA)

This example shows how to insert a part number column in a BOM table.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a drawing that contains a BOM table.
' 2. Right-click the BOM table, select Select,
'    and select Table.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Inserts a part number column at the end of the
'    the BOM table.
' 2. Examine the BOM table and Immediate window.
'---------------------------------------------------
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim boolstatus As Boolean
Dim SelMgr As Object
Dim theTableAnnotation As SldWorks.TableAnnotation
Dim SelObjType As Long
Dim TableAnnotationType As Long

Sub DisplayTableColumnProps(theTableAnnotation As Object)

    Dim ColCount As Long
    Dim i As Long
    Dim ColType As swTableColumnTypes_e
    Dim ColTitle As String

    Debug.Print "Col#"; vbTab; "Type"; vbTab; "Title"
    ColCount = theTableAnnotation.ColumnCount
    For i = 0 To ColCount - 1
        ColType = theTableAnnotation.GetColumnType2(i, True)
        ColTitle = theTableAnnotation.GetColumnTitle2(i, True)
        Debug.Print i; vbTab; ColType; vbTab; ColTitle
    Next i

End Sub

Sub main()

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set SelMgr = swModel.SelectionManager

    SelObjType = SelMgr.GetSelectedObjectType3(1, -1)
    If SelObjType <> swSelANNOTATIONTABLES Then
        MsgBox "Select a BOM table in the drawing before running this example."
        End
    End If

    Set theTableAnnotation = SelMgr.GetSelectedObject6(1, -1)
    TableAnnotationType = theTableAnnotation.Type
    If TableAnnotationType <> swTableAnnotation_BillOfMaterials Then
        MsgBox "Select a BOM table in the drawing before running this example."
        End
    End If

    Debug.Print "Table before inserting a column..."
    ' Display table before inserting a column
    DisplayTableColumnProps theTableAnnotation

    ' Insert new column
    boolstatus = theTableAnnotation.InsertColumn2(swTableItemInsertPosition_Last, 0, "New Column", swInsertColumn_DefaultWidth)
    boolstatus = theTableAnnotation.SetColumnType2(theTableAnnotation.ColumnCount - 1, swBomTableColumnType_PartNumber, True)

    Debug.Print " "
    Debug.Print "Table after inserting a column..."
    ' Display table after inserting a column
    DisplayTableColumnProps theTableAnnotation

End Sub
```
