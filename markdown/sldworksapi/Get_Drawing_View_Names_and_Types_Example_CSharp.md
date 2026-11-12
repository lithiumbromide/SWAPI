---
title: "Get Drawing View Names and Types Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Drawing_View_Names_and_Types_Example_CSharp.htm"
---

# Get Drawing View Names and Types Example (C#)

This example shows how to get the names and types of all of the drawing views on the current sheet.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a drawing document.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Traverses the views on the current sheet and gets each view's type.
 // 2. Inspect the Immediate window.
 //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace GetNextView_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             DrawingDoc swDraw = default(DrawingDoc);
             Sheet swSheet = default(Sheet);
             View swView = default(View);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swDraw = (DrawingDoc)swModel;
             swSheet = (Sheet)swDraw.GetCurrentSheet();
             swView = (View)swDraw.GetFirstView();

             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print("  " + swSheet.GetName());

             while ((swView != null))
             {
                 Debug.Print("    " + swView.GetName2() + " [" + swView.Type + "]");
                 swView = (View)swView.GetNextView();
             }
         }

         public SldWorks swApp;

     }
 }
```
