---
title: "Determine Type of Face Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Determine_Type_of_Face_Example_VB.htm"
---

# Determine Type of Face Example (VBA)

This example shows how to identify holes, bosses, and tangent faces on a selected face.

**NOTE:** To determine the type of face, start from a selected face and use IFace2::GetFirstLoop to get the first loop in the face. For every loop on the face (use ILoop2::GetNext), if the loop is not the outer loop (ILoop2::IsOuter equals false), then get the coedge for this loop and the partner coedge for the coedge.

For each coedge, get the face normal at the middle of the coedge. This is found by obtaining the middle of the coedge with a call to ICoEdge::GetCurveParams, and a call to ICoEdge::Evaluate on the midpoint of the coedge to get the point’s coordinates.

The normal is returned by a call to ISurface::EvaluateAtPoint at the point in the middle of the coedge. If the normals for the two faces are equal, then there is a tangent face (fillet) on the selected face. If the normals are not equal, then if the cross product of the two normals is equal to the tangent of the face, there is a hole at the coedge. Otherwise, if there is a loop that is not the outer loop that does not meet any of the other conditions, it is a boss.

```
'----------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\block.sldprt.
' 2. Select either face that contains a hole.
'
' Postconditions:
' 1. Identifies the hole in the selected face
'    and displays a message box.
' 2. Click OK to close the message box.
'
' NOTE: If you run this macro and select a face
' that does not have a hole, boss, or tangent face,
' then a message box is not displayed.
'------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swDoc As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFace As SldWorks.Face2
    Dim swSelData As SldWorks.SelectData
```

```
    Set swApp = GetObject(, "SldWorks.Application")
    Set swDoc = swApp.ActiveDoc
```

```
    'Verify that a face is selected
    Set swSelMgr = swDoc.SelectionManager
    If swSelMgr.GetSelectedObjectCount <> 1 Then Exit Sub
    If swSelMgr.GetSelectedObjectType2(1) <> swSelFACES Then Exit Sub
```

```
    'Get the selected face
    Set swFace = swSelMgr.GetSelectedObject6(1, -1)
    Set swSelData = swSelMgr.CreateSelectData
```

```
    'Find the holes and bosses in the selected face
    Call FindHolesAndBosses(swFace, swSelData)
```

```
End Sub
```

```
'This subroutine locates all holes, bosses,
'and tangent faces in the selected face
Sub FindHolesAndBosses(swFace, swSelData)
    Dim swThisLoop As SldWorks.Loop2
    Dim swThisCoEdge As SldWorks.CoEdge
    Dim swPartnerFace As SldWorks.Face2
    Dim swPartnerLoop As SldWorks.Loop2
    Dim swPartnerCoEdge As SldWorks.CoEdge
    Dim swEntity As SldWorks.Entity
    Dim varThisNormal As Variant
    Dim varPartnerNormal As Variant
    Dim varCrossProduct As Variant
    Dim varTangent As Variant
```

```
    Set swThisLoop = swFace.GetFirstLoop
```

```
    'For every loop on the face
    Do While Not swThisLoop Is Nothing
        If swThisLoop.IsOuter = False Then
            Set swThisCoEdge = swThisLoop.GetFirstCoEdge
            Set swPartnerCoEdge = swThisCoEdge.GetPartner
            varThisNormal = GetFaceNormalAtMidCoEdge(swThisCoEdge)
            varPartnerNormal = GetFaceNormalAtMidCoEdge(swPartnerCoEdge)
            If VectorsAreEqual(varThisNormal, varPartnerNormal) Then
               ' The neighboring face is tangent to the
               ' selected face; additional code is necessary for
               ' determining how the surface moves away from the
               ' selected face
                Set swPartnerLoop = swPartnerCoEdge.GetLoop
                Set swPartnerFace = swPartnerLoop.GetFace
                Set swEntity = swPartnerFace
                swEntity.Select4 False, swSelData
                MsgBox "This face is tangent."
            Else
               ' There is a sufficient change between
               ' the two faces to determine the kind of transition
               ' being made
                varCrossProduct = GetCrossProduct(varThisNormal, varPartnerNormal)
                varTangent = GetTangentAtMidCoEdge(swThisCoEdge)
                If VectorsAreEqual(varCrossProduct, varTangent) Then
                    'Hole
                    Set swPartnerLoop = swPartnerCoEdge.GetLoop
                    Set swPartnerFace = swPartnerLoop.GetFace
                    Set swEntity = swPartnerFace
                    swEntity.Select4 False, swSelData
                    MsgBox "This face is a hole."
                Else
                    'Boss
                    Set swPartnerLoop = swPartnerCoEdge.GetLoop
                    Set swPartnerFace = swPartnerLoop.GetFace
                    Set swEntity = swPartnerFace
                    swEntity.Select4 False, swSelData
                    MsgBox "This face is a boss."
                End If
            End If
        End If
        Set swThisLoop = swThisLoop.GetNext
    Loop
End Sub
```

