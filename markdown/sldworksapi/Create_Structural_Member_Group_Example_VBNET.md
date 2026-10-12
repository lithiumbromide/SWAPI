---
title: "Create a Structural-Member Group Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Structural_Member_Group_Example_VBNET.htm"
---

# Create a Structural-Member Group Example (VB.NET)

This example shows how to create structural-member groups for weldment features.

```vb
' ----------------------------------------------------------------------
 ' Preconditions:
 ' 1. Ensure that the specified weldment profile and path exist.
 ' 2. If necessary, modify the path in both calls to
 '    InsertStructuralWeldment3.
 '
 ' Postconditions:
 ' 1. Two structural-member features are created.
 ' 2. Each feature consists of one structural-member group of two
 '    sketch segments.
 ' 3. Inspect the Immediate Window for information.
 '----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Partial Class SolidWorksMacro
    Dim Part As ModelDoc2
    Dim boolstatus As Boolean
    Dim FeatMgr As FeatureManager
    Dim SelMgr As SelectionMgr
    Dim swWeldFeat As Feature
    Dim swWeldFeatData As StructuralMemberFeatureData

    Public Sub Main()
        Dim MacroFolder As String
        MacroFolder = swApp.GetCurrentMacroPathFolder()
        swApp.SetCurrentWorkingDirectory(MacroFolder)
        Dim Template As String
        Template = swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swDefaultTemplatePart)
        Part = swApp.NewDocument(Template, 0, 0, 0)
        FeatMgr = Part.FeatureManager
        SelMgr = Part.SelectionManager
        Part.ClearSelection2(True)
        Dim vSkLines As Object
        vSkLines = Part.SketchManager.CreateCornerRectangle(-0.1872393706766, 0.1133237194389, 0, -0.07003610048208, 0.009188409684237, 0)
        Part.ClearSelection2(True)
        vSkLines = Part.SketchManager.CreateCornerRectangle(0.06513561531715, 0.03369083550887, 0, 0.1807053904567, -0.08106219210316, 0)
        Part.ClearSelection2(True)
        Part.SketchManager.InsertSketch(True)
        Part.ViewZoomtofit2()
        Dim myFeature As Feature
        myFeature = Part.FeatureManager.InsertWeldmentFeature()
        Dim Group1 As StructuralMemberGroup
        Group1 = FeatMgr.CreateStructuralMemberGroup
        Dim segments1(1) As SketchSegment
        Dim GroupArray1(0) As StructuralMemberGroup
        boolstatus = Part.Extension.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.1495427140733, 0.1133237194389, 0, False, 0, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", -0.1872393706766, 0.08238014634844, 0, True, 0, Nothing, 0)
        segments1(0) = SelMgr.GetSelectedObject6(1, 0)
        segments1(1) = SelMgr.GetSelectedObject6(2, 0)
        Group1.Segments = segments1
        GroupArray1(0) = Group1
        myFeature = Part.FeatureManager.InsertStructuralWeldment3("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\weldment profiles\ansi inch\c channel\3 x 5.sldlfp", 1, 0, False, GroupArray1)
        Part.ClearSelection2(True)
        Dim Group2 As StructuralMemberGroup
        Group2 = FeatMgr.CreateStructuralMemberGroup
        Dim segments2(1) As SketchSegment
        Dim GroupArray2(0) As StructuralMemberGroup
        boolstatus = Part.Extension.SelectByID2("Line5@Sketch1", "EXTSKETCHSEGMENT", 0.1185825251083, 0.03369083550887, 0, False, 0, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("Line6@Sketch1", "EXTSKETCHSEGMENT", 0.06513561531715, -0.02774616865332, 0, True, 0, Nothing, 0)
        segments2(0) = SelMgr.GetSelectedObject6(1, 0)
        segments2(1) = SelMgr.GetSelectedObject6(2, 0)
        Group2.Segments = segments2
        GroupArray2(0) = Group2
        myFeature = Part.FeatureManager.InsertStructuralWeldment3("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\weldment profiles\ansi inch\c channel\3 x 5.sldlfp", 1, 0, False, GroupArray2)
        Part.ClearSelection2(True)
        ' Get Group Information
        Dim Group As StructuralMemberGroup
        Dim vGroups As Object
        Dim vSegments As Object
        boolstatus = Part.Extension.SelectByID2("Structural Member1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swWeldFeat = SelMgr.GetSelectedObject6(1, 0)
        swWeldFeatData = swWeldFeat.GetDefinition
        swWeldFeatData.AccessSelections(Part, Nothing)
        Debug.Print("")
        Debug.Print("Groups Count : " & swWeldFeatData.GetGroupsCount)
        Debug.Print(" Feature Name : " & swWeldFeat.Name)
        vGroups = swWeldFeatData.Groups
        Dim i As Long, j As Long
        For i = LBound(vGroups) To UBound(vGroups)
            Group = vGroups(i)
            Debug.Print(" Segment Count in Group " & i + 1 & "  : " & Group.GetSegmentsCount)
            Debug.Print(" Rotational angle for group: " + Group.Angle.ToString())
            vSegments = Group.Segments
            For j = LBound(vSegments) To UBound(vSegments)
                vSegments(j).Select(False)
            Next j
        Next i
        swWeldFeatData.ReleaseSelectionAccess()
        boolstatus = Part.Extension.SelectByID2("Structural Member2", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swWeldFeat = SelMgr.GetSelectedObject6(1, 0)
        swWeldFeatData = swWeldFeat.GetDefinition
        swWeldFeatData.AccessSelections(Part, Nothing)
        Debug.Print("")
        Debug.Print("Groups Count : " & swWeldFeatData.GetGroupsCount)
        Debug.Print(" Feature Name : " & swWeldFeat.Name)
        vGroups = swWeldFeatData.Groups
        For i = LBound(vGroups) To UBound(vGroups)
            Group = vGroups(i)
            Debug.Print(" Segment Count in Group " & i + 1 & "  : " & Group.GetSegmentsCount)
            Debug.Print(" Rotational angle for group: " + Group.Angle.ToString())
            vSegments = Group.Segments
            For j = LBound(vSegments) To UBound(vSegments)
                vSegments(j).Select(False)
            Next j
        Next i
        swWeldFeatData.ReleaseSelectionAccess()
    End Sub

    Public swApp As SldWorks
End Class
```
