---
title: "Merge Arc Segment Bodies With Adjacent Bodies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Merge_Arc_Segment_Bodies_With_Adjacent_Bodies_Example_VB.htm"
---

# Merge Arc Segment Bodies With Adjacent Bodies Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swFeature As SldWorks.Feature
Dim swFeatureManager As SldWorks.FeatureManager
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchMgr As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim group1 As SldWorks.StructuralMemberGroup
Dim group2 As SldWorks.StructuralMemberGroup
Dim group As SldWorks.StructuralMemberGroup
Dim swStructuralMemberFeatureData As SldWorks.StructuralMemberFeatureData
Dim segmentsArray(1) As SldWorks.SketchSegment
Dim status As Boolean
Dim groups As Variant
Dim groupArray(0) As Object
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
    Set swFeatureManager = swModel.FeatureManager
    Set swModelDocExt = swModel.Extension
    Set swSketchMgr = swModel.SketchManager
    Set swSelectionMgr = swModel.SelectionManager
```

```
    'Insert weldment feature
    Set swFeature = swFeatureManager.InsertWeldmentFeature
```

```
    'Create sketch of two lines and two tangent arcs
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
    swSketchMgr.InsertSketch True
    Set swSketchSegment = swSketchMgr.CreateLine(0#, 0#, 0#, -0.101812, 0#, 0#)
    Set swSketchSegment = swSketchMgr.CreateLine(-0.1016, -0.059455, 0#, 0#, -0.059455, 0#)
    Set swSketchSegment = swSketchMgr.CreateTangentArc(0#, -0.059455, 0#, 0#, 0#, 0#, 1)
    Set swSketchSegment = swSketchMgr.CreateTangentArc(-0.1016, -0#, 0#, -0.1016, -0.059455, 0#, 1)
    swModel.ClearSelection2 True
    swSketchMgr.InsertSketch True
    swModel.ViewZoomtofit2
    swModel.ShowNamedView2 "*Normal To", -1
    swModel.ClearSelection2 True
```

```
    'Create structural-member group
    Set group1 = swFeatureManager.CreateStructuralMemberGroup()
    status = swModelDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -9.63105065508915E-02, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Arc1@Sketch1", "EXTSKETCHSEGMENT", 7.2699684110568E-03, -9.02652809559659E-04, 0, True, 0, Nothing, 0)
    Set segmentsArray(0) = swSelectionMgr.GetSelectedObject6(1, -1)
    Set segmentsArray(1) = swSelectionMgr.GetSelectedObject6(2, -1)
    group1.segments = segmentsArray
    group1.ApplyCornerTreatment = True
    group1.CornerTreatmentType = 1
    group1.GapWithinGroup = 0
    group1.GapForOtherGroups = 0
    group1.Angle = 0
    group1.MergeArcSegmentBodies = True
    Set groupArray(0) = group1
    groups = groupArray
    Set swFeature = swFeatureManager.InsertStructuralWeldment5("C:\Program Files\SolidWorks Corp\SOLIDWORKS\lang\english\weldment profiles\ansi inch\pipe\0.5 sch 40.sldlfp", swConnectedSegmentsOption_e.swConnectedSegments_SimpleCut, False, (groups), "")
    swModel.ClearSelection2 True
```

```
    'Create structural-member group
    Set group2 = swFeatureManager.CreateStructuralMemberGroup()
    status = swModelDocExt.SelectByID2("Arc2@Sketch1", "EXTSKETCHSEGMENT", -0.106961319560779, -4.49372254001996E-04, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", -4.25304114129424E-02, -0.059455, 0, True, 0, Nothing, 0)
    Set segmentsArray(0) = swSelectionMgr.GetSelectedObject6(1, -1)
    Set segmentsArray(1) = swSelectionMgr.GetSelectedObject6(2, -1)
    group2.segments = segmentsArray
    group2.ApplyCornerTreatment = True
    group2.CornerTreatmentType = 1
    group2.GapWithinGroup = 0
    group2.GapForOtherGroups = 0
    group2.Angle = 0
    group2.MergeArcSegmentBodies = False
    Set groupArray(0) = group2
    groups = groupArray
    Set swFeature = swFeatureManager.InsertStructuralWeldment5("C:\Program Files\SolidWorks Corp\SOLIDWORKS\lang\english\weldment profiles\ansi inch\pipe\0.5 sch 40.sldlfp", swConnectedSegmentsOption_e.swConnectedSegments_SimpleCut, False, (groups), "")
    swModel.ClearSelection2 True
```

```
    status = swModelDocExt.SelectByID2("pipe 0.5 sch 40(1)", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swStructuralMemberFeatureData = swFeature.GetDefinition
    swStructuralMemberFeatureData.AccessSelections swModel, Nothing
    Debug.Print ""
    Debug.Print "Number of groups: " & swStructuralMemberFeatureData.GetGroupsCount
    Debug.Print " Feature name: " & swFeature.Name
    groups = swStructuralMemberFeatureData.groups
        For i = LBound(groups) To UBound(groups)
           Set group = groups(i)
            Debug.Print (" Arc segment merged? " & group.MergeArcSegmentBodies)
         Next i
    swStructuralMemberFeatureData.ReleaseSelectionAccess
```

```
    Debug.Print ""
```

```
    status = swModelDocExt.SelectByID2("pipe 0.5 sch 40(2)", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swStructuralMemberFeatureData = swFeature.GetDefinition
    swStructuralMemberFeatureData.AccessSelections swModel, Nothing
    Debug.Print ""
    Debug.Print "Number of groups: " & swStructuralMemberFeatureData.GetGroupsCount
    Debug.Print " Feature name: " & swFeature.Name
    groups = swStructuralMemberFeatureData.groups
        For i = LBound(groups) To UBound(groups)
           Set group = groups(i)
            Debug.Print (" Arc segment merged? " & group.MergeArcSegmentBodies)
         Next i
    swStructuralMemberFeatureData.ReleaseSelectionAccess
```

```
End Sub
```
