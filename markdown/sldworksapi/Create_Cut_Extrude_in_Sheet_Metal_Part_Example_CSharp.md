---
title: "Create Cut Extrude in Sheet Metal Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Cut_Extrude_in_Sheet_Metal_Part_Example_CSharp.htm"
---

# Create Cut Extrude in Sheet Metal Part Example (C#)

This example shows how to create an optimized, normal, cut extrude in a sheet metal part.

```
//-------------------------------------------------------------
// Preconditions:
// 1. Verify that the sheet metal part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the sheet metal part.
// 2. Selects a face.
// 3. Sketches a circle on the selected face.
// 4. Creates Cut-Extrude2, which is an optimized, normal, cut
//    extrude.
// 5. Examine the FeatureManager design tree, graphics area, and
//    Immediate window.
//
// NOTE: Because the part document is used elsewhere, do not save
// changes.
//--------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
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
            ExtrudeFeatureData2 swExtrudeFeatureData = default(ExtrudeFeatureData2);
            bool status = false;
            int errors = 0;
            int warnings = 0;

            swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\2012-sm.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Select a face
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByRay(-0.0287275955400048, 0.0301558252805876, 0.00509460972091347, 0.369531106281609, -0.495005022745071, -0.786394804756136, 0.00115698538052806, 2, false, 0,
            0);

            //Sketch a circle
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchSegment = (SketchSegment)swSketchManager.CreateCircle(0.0, 0.0, 0.0, 0.004122, -0.003029, 0.0);

            //Create an optimized, normal, cut extrude
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureManager.FeatureCut4(true, false, false, 1, 0, 0.01, 0.01, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true,
            true, true, false, 0, 0, false, true);

            swModel.ClearSelection2(true);
```

```
 	    swExtrudeFeatureData = (ExtrudeFeatureData2)swFeature.GetDefinition();
	    Debug.Print("Normal cut? " + swExtrudeFeatureData.NormalCut);
	    Debug.Print("Geometry optimized? " + swExtrudeFeatureData.OptimizeGeometry);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
