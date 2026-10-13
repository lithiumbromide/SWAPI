---
title: "Insert Weldment Features Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weldment_Features_Example_CSharp.htm"
---

# Insert Weldment Features Example (C#)

This example shows how to insert the following weldment features into the FeatureManager design tree:

* End cap feature

* Fillet bead feature

* Gusset feature

* Structural weldment

* Sub weld folder

* Weldment trim feature

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\weldments\weldment_box2.sldprt
 // 2. Expand the Cut list folder in the FeatureManager design tree
 //    and observe its contents.
 // 3. Delete End cap1 from the FeatureManager design tree.
 // 4. Change the path specified for profilePathName, if necessary.
 //
 // Postconditions: Observe the following in the FeatureManager design tree:
 //    * Gusset1 moves to the sub weld folder, Sub Folder1, in the Cut list
 //      folder
 //    * Trim/Extend8 feature appears at the bottom of the design tree and at
 //      the end of the Cut list folder
 //    * Structural Member6 feature appears at the bottom of the design tree
 //      and at the end of the Cut list folder
 //    * End cap5 feature appears at the bottom of the design tree and in the
 //      Cut list folder
 //    * Gusset5 feature appears at the bottom of the design tree and in the
 //      Cut list folder
 //    * Fillet Bead5 feature appears at the bottom of the design tree and
 //      in the Cut list folder
 //
 //  NOTE: Because this part is used elsewhere,
 // do not save any changes when you close it.
 //---------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
