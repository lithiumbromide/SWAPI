---
title: "Insert Cut List Item Property Note Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Cut_List_Item_Property_Note_Example_CSharp.htm"
---

# Insert Cut List Item Property Note Example (C#)

This example shows how to insert a note containing all of the cut list item properties into the selected flat pattern drawing view of a sheet metal part.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\api\2012-sm.slddrw.
 //
 // Postconditions:
 // 1. Inserts a note with all of the cut list item properties in Drawing View1.
 // 2. Examine the graphics area.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace InsertCutListPropertyNote_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         SelectionMgr SelMgr;
         View aView;
         bool boolstatus;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             boolstatus = Part.Extension.SelectByID2("Drawing View1",  "DRAWINGVIEW", 0, 0, 0,  false, 0,  null, 0);
             SelMgr = (SelectionMgr)Part.SelectionManager;
             aView = (View)SelMgr.GetSelectedObject6(1, -1);
             aView.InsertCutListPropertyNote(0.11, 0.17, 0.0);
         }

         public SldWorks swApp;

     }
 }
```
