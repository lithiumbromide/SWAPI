---
title: "Sort Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Sort_Table_Example_CSharp.htm"
---

# Sort Table Example (C#)

This example shows how to sort bill of materials, hole, general, and weldment cut list tables.

```vb
//---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a drawing of an assembly with multiple components
 //    and one of these tables:
 //    * General
 //    * Hole chart
 //    * Weldment cut list
 //    * Bill of materials parts-only table that contains
 //      four columns: ITEM NO., PART NUMBER, DESCRIPTION, and QTY.
 // 2. Click the move-table icon in the upper-left corner
 //    of the table to open the table's PropertyManager page.
 // 3. If the table is a BOM table, then verify that
 //    Follow assembly order in Item Numbers is not selected.
 // 4. Open the Immediate window.
 //
 // Postconditions:
 // 1. Sorts:
 //    * BOM table as follows:
 //      * Primary sort is on column one (PART NUMBER).
 //      * Secondary sort is on column three (QTY.).
 //      * There is no tertiary sort.
 //      * All column sorts are literal ascending.
 //      * Rows are sorted into categories in the following order:
 //        1. Parts
 //        2. User-defined
 //      * Inserts a row in the table.
 //      * Attempts to sort the table again by applying the
 //        saved sorting scheme.
 //    * General table in descending order on the first column.
 //    * Hole table in ascending order on the TAG column.
 //    * Weldment cut list table in descending order on the third
 //      column.
 // 2. Inspect the Immediate window.
 //--------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace Macro1.csproj
 {
     public partial class SolidWorksMacro
     {
         IModelDoc2 swModDoc = null;
         ITableAnnotation swTable = null;

         public void Main()
         {
             GetSelTable();
             SortSelTable();
         }

         public void GetSelTable()
         {
             swModDoc = (IModelDoc2)swApp.ActiveDoc;
             ISelectionMgr swSM = null;
             swSM = (ISelectionMgr)swModDoc.SelectionManager;
             swTable = (ITableAnnotation)swSM.GetSelectedObject6(1, -1);
             swModDoc.ClearSelection2(true);
         }

         public void SortSelTable()
         {
             if (swTable != null)
             {
                 swTableAnnotationType_e tableType = (swTableAnnotationType_e)swTable.Type;
                 bool status = false;
                 switch (tableType)
                 {
                     case swTableAnnotationType_e.swTableAnnotation_General:
                         status = SortGeneralTable();
                         break;
                     case swTableAnnotationType_e.swTableAnnotation_HoleChart:
                         status = SortHoleChartTable();
                         break;
                     case swTableAnnotationType_e.swTableAnnotation_WeldmentCutList:
                         status = SortWeldmentCutlistTable();
                         break;
                     case swTableAnnotationType_e.swTableAnnotation_BillOfMaterials:
                         status = SortBOMTable();
                         break;
                     default:
                         Debug.Print("Unspecified table type selected.");
                         break;
                 }
             }
         }

         public bool SortGeneralTable()
         {
             Debug.Print("Table type selected : swTableAnnotation_General");
             IGeneralTableAnnotation swSpecTable = (IGeneralTableAnnotation)swTable;
             bool status =  swSpecTable.Sort(0, false);//sort descending
             return status;
         }

         public bool SortHoleChartTable()
         {
             Debug.Print("Table type selected : swTableAnnotation_HoleChart");
             IHoleTableAnnotation swSpecTable = (IHoleTableAnnotation)swTable;
             bool status = swSpecTable.Sort(0, true );//sort ascending
             return status;
         }

         public bool SortWeldmentCutlistTable()
         {
             Debug.Print("Table type selected : swTableAnnotation_WeldmentCutList");
             IWeldmentCutListAnnotation swSpecTable = (IWeldmentCutListAnnotation)swTable;
             bool status = swSpecTable.Sort(2, false);//sort descending
             return status;
         }

         public bool SortBOMTable()
         {
             Debug.Print("Table type selected : swTableAnnotation_BillOfMaterials");
             IBomTableAnnotation swSpecTable = (IBomTableAnnotation)swTable;
             BomTableSortData swSortData = swSpecTable.GetBomTableSortData();
```

```vb
            bool sortSaved =  false;
```

```vb
             // Specify the sort order indexes for three columns in the table
             // Specify the direction of sort for the three sort order indexes
             swSortData.set_ColumnIndex(0, 1); // primary sort on column 1
             swSortData.set_Ascending(0,  true);  // sort ascending
             swSortData.set_ColumnIndex(1, 3); // secondary sort on column 3
             swSortData.set_Ascending(1,  true);  // sort ascending
             swSortData.set_ColumnIndex(2, -1); // no tertiary sort

             // Specify the literal sort method
             swSortData.SortMethod = (int)swBomTableSortMethod_e.swBomTableSortMethod_Literal;

             int pos1 = swSortData.get_ColumnIndex(0);
             Debug.Print("Column for primary sort is " + pos1);  // should be 1
             int pos2 = swSortData.get_ColumnIndex(1);
             Debug.Print("Column for secondary sort is " + pos2);  // should be 3
             int pos3 = swSortData.get_ColumnIndex(2);
             Debug.Print("Column for tertiary sort is " + pos3);  // should be -1

             int[] listGrpArray = null;
             object grpArray = null;
             grpArray = listGrpArray;
             bool bWantGrp = true;

             if(bWantGrp)
             {
                 // Sort rows into part and user-defined categories
                 listGrpArray =  new  int[2];

                 listGrpArray[0] = (int)swBomTableSortItemGroup_e.swBomTableSortItemGroup_Parts;
                 listGrpArray[1] = (int)swBomTableSortItemGroup_e.swBomTableSortItemGroup_Other;
                 grpArray = listGrpArray;
             }
             swSortData.ItemGroups = grpArray;

             // After sorting, do not re-number the items
             swSortData.DoNotChangeItemNumber = true;
```

```vb
            // Save the sort settings to the BOM Table in the drawing
             sortSaved = swSortData.SaveCurrentSortParameters;

             bool status = false;
             status = swSpecTable.Sort(swSortData);
             Debug.Print("BOM table sorted? " + status);

             // Insert a row
             swTable.InsertRow(2, 2);

             // Apply the sort settings saved in the BOM table
             swSpecTable.ApplySavedSortScheme(swSortData);
             Debug.Print("BOM sorting scheme applied? " + status);
```

```vb
             return status;
         }

         public SldWorks swApp;
     }
 }
```
