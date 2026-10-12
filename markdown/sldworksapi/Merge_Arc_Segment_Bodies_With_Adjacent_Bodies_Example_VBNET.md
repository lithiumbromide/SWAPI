---
title: "Merge Arc Segment Bodies With Adjacent Bodies Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Merge_Arc_Segment_Bodies_With_Adjacent_Bodies_Example_VBNET.htm"
---

# Merge Arc Segment Bodies With Adjacent Bodies Example (VB.NET)

This example shows how to create structural-member groups with and without merging arc segment bodies with adjacent bodies.

```
'--------------------------------------------------------
' Preconditions:
' 1. Verify that the specified files exist:
'    * part template
'    * weldment profile
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part.
' 2. Creates a sketch of two lines and two tangent arcs.
' 3. Creates a structural-member group using an adjacent line and arc
'    and merges the arc segment's body with the line's body.
' 4. Creates another structural-member group using the other adjacent
'    line and arc and does not merge the arc segment's body with the
'    line's body.
' 5. Examine the Immediate window.
' 6. Expand Cut list(3) in the FeatureManager design tree.
' 7. Point at each PIPE, SCH 40, 12.70 DIA. and examine the
'    graphics area to verify whether that PIPE, SCH 40, 12.70
'    DIA. is merged.
'---------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swFeature As Feature
        Dim swFeatureManager As FeatureManager
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchMgr As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim swSelectionMgr As SelectionMgr
        Dim group1 As StructuralMemberGroup
        Dim group2 As StructuralMemberGroup
        Dim group As StructuralMemberGroup
        Dim swStructuralMemberFeatureData As StructuralMemberFeatureData
        Dim segmentsArray(1) As SketchSegment
        Dim status As Boolean
        Dim groups(0) As DispatchWrapper
        Dim groupArray(0) As Object
        Dim i As Integer

        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
        swFeatureManager = swModel.FeatureManager
        swModelDocExt = swModel.Extension
        swSketchMgr = swModel.SketchManager
        swSelectionMgr = swModel.SelectionManager

        'Insert weldment feature
        swFeature = swFeatureManager.InsertWeldmentFeature

        'Create sketch of two lines and two tangent arcs
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        swSketchMgr.InsertSketch(True)
        swSketchSegment = swSketchMgr.CreateLine(0.0#, 0.0#, 0.0#, -0.101812, 0.0#, 0.0#)
        swSketchSegment = swSketchMgr.CreateLine(-0.1016, -0.059455, 0.0#, 0.0#, -0.059455, 0.0#)
        swSketchSegment = swSketchMgr.CreateTangentArc(0.0#, -0.059455, 0.0#, 0.0#, 0.0#, 0.0#, 1)
        swSketchSegment = swSketchMgr.CreateTangentArc(-0.1016, -0.0#, 0.0#, -0.1016, -0.059455, 0.0#, 1)
        swModel.ClearSelection2(True)
        swSketchMgr.InsertSketch(True)
        swModel.ViewZoomtofit2()
        swModel.ShowNamedView2("*Normal To", -1)
        swModel.ClearSelection2(True)

        'Create structural-member group
        group1 = swFeatureManager.CreateStructuralMemberGroup()
        status = swModelDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.0963105065508915, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Arc1@Sketch1", "EXTSKETCHSEGMENT", 0.0072699684110568, -0.000902652809559659, 0, True, 0, Nothing, 0)
        segmentsArray(0) = swSelectionMgr.GetSelectedObject6(1, -1)
        segmentsArray(1) = swSelectionMgr.GetSelectedObject6(2, -1)
        group1.Segments = segmentsArray
        group1.ApplyCornerTreatment = True
        group1.CornerTreatmentType = 1
        group1.GapWithinGroup = 0
        group1.GapForOtherGroups = 0
        group1.Angle = 0
        group1.MergeArcSegmentBodies = True
        groupArray(0) = group1
        groups(0) = New DispatchWrapper(groupArray(0))
        swFeature = swFeatureManager.InsertStructuralWeldment5("C:\Program Files\SolidWorks Corp\SOLIDWORKS\lang\english\weldment profiles\ansi inch\pipe\0.5 sch 40.sldlfp", swConnectedSegmentsOption_e.swConnectedSegments_SimpleCut, False, (groups), "")
        swModel.ClearSelection2(True)

        'Create structura- member group
        group2 = swFeatureManager.CreateStructuralMemberGroup()
        status = swModelDocExt.SelectByID2("Arc2@Sketch1", "EXTSKETCHSEGMENT", -0.106961319560779, -0.000449372254001996, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", -0.0425304114129424, -0.059455, 0, True, 0, Nothing, 0)
        segmentsArray(0) = swSelectionMgr.GetSelectedObject6(1, -1)
        segmentsArray(1) = swSelectionMgr.GetSelectedObject6(2, -1)
        group2.Segments = segmentsArray
        group2.ApplyCornerTreatment = True
        group2.CornerTreatmentType = 1
        group2.GapWithinGroup = 0
        group2.GapForOtherGroups = 0
        group2.Angle = 0
        group2.MergeArcSegmentBodies = False
        groupArray(0) = group2
        groups(0) = New DispatchWrapper(groupArray(0))
        swFeature = swFeatureManager.InsertStructuralWeldment5("C:\Program Files\SolidWorks Corp\SOLIDWORKS\lang\english\weldment profiles\ansi inch\pipe\0.5 sch 40.sldlfp", swConnectedSegmentsOption_e.swConnectedSegments_SimpleCut, False, (groups), "")
         swModel.ClearSelection2(True)

        status = swModelDocExt.SelectByID2("pipe 0.5 sch 40(1)", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swStructuralMemberFeatureData = swFeature.GetDefinition
        swStructuralMemberFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("")
        Debug.Print("Number of groups: " & swStructuralMemberFeatureData.GetGroupsCount)
        Debug.Print(" Feature name: " & swFeature.Name)
        groupArray = swStructuralMemberFeatureData.Groups
        For i = LBound(groupArray) To UBound(groupArray)
            group = groupArray(i)
            Debug.Print(" Arc segment merged? " & group.MergeArcSegmentBodies)
        Next i
        swStructuralMemberFeatureData.ReleaseSelectionAccess()

        Debug.Print("")

        status = swModelDocExt.SelectByID2("pipe 0.5 sch 40(2)", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swStructuralMemberFeatureData = swFeature.GetDefinition
        swStructuralMemberFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("")
        Debug.Print("Number of groups: " & swStructuralMemberFeatureData.GetGroupsCount)
        Debug.Print(" Feature name: " & swFeature.Name)
        groupArray = swStructuralMemberFeatureData.Groups
        For i = LBound(groupArray) To UBound(groupArray)
            group = groupArray(i)
            Debug.Print(" Arc segment merged? " & group.MergeArcSegmentBodies)
        Next i
        swStructuralMemberFeatureData.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
