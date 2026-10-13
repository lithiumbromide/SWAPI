---
title: "Insert Weldment Features Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weldment_Features_Example_VB.htm"
---

# Insert Weldment Features Example (VBA)

This example shows how to insert the following weldment features into the FeatureManager design tree:

* End cap feature

* Fillet bead feature

* Gusset feature

* Structural weldment

* Sub weld folder

* Weldment trim feature

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\weldments\weldment_box2.sldprt
 ' 2. Expand the Cut list folder in the FeatureManager design tree
 '    and observe its contents.
 ' 3. Delete End cap1 from the FeatureManager design tree.
 ' 4. Change the path specified for profilePathName, if necessary.
 '
 ' Postconditions: Observe the following in the FeatureManager design tree:
 '    * Gusset1 moves to Sub Folder1 in the Cut list folder
 '    * Trim/Extend8 feature appears at the bottom of the design tree
 '      and at the end of the Cut list folder
 '    * Structural Member6 feature appears at the bottom of the design tree
 '      and at the end of the Cut list folder
 '    * End cap5 feature appears at the bottom of the design tree
 '      and in the Cut list folder
 '    * Gusset5 feature appears at the bottom of the design tree
 '      and in the Cut list folder
 '    * Fillet Bead5 feature appears at the bottom of the design tree
 '      and in the Cut list folder
 '
 ' NOTE: Because this part is used elsewhere,
 ' do not save any changes when you close it.
 '----------------------------------------------------------------------------
