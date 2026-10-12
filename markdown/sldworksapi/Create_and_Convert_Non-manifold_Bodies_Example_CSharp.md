---
title: "Create and Convert Non-manifold Bodies Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Convert_Non-manifold_Bodies_Example_CSharp.htm"
---

# Create and Convert Non-manifold Bodies Example (C#)

This example shows how to create non-manifold bodies, which by default are not allowed in SOLIDWORKS Design, and then convert the non-manifold bodies to manifold bodies.

```
//-----------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document
//    template exists.
// 2. Add a reference to Microsoft.VisualBasic (right-click
//    the project name in the Project Explorer and click
//    Add Reference > Microsoft.VisualBasic on the .NET tab >
//    OK.
//
// Postconditions:
// 1. Set a breakpoint at this line:
//    swModeler.GeneralTopology = false;
// 2. Step through the macro by pressing F10
//    while observing the graphics area.
// 3. Creates and tessellates non-manifold bodies
//    and coverts them to manifold bodies.
//----------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using Microsoft.VisualBasic;

namespace GeneralTopologyCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        ModelDoc2 swModel = default(ModelDoc2);

        public void Main()
        {
            Modeler swModeler = default(Modeler);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchManager swSketchManager = default(SketchManager);
            Feature swFeature = default(Feature);
            SelectionMgr swSelMgr = default(SelectionMgr);
            SketchSegment swSketchSegment = default(SketchSegment);
            FeatureManager swFeatureManager = default(FeatureManager);
            Tessellation tess = default(Tessellation);
            Body2 tool = default(Body2);
            Body2 tgt1 = default(Body2);
            Body2 tgt0 = default(Body2);
            object[] sketchLines = null;
            object[] resVar = null;
            object[] resvar2 = null;
            object[] manifVar = null;
            int[] vFacetId = null;
            int[] vFinId = null;
            int[] vVertexId = null;
            double[] vVertex1 = null;
            double[] vVertex2 = null;
            Face2 f = default(Face2);
            bool boolstatus = false;
            int i = 0;
            int j = 0;
            int[] clr = new int[2];

            swModeler = (Modeler)swApp.GetModeler();

            //SOLIDWORKS requires this option to be
            //false, so make sure it is set to false
            swModeler.GeneralTopology = false;

            //Create part having a tool and target bodies
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
            swModelDocExt = swModel.Extension;
            boolstatus = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
            boolstatus = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, true);
            swSketchManager = swModel.SketchManager;
            sketchLines = (object[])swSketchManager.CreateCornerRectangle(0, 0, 0, 0.13786334229408, 0.069192775961991, 0);
            boolstatus = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, false, 4, null, 0);
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swFeature = (Feature)swFeatureManager.FeatureExtrusion2(true, false, false, (int)swEndConditions_e.swEndCondBlind, 0, 0.01524, 0.00254, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true,
            (int)swStartConditions_e.swStartSketchPlane, 0, false);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swSelMgr.EnableContourSelection = false;
            swModel.ClearSelection2(true);
            swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
            swSketchManager.InsertSketch(true);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(0.0, 0.034596, 0.0, 0.137863, 0.034596, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(0.068932, 0.069193, 0.0, 0.068932, 0.0, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(0.0, 0.0, 0.0, 0.137863, 0.0, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(0.137863, 0.0, 0.0, 0.137863, 0.069193, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(0.137863, 0.069193, 0.0, 0.0, 0.069193, 0.0);
            swSketchSegment = (SketchSegment)swSketchManager.CreateLine(0.0, 0.069193, 0.0, 0.0, 0.0, 0.0);
            boolstatus = swModelDocExt.SelectByID2("Sketch2", "SKETCHREGION", 0.0295651111315002, 0.0562122082077101, 0.00761999999999985, true, 4, null, 0);
            boolstatus = swModelDocExt.SelectByID2("Sketch2", "SKETCHREGION", 0.0812426680973543, 0.0181340083381333, 0.00762000000000011, true, 4, null, 0);
            swModel.ClearSelection2(true);
            boolstatus = swModelDocExt.SelectByID2("Line9", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0.0295651111315002, 0.0562122082077101, 0.00761999999999985, true, 4, null, 0);
            swSelMgr.EnableContourSelection = true;
            boolstatus = swModelDocExt.SelectByID2("Sketch2", "SKETCHREGION", 0.0295651111315002, 0.0562122082077101, 0.00761999999999985, true, 4, null, 0);
            boolstatus = swModelDocExt.SelectByID2("Sketch2", "SKETCHREGION", 0.0812426680973543, 0.0181340083381333, 0.00762000000000011, true, 4, null, 0);
            swFeature = (Feature)swFeatureManager.FeatureExtrusion2(true, false, false, (int)swEndConditions_e.swEndCondBlind, 0, 0.01524, 0.01524, false, false, false,
            false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, false, true, true,
            (int)swStartConditions_e.swStartSketchPlane, 0, false);
            swSelMgr.EnableContourSelection = false;

            //Hide the boss-extrude and sketch features
            boolstatus = swModelDocExt.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swFeatureManager.HideBodies();
            boolstatus = swModelDocExt.SelectByID2("Boss-Extrude2", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swFeatureManager.HideBodies();

            //Make selections of tool and target bodies;
            //Boss-Extrude1 is larger cube, whereas Boss-Extrude2[1]
            //and Boss-Extrude2[2] are 1/4 the size of Boss-Extrude1,
            //so (Boss-Extrude - Boss-Extrude2[1]) - Boss-Extrude2[2])
            //results in non-manifold bodies; under normal conditions,
            //i.e., when non-manifold bodies are not allowed,
            //such an operation results in two bodies;
            //when creation of non-manifold bodies is allowed,
            //then one general body is the result
            boolstatus = swModelDocExt.SelectByID2("Boss-Extrude1", "SOLIDBODY", 0, 0, 0, false, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("Boss-Extrude2[1]", "SOLIDBODY", 0, 0, 0, true, 0, null, 0);
            boolstatus = swModelDocExt.SelectByID2("Boss-Extrude2[2]", "SOLIDBODY", 0, 0, 0, true, 0, null, 0);
            tool = (Body2)swSelMgr.GetSelectedObject6(1, -1);
            tgt0 = (Body2)swSelMgr.GetSelectedObject6(2, -1);
            tgt1 = (Body2)swSelMgr.GetSelectedObject6(3, -1);

            //Create temporary bodies
            tool = (Body2)tool.Copy();
            tgt0 = (Body2)tgt0.Copy();
            tgt1 = (Body2)tgt1.Copy();

            swModel.ClearSelection2(true);

            //First cut operation : Boss-Extrude1 - Boss-Extrude2[1]
            int errCode = 0;
            resVar = (object[])tool.Operations2((int)swBodyOperationType_e.SWBODYCUT, tgt0, out errCode);

            //SOLIDWORKS requires this option
            //to be false; thus, switch it back to false
            //as soon as your intended operations complete
            swModeler.GeneralTopology = true;

            //Second cut operation: (Boss-Extrude1 - Boss-Extrude2[1])- Boss-Extrude2[2])
            Body2 swBody = default(Body2);
            swBody = (Body2)resVar[0];
            resvar2 = (object[])swBody.Operations2((int)swBodyOperationType_e.SWBODYCUT, tgt1, out errCode);

            //Reset the option back to false
            swModeler.GeneralTopology = false;
            clr[0] = Information.RGB(0, 0, 255);
            clr[1] = Information.RGB(255, 0, 0);
            for (i = 0; i < resvar2.Length; i++)
            {
                DisplayBody(resvar2[i], clr[i]);
            }

            //Hide the displayed bodies
            for (i = 0; i < resvar2.Length; i++)
            {
                HideBody(resvar2[i]);
            }

            //Try tessellation

            //Add sketch for this face
            swModel.Insert3DSketch2(false);

            //Add lines directly to sketch to increase performance
            swModel.SetAddToDB(true);
            Body2 swBody2 = default(Body2);
            swBody2 = (Body2)resvar2[0];
            tess = (Tessellation)swBody2.GetTessellation(null);
            tess.NeedFaceFacetMap = true;
            tess.MatchType = (int)swTesselationMatchType_e.swTesselationMatchFacetGeometry;
            boolstatus = tess.Tessellate();
            Face2 swFace = default(Face2);
            f = (Face2)swBody2.GetFirstFace();
            while ((f != null))
            {
                vFacetId = (int[])tess.GetFaceFacets(f);
                for (i = 0; i < vFacetId.Length; i++)
                {
                    vFinId = (int[])tess.GetFacetFins(vFacetId[i]);
                    for (j = 0; j <= 2; j++)
                    {
                        //Should always be three fins per facet
                        vVertexId = (int[])tess.GetFinVertices(vFinId[j]);
                        //Should always be two vertices per fin
                        vVertex1 = (double[])tess.GetVertexPoint(vVertexId[0]);
                        vVertex2 = (double[])tess.GetVertexPoint(vVertexId[1]);
                        swModel.CreateLine2(vVertex1[0], vVertex1[1], vVertex1[2], vVertex2[0], vVertex2[1], vVertex2[2]);
                    }
                }
                f = (Face2)f.GetNextFace();
            }

            //Convert non-manifold bodies to manifold bodies
            manifVar = (object[])swModeler.MakeManifoldBodies(swBody2);
            for (i = 0; i < manifVar.Length; i++)
            {
                DisplayBody(manifVar[i], Information.RGB(0, 255, 0));
            }

            swModel.ClearSelection2(true);

            for (i = 0; i < manifVar.Length; i++)
            {
                HideBody(manifVar[i]);
            }

        }

        public void DisplayBody(object b, int col)
        {
            Body2 body = null;
            body = (Body2)b;
            PartDoc swPart = default(PartDoc);
            swPart = (PartDoc)swModel;
            body.Display2(swPart, col, (int)swTempBodySelectOptions_e.swTempBodySelectable);
        }
        public void HideBody(object b)
        {
            Body2 body = null;
            body = (Body2)b;
            body.Hide(swModel);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
