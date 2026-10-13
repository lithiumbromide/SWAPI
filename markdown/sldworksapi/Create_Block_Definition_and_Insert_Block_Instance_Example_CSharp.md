---
title: "Create Block Definition and Insert Block Instance Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Block_Definition_and_Insert_Block_Instance_Example_CSharp.htm"
---

# Create Block Definition and Insert Block Instance Example (C#)

This example shows how to create a block definition and insert a block instance in a drawing.

```vb
//---------------------------------------------------------------------------
 // Preconditions: Open a drawing document.
 //
 // Postconditions:
 // 1. Creates a block definition.
 // 2. Inserts a first instance of the block in the upper-left corner of the
 //    drawing sheet.
 // 3. Inserts a second instance of the block in the drawing sheet.
 //---------------------------------------------------------------------------
```

```vb
using System;
using System.Collections.Generic;
using System.Text;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
namespace SketchBlocks.csproj
{
    partial  class SolidWorksMacro
    {
        public void Main()
        {
            SldWorks.SldWorks swApp = new SldWorks.SldWorks();
            ModelDoc2 swModel;
            ModelDoc2 swModel2;
            DrawingDoc swDraw;
            SketchSegment[] swSkSeg = new SketchSegment[14];
            SketchPoint[] swSkPt = new SketchPoint[4];
            Note[] swSkNote = new Note[3];
            Object vSkSeg;
            Object vSkPt;
            Object vSkNote;
            SketchBlockDefinition swSketchBlockDef;
            SketchBlockInstance swBlockInst;
            SketchManager swSketchMgr;
            ModelDocExtension swModelDocExt;
            MathUtility swMathUtil;
            MathPoint swMathPoint;
            double[] nPt = new double[3];
            Object vPt;
            int nbrSelObjects;

            swModel = swApp.IActiveDoc2;
            swDraw = (DrawingDoc)swModel;

            //Interfaces needed for block APIs
            swSketchMgr = swModel.SketchManager;
            swModelDocExt = swModel.Extension;
            swMathUtil = swApp.IGetMathUtility();

            swSketchMgr.AddToDB = true;

            // Revision box
            swSkSeg[0] = (SketchSegment)swSketchMgr.CreateLine(0.008372353756316, 0.207929860362, 0, 0.05495488122133, 0.207929860362, 0);
            swSkSeg[1] = (SketchSegment)swSketchMgr.CreateLine(0.05495488122133, 0.207929860362, 0, 0.05495488122133, 0.1992788195471, 0);
            swSkSeg[2] = (SketchSegment)swSketchMgr.CreateLine(0.05495488122133, 0.1992788195471, 0, 0.008372353756316, 0.1992788195471, 0);
            swSkSeg[3] = (SketchSegment)swSketchMgr.CreateLine(0.008372353756316, 0.1992788195471, 0, 0.008372353756316, 0.207929860362, 0);
            swSkSeg[4] = (SketchSegment)swSketchMgr.CreateLine(0.023613610833382, 0.207929860362, 0, 0.023613610833382, 0.1992788195471, 0);
            swSkSeg[5] = (SketchSegment)swSketchMgr.CreateLine(0.03964919362569, 0.207929860362, 0, 0.03964919362569, 0.1992788195471, 0);

            // Clear selections; otherwise, notes are attached to line
            swModel.ClearSelection2(true);
            // Revision notes
            swSkNote[0] = (Note)swModel.InsertNote("Cell 1");
            swSkNote[1] = (Note)swModel.InsertNote("Cell 2");
            swSkNote[2] = (Note)swModel.InsertNote("Cell 3");
            PositionNote(swModel, swSkNote[0], 0.009481461553102, 0.2052680016497, 0.0);
            PositionNote(swModel, swSkNote[1], 0.025613610833382, 0.2052680016497, 0.0);
            PositionNote(swModel, swSkNote[2], 0.04275469545669, 0.2052680016497, 0.0);

            // Points for circles
            swSkPt[0] = (SketchPoint)swSketchMgr.CreatePoint(0.02700536474232, 0.1708856599494, 0);
            swSkPt[1] = (SketchPoint)swSketchMgr.CreatePoint(0.02700536474232, 0.1815330947985, 0);
            swSkPt[2] = (SketchPoint)swSketchMgr.CreatePoint(0.03964919362569, 0.1815330947985, 0);
            swSkPt[3] = (SketchPoint)swSketchMgr.CreatePoint(0.05029662847483, 0.1708856599494, 0);

            // Circles
            swSkSeg[6] = (SketchSegment)swSketchMgr.CreateCircle(swSkPt[0].X, swSkPt[0].Y, swSkPt[0].Z, 0.03050393605009, 0.169349494074, 0.0);
            swSkSeg[7] = (SketchSegment)swSketchMgr.CreateCircle(swSkPt[1].X, swSkPt[1].Y, swSkPt[1].Z, 0.03305243799009, 0.183621104938, 0.0);
            swSkSeg[8] = (SketchSegment)swSketchMgr.CreateCircle(swSkPt[2].X, swSkPt[2].Y, swSkPt[2].Z, 0.04426584652606, 0.182092003774, 0.0);
            swSkSeg[9] = (SketchSegment)swSketchMgr.CreateCircle(swSkPt[3].X, swSkPt[3].Y, swSkPt[3].Z, 0.05496955467404, 0.164252490194, 0.0);

            // Lines between circles
            swSkSeg[10] = (SketchSegment)swSketchMgr.CreateLine(swSkPt[0].X, swSkPt[0].Y, swSkPt[0].Z, swSkPt[1].X, swSkPt[1].Y, swSkPt[1].Z);
            swSkSeg[11] = (SketchSegment)swSketchMgr.CreateLine(swSkPt[1].X, swSkPt[1].Y, swSkPt[1].Z, swSkPt[2].X, swSkPt[2].Y, swSkPt[2].Z);
            swSkSeg[12] = (SketchSegment)swSketchMgr.CreateLine(swSkPt[2].X, swSkPt[2].Y, swSkPt[2].Z, swSkPt[3].X, swSkPt[3].Y, swSkPt[3].Z);
            swSkSeg[13] = (SketchSegment)swSketchMgr.CreateLine(swSkPt[3].X, swSkPt[3].Y, swSkPt[3].Z, swSkPt[0].X, swSkPt[0].Y, swSkPt[0].Z);
            vSkSeg = swSkSeg;
            vSkPt = swSkPt;
            vSkNote = swSkNote;

            // Select all sketch segments, sketch points,
            // and notes for the block definition
            nbrSelObjects = swModelDocExt.MultiSelect2(vSkSeg, true, null);
            nbrSelObjects = swModelDocExt.MultiSelect2(vSkPt, true, null);
            nbrSelObjects = swModelDocExt.MultiSelect2(vSkNote, true, null);

            //Create block definition
            swSketchBlockDef = swSketchMgr.MakeSketchBlockFromSelected(null);

            swModel2 = (ModelDoc2)swApp.ActiveDoc;
            swSketchMgr = swModel2.SketchManager;

            // Define an insertion point
            nPt[0] = 60.0 / 1000.0;
            nPt[1] = 60.0 / 1000.0;
            nPt[2] = 0.0;
            vPt = nPt;
            swMathPoint = (MathPoint)swMathUtil.CreatePoint(vPt);

            // Insert an instance of the block definition
            swBlockInst = swSketchMgr.InsertSketchBlockInstance(swSketchBlockDef, swMathPoint, 1, 0);

            swSketchMgr.AddToDB = false;

            // Redraw to see all changes
            swModel2.GraphicsRedraw2();
        }
        static private void PositionNote(ModelDoc2 swModel, Note swSkNote, double X_pos, double Y_pos, double Z_pos)
        {
            Annotation swAnn;
            int nRetVal;
            bool bRet;

            swAnn = (Annotation)swSkNote.GetAnnotation();

            swSkNote.Angle = 0.0;
            bRet = swSkNote.SetBalloon((int)swBalloonStyle_e.swBS_None, (int)swBalloonFit_e.swBF_Tightest);
            nRetVal = swAnn.SetLeader3((int)swLeaderStyle_e.swBENT, (int)swLeaderSide_e.swLS_SMART, true, false, false, false);
            bRet = swAnn.SetPosition2(X_pos, Y_pos, Z_pos);

            // Redraw to see changes; however, this is expensive
            swModel.GraphicsRedraw2();
        }
        public SldWorks swApp;
    }
}
```
