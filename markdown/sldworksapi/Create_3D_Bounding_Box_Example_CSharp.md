---
title: "Create 3D Bounding Box for Cut List Item Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_3D_Bounding_Box_Example_CSharp.htm"
---

# Create 3D Bounding Box for Cut List Item Example (C#)

This example shows how to create a 3D bounding box for a cut list item in a weldment part.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open: public_documents\samples\tutorial\api\weldment_box3.sldprt.
 // 2. Right-click the Cut list folder and select Update.
 //
 // Postconditions:
 // 1. Expand the Cut-List-Item5 folder.
 // 2. Select Bounding-Box_Cut-List-Item5.
 // 3. Observe the sketch of the bounding box in the graphics area.
 //
 // NOTE: Because the model is used elsewhere, do not save changes when closing it.
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
 namespace CreateBoundingBox_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         ModelDocExtension modDocExt;

         bool boolstatus;
         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;
             modDocExt = Part.Extension;

             boolstatus = modDocExt.SelectByID2("Cut-List-Item5", "SUBWELDFOLDER", 0, 0, 0, false, 0, null, 0);
             modDocExt.Create3DBoundingBox();
         }

         public SldWorks swApp;

     }
 }
```
