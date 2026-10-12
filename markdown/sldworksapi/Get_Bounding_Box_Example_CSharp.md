---
title: "Get Bounding Box Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Bounding_Box_Example_CSharp.htm"
---

# Get Bounding Box Example (C#)

This example shows how to get the bounding boxes for the selected feature and face. This example also shows how to draw 3D sketches depicting the bounding boxes.

```
//----------------------------------------------
// Preconditions:
// 1. Verify that the part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Selects the Sweep1 feature.
// 2. Creates a 3D sketch of the bounding box of
//    the selected Sweep1 feature.
// 3. Selects the top face.
// 4. Creates a 3D sketch of the bounding box of the
//    selected face.
// 5. Examine the graphics area and the Immediate
//    window.
//
// NOTE: Because this part is used elsewhere,
// do not save changes.
//----------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GetBoxFeatureFaceCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Feature swFeat = default(Feature);
            Face2 swFace = default(Face2);
            object BoxFeatureArray = null;
            double[] BoxFeatureDblArray = new double[7];
            object BoxFaceArray = null;
            double[] BoxFaceDblArray = new double[7];
            SketchManager swSketchMgr = default(SketchManager);
            SketchPoint[] swSketchPt = new SketchPoint[9];
            SketchSegment[] swSketchSeg = new SketchSegment[13];
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;
            int i = 0;

            // Open part document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\cstick.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            // Select feature
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            status = swModelDocExt.SelectByID2("Sweep1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);

            // Get selected feature's bounding box
            Debug.Print("Feature:");
            status = swFeat.GetBox(ref BoxFeatureArray);
            Debug.Assert(status);

            BoxFeatureDblArray = (double[])BoxFeatureArray;

            Debug.Print("  Pt1 = " + "(" + BoxFeatureDblArray[0] * 1000.0 + ", " + BoxFeatureDblArray[1] * 1000.0 + ", " + BoxFeatureDblArray[2] * 1000.0 + ") mm");
            Debug.Print("  Pt2 = " + "(" + BoxFeatureDblArray[3] * 1000.0 + ", " + BoxFeatureDblArray[4] * 1000.0 + ", " + BoxFeatureDblArray[5] * 1000.0 + ") mm");
            swModel.Insert3DSketch2(true);
            swModel.SetAddToDB(true);
            swModel.SetDisplayWhenAdded(false);

            swSketchMgr = (SketchManager)swModel.SketchManager;
```

```
            // Draw points at each corner of bounding box
            swSketchPt[0] = (SketchPoint)swSketchMgr.CreatePoint(BoxFeatureDblArray[3], BoxFeatureDblArray[1], BoxFeatureDblArray[5]);
            swSketchPt[1] = (SketchPoint)swSketchMgr.CreatePoint(BoxFeatureDblArray[0], BoxFeatureDblArray[1], BoxFeatureDblArray[5]);
            swSketchPt[2] = (SketchPoint)swSketchMgr.CreatePoint(BoxFeatureDblArray[0], BoxFeatureDblArray[1], BoxFeatureDblArray[2]);
            swSketchPt[3] = (SketchPoint)swSketchMgr.CreatePoint(BoxFeatureDblArray[3], BoxFeatureDblArray[1], BoxFeatureDblArray[2]);
            swSketchPt[4] = (SketchPoint)swSketchMgr.CreatePoint(BoxFeatureDblArray[3], BoxFeatureDblArray[4], BoxFeatureDblArray[5]);
            swSketchPt[5] = (SketchPoint)swSketchMgr.CreatePoint(BoxFeatureDblArray[0], BoxFeatureDblArray[4], BoxFeatureDblArray[5]);
            swSketchPt[6] = (SketchPoint)swSketchMgr.CreatePoint(BoxFeatureDblArray[0], BoxFeatureDblArray[4], BoxFeatureDblArray[2]);
            swSketchPt[7] = (SketchPoint)swSketchMgr.CreatePoint(BoxFeatureDblArray[3], BoxFeatureDblArray[4], BoxFeatureDblArray[2]);
```

