---
title: "Create Hidden Undo Object Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Multiple_Undo_Command_Example_CSharp.htm"
---

# Create Hidden Undo Object Example (C#)

This example shows how to create an Undo object that is hidden in the SOLIDWORKS Undo list.

```
//-----------------------------------------------------------------------------
// Preconditions: Ensure the part template path exists.
//
// Postconditions:
// 1. A part with four sketches is created.
// 2. One sketch is extruded.
// 3. A hidden Undo object, API Undo, is created with two extrusions.
// 4. One sketch is cut extruded.
// 5. The following items appear in the SOLIDWORKS Undo list in this order:
//    a. Extruded Cut
//    b. (API Undo, hidden from view)
//    c. Base
//
// NOTE: If you select Base in the SOLIDWORKS Undo list:
// 1. The base boss created before the recording of the hidden API Undo object is undone.
// 2. The two bosses created during the recording of the hidden API Undo object are undone.
// 3. The cut extrusion created after the recording of the hidden API Undo object is undone.
//----------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace HiddenObjectUndoCSharp.csproj
{
    partial class SolidWorksMacro
    {
        ModelDoc2 swModel;
        ModelView swModelView;
        ModelDocExtension swModelDocExt;
        SketchManager swSketchManager;
        SketchSegment swSketchSegment;
        Feature swFeature;
        FeatureManager swFeatureManager;
        SelectionMgr swSelectionManager;
        bool status;
        int docErrors;

        public void Main()
        {

            swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2013\\templates\\Part.prtdot", (int)swDwgPaperSizes_e.swDwgPaperAsize, 0, 0);
            swApp.ActivateDoc3("Part2.sldprt", false, (int)swRebuildOnActivation_e.swDontRebuildActiveDoc, ref docErrors);
            swModel = (ModelDoc2)swApp.ActiveDoc;

            swModelDocExt = (ModelDocExtension)swModel.Extension;

            swModelView = (ModelView)swModel.ActiveView;
            swModelView.FrameState = (int)swWindowState_e.swWindowMaximized;

            swSketchManager = (SketchManager)swModel.SketchManager;

            swSketchManager.InsertSketch(true);
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", -0.0692248508634211, 0.0392379182115397, 0.00987134779060705, false, 0, null, 0);
            swModel.ClearSelection2(true);

            object vSkLines = null;
            vSkLines = swSketchManager.CreateCornerRectangle(-0.0891172006155176, 0.0314069429482, 0, -0.0425302352423542, 0.00601966406507166, 0);
            swModel.ClearSelection2(true);

            swSketchManager.InsertSketch(true);
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);

            swSketchSegment = (SketchSegment)swSketchManager.CreateCircle(0.009029, 0.03036, 0.0, 0.021854, 0.019629, 0.0);
            swModel.ClearSelection2(true);

            swSketchManager.InsertSketch(true);
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);

            swModel.ClearSelection2(true);
            swSketchSegment = (SketchSegment)swSketchManager.CreateEllipse(0.0306284568434307, 0.00619756829649987, 0, 0.0309763470298606, 0.00997419305453208, 0, 0.0286971648691861, 0.00637547252792807, 0);
            swModel.ClearSelection2(true);

            swSketchManager.InsertSketch(true);
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);

            swSketchSegment = (SketchSegment)swSketchManager.CreateEllipse(0.0240620641310443, 0.0131240684851264, 0, 0.0771974468433887, 0.0706711158113391, 0, 0.000886560440335415, 0.0345228945826079, 0);
            swModel.ClearSelection2(true);
            swSketchManager.InsertSketch(true);

            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 4, null, 0);

            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureManager.FeatureExtrusion2(true, false, false, 0, 0, 0.00254, 0.00254, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true,
            0, 0, false);
            swSelectionManager = (SelectionMgr)swModel.SelectionManager;
            swSelectionManager.EnableContourSelection = false;

            // Start recording the SOLIDWORKS Undo object
            swModelDocExt.StartRecordingUndoObject();
            status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, false, 4, null, 0);
            swFeature = (Feature)swFeatureManager.FeatureExtrusion2(true, false, false, 0, 0, 0.00254, 0.00254, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true,
            0, 0, false);
            swSelectionManager.EnableContourSelection = false;
            status = swModelDocExt.SelectByID2("Sketch4", "SKETCH", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swFeatureManager.FeatureExtrusion2(true, false, false, 0, 0, 0.00254, 0.00254, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true,
            0, 0, false);
            swSelectionManager.EnableContourSelection = false;

            // End recording the SOLIDWORKS Undo object with name "API Undo" and hide it in the Undo list
            swModelDocExt.FinishRecordingUndoObject2("API Undo", true);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, false, 4, null, 0);
            swFeature = (Feature)swFeatureManager.FeatureCut3(true, false, true, 0, 0, 0.00254, 0.00254, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, false, true, true,
            true, true, false, 0, 0, false);
            swSelectionManager.EnableContourSelection = false;

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;
    }
}
```
