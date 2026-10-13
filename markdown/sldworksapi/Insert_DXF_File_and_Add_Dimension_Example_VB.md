---
title: "Insert DXF/DWG File and Add Dimensions Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_DXF_File_and_Add_Dimension_Example_VB.htm"
---

# Insert DXF/DWG File and Add Dimensions Example (VBA)

This example shows how to insert a DXF/DWG image on a preselected plane or face and then autodimension it.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Replace path_name with the pathname of an existing DXF/DWG file.
' 3. Select a plane or face on which to insert the DXF/DWG image.
'
' Postconditions:
' 1. Adds the DXF/DWG image as a sketch.
' 2. Autodimensions the sketch.
' 3. Use Zoom to Area to inspect the sketch dimensioning.
' 4. Press F5 to rebuild the model.
'---------------------------------------------------------------------------
Option Explicit
```

```vb
Const nTolerance As Double = 0.00000001
 Dim swModelView As SldWorks.ModelView
 Dim swSketchMgr As SldWorks.SketchManager
 Dim nRetVal As Long
Sub main()
    Const sDwgFileName                  As String = "path_name"
    Dim swApp As SldWorks.SldWorks
     Dim swModel As SldWorks.ModelDoc2
     Dim swFeatMgr As SldWorks.FeatureManager
     Dim swFeat As SldWorks.Feature
     Dim swSketch As SldWorks.Sketch
     Dim swSelMgr As SldWorks.SelectionMgr
     Dim swSelData As SldWorks.SelectData
     Dim bRet As Boolean
     Dim importData As SldWorks.ImportDxfDwgData
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelView = swModel.ActiveView
     Set swFeatMgr = swModel.FeatureManager
     Set importData = swApp.GetImportFileData(sDwgFileName)

    'Unit
     importData.LengthUnit("") = SwConst.swLengthUnit_e.swMM

    'Position
     bRet = importData.SetPosition("", swDwgEntitiesCentered, 0, 0)

    'Sheet scale
     bRet = importData.SetSheetScale("", 1#, 2#)

    'Paper size
     bRet = importData.SetPaperSize("", SwConst.swDwgPaperSizes_e.swDwgPaperAsize, 0#, 0#)

    'Import method
     importData.ImportMethod("") = swImportDxfDwg_ImportMethod_e.swImportDxfDwg_ImportToExistingPart
    Set swFeat = swFeatMgr.InsertDwgOrDxfFile2(sDwgFileName, importData)

    Set swSketch = swFeat.GetSpecificFeature2
     Set swSelMgr = swModel.SelectionManager
     Set swSelData = swSelMgr.CreateSelectData
    nRetVal = AutoDimensionSketch(swApp, swModel, swSketch, swSelData)
    Stop

    ' Rebuild to update sketch
     swModel.EditRebuild3
End Sub

Function GetAllSketchLines(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch) As Variant
    Dim vSketchSegArr As Variant
     Dim vSketchSeg As Variant
     Dim swSketchSeg As SldWorks.SketchSegment
     Dim swSketchCurrLine As SldWorks.SketchLine
     Dim swSketchLineArr( As SldWorks.SketchLine
     ReDim swSketchLineArr(0)
    vSketchSegArr = swSketch.GetSketchSegments
    If Not IsEmpty(vSketchSegArr) Then
         For Each vSketchSeg In vSketchSegArr
             Set swSketchSeg = vSketchSeg
             If swSketchLINE = swSketchSeg.GetType Then
                 Set swSketchCurrLine = swSketchSeg
                 Set swSketchLineArr(UBound(swSketchLineArr)) = swSketchCurrLine
                 ReDim Preserve swSketchLineArr(UBound(swSketchLineArr) + 1)
             End If
         Next
     End If
    If 0 = UBound(swSketchLineArr) Then
         ' No straight lines in this sketch
         GetAllSketchLines = Empty
         Exit Function
     End If
    ' Remove last, empty sketch line
     ReDim Preserve swSketchLineArr(UBound(swSketchLineArr) - 1)
     GetAllSketchLines = swSketchLineArr
End Function
Function GetSketchPoint(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch, swSketchPt As SldWorks.SketchPoint) As Boolean
    Dim vSketchPtArr                    As Variant
     vSketchPtArr = swSketch.GetSketchPoints2
     If Not IsEmpty(vSketchPtArr) Then
         ' Use first point
         Set swSketchPt = vSketchPtArr(0)
         GetSketchPoint = True
         Exit Function
     End If
     GetSketchPoint = False
End Function
Function FindVerticalOrigin(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch, swSketchSegVert As SldWorks.SketchSegment, swSketchPtVert As SldWorks.SketchPoint) As Boolean
    Dim vSketchLineArr As Variant
     Dim vSketchLine As Variant
     Dim swSketchCurrLine As SldWorks.SketchLine
     Dim swStartPt As SldWorks.SketchPoint
     Dim swEndPt As SldWorks.SketchPoint
    ' Get first vertical line
     vSketchLineArr = GetAllSketchLines(swApp, swModel, swSketch)
    If Not IsEmpty(vSketchLineArr) Then
         For Each vSketchLine In vSketchLineArr
             Set swSketchCurrLine = vSketchLine
             Set swStartPt = swSketchCurrLine.GetStartPoint2
             Set swEndPt = swSketchCurrLine.GetEndPoint2
            If Abs(swStartPt.X - swEndPt.X) < nTolerance Then
                 Set swSketchSegVert = swSketchCurrLine
                 FindVerticalOrigin = True
                 Exit Function
             End If
         Next
     End If
    ' Get first point
     FindVerticalOrigin = GetSketchPoint(swApp, swModel, swSketch, swSketchPtVert)
End Function
Function FindHorizontalOrigin(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch, swSketchSegHoriz As SldWorks.SketchSegment, swSketchPtHoriz As SldWorks.SketchPoint) As Boolean
    Dim vSketchLineArr As Variant
     Dim vSketchLine As Variant
     Dim swSketchCurrLine As SldWorks.SketchLine
     Dim swStartPt As SldWorks.SketchPoint
     Dim swEndPt As SldWorks.SketchPoint
    ' Get first horizontal line
     vSketchLineArr = GetAllSketchLines(swApp, swModel, swSketch)
    If Not IsEmpty(vSketchLineArr) Then
         For Each vSketchLine In vSketchLineArr
             Set swSketchCurrLine = vSketchLine
             Set swStartPt = swSketchCurrLine.GetStartPoint2
             Set swEndPt = swSketchCurrLine.GetEndPoint2
            If Abs(swStartPt.Y - swEndPt.Y) < nTolerance Then
                 Set swSketchSegHoriz = swSketchCurrLine
                 FindHorizontalOrigin = True
                 Exit Function
             End If
         Next
     End If
    ' Get first point
     FindHorizontalOrigin = GetSketchPoint(swApp, swModel, swSketch, swSketchPtHoriz)
End Function
Function AutoDimensionSketch(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSketch As SldWorks.Sketch, swSelData As SldWorks.SelectData) As Long
    Dim swFeat As SldWorks.Feature
     Dim swSketchSegHoriz As SldWorks.SketchSegment
     Dim swSketchPtHoriz As SldWorks.SketchPoint
     Dim swSketchSegVert As SldWorks.SketchSegment
     Dim swSketchPtVert As SldWorks.SketchPoint
     Dim bRet As Boolean
    If False = FindHorizontalOrigin(swApp, swModel, swSketch, swSketchSegHoriz, swSketchPtHoriz) Then
         AutoDimensionSketch = swAutodimStatusDatumLineNotHorizontal
         Exit Function
     End If
    If False = FindVerticalOrigin(swApp, swModel, swSketch, swSketchSegVert, swSketchPtVert) Then
         AutoDimensionSketch = swAutodimStatusDatumLineNotVertical
         Exit Function
     End If
    Set swFeat = swSketch
    bRet = swFeat.Select2(False, 0)
    ' Editing sketch clears selections
     swModel.EditSketch
    ' Reselect sketch segments with correct marks for auto-dimensioning
     If Not swSketchSegVert Is Nothing Then
         ' Vertical line is for horizontal datum
         bRet = swSketchSegVert.Select4(True, swSelData)
     ElseIf Not swSketchPtHoriz Is Nothing Then
             bRet = swSketchPtHoriz.Select4(True, swSelData)
     ElseIf Not swSketchPtVert Is Nothing Then
             ' Use any sketch point for horizontal datum
             bRet = swSketchPtVert.Select4(True, swSelData)
     End If
    If Not swSketchSegHoriz Is Nothing Then
         ' Horizontal line is for vertical datum
         bRet = swSketchSegHoriz.Select4(True, swSelData)
     ElseIf Not swSketchPtVert Is Nothing Then
         bRet = swSketchPtVert.Select4(True, swSelData)
     ElseIf Not swSketchPtHoriz Is Nothing Then
             ' Use any sketch point for vertical datum
             bRet = swSketchPtHoriz.Select4(True, swSelData)
     End If
    ' No straight lines, probably contains circles
     ' so use sketch points for datums
     If IsEmpty(GetAllSketchLines(swApp, swModel, swSketch)) Then
         If Not swSketchPtHoriz Is Nothing Then
             bRet = swSketchPtHoriz.Select4(False, swSelData)
         ElseIf Not swSketchPtVert Is Nothing Then
             bRet = swSketchPtVert.Select4(False, swSelData)
         End If
     End If
    Set swSketchMgr = swModel.SketchManager
     nRetVal = swSketchMgr.FullyDefineSketch(True, True, swSketchFullyDefineRelationType_e.swSketchFullyDefineRelationType_Vertical Or swSketchFullyDefineRelationType_e.swSketchFullyDefineRelationType_Horizontal, True, 1, Nothing, 1, Nothing, 1, 1)

    ' Redraw so dimensions are displayed immediately
     Dim rect() As Double
     swModelView.GraphicsRedraw (rect)

End Function
```