Option Explicit
Dim swApp As Object
Dim fm As FeatureManager
Dim selMgr As SelectionMgr
Dim Part As ModelDoc2
Dim boolstatus As Boolean
Dim longstatus As Long, longwarnings As Long
Sub main()
    Dim myFeature As Object
    Dim obj(0) As Object
    Dim v As Variant
    Set swApp = Application.SldWorks

    Set Part = swApp.ActiveDoc
    Dim myModelView As Object
    Set myModelView = Part.ActiveView
    myModelView.FrameState = swWindowState_e.swWindowMaximized

    Set selMgr = Part.SelectionManager

    'InsertSubWeldFolder2

    boolstatus = Part.Extension.SelectByID2("Gusset1", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
    Set obj(0) = selMgr.GetSelectedObject6(1, -1)
    v = obj

    Set fm = Part.FeatureManager
    Set myFeature = fm.InsertSubWeldFolder2((v))

    Part.ClearSelection2 True

    'InsertWeldmentTrimFeature2

    Dim obj1(0) As Object
    Dim obj2(0) As Object

    Dim Options As Long
    Dim v1 As Variant
    Dim v2 As Variant

    boolstatus = Part.Extension.SelectByID2("Structural Member1[2]", "SOLIDBODY", 0, 0, 0, True, 2, Nothing, 0)
    boolstatus = Part.Extension.SelectByID2("Structural Member1[1]", "SOLIDBODY", 0, 0, 0, True, 1, Nothing, 0)

    Set selMgr = Part.SelectionManager
    Dim Count As Long
    Count = selMgr.GetSelectedObjectCount
    If Count = 2 Then
        Set obj1(0) = selMgr.GetSelectedObject2(1)
        v1 = obj1
        Set obj2(0) = selMgr.GetSelectedObject2(2)
        v2 = obj2
        Part.ClearSelection2 True

        Options = swWeldmentTrimExtendOption_AllowTrimmedExtensionTrim + swWeldmentTrimExtendOption_AllowTrimmingExtensionTrim + swWeldmentTrimExtendOption_CopedCut + swWeldmentTrimExtendOption_WeldGap

        Set myFeature = fm.InsertWeldmentTrimFeature2(1, Options, 0.01, (v1), (v2))
    End If

    Part.ClearSelection2 True

    'InsertFilletBeadFeature3

    Dim fbFaceObj1(0) As Object
    Dim fbFaceObj2(1) As Object

    Part.ClearSelection2 True
    boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0412896304482, 0.02548020566445, 0, True, 1, Nothing, 0)
    boolstatus = Part.Extension.SelectByID2("", "FACE", 0.09804264728081, 0.01499999999999, 8.069730266129E-04, True, 2, Nothing, 0)
    boolstatus = Part.Extension.SelectByID2("", "FACE", 0.01364526875011, 0.08738481720087, 0.01330055827532, True, 4, Nothing, 0)

    Count = selMgr.GetSelectedObjectCount

    ' Face Set 1
    Set fbFaceObj1(0) = selMgr.GetSelectedObject6(1, 1)
    ' Face Set 2
    Set fbFaceObj2(0) = selMgr.GetSelectedObject6(1, 2)
    Set fbFaceObj2(1) = selMgr.GetSelectedObject6(1, 4)

    v1 = fbFaceObj1
    v2 = fbFaceObj2

    Dim fbEdges() As Long
    ReDim fbEdges(0 To 0) As Long
    fbEdges(0) = 0

    Set myFeature = fm.InsertFilletBeadFeature3(0, 0.003, 0.003, 2, 0.003, 0.006, 0, 0.003, 0.003, 2, 0.003, 0, 1, fbEdges, 0, Nothing, v1, v2)

    Part.ClearSelection2 True

    'InsertStructuralWeldment3

    Dim errors As Long
    Dim warnings As Long
    Dim sketchSegments As Variant
    Dim profilePathName As String
    Dim structuralMember As Feature
    Dim group As StructuralMemberGroup
    Dim GroupArray2(0) As Object
    Dim vGroups2 As Variant

    errors = 0
    warnings = 0

    Set Part = swApp.ActiveDoc

    Part.ClearSelection2 True

    Part.InsertSketch2 True
    sketchSegments = Part.SketchManager.CreateCornerRectangle(0, 0, 0, 1#, 2#, 0)
    Set group = fm.CreateStructuralMemberGroup
    group.Segments = (sketchSegments)
    Set GroupArray2(0) = group
    vGroups2 = GroupArray2

    Part.ViewZoomtofit2
    Part.InsertSketch2 True

    profilePathName = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\weldment profiles\ansi inch\s section\5 X 10.SLDLFP"

    Set structuralMember = fm.InsertStructuralWeldment3(profilePathName, swSolidworksWeldmentEndCondOptions_e.swEndConditionButt1, 0#, False, (vGroups2))

    Part.ClearSelection2 True
    'InsertEndCapFeature

    Dim endCapFeature As Feature
    Dim y As Variant
    Dim faceECObj1(0) As Object
    Dim face As Face2

    Set selMgr = Part.SelectionManager
    boolstatus = Part.Extension.SelectByID2("", "FACE", 0.6023443450227, 0.6150000000001, -1.013201139555, True, 1, Nothing, 0)
    Set face = selMgr.GetSelectedObject6(1, -1)
    Set faceECObj1(0) = face
    y = faceECObj1
    Set endCapFeature = fm.InsertEndCapFeature2(0.005, False, True, 0.003, 0.5, 0.003, y)

    Part.ClearSelection2 True

    'InsertGussetFeature2

    Dim faceGFObj(1) As Object
    Dim z As Variant

    boolstatus = Part.Extension.SelectByID2("", "FACE", 0.02539999999988, 1.94542628561, 0.00429028534694, True, 1, Nothing, 0)
    boolstatus = Part.Extension.SelectByID2("", "FACE", 0.07780718114736, 1.9746, -0.001856983219, True, 2, Nothing, 0)

    Count = selMgr.GetSelectedObjectCount
    If Count = 2 Then
        Set faceGFObj(0) = selMgr.GetSelectedObject6(1, 1)
        Set faceGFObj(1) = selMgr.GetSelectedObject6(1, 2)
        z = faceGFObj
        Part.ClearSelection2 True

        Set myFeature = fm.InsertGussetFeature2(0.005, 0, 0, False, 0.025, 0.025, 0.015, 0.7853981633975, 0.015, True, 0.005, 0, False, False, False, z)

    End If
End Sub
```
