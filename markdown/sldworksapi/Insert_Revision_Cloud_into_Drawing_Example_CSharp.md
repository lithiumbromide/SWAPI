---
title: "Insert Revision Cloud into a Drawing Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Revision_Cloud_into_Drawing_Example_CSharp.htm"
---

# Insert Revision Cloud into a Drawing Example (C#)

This example shows how to insert revision clouds into a drawing and access revision cloud data.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\api\resetsketchvisibility.slddrw.
 //
 // Postconditions:
 // 1. Inserts an elliptical revision cloud in the drawing.
 // 2. Examine the Immediate window.
 //
 // NOTE: Because the drawing is used elsewhere, do not save changes.
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
 namespace InsertRevisionCloud_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         DrawingDoc Part;
         RevisionCloud RevCloud;
         Annotation RevCloudAnno;

         bool boolstatus;

         public void Main()
         {
             Part = (DrawingDoc)swApp.ActiveDoc;
             boolstatus = Part.ActivateView("Drawing View1");

             // Create a revision cloud with an elliptical shape
             RevCloud = (RevisionCloud)Part.InsertRevisionCloud(1);
             if ((RevCloud != null))
             {
                 RevCloudAnno = (Annotation)RevCloud.GetAnnotation();
                 if ((RevCloudAnno != null))
                 {
                     // Position the center of the elliptical revision cloud
                     boolstatus = RevCloudAnno.SetPosition(0.270847371964905, 0.553263328912467, 0);
                     RevCloud.ArcRadius = 0.00508;
                     // Create a path point on the corner of an ellipse-inscribed rectangle
                     boolstatus = RevCloud.SetPathPointAtIndex(-1, 0.378419710263212, 0.511051398694144, 0);
                     // Close the revision cloud path
                     boolstatus = RevCloud.Finalize();
                 }
             }

         }

         public SldWorks swApp;

     }
 }
```
