---
title: "Create Block Definition and Insert Block Instance Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Block_Definition_and_Insert_Block_Instance_Example_VB.htm"
---

# Create Block Definition and Insert Block Instance Example (VBA)

This example shows how to create a block definition and insert a block instance in a drawing.

```vb
'---------------------------------------------------------------------------
 ' Preconditions: Open a drawing document.
 '
 ' Postconditions:
 ' 1. Creates a block definition.
 ' 2. Inserts a first instance of the block in the upper-left corner of the
 '    drawing sheet.
 ' 3. Inserts a second instance of the block in the drawing sheet.
 '---------------------------------------------------------------------------
Option Explicit

Sub main()
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swDraw                      As SldWorks.DrawingDoc
    Dim swSkSeg(13)                 As SldWorks.SketchSegment
    Dim swSkPt(3)                   As SldWorks.SketchPoint
    Dim swSkNote(2)                 As SldWorks.Note
    Dim vSkSeg                      As Variant
    Dim vSkPt                       As Variant
    Dim vSkNote                     As Variant
    Dim swSketchBlockDef            As SldWorks.SketchBlockDefinition
    Dim swBlockInst                 As SldWorks.SketchBlockInstance
    Dim swSketchMgr                 As SldWorks.SketchManager
    Dim swModelDocExt               As SldWorks.ModelDocExtension
    Dim swMathUtil                  As SldWorks.MathUtility
    Dim swMathPoint                 As SldWorks.MathPoint
    Dim nPt(2)                      As Double
    Dim vPt                         As Variant
    Dim nbrSelObjects               As Long

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel

    Set swSketchMgr = swModel.SketchManager
    Set swModelDocExt = swModel.Extension
    Set swMathUtil = swApp.GetMathUtility

    swSketchMgr.AddToDB = True

    ' Revision box
    Set swSkSeg(0) = swSketchMgr.CreateLine(0.008372353756316, 0.207929860362, 0#, 0.05495488122133, 0.207929860362, 0#)
    Set swSkSeg(1) = swSketchMgr.CreateLine(0.05495488122133, 0.207929860362, 0#, 0.05495488122133, 0.1992788195471, 0#)
    Set swSkSeg(2) = swSketchMgr.CreateLine(0.05495488122133, 0.1992788195471, 0#, 0.008372353756316, 0.1992788195471, 0#)
    Set swSkSeg(3) = swSketchMgr.CreateLine(0.008372353756316, 0.1992788195471, 0#, 0.008372353756316, 0.207929860362, 0#)
    Set swSkSeg(4) = swSketchMgr.CreateLine(0.023613610833382, 0.207929860362, 0#, 0.023613610833382, 0.1992788195471, 0#)
    Set swSkSeg(5) = swSketchMgr.CreateLine(0.03964919362569, 0.207929860362, 0#, 0.03964919362569, 0.1992788195471, 0#)

    ' Clear selections; otherwise, notes are attached to line
    swModel.ClearSelection2 True

    ' Revision notes
    Set swSkNote(0) = swModel.InsertNote("Cell 1")
    Set swSkNote(1) = swModel.InsertNote("Cell 2")
    Set swSkNote(2) = swModel.InsertNote("Cell 3")
    PositionNote swApp, swModel, swSkNote(0), 0.009481461553102, 0.2052680016497, 0#
    PositionNote swApp, swModel, swSkNote(1), 0.025613610833382, 0.2052680016497, 0#
    PositionNote swApp, swModel, swSkNote(2), 0.04275469545669, 0.2052680016497, 0#

    ' Points for circles
    Set swSkPt(0) = swSketchMgr.CreatePoint(0.02700536474232, 0.1708856599494, 0#)
    Set swSkPt(1) = swSketchMgr.CreatePoint(0.02700536474232, 0.1815330947985, 0#)
    Set swSkPt(2) = swSketchMgr.CreatePoint(0.03964919362569, 0.1815330947985, 0#)
    Set swSkPt(3) = swSketchMgr.CreatePoint(0.05029662847483, 0.1708856599494, 0#)

    ' Circles
    Set swSkSeg(6) = swSketchMgr.CreateCircle(swSkPt(0).X, swSkPt(0).Y, swSkPt(0).Z, 0.03050393605009, 0.169349494074, 0#)
    Set swSkSeg(7) = swSketchMgr.CreateCircle(swSkPt(1).X, swSkPt(1).Y, swSkPt(1).Z, 0.03305243799009, 0.183621104938, 0#)
    Set swSkSeg(8) = swSketchMgr.CreateCircle(swSkPt(2).X, swSkPt(2).Y, swSkPt(2).Z, 0.04426584652606, 0.182092003774, 0#)
    Set swSkSeg(9) = swSketchMgr.CreateCircle(swSkPt(3).X, swSkPt(3).Y, swSkPt(3).Z, 0.05496955467404, 0.164252490194, 0#)

    ' Lines between circles
    Set swSkSeg(10) = swSketchMgr.CreateLine(swSkPt(0).X, swSkPt(0).Y, swSkPt(0).Z, swSkPt(1).X, swSkPt(1).Y, swSkPt(1).Z)
    Set swSkSeg(11) = swSketchMgr.CreateLine(swSkPt(1).X, swSkPt(1).Y, swSkPt(1).Z, swSkPt(2).X, swSkPt(2).Y, swSkPt(2).Z)
    Set swSkSeg(12) = swSketchMgr.CreateLine(swSkPt(2).X, swSkPt(2).Y, swSkPt(2).Z, swSkPt(3).X, swSkPt(3).Y, swSkPt(3).Z)
    Set swSkSeg(13) = swSketchMgr.CreateLine(swSkPt(3).X, swSkPt(3).Y, swSkPt(3).Z, swSkPt(0).X, swSkPt(0).Y, swSkPt(0).Z)

    vSkSeg = swSkSeg
    vSkPt = swSkPt
    vSkNote = swSkNote

    nbrSelObjects = swModelDocExt.MultiSelect2(vSkSeg, True, Nothing)
    nbrSelObjects = swModelDocExt.MultiSelect2(vSkPt, True, Nothing)
    nbrSelObjects = swModelDocExt.MultiSelect2(vSkNote, True, Nothing)

    Set swSketchBlockDef = swSketchMgr.MakeSketchBlockFromSelected(Nothing)

     ' Define an insertion point
    nPt(0) = 60# / 1000#
    nPt(1) = 60# / 1000#
    nPt(2) = 0#
    vPt = nPt
    Set swMathPoint = swMathUtil.CreatePoint(vPt)

    ' Insert an instance of the block definition
    Set swBlockInst = swSketchMgr.InsertSketchBlockInstance(swSketchBlockDef, swMathPoint, 1, 0)

    swSketchMgr.AddToDB = False

    ' Redraw to see all changes
    swModel.GraphicsRedraw2

End Sub
Sub PositionNote (swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSkNote As SldWorks.Note, X_pos As Double, Y_pos As Double, Z_pos As Double)
    Dim swAnn                       As SldWorks.Annotation
    Dim nRetVal                     As Long
    Dim bRet                        As Boolean

    Set swAnn = swSkNote.GetAnnotation

    swSkNote.Angle = 0#
    bRet = swSkNote.SetBalloon(swBS_None, swBF_Tightest)
    nRetVal = swAnn.SetLeader3(swLeaderStyle_e.swBENT, swLS_SMART, True, False, False, False)
    bRet = swAnn.SetPosition2(X_pos, Y_pos, Z_pos)

    ' Redraw to see changes
    swModel.GraphicsRedraw2
End Sub
```
