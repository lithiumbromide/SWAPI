---
title: "Insert Bend Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Bend_Table_Example_CSharp.htm"
---

# Insert Bend Table Example (C#)

This example shows how to insert a bend table in a drawing of a flattened sheet metal part.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a drawing that contains a flat pattern view
 //    of a flattened sheet metal part.
 // 2. Replace install_dir with your SOLIDWORKS installation directory.
 // 3. Select the flat pattern view (Drawing View1)
 //    in the FeatureManager design tree.
 // 4. Ensure the namespace matches the name of your C# project.
 //
 // Postconditions:
 // 1. A bend table is inserted for the selected view.
 // 2. Inspect the Immediate Window.
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
 namespace InsertBendTable_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         View swView;
         BendTableAnnotation myBendTableAnnot;
         BendTable myBendTableFeat;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;

             swView = ((SelectionMgr)(Part.SelectionManager)).GetSelectedObjectsDrawingView2(1, -1);
             myBendTableAnnot = swView.InsertBendTable(false, 0.3018189506239, 0.4876053587373,(int)  swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft, "A", "install_dir\\lang\\english\\bendtable-standard.sldbndtbt");

             myBendTableFeat = myBendTableAnnot.BendTable;
             Debug.Print(myBendTableFeat.GetFeature().Name);
             Debug.Print("Starting tag: " + myBendTableFeat.StartingValue);
             Debug.Print("swBendTableTagStyle_e option: " + myBendTableFeat.TagStyle);
             Debug.Print("Number of bend table annotations: " + myBendTableFeat.GetTableAnnotationCount());

             Part.ClearSelection2(true);

         }

         public SldWorks swApp;
     }

 }
```
