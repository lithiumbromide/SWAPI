---
title: "Insert Cut Extrude Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Cut_Extrude_Example_CSharp.htm"
---

# Insert Cut Extrude Example (C#)

This example shows how to insert a cut extrude feature.

```vb
//----------------------------------------------------------
 // Preconditions: Verify that specified part to open exists.
 //
 // Postconditions:
 // 1. Inserts a cut extrude feature is in the model.
 // 2. Examine the graphics area.
 //
 // NOTE: Because the part document is used elsewhere, do not save
 // changes.
 //----------------------------------------------
using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
namespace FeatureCut3FeatureManagerCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModelDocExt = default(ModelDocExtension);
             SketchManager swSketchManager = default(SketchManager);
             SketchSegment swSketchSegment = default(SketchSegment);
             FeatureManager swFeatureManager = default(FeatureManager);
             Feature swFeature = default(Feature);
             bool boolstatus = false;
             int fileerror = 0;
             int filewarning = 0;

             // Open part document
             swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\plate.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref fileerror, ref filewarning);
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Select the face where to sketch a circle
             boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.02031412853728, 0.006977746007294, -0.008053400767039, false, 0, null, 0);
             swSketchManager = (SketchManager)swModel.SketchManager;
             swSketchManager.InsertSketch(true);
             swModel.ClearSelection2(true);

            // Sketch a circle
             swSketchSegment = (SketchSegment)swSketchManager.CreateCircle(0.0, 0.0, 0.0, 0.01708, -0.030458, 0.0);
             boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
             swModel.ClearSelection2(true);

            // Insert a cut-extrude feature using the circle
             swFeatureManager = (FeatureManager)swModel.FeatureManager;
 swFeature = (Feature)swFeatureManager.FeatureCut3(true, false, false, (int)swEndConditions_e.swEndCondThroughAll,
   (int)swEndConditions_e.swEndCondBlind, 0.01, 0.01, false, false, false,
                false, 0.01745329251994, 0.01745329251994, false, false, false, false, false, true, true,
                false, false, false, (int)swStartConditions_e.swStartSketchPlane, 0, false);
         }

        /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;

     }
}
```
