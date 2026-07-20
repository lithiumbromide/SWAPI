---
title: "Expand, Collapse, and Dissolve Subassembly in a BOM Table Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Dissolve_Subassembly_in_a_BOM_Table_Example_CSharp.htm"
---

# Expand, Collapse, and Dissolve Subassembly in a BOM Table Example (C#)

This example shows how to expand, collapse, dissolve, and restore a subassembly in a BOM table.

```vb
 //-----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\assemblyvisualize\food_processor.sldasm.
 // 2. Select File > Make Drawing from Assembly.
 // 3. Click OK.
 // 4. Drag one or more views onto the drawing.
 // 5. Ensure that the specified template exists.
 //
 // Postconditions:
 // 1. Inserts an indented BOM table in the drawing.
  // 2. Collapses the blade shaft subassembly. Press F5 to continue.
  // 3. Expands the blade shaft subassembly. Press F5 to continue.
  // 4. Dissolves the blade shaft subassembly. Press F5 to restore the blade
 //    shaft subassembly.
 //
 // NOTE: Because this document is used by a SOLIDWORKS
 // online tutorial, do not save any changes when
 // closing it.
 //-----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace DissolveBOMItem_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         ModelDocExtension swModelDocExt;
         DrawingDoc swDrawing;
         View swView;
         bool boolstatus;
         BomTableAnnotation swBOMAnnotation;
         int AnchorType;
         int BomType;
         string Configuration;

         string TableTemplate;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             swDrawing = (DrawingDoc)Part;
             swModelDocExt = Part.Extension;
             boolstatus = swDrawing.ActivateView("Drawing View1");
             swView = (View)swDrawing.ActiveDrawingView;

             AnchorType = (int)swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft;
             BomType = (int)swBomType_e.swBomType_Indented;
             TableTemplate = "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\bom-standard.sldbomtbt";
             Configuration = "";
             swBOMAnnotation = swView.InsertBomTable6(false, 0.4, 0.3, AnchorType, BomType, Configuration, TableTemplate,  false, (int)swNumberingType_e.swNumberingType_Detailed, true, true, true);

             //Collapse blade shaft subassembly
             swBOMAnnotation.Collapse(1, 8);
             System.Diagnostics.Debugger.Break();

             //Expand blade shaft subassembly
             swBOMAnnotation.Expand(1, 8);
             System.Diagnostics.Debugger.Break();

             //Dissolve blade shaft subassembly
             boolstatus = swBOMAnnotation.Dissolve(8);
              System.Diagnostics.Debugger.Break();

              //Restore blade shaft subassembly
             boolstatus = swBOMAnnotation.RestoreRestructuredComponents(0);

         }

         public SldWorks swApp;

     }

 }
```
