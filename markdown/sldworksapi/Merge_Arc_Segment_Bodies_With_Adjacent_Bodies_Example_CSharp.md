---
title: "Merge Arc Segment Bodies With Adjacent Bodies Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Merge_Arc_Segment_Bodies_With_Adjacent_Bodies_Example_CSharp.htm"
---

# Merge Arc Segment Bodies With Adjacent Bodies Example (C#)

This example shows how to create structural-member groups with and without merging arc segment bodies with adjacent bodies.

```
//--------------------------------------------------------
// Preconditions:
// 1. Verify that the specified files exist:
//    * part template
//    * weldment profile
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens a new part.
// 2. Creates a sketch of two lines and two tangent arcs.
// 3. Creates a structural-member group using an adjacent line and arc
//    and merges the arc segment's body with the line's body.
// 4. Creates another structural-member group using the other adjacent
//    line and arc and does not merge the arc segment's body with the
//    line's body.
// 5. Examine the Immediate window.
// 6. Expand Cut list(3) in the FeatureManager design tree.
// 7. Point at each PIPE, SCH 40, 12.70 DIA. and examine the
//    graphics area to verify whether that PIPE, SCH 40, 12.70
//    DIA. is merged.
//---------------------------------------------------------

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
            Feature swFeature = default(Feature);
            FeatureManager swFeatureManager = default(FeatureManager);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchManager swSketchMgr = default(SketchManager);
            SketchSegment swSketchSegment = default(SketchSegment);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            StructuralMemberGroup group1 = default(StructuralMemberGroup);
            StructuralMemberGroup group2 = default(StructuralMemberGroup);
            StructuralMemberGroup group = default(StructuralMemberGroup);
            StructuralMemberFeatureData swStructuralMemberFeatureData = default(StructuralMemberFeatureData);
            SketchSegment[] segmentsArray = new SketchSegment[2];
            bool status = false;
            DispatchWrapper[] groups = new DispatchWrapper[1];
            object[] groupArray = new object[1];
            int i = 0;

            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSketchMgr = (SketchManager)swModel.SketchManager;
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;

            //Insert weldment feature
            swFeature = (Feature)swFeatureManager.InsertWeldmentFeature();

            //Create sketch of two lines and two tangent arcs
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.ClearSelection2(true);
            swSketchMgr.InsertSketch(true);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateLine(0.0, 0.0, 0.0, -0.101812, 0.0, 0.0);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateLine(-0.1016, -0.059455, 0.0, 0.0, -0.059455, 0.0);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateTangentArc(0.0, -0.059455, 0.0, 0.0, 0.0, 0.0, 1);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateTangentArc(-0.1016, -0.0, 0.0, -0.1016, -0.059455, 0.0, 1);
            swModel.ClearSelection2(true);
            swSketchMgr.InsertSketch(true);
            swModel.ViewZoomtofit2();
            swModel.ShowNamedView2("*Normal To", -1);
            swModel.ClearSelection2(true);

            //Create structural-member group
            group1 = (StructuralMemberGroup)swFeatureManager.CreateStructuralMemberGroup();
            status = swModelDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.0963105065508915, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Arc1@Sketch1", "EXTSKETCHSEGMENT", 0.0072699684110568, -0.000902652809559659, 0, true, 0, null, 0);
            segmentsArray[0] = (SketchSegment)swSelectionMgr.GetSelectedObject6(1, -1);
            segmentsArray[1] = (SketchSegment)swSelectionMgr.GetSelectedObject6(2, -1);
            group1.Segments = segmentsArray;
            group1.ApplyCornerTreatment = true;
            group1.CornerTreatmentType = 1;
            group1.GapWithinGroup = 0;
            group1.GapForOtherGroups = 0;
            group1.Angle = 0;
            group1.MergeArcSegmentBodies = true;
            groupArray[0] = group1;
            groups[0] = new DispatchWrapper(groupArray[0]);
            swFeature = (Feature)swFeatureManager.InsertStructuralWeldment5("C:\\Program Files\\SolidWorks Corp\\SOLIDWORKS\\lang\\english\\weldment profiles\\ansi inch\\pipe\\0.5 sch 40.sldlfp", (int)swConnectedSegmentsOption_e.swConnectedSegments_SimpleCut, false, (groups), "");
            swModel.ClearSelection2(true);

            //Create structural-member group
            group2 = (StructuralMemberGroup)swFeatureManager.CreateStructuralMemberGroup();
            status = swModelDocExt.SelectByID2("Arc2@Sketch1", "EXTSKETCHSEGMENT", -0.106961319560779, -0.000449372254001996, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", -0.0425304114129424, -0.059455, 0, true, 0, null, 0);
            segmentsArray[0] = (SketchSegment)swSelectionMgr.GetSelectedObject6(1, -1);
            segmentsArray[1] = (SketchSegment)swSelectionMgr.GetSelectedObject6(2, -1);
            group2.Segments = segmentsArray;
            group2.ApplyCornerTreatment = true;
            group2.CornerTreatmentType = 1;
            group2.GapWithinGroup = 0;
            group2.GapForOtherGroups = 0;
            group2.Angle = 0;
            group2.MergeArcSegmentBodies = false;
            groupArray[0] = group2;
            groups[0] = new DispatchWrapper(groupArray[0]);
            swFeature = (Feature)swFeatureManager.InsertStructuralWeldment5("C:\\Program Files\\SolidWorks Corp\\SOLIDWORKS\\lang\\english\\weldment profiles\\ansi inch\\pipe\\0.5 sch 40.sldlfp", (int)swConnectedSegmentsOption_e.swConnectedSegments_SimpleCut, false, (groups), "");
            swModel.ClearSelection2(true);

            status = swModelDocExt.SelectByID2("pipe 0.5 sch 40(1)", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swStructuralMemberFeatureData = (StructuralMemberFeatureData)swFeature.GetDefinition();
            swStructuralMemberFeatureData.AccessSelections(swModel, null);
            Debug.Print("");
            Debug.Print("Number of groups: " + swStructuralMemberFeatureData.GetGroupsCount());
            Debug.Print(" Feature name: " + swFeature.Name);
            groupArray = (object[])swStructuralMemberFeatureData.Groups;
            for (i = 0; i < groupArray.Length; i++)
            {
                group = (StructuralMemberGroup)groupArray[i];
                Debug.Print(" Arc segment merged? " + group.MergeArcSegmentBodies);
            }
            swStructuralMemberFeatureData.ReleaseSelectionAccess();

            Debug.Print("");

            status = swModelDocExt.SelectByID2("pipe 0.5 sch 40(2)", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swStructuralMemberFeatureData = (StructuralMemberFeatureData)swFeature.GetDefinition();
            swStructuralMemberFeatureData.AccessSelections(swModel, null);
            Debug.Print("");
            Debug.Print("Number of groups: " + swStructuralMemberFeatureData.GetGroupsCount());
            Debug.Print(" Feature name: " + swFeature.Name);
            groupArray = (object[])swStructuralMemberFeatureData.Groups;
            for (i = 0; i < groupArray.Length; i++)
            {
                group = (StructuralMemberGroup)groupArray[i];
                Debug.Print(" Arc segment merged? " + group.MergeArcSegmentBodies);
            }
            swStructuralMemberFeatureData.ReleaseSelectionAccess();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
