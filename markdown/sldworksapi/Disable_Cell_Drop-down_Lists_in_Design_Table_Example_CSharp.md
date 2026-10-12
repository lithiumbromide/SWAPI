---
title: "Disable Cell Drop-down Lists in Design Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Disable_Cell_Drop-down_Lists_in_Design_Table_Example_CSharp.htm"
---

# Disable Cell Drop-down Lists in Design Table Example (C#)

This example shows how to disable drop-down lists for cells in a design table.

```
//----------------------------------------------------------
// Preconditions:
// 1. Open a part that has a design table.
// 2. In the SolidWorks Visual Studio for Applications Tools
//    IDE, click Project > Add Reference > .NET >
//    Microsoft.Office.Interop.Excel > OK.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Gets and edits the design table.
// 2. Disables drop-down lists for cells in the design table.
// 3. Updates and closes the design table.
// 4. Examine the Immediate window.
//
// NOTE: You can also expand Tables on the ConfigurationManager
// tab, right-click Design Table, and click Edit Feature to
// verify that Enable cell drop-down lists (may be slower)
// is not selected.
//------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            DesignTable swDesignTable = default(DesignTable);
            bool status = false;
            Microsoft.Office.Interop.Excel.Worksheet myWorksheet = default(Microsoft.Office.Interop.Excel.Worksheet);

            swModel = (ModelDoc2)swApp.ActiveDoc;

            //Get and edit design table
            swDesignTable = (DesignTable)swModel.GetDesignTable();
            myWorksheet = (Microsoft.Office.Interop.Excel.Worksheet)swDesignTable.EditTable2(false);
```

```
            //Allow changes to characteristics of design table
            swDesignTable.EditFeature();

            //Disable cell drop-down lists
            status = swDesignTable.EnableCellDropdownLists;
            Debug.Print("Current \"Enable cell drop-down lists (may be slower)\" setting: " + status);
            swDesignTable.EnableCellDropdownLists = false;
            status = swDesignTable.EnableCellDropdownLists;
            Debug.Print("Modified \"Enable cell drop-down lists (may be slower)\" setting: " + status);

            status = swDesignTable.UpdateFeature();
            Debug.Print("Design table feature updated? " + status);

            //Update and close design table
            swDesignTable.UpdateTable((int)swDesignTableUpdateOptions_e.swUpdateDesignTableAll, true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