```
           // Now draw bounding box
           swSketchSeg[0] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[0].X, swSketchPt[0].Y, swSketchPt[0].Z, swSketchPt[1].X, swSketchPt[1].Y, swSketchPt[1].Z);
           swSketchSeg[1] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[1].X, swSketchPt[1].Y, swSketchPt[1].Z, swSketchPt[2].X, swSketchPt[2].Y, swSketchPt[2].Z);
           swSketchSeg[2] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[2].X, swSketchPt[2].Y, swSketchPt[2].Z, swSketchPt[3].X, swSketchPt[3].Y, swSketchPt[3].Z);
           swSketchSeg[3] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[3].X, swSketchPt[3].Y, swSketchPt[3].Z, swSketchPt[0].X, swSketchPt[0].Y, swSketchPt[0].Z);
           swSketchSeg[4] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[0].X, swSketchPt[0].Y, swSketchPt[0].Z, swSketchPt[4].X, swSketchPt[4].Y, swSketchPt[4].Z);
           swSketchSeg[5] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[1].X, swSketchPt[1].Y, swSketchPt[1].Z, swSketchPt[5].X, swSketchPt[5].Y, swSketchPt[5].Z);
           swSketchSeg[6] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[2].X, swSketchPt[2].Y, swSketchPt[2].Z, swSketchPt[6].X, swSketchPt[6].Y, swSketchPt[6].Z);
           swSketchSeg[7] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[3].X, swSketchPt[3].Y, swSketchPt[3].Z, swSketchPt[7].X, swSketchPt[7].Y, swSketchPt[7].Z);
           swSketchSeg[8] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[4].X, swSketchPt[4].Y, swSketchPt[4].Z, swSketchPt[5].X, swSketchPt[5].Y, swSketchPt[5].Z);
           swSketchSeg[9] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[5].X, swSketchPt[5].Y, swSketchPt[5].Z, swSketchPt[6].X, swSketchPt[6].Y, swSketchPt[6].Z);
           swSketchSeg[10] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[6].X, swSketchPt[6].Y, swSketchPt[6].Z, swSketchPt[7].X, swSketchPt[7].Y, swSketchPt[7].Z);
           swSketchSeg[11] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[7].X, swSketchPt[7].Y, swSketchPt[7].Z, swSketchPt[4].X, swSketchPt[4].Y, swSketchPt[4].Z);

            swModel.SetDisplayWhenAdded(true);
            swModel.SetAddToDB(false);
            swModel.Insert3DSketch2(true);

            swModel.ClearSelection2(true);

            // Get selected face's bounding box
            status = swModelDocExt.SelectByID2("", "FACE", -7.62173696102764E-05, 0.219999999999857, 0.00945327855254163, false, 0, null, 0);
            swFace = (Face2)swSelMgr.GetSelectedObject6(1, -1);

            // Get selected face's bounding box
            Debug.Print("Face =");
            BoxFaceArray = (object)swFace.GetBox();

            BoxFaceDblArray = (double[])BoxFaceArray;

            Debug.Print("  Pt1 = " + "(" + BoxFaceDblArray[0] * 1000.0 + ", " + BoxFaceDblArray[1] * 1000.0 + ", " + BoxFaceDblArray[2] * 1000.0 + ") mm");
            Debug.Print("  Pt2 = " + "(" + BoxFaceDblArray[3] * 1000.0 + ", " + BoxFaceDblArray[4] * 1000.0 + ", " + BoxFaceDblArray[5] * 1000.0 + ") mm");

            swModel.Insert3DSketch2(true);
            swModel.SetAddToDB(true);
            swModel.SetDisplayWhenAdded(false);

            // Draw points at each corner of bounding box
            swSketchPt[0] = (SketchPoint)swSketchMgr.CreatePoint(BoxFaceDblArray[3], BoxFaceDblArray[1], BoxFaceDblArray[5]);
            swSketchPt[1] = (SketchPoint)swSketchMgr.CreatePoint(BoxFaceDblArray[0], BoxFaceDblArray[1], BoxFaceDblArray[5]);
            swSketchPt[2] = (SketchPoint)swSketchMgr.CreatePoint(BoxFaceDblArray[0], BoxFaceDblArray[1], BoxFaceDblArray[2]);
            swSketchPt[3] = (SketchPoint)swSketchMgr.CreatePoint(BoxFaceDblArray[3], BoxFaceDblArray[1], BoxFaceDblArray[2]);
            swSketchPt[4] = (SketchPoint)swSketchMgr.CreatePoint(BoxFaceDblArray[3], BoxFaceDblArray[4], BoxFaceDblArray[5]);
            swSketchPt[5] = (SketchPoint)swSketchMgr.CreatePoint(BoxFaceDblArray[0], BoxFaceDblArray[4], BoxFaceDblArray[5]);
            swSketchPt[6] = (SketchPoint)swSketchMgr.CreatePoint(BoxFaceDblArray[0], BoxFaceDblArray[4], BoxFaceDblArray[2]);
            swSketchPt[7] = (SketchPoint)swSketchMgr.CreatePoint(BoxFaceDblArray[3], BoxFaceDblArray[4], BoxFaceDblArray[2]);

            // Now draw bounding box
           swSketchSeg[0] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[0].X, swSketchPt[0].Y, swSketchPt[0].Z, swSketchPt[1].X, swSketchPt[1].Y, swSketchPt[1].Z);
           swSketchSeg[1] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[1].X, swSketchPt[1].Y, swSketchPt[1].Z, swSketchPt[2].X, swSketchPt[2].Y, swSketchPt[2].Z);
           swSketchSeg[2] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[2].X, swSketchPt[2].Y, swSketchPt[2].Z, swSketchPt[3].X, swSketchPt[3].Y, swSketchPt[3].Z);
           swSketchSeg[3] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[3].X, swSketchPt[3].Y, swSketchPt[3].Z, swSketchPt[0].X, swSketchPt[0].Y, swSketchPt[0].Z);
           swSketchSeg[4] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[0].X, swSketchPt[0].Y, swSketchPt[0].Z, swSketchPt[4].X, swSketchPt[4].Y, swSketchPt[4].Z);
           swSketchSeg[5] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[1].X, swSketchPt[1].Y, swSketchPt[1].Z, swSketchPt[5].X, swSketchPt[5].Y, swSketchPt[5].Z);
           swSketchSeg[6] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[2].X, swSketchPt[2].Y, swSketchPt[2].Z, swSketchPt[6].X, swSketchPt[6].Y, swSketchPt[6].Z);
           swSketchSeg[7] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[3].X, swSketchPt[3].Y, swSketchPt[3].Z, swSketchPt[7].X, swSketchPt[7].Y, swSketchPt[7].Z);
           swSketchSeg[8] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[4].X, swSketchPt[4].Y, swSketchPt[4].Z, swSketchPt[5].X, swSketchPt[5].Y, swSketchPt[5].Z);
           swSketchSeg[9] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[5].X, swSketchPt[5].Y, swSketchPt[5].Z, swSketchPt[6].X, swSketchPt[6].Y, swSketchPt[6].Z);
           swSketchSeg[10] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[6].X, swSketchPt[6].Y, swSketchPt[6].Z, swSketchPt[7].X, swSketchPt[7].Y, swSketchPt[7].Z);
           swSketchSeg[11] = (SketchSegment)swSketchMgr.CreateLine(swSketchPt[7].X, swSketchPt[7].Y, swSketchPt[7].Z, swSketchPt[4].X, swSketchPt[4].Y, swSketchPt[4].Z);

            swModel.SetDisplayWhenAdded(true);
            swModel.SetAddToDB(false);
            swModel.Insert3DSketch2(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
