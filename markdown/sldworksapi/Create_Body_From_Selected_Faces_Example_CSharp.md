---
title: "Create Body From Selected Faces Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Body_From_Selected_Faces_Example_CSharp.htm"
---

# Create Body From Selected Faces Example (C#)

This example shows how to:

- use SOLIDWORKS geometry and topology methods to construct a temporary body from selected faces.
- create a solid body feature from the temporary body and a new part containing the solid body feature.

```
//------------------------------------------
// Preconditions:
// 1. Verify that the specified part document
//    template exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens a new part document and creates an
//    extruded thin feature.
// 2. Selects connecting faces on the extruded thin feature.
// 3. Knits the faces into a solid, creates a
//    a new part, and inserts the solid as an imported
//    solid body feature.
// 4. Examine the Immediate window, graphics area,
//    FeatureManager design tree, and document name
//    in the SOLIDWORKS menu bar.
//-------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace CreateBodyFromFacesCSharp.csproj
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
            PartDoc swPart = default(PartDoc);
            PartDoc swNewPart = default(PartDoc);
            Modeler swModeler = default(Modeler);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Face2[] swSelFace = null;
            object vFaceList = null;
            Body2 swBody = default(Body2);
            Body2 swNewBody = default(Body2);
            Feature swFeat = default(Feature);
            int nSelCount = 0;
            int i = 0;
            bool bRet = false;

            //Create part and select connecting faces
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2014\\templates\\Part.prtdot", 0, 0, 0);
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchManager.InsertSketch(true);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(0.0, 0.0, 0.0, -0.062359, 0.0, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(-0.062359, 0.0, 0.0, -0.020485, 0.066264, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(-0.020485, 0.066264, 0.0, 0.0, 0.0, 0.0);
            swModel.ClearSelection2(true);
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureManager.FeatureExtrusionThin2(true, false, false, 0, 0, 0.03048, 0.00254, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, 0.00254, 0.00254,
            0.00254, 0, 0, false, 0.005, true, true, 0, 0, false);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swSelMgr.EnableContourSelection = false;
            swModel.ClearSelection2(true);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            bRet = swModelDocExt.SelectByID2("", "FACE", -0.0484137409629284, 0, 0.018103012393226, true, 0, null, 0);
            bRet = swModelDocExt.SelectByID2("", "FACE", -0.0396839112014504, 0.035882458904041, 0.0207108765403632, true, 0, null, 0);
            bRet = swModelDocExt.SelectByID2("", "FACE", -0.0175462018075336, 0.0567577015655729, 0.021527257415471, true, 0, null, 0);

            //Get the selected faces
            swModeler = (Modeler)swApp.GetModeler();
            nSelCount = swSelMgr.GetSelectedObjectCount();
            Array.Resize(ref swSelFace, nSelCount);
            for (i = 1; i <= nSelCount; i++)
            {
                swSelFace[i - 1] = (Face2)swSelMgr.GetSelectedObject6(i, -1);
            }
            vFaceList = (object)swSelFace;

            //Create solid body feature using selected faces
            swPart = (PartDoc)swModel;
            swBody = (Body2)swPart.CreateNewBody();
            swNewBody = (Body2)swBody.CreateBodyFromFaces(nSelCount, (vFaceList));
            if (swNewBody == null)
            {
                Debug.Print("Failed to create solid body from selected faces.");
                return;
            }
            else
            {
                Debug.Print("Solid body and new part can be created from selected faces.");
            }
            //Open new part and force creation of solid body feature
            swNewPart = (PartDoc)swApp.NewPart();
            swFeat = (Feature)swNewPart.CreateFeatureFromBody3(swNewBody, false, (int)swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck + (int)swCreateFeatureBodyOpts_e.swCreateFeatureBodySimplify);
            if ((swFeat != null))
            {
                Debug.Print("New part with imported solid body created.");
            }
            else
            {
                Debug.Print("New part with imported solid body not created.");
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
