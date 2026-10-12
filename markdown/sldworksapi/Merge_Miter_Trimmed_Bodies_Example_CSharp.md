---
title: "Merge Miter Trimmed Bodies Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Merge_Miter_Trimmed_Bodies_Example_CSharp.htm"
---

# Merge Miter Trimmed Bodies Example (C#)

This example shows how to specify to merge miter trimmed bodies in a structural-member group.

```
//---------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified weldment profile exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Creates a new document containing a weldment and a structural member.
// 2. Sets to merge miter trimmed bodies in the structural-member group.
// 3. Examine the Immediate window.
//---------------------------------------------------------------------------
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
            FeatureManager swFeatMgr = default(FeatureManager);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Feature swWeldFeat = default(Feature);
            StructuralMemberFeatureData swWeldFeatData = default(StructuralMemberFeatureData);
            Feature swFeature = default(Feature);
            bool status = false;
            string template = null;
            object[] skLines = null;
            StructuralMemberGroup group1 = default(StructuralMemberGroup);
            SketchSegment[] segments1 = new SketchSegment[2];
            DispatchWrapper[] groups1 = new DispatchWrapper[1];
            object[] groupArray1 = new object[1];
            StructuralMemberGroup group = default(StructuralMemberGroup);
            object[] groups = null;
            object[] segments = null;
            int i = 0;
            int j = 0;

            template = swApp.GetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swDefaultTemplatePart);
            swModel = (ModelDoc2)swApp.NewDocument(template, 0, 0, 0);
            swFeatMgr = (FeatureManager)swModel.FeatureManager;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swModel.ClearSelection2(true);

            // Create weldment and structural member
            skLines = (object[])swModel.SketchManager.CreateCornerRectangle(-0.1872393706766, 0.1133237194389, 0, -0.07003610048208, 0.009188409684237, 0);
            swModel.ClearSelection2(true);
            swModel.SketchManager.InsertSketch(true);
            swModel.ViewZoomtofit2();
            swFeature = (Feature)swFeatMgr.InsertWeldmentFeature();
            group1 = (StructuralMemberGroup)swFeatMgr.CreateStructuralMemberGroup();
            status = swModel.Extension.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.1495427140733, 0.1133237194389, 0, false, 0, null, 0);
            status = swModel.Extension.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", -0.1872393706766, 0.08238014634844, 0, true, 0, null, 0);
            segments1[0] = (SketchSegment)swSelMgr.GetSelectedObject6(1, 0);
            segments1[1] = (SketchSegment)swSelMgr.GetSelectedObject6(2, 0);
            group1.Segments = segments1;
            group1.Angle = 0;
            group1.ApplyCornerTreatment = true;
            group1.CornerTreatmentType = (int)swSolidworksWeldmentEndCondOptions_e.swEndConditionMiter;
            group1.MirrorProfile = true;
            group1.MirrorProfileAxis = (int)swMirrorProfileOrAlignmentAxis_e.swMirrorProfileOrAlignmentAxis_Vertical;
            group1.GapWithinGroup = 0;
            groupArray1[0] = (object)group1;
            groups1[0] = new DispatchWrapper(groupArray1[0]);
            swFeature = (Feature)swFeatMgr.InsertStructuralWeldment5("C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\weldment profiles\\ansi inch\\c channel\\3 x 5.sldlfp", (int)swConnectedSegmentsOption_e.swConnectedSegments_SimpleCut, false, groups1, "");
            swModel.ClearSelection2(true);

            // Get and set structural-member group information
            status = swModel.Extension.SelectByID2("c channel 3 x 5(1)", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swWeldFeat = (Feature)swSelMgr.GetSelectedObject6(1, 0);
            swWeldFeatData = (StructuralMemberFeatureData)swWeldFeat.GetDefinition();
            swWeldFeatData.AccessSelections(swModel, null);
            Debug.Print("");
            Debug.Print("Number of groups: " + swWeldFeatData.GetGroupsCount());
            Debug.Print(" Feature name: " + swWeldFeat.Name);
            groups = (object[])swWeldFeatData.Groups;
            for (i = 0; i < groups.Length; i++)
            {
                group = (StructuralMemberGroup)groups[i];
                Debug.Print(" Number of segments in group " + i + 1 + ": " + group.GetSegmentsCount());
                Debug.Print(" Apply corner treatment? " + group.ApplyCornerTreatment);
                Debug.Print(" Corner treatment type (1 = swSolidworksWeldmentEndCondOptions_e.swEndconditionMiter): " + group.CornerTreatmentType);
                Debug.Print(" Original merge miter trimmed bodies setting: " + group.MiterMergeCondition);
                if (group.CornerTreatmentType == (int)swSolidworksWeldmentEndCondOptions_e.swEndConditionMiter)
                {
                    group.MiterMergeCondition = true;
                }
                Debug.Print(" Modified merge miter trimmed bodies setting: " + group.MiterMergeCondition);
                segments = (object[])group.Segments;
                for (j = 0; j < segments.Length; j++)
                {
                    ((SketchSegment)segments[j]).Select4(false, null);
                }
            }
            swFeature.ModifyDefinition(swWeldFeatData, swModel, null);

            swModel.ClearSelection2(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
