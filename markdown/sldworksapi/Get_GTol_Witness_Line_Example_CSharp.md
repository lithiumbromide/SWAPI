---
title: "Get GTol Witness Line Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_GTol_Witness_Line_Example_CSharp.htm"
---

# Get GTol Witness Line Example (C#)

This example shows how to get the witness line of a geometric tolerance frame.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open:
 //    public_documents\samples\tutorial\api\GTolWitnessLine.slddrw
 // 2. Rename the namespace to match the name of your C# project.
 // 3. Select the geometric tolerance frame.
 // 4. Open an Immediate window.
 //
 // Postconditions: Inspect the Immediate window for the
 // witness line start and end point coordinates.
 //
 // NOTE: Because the model is used elsewhere,
 // do not save changes when closing it.
 //---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace GTolWitnessLine_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         ModelDocExtension swModelDocExt;
         SelectionMgr swSelMgr;
         Gtol selGtol;
         int i;

         object coords;
         Double[] dbls;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = swModel.Extension;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             selGtol = (Gtol)swSelMgr.GetSelectedObject6(1, 0);

              selGtol.SetPosition(0.433, 0.432, 0.0);
             swModel.ForceRebuild3(false);

             coords = selGtol.GetWitnessLine();
             dbls = (Double[])coords;

             for (i = 0; i < dbls.Length; i++)
             {
                 Debug.Print(dbls[i].ToString());
             }
         }

         public SldWorks swApp;

     }
 }
```
