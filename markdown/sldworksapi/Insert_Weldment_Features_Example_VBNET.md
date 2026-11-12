---
title: "Insert Weldment Features Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weldment_Features_Example_VBNET.htm"
---

# Insert Weldment Features Example (VB.NET)

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
 ' 2. Expand the Cut list folder in the FeatureManager design tree and
 '    observe its contents.
 ' 3. Delete End cap1 from the FeatureManager design tree.
 ' 4. Change the path specified for profilePathName, if necessary.
 '
 ' Postconditions: Observe the following in the FeatureManager design tree:
 '    * Gusset1 moves to the sub weld folder, Sub Folder1, in the
 '      Cut list folder
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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Partial Class SolidWorksMacro
    Dim fm As FeatureManager
    Dim selMgr As SelectionMgr
    Dim Part As ModelDoc2
    Dim boolstatus As Boolean
    Sub main()
        Dim myFeature As Object
        Dim obj(0) As Body2
        Dim v As Array
        Part = swApp.ActiveDoc
        Dim myModelView As Object
        myModelView = Part.ActiveView
        myModelView.FrameState = swWindowState_e.swWindowMaximized
        selMgr = Part.SelectionManager
        'InsertSubWeldFolder2
        boolstatus = Part.Extension.SelectByID2("Gusset1", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
        obj(0) = selMgr.GetSelectedObject6(1, -1)
        v = obj
        fm = Part.FeatureManager
        myFeature = fm.InsertSubWeldFolder2(v)
        Part.ClearSelection2(True)
        'InsertWeldmentTrimFeature2
        Dim obj1(0) As Body2
        Dim obj2(0) As Body2
        Dim Options As Long
        Dim v1 As Array
        Dim v2 As Array
        boolstatus = Part.Extension.SelectByID2("Structural Member1[2]", "SOLIDBODY", 0, 0, 0, True, 2, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("Structural Member1[1]", "SOLIDBODY", 0, 0, 0, True, 1, Nothing, 0)
        selMgr = Part.SelectionManager
        Dim Count As Long
        Count = selMgr.GetSelectedObjectCount
        If Count = 2 Then
            obj1(0) = selMgr.GetSelectedObject2(1)
            v1 = obj1
            obj2(0) = selMgr.GetSelectedObject2(2)
            v2 = obj2
            Part.ClearSelection2(True)
            Options = swWeldmentTrimExtendOptionType_e.swWeldmentTrimExtendOption_AllowTrimmedExtensionTrim + swWeldmentTrimExtendOptionType_e.swWeldmentTrimExtendOption_AllowTrimmingExtensionTrim + swWeldmentTrimExtendOptionType_e.swWeldmentTrimExtendOption_CopedCut + swWeldmentTrimExtendOptionType_e.swWeldmentTrimExtendOption_WeldGap
            myFeature = fm.InsertWeldmentTrimFeature2(1, Options, 0.01, v1, v2)
        End If
        'InsertEndCapFeature
        Dim endCapFeature As Feature
        Dim face1(0) As Face2
        Dim x As Array
        selMgr = Part.SelectionManager
        boolstatus = Part.Extension.SelectByID2("", "FACE", 0.6023443450227, 0.6150000000001, -1.013201139555, True, 1, Nothing, 0)
        face1(0) = selMgr.GetSelectedObject6(1, -1)
        x = face1
        endCapFeature = fm.InsertEndCapFeature2(0.005, False, True, 0.003, 0.5, 0.003, x)
        Part.ClearSelection2(True)

        'InsertStructuralWeldment3

        Dim segmentObjects As Array
        Dim sketchSegments(3) As SketchSegment
        Dim profilePathName As String
        Dim structuralMember As Feature
        Dim group As StructuralMemberGroup
        Dim GroupArray1(0) As StructuralMemberGroup
        Dim i As Long

        group = fm.CreateStructuralMemberGroup
        Part = swApp.ActiveDoc
        Part.ClearSelection2(True)
        Part.InsertSketch2(True)
        segmentObjects = Part.SketchManager.CreateCornerRectangle(0, 0, 0, 1.0#, 2.0#, 0)
        For i = 0 To UBound(segmentObjects)
            sketchSegments(i) = CType(segmentObjects(i), SketchSegment)
        Next
        group.Segments = sketchSegments
        GroupArray1(0) = group
        Part.ViewZoomtofit2()
        Part.InsertSketch2(True)
        profilePathName = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\weldment profiles\ansi inch\square tube\2 x 2 x 0.25.SLDLFP"
        structuralMember = fm.InsertStructuralWeldment3(profilePathName, 1, 0.0#, False, GroupArray1)
        Part.ClearSelection2(True)
        'InsertGussetFeature2
        Dim faceGFObj(1) As Face2
        Dim z As Object
        boolstatus = Part.Extension.SelectByID2("", "FACE", 0.02539999999988, 1.94542628561, 0.00429028534694, True, 1, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("", "FACE", 0.07780718114736, 1.9746, -0.001856983219, True, 2, Nothing, 0)
        Count = selMgr.GetSelectedObjectCount
        If Count = 2 Then
            faceGFObj(0) = selMgr.GetSelectedObject6(1, 1)
            faceGFObj(1) = selMgr.GetSelectedObject6(1, 2)
            z = faceGFObj
            Part.ClearSelection2(True)
            myFeature = fm.InsertGussetFeature2(0.005, 0, 0, False, 0.025, 0.025, 0.015, 0.7853981633975, 0.015, True, 0.005, 0, False, False, False, z)
        End If
        'InsertFilletBeadFeature3
        Dim fbFaceObj1(0) As Face2
        Dim fbFaceObj2(1) As Face2
        Part.ClearSelection2(True)
        boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0412896304482, 0.02548020566445, 0, True, 1, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("", "FACE", 0.09804264728081, 0.01499999999999, 0.0008069730266129, True, 2, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("", "FACE", 0.01364526875011, 0.08738481720087, 0.01330055827532, True, 4, Nothing, 0)
        Count = selMgr.GetSelectedObjectCount
        ' Face Set 1
        fbFaceObj1(0) = selMgr.GetSelectedObject6(1, 1)
        ' Face Set 2
        fbFaceObj2(0) = selMgr.GetSelectedObject6(1, 2)
        'fbFaceObj2(0) = selMgr.GetSelectedObject6(1, 4)
        v1 = fbFaceObj1
        v2 = fbFaceObj2
        Part.ClearSelection2(True)
        Dim edges(0) As Integer
        Dim edgeArray As Array
        edges(0) = 0
        'edges(1) = 0
        edgeArray = edges
        myFeature = fm.InsertFilletBeadFeature3(0, 0.003, 0.003, 2, 0.003, 0.006, 0, 0.003, 0.003, 2, 0.003, 0, 1, edgeArray, 0, Nothing, v1, v2)
        Part.ClearSelection2(True)
    End Sub
    Public swApp As SldWorks
End Class
```
