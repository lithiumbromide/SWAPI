---
title: "Select Plane Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Plane_Example_CSharp.htm"
---

# Select Plane Example (C#)

This example shows how to select the default Right Plane.

```vb
 //---------------------------------------------------------
 // Preconditions: Open a new part document.
 //
 // Postconditions:
 // 1. Selects the Right Plane.
 // 2. Examine the graphics area.
 //---------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 namespace GetPlanes_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             // Select Right Plane (1-based index)
             const long ReqPlane = 3;

             ModelDoc2 swModel = default(ModelDoc2);
             Feature swFeat = default(Feature);
             long PlaneCount = 0;
             bool bRet = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swFeat = (Feature)swModel.FirstFeature();

             while ((swFeat != null))
             {
                 if ("RefPlane" == swFeat.GetTypeName())
                 {
                     PlaneCount = PlaneCount + 1;

                     if (ReqPlane == PlaneCount)
                     {
                         bRet = swFeat.Select2(false, 0);
                         break;
                     }
                 }

                 swFeat = (Feature)swFeat.GetNextFeature();
             }

         }

         public SldWorks swApp;

     }
 }
```
