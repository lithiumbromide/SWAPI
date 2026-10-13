---
title: "Get Table Cell Text Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Table_Cell_Text_Example_CSharp.htm"
---

# Get Table Cell Text Example (C#)

This example shows how to get all of the cell text from a BOM table using the SOLIDWORKS Document Manager API.

```vb
// -------------------------------------------------------------------------
// Preconditions:
// 1. Read the SOLIDWORKS Document Manager API Help
//    Getting Started topic and ensure that the
//    required DLLs are registered.
// 2. Open SOLIDWORKS and copy the code below to a C# macro.
// 3. Ensure that the latest SolidWorks.Interop.swdocumentmgr.dll
//    interop assembly is loaded in the project.
//    (Right-click on the project in Project Explorer, click
//    Add Reference,  click the interop assembly in the .NET
//    tab, or browse for the DLL in install_dir\api\redist.)
// 4. In SOLIDWORKS, create a part document with a BOM table.
// 5. Save the part and close it.
// 6. Substitute your license key for your_license_key in the code.
// 7. Substitute the new file name for sFile in the code.
// 8. Uncomment the appropriate swDoc line.
//
// Postconditions: The Immediate Window displays the BOM
// table row and column count and all of the table's cell
// text in row order.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swdocumentmgr;
using System;
using System.Diagnostics;

    partial class SolidWorksMacro
    {
        SwDMClassFactory classfac;
        SwDMApplication tapp;
        SwDMDocument13 swDoc;
        SwDMTable3 swTable;
        SwDmDocumentOpenError e;
        string sFile;
        String[] vTables;
        String[] vTabArr;
        SwDmTableError err;
        int row;
        int col;
        int j;
        public void Main()
        {
            classfac = new SwDMClassFactory();
            tapp = classfac.GetApplication("your_license_key");

            sFile = "C:\\temp\\Part1.SLDPRT";

            //get the SW document file
swDoc = (SwDMDocument13)tapp.GetDocument(sFile, SwDmDocumentType.swDmDocumentPart, false, out e);
            //swDoc = (SwDMDocument13)tapp.GetDocument(sFile, SwDmDocumentType.swDmDocumentAssembly, false, out e)
            //swDoc = (SwDMDocument13)tapp.GetDocument(sFile, SwDmDocumentType.swDmDocumentDrawing, false, out e)

            Debug.Print("Doc Version is " + swDoc.GetVersion());
            Debug.Print("Doc name is " + swDoc.FullName);
            vTables = (String[])swDoc.GetTableNames(SwDmTableType.swDmTableTypeBOM);
            if ((vTables != null))
            {
                swTable = (SwDMTable3)swDoc.GetTable((String)vTables[0]);
                if ((swTable != null))
                {
                    Debug.Print("Table retrieved is " + vTables[0]);
                    vTabArr = (String[])swTable.GetTableCellText(out err, out row, out col);
                    Debug.Print("Row count is " + row);
                    Debug.Print("Column count is " + col);
                    Debug.Print("Table cell text:");
                    for (j = 0; j <= vTabArr.GetUpperBound(0); j++)
                    {
                        Debug.Print(" " + vTabArr[j]);
                    }
                }
            }
            swDoc.CloseDoc();
        }
        public SldWorks swApp;
    }
```
