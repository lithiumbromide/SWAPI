---
title: "Check for Interference Between Two Bodies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Check_Interference_Between_Two_Bodies_Example_VB.htm"
---

# Check for Interference Between Two Bodies Example (VBA)

This example shows how to check for interference between two bodies in an assembly.

```vb
 '--------------------------------------------------------------------------
 ' Preconditions:
 ' Open public_documents\samples\tutorial\api\Cube_Assem.sldasm.
 '
 ' Postconditions:
 ' 1. Gets the bodies of two components and transforms them in the
 '    context of the assembly.
 ' 2. Checks for interference between the two bodies.
 ' 3. Sketches lines around the faces involved in the interference.
 ' 4. Inspect the graphics area after selecting 3DSketch1 in the
 '    FeatureManager design tree.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '--------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
Sub main()
    Dim swModel                 As SldWorks.ModelDoc2
     Dim swComponent1            As SldWorks.Component2
     Dim swComponent2            As SldWorks.Component2
     Dim bValue                  As Boolean
     Dim swBody1                 As SldWorks.Body2
     Dim swBody2                 As SldWorks.Body2
     Dim swBodyCopy1             As SldWorks.Body2
     Dim swBodyCopy2             As SldWorks.Body2
     Dim vBodies                 As Variant
     Dim swModeler               As SldWorks.Modeler
     Dim vFaces1                 As Variant
     Dim vFaces2                 As Variant
     Dim vFace                   As Variant
     Dim swFace                  As SldWorks.Face2
     Dim vEdges                  As Variant
     Dim vEdge                   As Variant
     Dim swEdge                  As SldWorks.Edge
     Dim swVertex1               As SldWorks.Vertex
     Dim swVertex2               As SldWorks.Vertex
     Dim vPoint1                 As Variant
     Dim vPoint2                 As Variant
     Dim swTransform1            As SldWorks.MathTransform
     Dim swTransform2            As SldWorks.MathTransform
     Dim lIdx                    As Long
     Dim lNumEdges               As Long
     Dim lCoord                  As Long
     Dim lEpsilon                As Double
    lEpsilon = 0.000000001
    Set swApp = Application.SldWorks
     Set swModeler = swApp.GetModeler
     Set swModel = swApp.ActiveDoc
    swModel.ClearSelection2 True
     bValue = swModel.Extension.SelectByID2("Cube-2@Cube_Assem", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
     Set swComponent1 = swModel.SelectionManager.GetSelectedObject6(1, -1)
    bValue = swModel.Extension.SelectByID2("Cube-3@Cube_Assem", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
     Set swComponent2 = swModel.SelectionManager.GetSelectedObject6(1, -1)

    'Get transform of each component
     Set swTransform1 = swComponent1.Transform
     Set swTransform2 = swComponent2.Transform
    'Get bodies of first component
     vBodies = swComponent1.GetBodies2(swBodyType_e.swSolidBody)
    Set swBody1 = vBodies(0)
     Set swBodyCopy1 = swBody1.Copy
    'Get bodies of second component
     vBodies = swComponent2.GetBodies2(swBodyType_e.swSolidBody)
    Set swBody2 = vBodies(0)
     Set swBodyCopy2 = swBody2.Copy
    'Apply transform to move copies to their correct positions in the assembly
     bValue = swBodyCopy1.ApplyTransform(swTransform1)
     bValue = swBodyCopy2.ApplyTransform(swTransform2)
    swModel.EditRebuild3

    bValue = swModeler.CheckInterferenceBetweenTwoBodies(swBodyCopy1, swBodyCopy2, False, vFaces1, vFaces2, vBodies)

    'Display edges of faces interfering in first body
     If (Not IsEmpty(vFaces1)) Then
        swModel.SetAddToDB True
         swModel.Insert3DSketch2 False
        For Each vFace In vFaces1
            Set swFace = vFace
             vEdges = swFace.GetEdges
            lNumEdges = (UBound(vEdges) - LBound(vEdges) + 1)
            For lIdx = 0 To (lNumEdges - 1)
                Set swEdge = vEdges(lIdx)
                 Set swVertex1 = swEdge.GetStartVertex
                 Set swVertex2 = swEdge.GetEndVertex
                vPoint1 = swVertex1.GetPoint
                 vPoint2 = swVertex2.GetPoint
                For lCoord = 0 To 2
                    If (Abs(vPoint1(lCoord)) < lEpsilon) Then
                         vPoint1(lCoord) = 0#
                     End If
                    If (Abs(vPoint2(lCoord)) < lEpsilon) Then
                         vPoint2(lCoord) = 0#
                     End If
                Next lCoord
                swModel.CreateLine2 vPoint1(0), vPoint1(1), vPoint1(2), vPoint2(0), vPoint2(1), vPoint2(2)
            Next lIdx
        Next vFace
        swModel.Insert3DSketch2 True
         swModel.SetAddToDB False
    End If
    'Display edges of faces interfering in second body
     If (Not IsEmpty(vFaces2)) Then
        swModel.SetAddToDB True
         swModel.Insert3DSketch2 False
        For Each vFace In vFaces2
            Set swFace = vFace
             vEdges = swFace.GetEdges
            lNumEdges = (UBound(vEdges) - LBound(vEdges) + 1)
            For lIdx = 0 To (lNumEdges - 1)
                Set swEdge = vEdges(lIdx)
                 Set swVertex1 = swEdge.GetStartVertex
                 Set swVertex2 = swEdge.GetEndVertex
                vPoint1 = swVertex1.GetPoint
                 vPoint2 = swVertex2.GetPoint
                For lCoord = 0 To 2
                    If (Abs(vPoint1(lCoord)) < lEpsilon) Then
                         vPoint1(lCoord) = 0#
                     End If
                    If (Abs(vPoint2(lCoord)) < lEpsilon) Then
                         vPoint2(lCoord) = 0#
                     End If
                Next lCoord
                swModel.CreateLine2 vPoint1(0), vPoint1(1), vPoint1(2), vPoint2(0), vPoint2(1), vPoint2(2)
            Next lIdx
        Next vFace
        swModel.Insert3DSketch2 True
         swModel.SetAddToDB False
    End If
End Sub
```
