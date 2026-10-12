---
title: "Insert Thin Cut Extrude Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Thin_Cut_Extrude_Example_CSharp.htm"
---

# Insert Thin Cut Extrude Example (C#)

This example shows how to insert a thin cut extrude feature.

```
//------------------------------------------------------
// Preconditions: Verify that the specified part exists.
//
// Postconditions:
// 1. Opens the part.
// 2. Inserts a thin cut extrude feature in the part.
// 3. Examine the FeatureManager design tree and
//    graphics area.
//
// NOTE: Because this part document is used elsewhere,
// do not save changes.
//-----------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;

namespace FeatureCutThin2FeatureManagerCSharp.csproj
{
    partial
 class SolidWorksMacro
    {
        public
 void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchManager swSketchManager = default(SketchManager);
            SketchSegment swSketchSegment = default(SketchSegment);
            FeatureManager swFeatureManager = default(FeatureManager);
            Feature swFeature = default(Feature);
            bool boolstatus = false;
            int errorstatus = 0;
            int warnings = 0;
```

```vb
             // Open part
             swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\water.sldprt", 1, 0, "",
 ref errorstatus, ref warnings);
             swModel = (ModelDoc2)swApp.ActiveDoc;

             // Select face on which to sketch a circle
             swModelDocExt = (ModelDocExtension)swModel.Extension;
             boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.0001655362220845, -0.0477671348753, 0.072, false, 0, null, 0)

             swModel.ShowNamedView2("*Normal To", (int)swStandardViews_e.swBackView);
             swModel.ClearSelection2(true);

             // Sketch a circle
             swSketchManager = (SketchManager)swModel.SketchManager;
             swSketchSegment = (SketchSegment)swSketchManager.CreateCircle(0.0, 0.0, 0.0, 0.030255, -0.042492, 0.0);
             swModel.ClearSelection2(true);

             // Create the thin cut extrude
             boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
             swFeatureManager = (FeatureManager)swModel.FeatureManager;
             swFeature = (Feature)swFeatureManager.FeatureCutThin2(true, false, false, (int)swEndConditions_e.swEndCondBlind,
                 (int)swEndConditions_e.swEndCondBlind, 0.01, 0.01, false, false, false,
                 false, 0.01745329251994, 0.01745329251994, false, false, false, false, 0.01, 0.01, 0.01,
                 0, 0, false, 0.005, true, true, (int)swStartConditions_e.swStartSketchPlane, 0, false);
             swModel.ShowNamedView2("*Isometric", (int)swStandardViews_e.swIsometricView);

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;

     }
 }
```
