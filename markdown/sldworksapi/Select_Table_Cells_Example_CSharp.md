---
title: "Select Table Cells Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Table_Cells_Example_CSharp.htm"
---

# Select Table Cells Example (C#)

This example shows how to interpret the results of selecting table cells in various ways.

```
//-----------------------------------------------------
// Preconditions:
// 1. A drawing with a table, which has multiple rows
//    and columns, is open.
// 2. Open the Immediate window.
// 3. Select a column.
// 4. Run the macro.
//
// Postconditions:
// 1. The range for all of the cells in the column is
//    printed to the Immediate window. Examine
//    the Immediate window.
// 2. Hold down the Ctrl key and click a cell.
// 3. Repeat step 2 to select additional adjacent cells.
// 4. Run the macro again.
// 5. The range for each selected cell is printed to
//    the Immediate window. Examine the Immediate
//    window.
//--------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GetCellRangeITableAnnotationCSharp.csproj
{

    partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            DrawingDoc swDrawing = default(DrawingDoc);
            Annotation swAnnotation = default(Annotation);
            TableAnnotation swTableAnnotation = default(TableAnnotation);
            int firstRow = 0;
            int lastRow = 0;
            int firstColumn = 0;
            int lastColumn = 0;
            int idx = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swDrawing = (DrawingDoc)swModel;

            for (idx = 1; idx <= swSelectionMgr.GetSelectedObjectCount2(-1); idx++)
            {
                swTableAnnotation = (TableAnnotation)swSelectionMgr.GetSelectedObject6(idx, -1);
                swAnnotation = (Annotation)swTableAnnotation.GetAnnotation();

                swTableAnnotation.GetCellRange(ref firstRow, ref lastRow, ref firstColumn, ref lastColumn);

                Debug.Print("First selected cell's row     = " + firstRow);
                Debug.Print("Last selected cell's row      = " + lastRow);
                Debug.Print("First selected cell's column  = " + firstColumn);
                Debug.Print("Last selected cell's column   = " + lastColumn);
                Debug.Print("");

            }

            if ((firstRow == -1))
            {
                Debug.Print("Selected entire table!");
            }

            swModel.ClearSelection2(true);

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
