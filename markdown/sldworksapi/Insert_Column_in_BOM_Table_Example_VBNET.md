---
title: "Insert Column in BOM Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Column_in_BOM_Table_Example_VBNET.htm"
---

# Insert Column in BOM Table Example (VB.NET)

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
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim boolstatus As Boolean
        Dim SelMgr As Object
        Dim theTableAnnotation As TableAnnotation
        Dim SelObjType As Long
        Dim TableAnnotationType As Long

        swModel = swApp.ActiveDoc
        SelMgr = swModel.SelectionManager
        SelObjType = SelMgr.GetSelectedObjectType3(1, -1)
        If SelObjType <> swSelectType_e.swSelANNOTATIONTABLES Then
            MsgBox("Select a BOM table in the drawing before running this example.")
            Exit Sub
        End If

        theTableAnnotation = SelMgr.GetSelectedObject6(1, -1)
        TableAnnotationType = theTableAnnotation.Type
        If TableAnnotationType <> swTableAnnotationType_e.swTableAnnotation_BillOfMaterials Then
            MsgBox("Select a BOM table in the drawing before running this example.")
            Exit Sub
        End If

        Debug.Print("Table before inserting a column...")
        ' Display table before inserting a column
        DisplayTableColumnProps(theTableAnnotation)

        ' Insert new column
        boolstatus = theTableAnnotation.InsertColumn2(swTableItemInsertPosition_e.swTableItemInsertPosition_Last, 0, "New Column", swInsertTableColumnWidthStyle_e.swInsertColumn_DefaultWidth)
        boolstatus = theTableAnnotation.SetColumnType2(theTableAnnotation.ColumnCount - 1, swTableColumnTypes_e.swBomTableColumnType_PartNumber, True)

        Debug.Print(" ")

        Debug.Print("Table after inserting a column...")
        ' Display table after inserting a column
        DisplayTableColumnProps(theTableAnnotation)
```

```vb
    End Sub

    Sub DisplayTableColumnProps(ByVal theTableAnnotation As Object)

        Dim ColCount As Long
        Dim i As Long
        Dim iString As String
        Dim ColType As Long
        Dim ColTypeString As String
        Dim ColTitle As String

        Debug.Print("Col#  " + "Type   " + "Title")

        ColCount = theTableAnnotation.ColumnCount
        For i = 0 To ColCount - 1
            ColType = theTableAnnotation.GetColumnType2(i, True)
            ColTypeString = CType(ColType, String)
            ColTitle = theTableAnnotation.GetColumnTitle2(i, True)
            iString = CType(i, String)
            Debug.Print(iString + "     " + ColTypeString + "    " + ColTitle)
        Next i
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
