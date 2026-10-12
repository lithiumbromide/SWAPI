---
title: "Insert Sheet Metal Edge Flange Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Sheet_Metal_Edge_Flange_Example_VB.htm"
---

# Insert Sheet Metal Edge Flange Example (VBA)

This example shows how to insert a sheet metal edge flange.

```vb
'-----------------------------------------------------
'
' Preconditions: A sheet metal part is open and the edge for
'                the flange is selected.
'
' Postconditions: An edge flange is created.
'
'------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
Sub main()
    Dim swModel          As SldWorks.ModelDoc2
    Dim bValue           As Boolean
    Dim swEdge           As SldWorks.Edge
    Dim dAngle           As Double
    Dim dLength          As Double
    Dim swFeature        As SldWorks.Feature
    Dim swEntity         As SldWorks.Entity
    Dim swSketch         As SldWorks.Sketch
    Dim vSketchSegments  As Variant
    Dim swSketchLine     As SldWorks.SketchLine
    Dim swStartPoint     As SldWorks.SketchPoint
    Dim swEndPoint       As SldWorks.SketchPoint
    Dim nOptions         As SwConst.swInsertEdgeFlangeOptions_e
    Dim dSize            As Double
    Dim dFactor1         As Double
    Dim dFactor2         As Double
    Dim aFlangeEdges(0)  As SldWorks.Edge
    Dim vFlangeEdges     As Variant
    Dim aSketchFeats(0)  As SldWorks.Sketch
    Dim vSketchFeats     As Variant

    ' Connect to SOLIDWORKS Design
    Set swApp = Application.SldWorks

    ' Get active document
    Set swModel = swApp.ActiveDoc

    '
    ' Flange parameters

    ' Set the angle.
    dAngle = (90# / 180#) * 3.1415926535897

    dLength = 0.01

    ' Position view so SelctByID2 coordinates will lead to a pick
    swModel.ShowNamedView2 "*Trimetric", -1
    swModel.ViewZoomtofit2

    ' Select edge for flange
    bValue = swModel.Extension.SelectByID2("", "EDGE", 0.007817329387943, 0.001156559535341, 0.04430115457222, False, 0, Nothing, 0)

    ' Get edge
    Set swEdge = swModel.SelectionManager.GetSelectedObject6(1, -1)

    ' Insert a sketch for an Edge Flange
    Set swFeature = swModel.InsertSketchForEdgeFlange(swEdge, dAngle, False)

    ' Select
    bValue = swFeature.Select2(False, 0)

    ' Start sketch editing
    swModel.EditSketch

    ' Get the active sketch
    Set swSketch = swModel.GetActiveSketch2

    '
    ' Add the edge to the sketch

    ' Cast edge to entity
    Set swEntity = swEdge

    ' Select edge
    bValue = swEntity.Select4(False, Nothing)

    ' Use the edge in the sketch
    bValue = swModel.SketchManager.SketchUseEdge(False)

    ' Get the created sketch line
    vSketchSegments = swSketch.GetSketchSegments

    Set swSketchLine = vSketchSegments(0)

    ' Get start and end point
    Set swStartPoint = swSketchLine.GetStartPoint2
    Set swEndPoint = swSketchLine.GetEndPoint2

    '
    ' Create additional lines to define sketch
    '

    ' Set parameters defining the sketch geometry
    dSize = swEndPoint.X - swStartPoint.X
    dFactor1 = 0.1
    dFactor2 = 1.25

    ' Add directly and do not display to speed things up
    swModel.SetAddToDB True
    swModel.SetDisplayWhenAdded False

    swModel.CreateLine2 swStartPoint.X, swStartPoint.Y, 0#, swStartPoint.X, swStartPoint.Y + dLength, 0#

    swModel.CreateLine2 swStartPoint.X, swStartPoint.Y + dLength, 0#, swStartPoint.X + dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0#

    swModel.CreateLine2 swStartPoint.X + dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0#, swEndPoint.X - dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0#

    swModel.CreateLine2 swEndPoint.X - dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0#, swEndPoint.X, swEndPoint.Y + dLength, 0#

    swModel.CreateLine2 swEndPoint.X, swEndPoint.Y, 0#, swEndPoint.X, swEndPoint.Y + dLength, 0#

    ' Reset
    swModel.SetDisplayWhenAdded True
    swModel.SetAddToDB False

    ' Commit changes made to the sketch
    swModel.InsertSketch2 True

    ' Set options
    nOptions = swInsertEdgeFlangeOptions_e.swInsertEdgeFlangeUseDefaultRadius + swInsertEdgeFlangeOptions_e.swInsertEdgeFlangeUseDefaultRelief
#If 0 Then
    ' Insert the edge flange
    Set swFeature = swModel.FeatureManager.InsertSheetMetalEdgeFlange(swEdge, swSketch, nOptions, dAngle, 0#, swFlangePositionTypes_e.swFlangePositionTypeBendOutside, dLength, swSheetMetalReliefTypes_e.swSheetMetalReliefNone, 0#, 0#, 0#, swFlangeDimTypes_e.swFlangeDimTypeInnerVirtualSharp, Nothing)

#Else

    Set aFlangeEdges(0) = swEdge
    Set aSketchFeats(0) = swSketch

    vFlangeEdges = aFlangeEdges
    vSketchFeats = aSketchFeats

    Set swFeature = swModel.FeatureManager.InsertSheetMetalEdgeFlange2((vFlangeEdges), (vSketchFeats), nOptions, dAngle, 0#, swFlangePositionTypes_e.swFlangePositionTypeBendOutside, dLength, swSheetMetalReliefTypes_e.swSheetMetalReliefNone, 0#, 0#, 0#, swFlangeDimTypes_e.swFlangeDimTypeInnerVirtualSharp, Nothing)

#End If
End Sub
```
