---
title: "Update Plane Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Update_Plane_Example_CSharp.htm"
---

# Update Plane Example (C#)

This example shows how to update a reference plane so that it is parallel to the screen.

```
//---------------------------------------------------------------------------
// Preconditions: Verify that the specified part template exists.
//
// Postconditions:
// 1. Creates Boss-Extrude1 and Plane1.
// 2. Rotates Boss-Extrude1.
// 3. Examine Plane1 in the graphics area.
// 4. Press F5.
// 5. Updates Plane1 so that it is parallel to the screen.
// 6. Examine Plane1 in the graphics area.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

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
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            RefPlane swRefPlane = default(RefPlane);
            ModelView swModelView = default(ModelView);
            RefPlaneFeatureData swRefPlaneFeatureData = default(RefPlaneFeatureData);
            bool status = false;

            //Create Boss-Extrude1 and Plane1
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2016\\templates\\part.prtdot", 0, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchManager.InsertSketch(true);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(-0.049503, 0.030205, 0.0, -0.049503, 0.0, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(-0.049503, 0.0, 0.0, 0.0, 0.0, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(0.0, 0.0, 0.0, 0.0, 0.019088, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(0.0, 0.019088, 0.0, -0.03503, 0.037127, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(-0.03503, 0.037127, 0.0, -0.049503, 0.030205, 0.0);
            swSketchManager.InsertSketch(true);
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureManager.FeatureExtrusion3(true, false, false, 0, 0, 0.04, 0.01, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true,
            0, 0, false);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swSelectionMgr.EnableContourSelection = false;
            status = swModelDocExt.SelectByID2("", "VERTEX", -0.0350298017733792, 0.0371273946939409, 0.04, true, 0, null, 0);
            swRefPlane = (RefPlane)swFeatureManager.InsertRefPlane(4096, 0, 0, 0, 0, 0);
            swModel.ClearSelection2(true);

            //Rotate Boss-Extrude1
            status = swModelDocExt.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0, 0.00828812132228465);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0, 0.00828812132228465);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.00576690959137988, 0);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.00576690959137988, 0.0165762426445693);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.00576690959137988, 0.00828812132228465);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0, 0.0165762426445693);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.0115338191827598, 0.0248643639668539);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.0115338191827598, 0.0331524852891386);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.00576690959137988, 0.0248643639668539);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.00576690959137988, 0.0165762426445693);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0, 0.0248643639668539);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.00576690959137988, 0.0165762426445693);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.00576690959137988, 0.0165762426445693);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.00576690959137988, 0.0414406066114233);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.00576690959137988, 0.0331524852891386);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.00576690959137988, 0.0331524852891386);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.0115338191827598, 0.0580168492559925);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.00576690959137988, 0.0414406066114233);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.00576690959137988, 0.0580168492559925);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0, 0.0663049705782772);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.00576690959137988, 0.0663049705782772);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0.00576690959137988, 0.1077455771897);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0, 0.0994574558674158);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0, 0.0745930919005618);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0, 0.0911693345451311);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0, 0.0828812132228465);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0, 0.0745930919005618);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0, 0.0580168492559925);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0, 0.0248643639668539);
            swModelView = (ModelView)swModel.ActiveView;
            swModelView.RotateAboutCenter(0, 0.00828812132228465);
            swModel.ClearSelection2(true);

            System.Diagnostics.Debugger.Break();
            //Examine Plane1
            //Press F5 to continue

            //Update Plane1 so that it is parallel to the screen
            status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swRefPlaneFeatureData = (RefPlaneFeatureData)swFeature.GetDefinition();
            swRefPlaneFeatureData.UpdatePlane = true;
            swFeature.ModifyDefinition(swRefPlaneFeatureData, swModel, null);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
