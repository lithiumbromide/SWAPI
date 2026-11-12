---
title: "Get Version of Display Dimension (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_SOLIDWORKS_Version_of_Display_Dimension_Example_CSharp.htm"
---

# Get Version of Display Dimension (C#)

This example shows how to find out if a display dimension in a drawing was created in SOLIDWORKS 2011 or later.

```vb
 //------------------------------------------------
 // Preconditions:
 // 1. Open a drawing document in which a display
 //    dimension exists.
 // 2. Open the Immediate window.
 // 3. Select the display dimension.
 //
 // Postconditions: Examine the Immediate window
 // to see if the selected display dimension
 // was created in SOLIDWORKS 2011 or later.
 //-------------------------------------------------
 using System;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Diagnostics;

 namespace GetSupportGenericTextDisplayDimensionCSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             DisplayDimension swDispDim =  default(DisplayDimension);
             object swSelObj = null;
             int selCount = 0;
             int selType = 0;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             selCount = swSelMgr.GetSelectedObjectCount2(-1);
             if (selCount < 1)
             {
                 Debug.Print("Select a display dimension and rerun the macro.");
                 return;
             }

             selType = swSelMgr.GetSelectedObjectType3(1, 0);
             swSelObj = (object)swSelMgr.GetSelectedObject6(1, 0);
             switch (selType)
             {
                 case (int)swSelectType_e.swSelDIMENSIONS:
                     swDispDim = (DisplayDimension)swSelObj;
                     Debug.Print("Was display dimension created in SOLIDWORKS 2011 or later? " + swDispDim.GetSupportsGenericText());
                     break;
             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