```
'This function returns the face normal from the provided coedge
Function GetFaceNormalAtMidCoEdge(swCoEdge As CoEdge) As Variant
    Dim swFace As SldWorks.Face2
    Dim swSurface As SldWorks.Surface
    Dim swLoop As SldWorks.Loop2
    Dim varParams As Variant
    Dim varPoint As Variant
    Dim dblMidParam As Double
    Dim dblNormal(2) As Double
    Dim bFaceSenseReversed As Boolean
```

```
    varParams = swCoEdge.GetCurveParams
    If varParams(6) > varParams(7) Then
        dblMidParam = (varParams(6) - varParams(7)) / 2 + varParams(7)
    Else
        dblMidParam = (varParams(7) - varParams(6)) / 2 + varParams(6)
    End If
    varPoint = swCoEdge.Evaluate(dblMidParam)
```

```
    ' Get the face of the given coedge; remember to check
    ' for the sense of the face
    Set swLoop = swCoEdge.GetLoop
    Set swFace = swLoop.GetFace
    Set swSurface = swFace.GetSurface
    bFaceSenseReversed = swFace.FaceInSurfaceSense
    varParams = swSurface.EvaluateAtPoint(varPoint(0), varPoint(1), varPoint(2))
    If bFaceSenseReversed Then
        ' Negate the surface normal as it is opposite from the face normal
        dblNormal(0) = -varParams(0)
        dblNormal(1) = -varParams(1)
        dblNormal(2) = -varParams(2)
    Else
        dblNormal(0) = varParams(0)
        dblNormal(1) = varParams(1)
        dblNormal(2) = varParams(2)
    End If
    GetFaceNormalAtMidCoEdge = dblNormal
End Function
```

```
'Get the tangent vector for the provided coedge
Function GetTangentAtMidCoEdge(swCoEdge As Variant) As Variant
    Dim varParams As Variant
    Dim dblMidParam As Double
    Dim dblTangent(2) As Double
```

```
    varParams = swCoEdge.GetCurveParams
    If varParams(6) > varParams(7) Then
        dblMidParam = (varParams(6) - varParams(7)) / 2 + varParams(7)
    Else
        dblMidParam = (varParams(7) - varParams(6)) / 2 + varParams(6)
    End If
```

```
    varParams = swCoEdge.Evaluate(dblMidParam)
    dblTangent(0) = varParams(3)
    dblTangent(1) = varParams(4)
    dblTangent(2) = varParams(5)
    GetTangentAtMidCoEdge = dblTangent
End Function
```

```
'Obtain the cross product of two vectors
Function GetCrossProduct(varVec1 As Variant, varVec2 As Variant) As Variant
    Dim dblCross(2) As Double
```

```
    dblCross(0) = varVec1(1) * varVec2(2) - varVec1(2) * varVec2(1)
    dblCross(1) = varVec1(2) * varVec2(0) - varVec1(0) * varVec2(2)
    dblCross(2) = varVec1(0) * varVec2(1) - varVec1(1) * varVec2(0)
    GetCrossProduct = dblCross
End Function
```

```
'Checks whether two vectors are equal within a tolerance of 1.0 e^-10
Function VectorsAreEqual(varVec1 As Variant, varVec2 As Variant) As Boolean
    Dim dblMag As Double
    Dim dblDot As Double
    Dim dblUnit1(2) As Double
    Dim dblUnit2(2) As Double
```

```
    dblMag = (varVec1(0) * varVec1(0) + varVec1(1) * varVec1(1) + varVec1(2) * varVec1(2)) ^ 0.5
    dblUnit1(0) = varVec1(0) / dblMag: dblUnit1(1) = varVec1(1) / dblMag: dblUnit1(2) = varVec1(2) / dblMag
    dblMag = (varVec2(0) * varVec2(0) + varVec2(1) * varVec2(1) + varVec2(2) * varVec2(2)) ^ 0.5
    dblUnit2(0) = varVec2(0) / dblMag: dblUnit2(1) = varVec2(1) / dblMag: dblUnit2(2) = varVec2(2) / dblMag
    dblDot = dblUnit1(0) * dblUnit2(0) + dblUnit1(1) * dblUnit2(1) + dblUnit1(2) * dblUnit2(2)
    dblDot = Abs(dblDot - 1#)
```

```
    If dblDot < 0.0000000001 Then '1.0e-10
        VectorsAreEqual = True
    Else
        VectorsAreEqual = False
    End If
End Function
```
