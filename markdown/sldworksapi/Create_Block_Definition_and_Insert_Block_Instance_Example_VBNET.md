---
title: "Create Block Definition and Insert Block Instance Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Block_Definition_and_Insert_Block_Instance_Example_VBNET.htm"
---

# Create Block Definition and Insert Block Instance Example (VB.NET)

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

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2

         Dim swDraw As DrawingDoc

         Dim swSkSeg(13) As SketchSegment

         Dim swSkPt(3) As SketchPoint

         Dim swSkNote(2) As Note

         Dim vSkSeg As Object

         Dim vSkPt As Object

         Dim vSkNote As Object

         Dim swSketchBlockDef As SketchBlockDefinition

         Dim swBlockInst As SketchBlockInstance

         Dim swSketchMgr As SketchManager

         Dim swModelDocExt As ModelDocExtension

         Dim swMathUtil As MathUtility

         Dim swMathPoint As MathPoint

         Dim nPt(2) As Double

         Dim vPt As Object

         Dim nbrSelObjects As Integer

         swModel = swApp.ActiveDoc

         swDraw = swModel

         swSketchMgr = swModel.SketchManager

         swModelDocExt = swModel.Extension

         swMathUtil = swApp.GetMathUtility

         swSketchMgr.AddToDB = True

         ' Revision box

         swSkSeg(0) = swSketchMgr.CreateLine(0.008372353756316, 0.207929860362, 0.0#, 0.05495488122133, 0.207929860362, 0.0#)

         swSkSeg(1) = swSketchMgr.CreateLine(0.05495488122133, 0.207929860362, 0.0#, 0.05495488122133, 0.1992788195471, 0.0#)

         swSkSeg(2) = swSketchMgr.CreateLine(0.05495488122133, 0.1992788195471, 0.0#, 0.008372353756316, 0.1992788195471, 0.0#)

         swSkSeg(3) = swSketchMgr.CreateLine(0.008372353756316, 0.1992788195471, 0.0#, 0.008372353756316, 0.207929860362, 0.0#)

         swSkSeg(4) = swSketchMgr.CreateLine(0.023613610833382, 0.207929860362, 0.0#, 0.023613610833382, 0.1992788195471, 0.0#)

         swSkSeg(5) = swSketchMgr.CreateLine(0.03964919362569, 0.207929860362, 0.0#, 0.03964919362569, 0.1992788195471, 0.0#)

         ' Clear selections; otherwise, notes are attached to line

         swModel.ClearSelection2(True)

         ' Revision notes

         swSkNote(0) = swModel.InsertNote("Cell 1")

         swSkNote(1) = swModel.InsertNote("Cell 2")

         swSkNote(2) = swModel.InsertNote("Cell 3")

         PositionNote(swApp, swModel, swSkNote(0), 0.009481461553102, 0.2052680016497, 0.0#)

         PositionNote(swApp, swModel, swSkNote(1), 0.025613610833382, 0.2052680016497, 0.0#)

         PositionNote(swApp, swModel, swSkNote(2), 0.04275469545669, 0.2052680016497, 0.0#)

         ' Points for circles

         swSkPt(0) = swSketchMgr.CreatePoint(0.02700536474232, 0.1708856599494, 0.0#)

         swSkPt(1) = swSketchMgr.CreatePoint(0.02700536474232, 0.1815330947985, 0.0#)

         swSkPt(2) = swSketchMgr.CreatePoint(0.03964919362569, 0.1815330947985, 0.0#)

         swSkPt(3) = swSketchMgr.CreatePoint(0.05029662847483, 0.1708856599494, 0.0#)

         ' Circles

         swSkSeg(6) = swSketchMgr.CreateCircle(swSkPt(0).X, swSkPt(0).Y, swSkPt(0).Z, 0.03050393605009, 0.169349494074, 0.0#)

         swSkSeg(7) = swSketchMgr.CreateCircle(swSkPt(1).X, swSkPt(1).Y, swSkPt(1).Z, 0.03305243799009, 0.183621104938, 0.0#)

         swSkSeg(8) = swSketchMgr.CreateCircle(swSkPt(2).X, swSkPt(2).Y, swSkPt(2).Z, 0.04426584652606, 0.182092003774, 0.0#)

         swSkSeg(9) = swSketchMgr.CreateCircle(swSkPt(3).X, swSkPt(3).Y, swSkPt(3).Z, 0.05496955467404, 0.164252490194, 0.0#)

         ' Lines between circles

         swSkSeg(10) = swSketchMgr.CreateLine(swSkPt(0).X, swSkPt(0).Y, swSkPt(0).Z, swSkPt(1).X, swSkPt(1).Y, swSkPt(1).Z)

         swSkSeg(11) = swSketchMgr.CreateLine(swSkPt(1).X, swSkPt(1).Y, swSkPt(1).Z, swSkPt(2).X, swSkPt(2).Y, swSkPt(2).Z)

         swSkSeg(12) = swSketchMgr.CreateLine(swSkPt(2).X, swSkPt(2).Y, swSkPt(2).Z, swSkPt(3).X, swSkPt(3).Y, swSkPt(3).Z)

         swSkSeg(13) = swSketchMgr.CreateLine(swSkPt(3).X, swSkPt(3).Y, swSkPt(3).Z, swSkPt(0).X, swSkPt(0).Y, swSkPt(0).Z)

         vSkSeg = swSkSeg

         vSkPt = swSkPt

         vSkNote = swSkNote

         nbrSelObjects = swModelDocExt.MultiSelect2(vSkSeg, True, Nothing)

         nbrSelObjects = swModelDocExt.MultiSelect2(vSkPt, True, Nothing)

         nbrSelObjects = swModelDocExt.MultiSelect2(vSkNote, True, Nothing)

         swSketchBlockDef = swSketchMgr.MakeSketchBlockFromSelected(Nothing)

         ' Define an insertion point

         nPt(0) = 60.0# / 1000.0#

         nPt(1) = 60.0# / 1000.0#

         nPt(2) = 0.0#

         vPt = nPt

         swMathPoint = swMathUtil.CreatePoint(vPt)

         ' Insert an instance of the block definition

         swBlockInst = swSketchMgr.InsertSketchBlockInstance(swSketchBlockDef, swMathPoint, 1, 0)

         ' Turn on grid and entity snapping

         swSketchMgr.AddToDB = False

         ' Redraw to see all changes

         swModel.GraphicsRedraw2()

     End Sub

     Sub PositionNote(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal swSkNote As Note, ByVal X_pos As Double, ByVal Y_pos As Double, ByVal Z_pos As Double)

         Dim swAnn As Annotation

         Dim nRetVal As Integer

         Dim bRet As Boolean

         swAnn = swSkNote.GetAnnotation

         swSkNote.Angle = 0.0#

         bRet = swSkNote.SetBalloon(swBalloonStyle_e.swBS_None, swBalloonFit_e.swBF_Tightest)

         nRetVal = swAnn.SetLeader3(swLeaderStyle_e.swBENT, swLeaderSide_e.swLS_SMART, True, False, False, False)

         bRet = swAnn.SetPosition2(X_pos, Y_pos, Z_pos)

         ' Redraw to see changes

         swModel.GraphicsRedraw2()

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
