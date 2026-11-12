---
title: "Merge Miter Trimmed Bodies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Merge_Miter_Trimmed_Bodies_Example_VB.htm"
---

# Merge Miter Trimmed Bodies Example (VBA)

This example shows how to specify to merge miter trimmed bodies in a structural-member group.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified weldment profile exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a new document containing a weldment and a structural member.
' 2. Sets to merge miter trimmed bodies in the structural-member group.
' 3. Examine the Immediate window.
'---------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swFeatMgr As SldWorks.FeatureManager
Dim swSelMgr As SldWorks.SelectionMgr
Dim swWeldFeat As SldWorks.Feature
Dim swWeldFeatData As SldWorks.StructuralMemberFeatureData
Dim swFeature As SldWorks.Feature
Dim status As Boolean
Dim template As String
Dim skLines As Variant
Dim group1 As SldWorks.StructuralMemberGroup
Dim seg1 As Variant
Dim segments1(1) As Object
Dim groups1 As Variant
Dim groupArray1(0) As Object
Dim group As SldWorks.StructuralMemberGroup
Dim groups As Variant
Dim segments As Variant
Dim i As Long
Dim j As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    template = swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swDefaultTemplatePart)
    Set swModel = swApp.NewDocument(template, 0, 0, 0)
    Set swFeatMgr = swModel.FeatureManager
    Set swSelMgr = swModel.SelectionManager
```

```
    swModel.ClearSelection2 True
```

```
    ' Create weldment and structural member
    skLines = swModel.SketchManager.CreateCornerRectangle(-0.1872393706766, 0.1133237194389, 0, -0.07003610048208, 0.009188409684237, 0)
    swModel.ClearSelection2 True
    swModel.SketchManager.InsertSketch True
    swModel.ViewZoomtofit2
    Set swFeature = swFeatMgr.InsertWeldmentFeature()
    Set group1 = swFeatMgr.CreateStructuralMemberGroup
    status = swModel.Extension.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.1495427140733, 0.1133237194389, 0, False, 0, Nothing, 0)
    status = swModel.Extension.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", -0.1872393706766, 0.08238014634844, 0, True, 0, Nothing, 0)
    Set segments1(0) = swSelMgr.GetSelectedObject6(1, 0)
    Set segments1(1) = swSelMgr.GetSelectedObject6(2, 0)
    seg1 = segments1
    group1.segments = (seg1)
    group1.Angle = 0
    group1.ApplyCornerTreatment = True
    group1.CornerTreatmentType = swSolidworksWeldmentEndCondOptions_e.swEndConditionMiter
    group1.MirrorProfile = True
    group1.MirrorProfileAxis = swMirrorProfileOrAlignmentAxis_e.swMirrorProfileOrAlignmentAxis_Vertical
    group1.GapWithinGroup = 0
    Set groupArray1(0) = group1
    groups1 = groupArray1
    Set swFeature = swFeatMgr.InsertStructuralWeldment5("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\weldment profiles\ansi inch\c channel\3 x 5.sldlfp", swConnectedSegmentsOption_e.swConnectedSegments_SimpleCut, False, (groups1), "")
    swModel.ClearSelection2 True
```

```
    ' Get and set structural-member group information
    status = swModel.Extension.SelectByID2("c channel 3 x 5(1)", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swWeldFeat = swSelMgr.GetSelectedObject6(1, 0)
    Set swWeldFeatData = swWeldFeat.GetDefinition
    swWeldFeatData.AccessSelections swModel, Nothing
    Debug.Print ""
    Debug.Print "Number of groups: " & swWeldFeatData.GetGroupsCount
    Debug.Print " Feature name: " & swWeldFeat.Name
    groups = swWeldFeatData.groups
        For i = LBound(groups) To UBound(groups)
           Set group = groups(i)
            Debug.Print " Number of segments in group " & i + 1 & ": " & group.GetSegmentsCount
            Debug.Print " Apply corner treatment? " & group.ApplyCornerTreatment
            Debug.Print " Corner treatment type (1 = swSolidworksWeldmentEndCondOptions_e.swEndconditionMiter): " & group.CornerTreatmentType
            Debug.Print " Original merge miter trimmed bodies setting: " & group.MiterMergeCondition
            If group.CornerTreatmentType = swSolidworksWeldmentEndCondOptions_e.swEndConditionMiter Then
                    group.MiterMergeCondition = True
            End If
            Debug.Print " Modified merge miter trimmed bodies setting: " & group.MiterMergeCondition
            segments = group.segments
            For j = LBound(segments) To UBound(segments)
                segments(j).Select4 False, Nothing
            Next j
        Next i
    swFeature.ModifyDefinition swWeldFeatData, swModel, Nothing
```

```
    swModel.ClearSelection2 True
```

```
End Sub
```