namespace InsertWeldmentFeatures_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        FeatureManager fm;
        SelectionMgr selMgr;
        ModelDoc2 Part;
        bool boolstatus;
        public void Main()
        {
            object myFeature = null;
            Body2[] obj = new Body2[1];
            Array v = default(Array);
            Part = (ModelDoc2)swApp.ActiveDoc;
            object myModelView = null;
            myModelView = Part.ActiveView;
            selMgr = (SelectionMgr)Part.SelectionManager;
            //InsertSubWeldFolder2
            boolstatus = Part.Extension.SelectByID2("Gusset1", "SOLIDBODY", 0, 0, 0, false, 0, null, 0);
            obj[0] = (Body2)selMgr.GetSelectedObject6(1, -1);
            v = obj;
            fm = Part.FeatureManager;
            myFeature = fm.InsertSubWeldFolder2(v);
            Part.ClearSelection2(true);
            //InsertWeldmentTrimFeature2
            Body2[] obj1 = new Body2[1];
            Body2[] obj2 = new Body2[1];
            long Options = 0;
            Array v1 = default(Array);
            Array v2 = default(Array);
            boolstatus = Part.Extension.SelectByID2("Structural Member1[2]", "SOLIDBODY", 0, 0, 0, true, 2, null, 0);
            boolstatus = Part.Extension.SelectByID2("Structural Member1[1]", "SOLIDBODY", 0, 0, 0, true, 1, null, 0);
            long Count = 0;
            Count = selMgr.GetSelectedObjectCount();
            if (Count == 2)
            {
                obj1[0] = (Body2)selMgr.GetSelectedObject2(1);
                v1 = obj1;
                obj2[0] = (Body2)selMgr.GetSelectedObject2(2);
                v2 = obj2;
                Part.ClearSelection2(true);
                Options = (long)swWeldmentTrimExtendOptionType_e.swWeldmentTrimExtendOption_AllowTrimmedExtensionTrim + (long)swWeldmentTrimExtendOptionType_e.swWeldmentTrimExtendOption_AllowTrimmingExtensionTrim + (long)swWeldmentTrimExtendOptionType_e.swWeldmentTrimExtendOption_CopedCut + (long)swWeldmentTrimExtendOptionType_e.swWeldmentTrimExtendOption_WeldGap;
                myFeature = fm.InsertWeldmentTrimFeature2(1, (int)Options, 0.01, v1, v2);
            }
            //InsertEndCapFeature
            Feature endCapFeature = default(Feature);
            Face2[] face1 = new Face2[1];
            Array x = default(Array);
            boolstatus = Part.Extension.SelectByID2("", "FACE", 0.6023443450227, 0.6150000000001, -1.013201139555, true, 1, null, 0);
            face1[0] = (Face2)selMgr.GetSelectedObject6(1, -1);
            x = face1;
            endCapFeature = fm.InsertEndCapFeature2(0.005, false, true, 0.003, 0.5, 0.003, x);
            Part.ClearSelection2(true);
            //InsertStructuralWeldment3
            Array segmentObjects = default(Array);
            SketchSegment[] sketchSegments = new SketchSegment[4];
            string profilePathName = null;
            Feature structuralMember = default(Feature);
            StructuralMemberGroup @group = default(StructuralMemberGroup);
            StructuralMemberGroup[] GroupArray1 = new StructuralMemberGroup[1];
            long i = 0;
            @group = fm.CreateStructuralMemberGroup();
            Part.ClearSelection2(true);
            Part.InsertSketch2(true);
            segmentObjects = (System.Array)Part.SketchManager.CreateCornerRectangle(0, 0, 0, 1.0, 2.0, 0);
            for (i = 0; i <= segmentObjects.GetUpperBound(0); i++)
            {
                sketchSegments[i] = (SketchSegment)segmentObjects.GetValue(i);
            }
            @group.Segments = sketchSegments;
            GroupArray1[0] = @group;
            Part.ViewZoomtofit2();
            Part.InsertSketch2(true);
            profilePathName = "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\english\\weldment profiles\\ansi inch\\square tube\\2 x 2 x 0.25.SLDLFP";
            structuralMember = fm.InsertStructuralWeldment3(profilePathName, 1, 0.0, false, GroupArray1);
            Part.ClearSelection2(true);
            //InsertGussetFeature2
            Face2[] faceGFObj = new Face2[2];
            object z = null;
            boolstatus = Part.Extension.SelectByID2("", "FACE", 0.02539999999988, 1.94542628561, 0.00429028534694, true, 1, null, 0);
            boolstatus = Part.Extension.SelectByID2("", "FACE", 0.07780718114736, 1.9746, -0.001856983219, true, 2, null, 0);
            Count = selMgr.GetSelectedObjectCount();
            if (Count == 2)
            {
                faceGFObj[0] = (Face2)selMgr.GetSelectedObject6(1, 1);
                faceGFObj[1] = (Face2)selMgr.GetSelectedObject6(1, 2);
                z = faceGFObj;
                Part.ClearSelection2(true);
                myFeature = fm.InsertGussetFeature2(0.005, 0, 0, false, 0.025, 0.025, 0.015, 0.7853981633975, 0.015, true,
                0.005, 0, false, false, false, z);
            }
            //InsertFilletBeadFeature3
            Face2[] fbFaceObj1 = new Face2[1];
            Face2[] fbFaceObj2 = new Face2[2];
            Part.ClearSelection2(true);
            boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0412896304482, 0.02548020566445, 0, true, 1, null, 0);
            boolstatus = Part.Extension.SelectByID2("", "FACE", 0.09804264728081, 0.01499999999999, 0.0008069730266129, true, 2, null, 0);
            boolstatus = Part.Extension.SelectByID2("", "FACE", 0.01364526875011, 0.08738481720087, 0.01330055827532, true, 4, null, 0);
            Count = selMgr.GetSelectedObjectCount();
            // Face Set 1
            fbFaceObj1[0] = (Face2)selMgr.GetSelectedObject6(1, 1);
            // Face Set 2
            fbFaceObj2[0] = (Face2)selMgr.GetSelectedObject6(1, 2);
            //fbFaceObj2(0) = selMgr.GetSelectedObject6(1, 4)
            v1 = fbFaceObj1;
            v2 = fbFaceObj2;
            Part.ClearSelection2(true);
            int[] edges = new int[1];
            Array edgeArray = default(Array);
            edges[0] = 0;
            //edges(1) = 0
            edgeArray = edges;
            myFeature = fm.InsertFilletBeadFeature3(0, 0.003, 0.003, 2, 0.003, 0.006, 0, 0.003, 0.003, 2, 0.003, 0, 1, edgeArray, 0, null, v1, v2);
            Part.ClearSelection2(true);
        }
        public SldWorks swApp;
    }
}
```
