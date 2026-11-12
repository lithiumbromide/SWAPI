---
title: "Change Tags in Hole Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Tags_in_Hole_Table_Example_CSharp.htm"
---

# Change Tags in Hole Table Example (C#)

This example shows how to change the tags in a hole table.

```
//-----------------------------------------------------
// Preconditions:
// 1. Open a drawing document that contains
//    a hole table named Hole Table1 that has
//    has four columns (TAG, X LOC, Y LOC, and SIZE)
//    and at least five rows.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Disables updating hole table tags.
// 2. Changes tag in column 1, row 2 to Test1.
// 3. Changes tag in column 1, row 5 to Test2.
// 4. Enables updating of hole table and model view
//    and shows new tags.
// 5. Examine the Immediate window and hole table.
//---------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace RenameHoleTableTag_CSharp.csproj
{
    partial
 class SolidWorksMacro
    {
        public
 void Main()
```

```
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            HoleTable swHoleTable = default(HoleTable);

            bool boolstatus = false;
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            boolstatus = swModel.Extension.SelectByID2("Hole Table1", "HOLETABLE",
 0, 0, 0, false, 0, null, 0);
            swHoleTable = (HoleTable)swSelMgr.GetSelectedObject6(1, -1);
            swHoleTable.EnableUpdate = false;

            //Disable
 updating hole table tags
            Debug.Print("Original name of tag in column1, row 2: " + swHoleTable.get_HoleTag(1));

            swHoleTable.set_HoleTag(1, "Test1");
            Debug.Print("New name of tag in column1, row 2: " + swHoleTable.get_HoleTag(1));
            Debug.Print("");
            Debug.Print("Original name of tag in column1, row 5: " + swHoleTable.get_HoleTag(4));
            swHoleTable.set_HoleTag(4, "Test1");
            //
 Fails because same name is used in row 2
            swHoleTable.set_HoleTag(4, "Test2");
            Debug.Print("New name of tag in column1, row 2: " + swHoleTable.get_HoleTag(4));

            //Enable
 updating hole table tags
            swHoleTable.EnableUpdate = true;
        }
        public SldWorks swApp;
    }
}
```
