---
title: "Sort Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Sort_Table_Example_VBNET.htm"
---

# Sort Table Example (VB.NET)

This example shows how to sort bill of materials, hole, general, and weldment cut list tables.

```vb
'---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing of an assembly with multiple components
 '    and one of these tables:
 '    * General
 '    * Hole chart
 '    * Weldment cut list
 '    * Bill of materials parts-only table that contains
 '      four columns: ITEM NO., PART NUMBER, DESCRIPTION, and QTY.
 ' 2. Click the move-table icon in the upper-left corner
 '    of the table to open the table's PropertyManager page.
 ' 3. If the table is a BOM table, then verify that
 '    Follow assembly order in Item Numbers is not selected.
 ' 4. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Sorts:
 '    * BOM table as follows:
 '      * Primary sort is on column one (PART NUMBER).
 '      * Secondary sort is on column three (QTY.).
 '      * There is no tertiary sort.
 '      * All column sorts are literal ascending.
 '      * Rows are sorted into categories in the following order:
 '        1. Parts
 '        2. User-defined
 '      * Inserts a row in the table.
 '      * Attempts to sort the table again by applying the
 '        saved sorting scheme.
 '    * General table in descending order on the first column.
 '    * Hole table in ascending order on the TAG column.
 '    * Weldment cut list table in descending order on the third
 '      column.
 ' 2. Inspect the Immediate window.
 '--------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Diagnostics

 Partial Public Class SolidWorksMacro
     Private swModDoc As IModelDoc2 = Nothing
     Private swTable As ITableAnnotation = Nothing

     Public Sub Main()
         GetSelTable()
         SortSelTable()
     End Sub

     Public Sub GetSelTable()
         swModDoc = DirectCast(swApp.ActiveDoc, IModelDoc2)
         Dim swSM As ISelectionMgr = Nothing
         swSM =  DirectCast(swModDoc.SelectionManager, ISelectionMgr)
         swTable = DirectCast(swSM.GetSelectedObject6(1, -1), ITableAnnotation)
         swModDoc.ClearSelection2(True)
     End Sub

     Public Sub SortSelTable()
         If swTable IsNot Nothing Then
             Dim tableType As swTableAnnotationType_e = DirectCast(swTable.Type, swTableAnnotationType_e)
             Dim status As Boolean = False
             Select Case tableType
                 Case swTableAnnotationType_e.swTableAnnotation_General
                     status = SortGeneralTable()
                     Exit Select
                 Case swTableAnnotationType_e.swTableAnnotation_HoleChart
                     status = SortHoleChartTable()
                     Exit Select
                 Case swTableAnnotationType_e.swTableAnnotation_WeldmentCutList
                     status = SortWeldmentCutlistTable()
                     Exit Select
                 Case swTableAnnotationType_e.swTableAnnotation_BillOfMaterials
                     status = SortBOMTable()
                     Exit Select
                 Case Else
                     Debug.Print("Unspecified table type selected.")
                     Exit Select
             End Select
         End If
     End Sub

     Public Function SortGeneralTable() As Boolean
         Debug.Print("Table type selected : swTableAnnotation_General")
         Dim swSpecTable As IGeneralTableAnnotation = DirectCast(swTable, IGeneralTableAnnotation)
         Dim status As Boolean = swSpecTable.Sort(0, False) 'sort descending

         Return status
     End Function

     Public Function SortHoleChartTable() As Boolean
         Debug.Print("Table type selected : swTableAnnotation_HoleChart")
         Dim swSpecTable As IHoleTableAnnotation = DirectCast(swTable, IHoleTableAnnotation)
         Dim status As Boolean = swSpecTable.Sort(0, True) 'sort ascending

         Return status
     End Function

     Public Function SortWeldmentCutlistTable() As Boolean
         Debug.Print("Table type selected : swTableAnnotation_WeldmentCutList")
         Dim swSpecTable As IWeldmentCutListAnnotation = DirectCast(swTable, IWeldmentCutListAnnotation)
         Dim status As Boolean = swSpecTable.Sort(2, False) 'sort descending

         Return status
     End Function

     Public Function SortBOMTable() As Boolean
         Debug.Print("Table type selected : swTableAnnotation_BillOfMaterials")
         Dim swSpecTable As IBomTableAnnotation = DirectCast(swTable, IBomTableAnnotation)
         Dim swSortData As BomTableSortData = swSpecTable.GetBomTableSortData()
```

```vb
        Dim sortSaved  As  Boolean
```

```vb
         ' Specify the sort order indexes for three columns in the table
         ' Specify the direction of sort for the three sort order indexes
         swSortData.ColumnIndex(0) = 1  ' primary sort on column 1
         swSortData.Ascending(0) =  True ' sort ascending

         swSortData.ColumnIndex(1) = 3  ' secondary sort on column 3
         swSortData.Ascending(1) =  True ' sort ascending

         swSortData.ColumnIndex(2) = -1 ' no tertiary sort

         ' Specify the literal sort method
         swSortData.SortMethod = swBomTableSortMethod_e.swBomTableSortMethod_Literal

         Dim pos1 As Integer = swSortData.ColumnIndex(0)
         Debug.Print("Column for primary sort is " & pos1)  ' should be 1

         Dim pos2 As Integer = swSortData.ColumnIndex(1)
         Debug.Print("Column for secondary sort is " & pos2)  ' should be 3

         Dim pos3 As Integer = swSortData.ColumnIndex(2)
         Debug.Print("Column for tertiary sort is " & pos3)  ' should be -1

         Dim listGrpArray As Integer() = Nothing
         Dim grpArray As Object = Nothing
         grpArray = listGrpArray
         Dim bWantGrp As Boolean = True

         If bWantGrp Then
             ' Sort rows into part and user-defined categories
             listGrpArray =  New  Integer(1) {}

             listGrpArray(0) = CInt(swBomTableSortItemGroup_e.swBomTableSortItemGroup_Parts)
             listGrpArray(1) = CInt(swBomTableSortItemGroup_e.swBomTableSortItemGroup_Other)
             grpArray = listGrpArray
         End If
         swSortData.ItemGroups = grpArray

         ' After sorting, do not re-number the items
         swSortData.DoNotChangeItemNumber = True
```

```vb
        ' Save the sort settings to the BOM table in the drawing
         sortSaved = swSortData.SaveCurrentSortParameters

         Dim status As Boolean
         status = swSpecTable.Sort(swSortData)
         Debug.Print("BOM table sorted? " & status)

         ' Insert a row
         swTable.InsertRow(2, 2)

         ' Apply the sort settings saved in the BOM table
         swSpecTable.ApplySavedSortScheme(swSortData)
         Debug.Print("BOM sorting scheme applied? " & status)
```

```vb
         Return status
     End Function

     Public swApp As SldWorks
 End  Class
```
