---
title: "Insert Column in BOM Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Column_in_BOM_Table_Example_CSharp.htm"
---

# Insert Column in BOM Table Example (C#)

This example shows how to insert a part number column in a BOM table.

```
//---------------------------------------------------
// Preconditions:
// 1. Open a drawing that contains a BOM table.
// 2. Right-click the BOM table, select Select,
//    and select Table.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Inserts a part number column at the end of the
//    the BOM table.
// 2. Examine the BOM table and Immediate window.
//---------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Windows.Forms;
```

```vb
namespace InsertColumn2TableAnnotationCSharp.csproj
{
partial class SolidWorksMacro
{

    public void Main()
    {
        ModelDoc2 swModel = default(ModelDoc2);
        bool boolstatus = false;
        SelectionMgr SelMgr = default(SelectionMgr);
        TableAnnotation theTableAnnotation = default(TableAnnotation);
        int SelObjType = 0;
        int TableAnnotationType = 0;

        swModel = (ModelDoc2)swApp.ActiveDoc;
        SelMgr = (SelectionMgr)swModel.SelectionManager;
        SelObjType = SelMgr.GetSelectedObjectType3(1, -1);
        if (SelObjType != (int)swSelectType_e.swSelANNOTATIONTABLES)
        {
            MessageBox.Show("Select a BOM table in the drawing before running this example.");
            return;
        }
        theTableAnnotation = (TableAnnotation)SelMgr.GetSelectedObject6(1, -1);
        TableAnnotationType = theTableAnnotation.Type;
        if (TableAnnotationType != (int)swTableAnnotationType_e.swTableAnnotation_BillOfMaterials)
        {
            MessageBox.Show("Select a BOM table in the drawing before running this example.");
            return;
        }
        Debug.Print("Table before inserting a column...");
        // Display table before inserting a column
        DisplayTableColumnProps(theTableAnnotation);

        // Insert new column
        boolstatus = theTableAnnotation.InsertColumn2((int)swTableItemInsertPosition_e.swTableItemInsertPosition_Last, 0, "New Column", (int)swInsertTableColumnWidthStyle_e.swInsertColumn_DefaultWidth);
        boolstatus = theTableAnnotation.SetColumnType2(theTableAnnotation.ColumnCount - 1, (int)swTableColumnTypes_e.swBomTableColumnType_PartNumber, true);

        Debug.Print(" ");

        Debug.Print("Table after inserting a column...");
        // Display table after inserting a column
        DisplayTableColumnProps(theTableAnnotation);
    }

    public void DisplayTableColumnProps(TableAnnotation theTableAnnotation)
    {
        int ColCount = 0;
        int i = 0;
        string iString = null;
        int ColType = 0;
        string ColTypeString = null;
        string ColTitle = null;
        Debug.Print("Col# " + "Type  " + "Title");
        ColCount = theTableAnnotation.ColumnCount;
        for (i = 0; i <= ColCount - 1; i++)
        {
            ColType = theTableAnnotation.GetColumnType2(i, true);
            ColTypeString = System.Convert.ToString(ColType);
            ColTitle = theTableAnnotation.GetColumnTitle2(i, true);
            iString = System.Convert.ToString(i);
            Debug.Print(iString + "    " + ColTypeString + "  " + ColTitle);
        }
    }
    /// <summary>
    /// The SldWorks swApp variable is pre-assigned for you.
    /// </summary>
    public SldWorks swApp;
}
}
```
