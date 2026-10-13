---
title: "Insert Structural Weldment Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Structural_Weldment_Example_VBNET.htm"
---

# Insert Structural Weldment Example (VB.NET)

This example shows how to create structural weldment features using structural member groups.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Verify the existence of the weldment profile pathname
'    as specified in both calls to IFeatureManager::InsertStructuralWeldment4.
' 2. Open an Immediate window.
'
' Postconditions:
' 1. Creates a new part document containing a weldment and structural members.
' 2. Rotates c channel 3 x 5(1).
' 3. Inspect the FeatureManager design tree, graphics area, and
'    Immediate window.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports System.Runtime.InteropServices

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
        Part.SketchManager.InsertSketch(True)

        Part.ViewZoomtofit2()

        Dim myFeature As Object
        myFeature = Part.FeatureManager.InsertWeldmentFeature()

        Dim Group1 As StructuralMemberGroup
        Group1 = FeatMgr.CreateStructuralMemberGroup
        Dim segments1(1) As SketchSegment
        Dim GroupArray1(0) As Object

        boolstatus = Part.Extension.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.1495427140733, 0.1133237194389, 0, False, 0, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", -0.1872393706766, 0.08238014634844, 0, True, 0, Nothing, 0)

        segments1(0) = SelMgr.GetSelectedObject6(1, 0)
        segments1(1) = SelMgr.GetSelectedObject6(2, 0)

        Group1.Segments = segments1
        Group1.Angle = 0.785714285714286 'radians
        Group1.ApplyCornerTreatment = True
        Group1.CornerTreatmentType = swSolidworksWeldmentEndCondOptions_e.swEndConditionMiter
        Group1.MirrorProfile = True
        Group1.MirrorProfileAxis = swMirrorProfileOrAlignmentAxis_e.swMirrorProfileOrAlignmentAxis_Vertical
        Group1.GapWithinGroup = 0.0127 'meters

        GroupArray1(0) = Group1
        Dim groups1(0) As DispatchWrapper
        groups1(0) = New DispatchWrapper(GroupArray1(0))

        myFeature = Part.FeatureManager.InsertStructuralWeldment4("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\weldment profiles\ansi inch\c channel\3 x 5.sldlfp", 1, False, groups1)

        Part.ClearSelection2(True)

        Dim Group2 As StructuralMemberGroup
        Group2 = FeatMgr.CreateStructuralMemberGroup
        Dim segments2(1) As SketchSegment
        Dim GroupArray2(0) As Object

        boolstatus = Part.Extension.SelectByID2("Line5@Sketch1", "EXTSKETCHSEGMENT", 0.1185825251083, 0.03369083550887, 0, False, 0, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("Line6@Sketch1", "EXTSKETCHSEGMENT", 0.06513561531715, -0.02774616865332, 0, True, 0, Nothing, 0)

        segments2(0) = SelMgr.GetSelectedObject6(1, 0)
        segments2(1) = SelMgr.GetSelectedObject6(2, 0)

        Group2.Segments = segments2
        Group2.AlignAxis = swMirrorProfileOrAlignmentAxis_e.swMirrorProfileOrAlignmentAxis_Vertical

        GroupArray2(0) = Group2
        Dim groups2(0) As DispatchWrapper
        groups2(0) = New DispatchWrapper(GroupArray2(0))

        myFeature = Part.FeatureManager.InsertStructuralWeldment4("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\weldment profiles\ansi inch\c channel\3 x 5.sldlfp", 1, False, groups2)

        Part.ClearSelection2(True)

        ' Get Group Information

        Dim Group As StructuralMemberGroup
        Dim vGroups As Object
        Dim vSegments As Object

        boolstatus = Part.Extension.SelectByID2("c channel 3 x 5(1)", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
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
            Debug.Print(" Rotational angle of group: " & Group.Angle)
            Debug.Print(" ApplyCornerTreatment: " & Group.ApplyCornerTreatment)
            Debug.Print(" CornerTreatmentType: " & Group.CornerTreatmentType)
            Debug.Print(" MirrorProfile: " & Group.MirrorProfile)
            Debug.Print(" MirrorProfileAxis: " & Group.MirrorProfileAxis)
            Debug.Print(" GapWithinGroup: " & Group.GapWithinGroup)
            vSegments = Group.Segments
            For j = LBound(vSegments) To UBound(vSegments)
                vSegments(j).Select(False)
            Next j
        Next i

        swWeldFeatData.ReleaseSelectionAccess()

        boolstatus = Part.Extension.SelectByID2("c channel 3 x 5(2)", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
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
            Debug.Print(" Rotational angle of group: " & Group.Angle)
            Debug.Print(" ApplyCornerTreatment: " & Group.ApplyCornerTreatment)
            Debug.Print(" CornerTreatmentType: " & Group.CornerTreatmentType)
            Debug.Print(" MirrorProfile: " & Group.MirrorProfile)
            Debug.Print(" MirrorProfileAxis: " & Group.MirrorProfileAxis)
            Debug.Print(" GapWithinGroup: " & Group.GapWithinGroup)
            vSegments = Group.Segments
            For j = LBound(vSegments) To UBound(vSegments)
                vSegments(j).Select(False)
            Next j
        Next i

        swWeldFeatData.ReleaseSelectionAccess()
        Part.ClearSelection2(True)

    End Sub

    Public swApp As SldWorks

End Class
```
