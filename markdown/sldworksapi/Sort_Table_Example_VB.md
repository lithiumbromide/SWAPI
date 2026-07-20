---
title: "Sort Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Sort_Table_Example_VB.htm"
---

# Sort Table Example (VBA)

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
 Dim swApp As SldWorks.SldWorks
 Dim swModDoc As SldWorks.IModelDoc2
 Dim swTable As SldWorks.ITableAnnotation

Option Explicit
Public Sub Main()
     Set swApp = Application.SldWorks
     GetSelTable
     SortSelTable
 End Sub
Public Sub GetSelTable()
     Set swModDoc = swApp.ActiveDoc
     Dim swSM As ISelectionMgr
     Set swSM = swModDoc.SelectionManager
     Set swTable = swSM.GetSelectedObject6(1, -1)
     swModDoc.ClearSelection2 (True)
 End Sub
Public Sub SortSelTable()
    Dim tableType As swTableAnnotationType_e
     tableType = swTable.Type
     Dim status As Boolean
     Select Case tableType
         Case swTableAnnotationType_e.swTableAnnotation_General
             status = SortGeneralTable()
             End
         Case swTableAnnotationType_e.swTableAnnotation_HoleChart
             status = SortHoleChartTable()
             End
         Case swTableAnnotationType_e.swTableAnnotation_WeldmentCutList
             status = SortWeldmentCutlistTable()
             End
         Case swTableAnnotationType_e.swTableAnnotation_BillOfMaterials
             status = SortBOMTable()
             End
         Case Else
             Debug.Print ("Unspecified table type selected.")
             End
     End Select
End Sub
Public Function SortGeneralTable() As Boolean
     Debug.Print ("Table type selected: swTableAnnotation_General")
     Dim swSpecTable As IGeneralTableAnnotation
     Set swSpecTable = swTable
     Dim status As Boolean
     status = swSpecTable.Sort(0, False) 'sort descending
End Function

 Public Function SortHoleChartTable() As Boolean
     Debug.Print ("Table type selected: swTableAnnotation_HoleChart")
     Dim swSpecTable As IHoleTableAnnotation
     Set swSpecTable = swTable
     Dim status As Boolean
     status = swSpecTable.Sort(0, True) 'sort ascending
 End Function
Public Function SortWeldmentCutlistTable() As Boolean
     Debug.Print ("Table type selected: swTableAnnotation_WeldmentCutList")
     Dim swSpecTable As IWeldmentCutListAnnotation
     Set swSpecTable = swTable
     Dim status As Boolean
     status = swSpecTable.Sort(2, False) 'sort descending
 End Function
Public Function SortBOMTable() As Boolean
     Debug.Print ("Table type selected: swTableAnnotation_BillOfMaterials")
     Dim swSpecTable As IBomTableAnnotation
     Set swSpecTable = swTable
     Dim swSortData As BomTableSortData
     Dim sortSaved As Boolean

    Set swSortData = swSpecTable.GetBomTableSortData
    ' Specify the sort order indexes for three columns in the table
     ' Specify the direction of sort for the three sort order indexes
     swSortData.ColumnIndex(0) = 1  ' primary sort on column 1
     swSortData.Ascending(0) = True ' sort ascending
     swSortData.ColumnIndex(1) = 3  ' secondary sort on column 3
     swSortData.Ascending(1) = True ' sort ascending
     swSortData.ColumnIndex(2) = -1 ' no tertiary sort

     ' Specify the literal sort method
     swSortData.SortMethod = swBomTableSortMethod_Literal
    Dim pos1 As Integer
     pos1 = swSortData.ColumnIndex(0)
     Debug.Print ("Column for primary sort is " & pos1) ' should be 1
     Dim pos2 As Integer
     pos2 = swSortData.ColumnIndex(1)
     Debug.Print ("Column for secondary sort is " & pos2) ' should be 3
     Dim pos3 As Integer
     pos3 = swSortData.ColumnIndex(2)
     Debug.Print ("Column for tertiary sort is " & pos3) ' should be -1

    Dim listGrpArray(1) As Integer
     Dim bWantGrp As Boolean
     bWantGrp = True
    If bWantGrp Then
         ' Sort rows into part and user-defined categories

         listGrpArray(0) = swBomTableSortItemGroup_Parts
         listGrpArray(1) = swBomTableSortItemGroup_Other
     End If

    swSortData.ItemGroups = listGrpArray

    ' After sorting, do not re-number the items
     swSortData.DoNotChangeItemNumber = True

    ' Save sorting scheme to the BOM table in the drawing
     sortSaved = swSortData.SaveCurrentSortParameters

    Dim status As Boolean
     status = swSpecTable.Sort(swSortData)
     Debug.Print ("BOM table sorted: " & status)

    ' Insert a row
     swTable.InsertRow 2, 2

    ' Apply sorting scheme saved in the BOM table
     status = swSpecTable.ApplySavedSortScheme(swSortData)
     Debug.Print ("BOM sorting scheme applied: " & status)
End Function
```
