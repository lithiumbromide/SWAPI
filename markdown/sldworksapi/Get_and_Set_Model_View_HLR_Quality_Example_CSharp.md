---
title: "Get and Set Model View HLR Quality Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Model_View_HLR_Quality_Example_CSharp.htm"
---

# Get and Set Model View HLR Quality Example (C#)

This example shows how to get and set the hidden-line removal quality of model edges.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open a part or assembly document.
 //
 // Postconditions:
 // 1. Sets the hidden-line removal quality to
 //    swHlrQuality_e.swFastHlr for a fast redraw and lower
 //    image quality of model edges.
 // 2. Examine the Immediate window.
 //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace HLRQuality_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelView swModView = default(ModelView);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModView = (ModelView)swModel.ActiveView;

             // Set HLR quality to a fast redraw and lower image quality of model edges
             swModView.HlrQuality = (int)swHlrQuality_e.swFastHlr;

             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print("  Hidden-line removal quality as defined in swHlrQuality_e = " + swModView.HlrQuality);

         }

         public SldWorks swApp;

     }

 }
```
