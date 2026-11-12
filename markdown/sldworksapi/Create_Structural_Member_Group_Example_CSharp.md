---
title: "Create a Structural-Member Group Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Structural_Member_Group_Example_CSharp.htm"
---

# Create a Structural-Member Group Example (C#)

This example shows how to create structural-member groups for weldment features.

```vb
// --------------------------------------------------------------------------
 // Preconditions:
 // 1. Ensure that the specified weldment profile and path exist.
 // 2. If necessary, modify the path in both calls to InsertStructuralWeldment3.
 //
 // Postconditions:
 // 1. Two structural-member features are created.
 // 2. Each feature consists of one structural-member group of two
 //    sketch segments.
 // 3. Inspect the Immediate Window for information.
 //---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace CreateStructureMemberGroup_CSharp.csproj
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
            Part.ClearSelection2(true);
            Part.SketchManager.InsertSketch(true);
            Part.ViewZoomtofit2();
            Feature myFeature = default(Feature);
            myFeature = Part.FeatureManager.InsertWeldmentFeature();
            StructuralMemberGroup Group1 = default(StructuralMemberGroup);
            Group1 = FeatMgr.CreateStructuralMemberGroup();
            SketchSegment[] segments1 = new SketchSegment[2];
            StructuralMemberGroup[] GroupArray1 = new StructuralMemberGroup[1];
            boolstatus = Part.Extension.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.1495427140733, 0.1133237194389, 0, false, 0, null, 0);
            boolstatus = Part.Extension.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", -0.1872393706766, 0.08238014634844, 0, true, 0, null, 0);
            segments1[0] = (SketchSegment)SelMgr.GetSelectedObject6(1, 0);
            segments1[1] = (SketchSegment)SelMgr.GetSelectedObject6(2, 0);
            Group1.Segments = segments1;
            GroupArray1[0] = Group1;
            myFeature = Part.FeatureManager.InsertStructuralWeldment3("C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\weldment profiles\\ansi inch\\c channel\\3 x 5.sldlfp", 1, 0, false, GroupArray1);
            Part.ClearSelection2(true);
            StructuralMemberGroup Group2 = default(StructuralMemberGroup);
            Group2 = FeatMgr.CreateStructuralMemberGroup();
            SketchSegment[] segments2 = new SketchSegment[2];
            StructuralMemberGroup[] GroupArray2 = new StructuralMemberGroup[1];
            boolstatus = Part.Extension.SelectByID2("Line5@Sketch1", "EXTSKETCHSEGMENT", 0.1185825251083, 0.03369083550887, 0, false, 0, null, 0);
            boolstatus = Part.Extension.SelectByID2("Line6@Sketch1", "EXTSKETCHSEGMENT", 0.06513561531715, -0.02774616865332, 0, true, 0, null, 0);
            segments2[0] = (SketchSegment)SelMgr.GetSelectedObject6(1, 0);
            segments2[1] = (SketchSegment)SelMgr.GetSelectedObject6(2, 0);
            Group2.Segments = segments2;
            GroupArray2[0] = Group2;
            myFeature = Part.FeatureManager.InsertStructuralWeldment3("C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\weldment profiles\\ansi inch\\c channel\\3 x 5.sldlfp", 1, 0, false, GroupArray2);
            Part.ClearSelection2(true);
            // Get Group Information
            StructuralMemberGroup Group = default(StructuralMemberGroup);
            Object[] vGroups = null;
            Object[] vSegments = null;
            SketchSegment skSegment = default(SketchSegment);
            boolstatus = Part.Extension.SelectByID2("Structural Member1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swWeldFeat = (Feature)SelMgr.GetSelectedObject6(1, 0);
            swWeldFeatData = (StructuralMemberFeatureData)swWeldFeat.GetDefinition();
            swWeldFeatData.AccessSelections(Part, null);
            Debug.Print("");
            Debug.Print("Groups Count : " + swWeldFeatData.GetGroupsCount());
            Debug.Print(" Feature Name : " + swWeldFeat.Name);
            vGroups = (Object[])swWeldFeatData.Groups;
            long i = 0;
            long j = 0;
            for (i = vGroups.GetLowerBound(0); i <= vGroups.GetUpperBound(0); i++)
            {
                Group = (StructuralMemberGroup)vGroups[i];
                Debug.Print(" Segment Count in Group " + i + 1 + " : " + Group.GetSegmentsCount());
                Debug.Print(" Rotational angle of group: " + Group.Angle.ToString());
                vSegments = (Object[])Group.Segments;
                for (j = vSegments.GetLowerBound(0); j <= vSegments.GetUpperBound(0); j++)
                {
                    skSegment = (SketchSegment)vSegments[j];
                    skSegment.Select(false);
                }
            }
            swWeldFeatData.ReleaseSelectionAccess();
            boolstatus = Part.Extension.SelectByID2("Structural Member2", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swWeldFeat = (Feature)SelMgr.GetSelectedObject6(1, 0);
            swWeldFeatData = (StructuralMemberFeatureData)swWeldFeat.GetDefinition();
            swWeldFeatData.AccessSelections(Part, null);
            Debug.Print("");
            Debug.Print("Groups Count : " + swWeldFeatData.GetGroupsCount());
            Debug.Print(" Feature Name : " + swWeldFeat.Name);
            vGroups = (Object[])swWeldFeatData.Groups;
            for (i = vGroups.GetLowerBound(0); i <= vGroups.GetUpperBound(0); i++)
            {
                Group = (StructuralMemberGroup)vGroups[i];
                Debug.Print(" Segment Count in Group " + i + 1 + " : " + Group.GetSegmentsCount());
                Debug.Print(" Rotational angle of group: " + Group.Angle.ToString());
                vSegments = (Object[])Group.Segments;
                for (j = vSegments.GetLowerBound(0); j <= vSegments.GetUpperBound(0); j++)
                {
                    skSegment = (SketchSegment)vSegments[j];
                    skSegment.Select(false);
                }
            }
            swWeldFeatData.ReleaseSelectionAccess();
        }
        public SldWorks swApp;
    }
}
```
