---
title: "Insert Structural Weldment Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Structural_Weldment_Example_CSharp.htm"
---

# Insert Structural Weldment Example (C#)

This example shows how to create structural weldment features using structural member groups.

```
//---------------------------------------------------------------------------
// Preconditions:
// 1. Verify the existence of the weldment profile pathname
//    as specified in both calls to IFeatureManager::InsertStructuralWeldment4.
// 2. Open an Immediate window.
//
// Postconditions:
// 1. Creates a new part document containing a weldment and structural members.
// 2. Rotates c channel 3 x 5(1).
// 3. Inspect the FeatureManager design tree, graphics area, and
//    Immediate window.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {

        ModelDoc2 Part;
        bool boolstatus;
        FeatureManager FeatMgr;
        SelectionMgr SelMgr;
        Feature swWeldFeat;
        StructuralMemberFeatureData swWeldFeatData;

        public void Main()
        {

            string MacroFolder = null;
            MacroFolder = swApp.GetCurrentMacroPathFolder();
            swApp.SetCurrentWorkingDirectory(MacroFolder);

            string Template = null;
            Template = swApp.GetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swDefaultTemplatePart);
            Part = (ModelDoc2)swApp.NewDocument(Template, 0, 0, 0);

            FeatMgr = Part.FeatureManager;
            SelMgr = (SelectionMgr)Part.SelectionManager;

            Part.ClearSelection2(true);

            object vSkLines = null;
            vSkLines = Part.SketchManager.CreateCornerRectangle(-0.1872393706766, 0.1133237194389, 0, -0.07003610048208, 0.009188409684237, 0);

            Part.ClearSelection2(true);

            vSkLines = Part.SketchManager.CreateCornerRectangle(0.06513561531715, 0.03369083550887, 0, 0.1807053904567, -0.08106219210316, 0);
            Part.SketchManager.InsertSketch(true);

            Part.ViewZoomtofit2();

            object myFeature = null;
            myFeature = Part.FeatureManager.InsertWeldmentFeature();

            StructuralMemberGroup Group1 = default(StructuralMemberGroup);
            Group1 = FeatMgr.CreateStructuralMemberGroup();
            SketchSegment[] segments1 = new SketchSegment[2];
            object[] GroupArray1 = new object[1];

            boolstatus = Part.Extension.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.1495427140733, 0.1133237194389, 0, false, 0, null, 0);
            boolstatus = Part.Extension.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", -0.1872393706766, 0.08238014634844, 0, true, 0, null, 0);

            segments1[0] = (SketchSegment)SelMgr.GetSelectedObject6(1, 0);
            segments1[1] = (SketchSegment)SelMgr.GetSelectedObject6(2, 0);

            Group1.Segments = segments1;
            Group1.Angle = 0.785714285714286;             //radians
            Group1.ApplyCornerTreatment = true;
            Group1.CornerTreatmentType = (int)swSolidworksWeldmentEndCondOptions_e.swEndConditionMiter;
            Group1.MirrorProfile = true;
            Group1.MirrorProfileAxis = (int)swMirrorProfileOrAlignmentAxis_e.swMirrorProfileOrAlignmentAxis_Vertical;
            Group1.GapWithinGroup = 0.0127;            //meters

            GroupArray1[0] = (object)Group1;
            DispatchWrapper[] groups1 = new DispatchWrapper[1];
            groups1[0] = new DispatchWrapper(GroupArray1[0]);

            myFeature = Part.FeatureManager.InsertStructuralWeldment4("C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\weldment profiles\\ansi inch\\c channel\\3 x 5.sldlfp", 1, false, groups1);

            Part.ClearSelection2(true);

            StructuralMemberGroup Group2 = default(StructuralMemberGroup);
            Group2 = FeatMgr.CreateStructuralMemberGroup();
            SketchSegment[] segments2 = new SketchSegment[2];
            object[] GroupArray2 = new object[1];

            boolstatus = Part.Extension.SelectByID2("Line5@Sketch1", "EXTSKETCHSEGMENT", 0.1185825251083, 0.03369083550887, 0, false, 0, null, 0);
            boolstatus = Part.Extension.SelectByID2("Line6@Sketch1", "EXTSKETCHSEGMENT", 0.06513561531715, -0.02774616865332, 0, true, 0, null, 0);

            segments2[0] = (SketchSegment)SelMgr.GetSelectedObject6(1, 0);
            segments2[1] = (SketchSegment)SelMgr.GetSelectedObject6(2, 0);

            Group2.Segments = segments2;
            Group2.AlignAxis = (int)swMirrorProfileOrAlignmentAxis_e.swMirrorProfileOrAlignmentAxis_Vertical;

            GroupArray2[0] = (object)Group2;
            DispatchWrapper[] groups2 = new DispatchWrapper[1];
            groups2[0] = new DispatchWrapper(GroupArray2[0]);

            myFeature = Part.FeatureManager.InsertStructuralWeldment4("C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\weldment profiles\\ansi inch\\c channel\\3 x 5.sldlfp", 1, false, groups2);

            Part.ClearSelection2(true);

            // Get Group Information

            StructuralMemberGroup Group = default(StructuralMemberGroup);
            object[] vGroups = null;
            object[] vSegments = null;

            boolstatus = Part.Extension.SelectByID2("c channel 3 x 5(1)", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swWeldFeat = (Feature)SelMgr.GetSelectedObject6(1, 0);

            swWeldFeatData = (StructuralMemberFeatureData)swWeldFeat.GetDefinition();
            swWeldFeatData.AccessSelections(Part, null);

            Debug.Print("");
            Debug.Print("Groups Count : " + swWeldFeatData.GetGroupsCount());
            Debug.Print(" Feature Name : " + swWeldFeat.Name);

            vGroups = (object[])swWeldFeatData.Groups;

            int i = 0;
            int j = 0;
            for (i = vGroups.GetLowerBound(0); i <= vGroups.GetUpperBound(0); i++)
            {
                Group = (StructuralMemberGroup)vGroups[i];
                Debug.Print(" Segment Count in Group " + i + 1 + " : " + Group.GetSegmentsCount());
                Debug.Print(" Rotational angle of group: " + Group.Angle);
                Debug.Print(" ApplyCornerTreatment: " + Group.ApplyCornerTreatment);
                Debug.Print(" CornerTreatmentType: " + Group.CornerTreatmentType);
                Debug.Print(" MirrorProfile: " + Group.MirrorProfile);
                Debug.Print(" MirrorProfileAxis: " + Group.MirrorProfileAxis);
                Debug.Print(" GapWithinGroup: " + Group.GapWithinGroup);
                vSegments = (object[])Group.Segments;
                for (j = vSegments.GetLowerBound(0); j <= vSegments.GetUpperBound(0); j++)
                {
                    ((SketchSegment)vSegments[j]).Select(false);
                }
            }

            swWeldFeatData.ReleaseSelectionAccess();

            boolstatus = Part.Extension.SelectByID2("c channel 3 x 5(2)", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swWeldFeat = (Feature)SelMgr.GetSelectedObject6(1, 0);
            swWeldFeatData = (StructuralMemberFeatureData)swWeldFeat.GetDefinition();
            swWeldFeatData.AccessSelections(Part, null);

            Debug.Print("");
            Debug.Print("Groups Count : " + swWeldFeatData.GetGroupsCount());
            Debug.Print(" Feature Name : " + swWeldFeat.Name);

            vGroups = (object[])swWeldFeatData.Groups;
            for (i = vGroups.GetLowerBound(0); i <= vGroups.GetUpperBound(0); i++)
            {
                Group = (StructuralMemberGroup)vGroups[i];
                Debug.Print(" Segment Count in Group " + i + 1 + " : " + Group.GetSegmentsCount());
                Debug.Print(" Rotational angle of group: " + Group.Angle);
                Debug.Print(" ApplyCornerTreatment: " + Group.ApplyCornerTreatment);
                Debug.Print(" CornerTreatmentType: " + Group.CornerTreatmentType);
                Debug.Print(" MirrorProfile: " + Group.MirrorProfile);
                Debug.Print(" MirrorProfileAxis: " + Group.MirrorProfileAxis);
                Debug.Print(" GapWithinGroup: " + Group.GapWithinGroup);
                vSegments = (object[])Group.Segments;
                for (j = vSegments.GetLowerBound(0); j <= vSegments.GetUpperBound(0); j++)
                {
                    ((SketchSegment)vSegments[j]).Select(false);
                }
            }

            swWeldFeatData.ReleaseSelectionAccess();

            Part.ClearSelection2(true);
        }

        public SldWorks swApp;

    }
}
```
