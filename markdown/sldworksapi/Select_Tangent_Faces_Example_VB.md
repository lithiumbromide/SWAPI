---
title: "Select Tangent Faces Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Tangent_Faces_Example_VB.htm"
---

# Select Tangent Faces Example (VBA)

This example shows how to select all faces tangent to a selected face.

1. Starting with the selected face, get the first loop in the face with IFace2::GetFirstLoop.

2. Starting with the first loop and using ILoop2::GetNext to get every loop on the face:

a. Iterate through every coedge contained in the loop using ILoop2::GetFirstCoEdge and ILoop2::GetNext.

b. Using ICoEdge::GetPartner, get the partner coedge.

c. For the current coedge and the partner coedge, get the face normal at the middle of the coedge. This is done by calling ICoEdge::Evaluate to get the middle point of the coedge, then calling ISurface::EvaluateAtPoint at the middle point on the surface that contains the coedge, and finally extracting the normal vector from the return value of ISurface::EvaluateAtPoint.

d. If the normal vectors are equal, then use the partner coedge to get the partner loop, which provides access to the partner face that can be selected.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open a part, assembly, or drawing document.
' 2. Select a face on the model.
'
' Postconditions:
' 1. Selects all faces tangent to the selected face.
' 2. Examine the graphics area.
'------------------------------------------------------------------
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
    'Get the ISelectionMgr and make sure that a face is selected
    Set swSelMgr = swDoc.SelectionManager
    If swSelMgr.GetSelectedObjectCount <> 1 Then Exit Sub
    If swSelMgr.GetSelectedObjectType2(1) <> swSelFACES Then Exit Sub
    Set swSelData = swSelMgr.CreateSelectData
```

```
    'Select all faces that are tangent to the selected face
    Set swFace = swSelMgr.GetSelectedObject6(1, -1)
```

```
    Call SelectTangentFaces(swFace, swSelData)
```

```
End Sub
```

```
'This subroutine selects all faces that are tangent to the given face
Sub SelectTangentFaces(swFace As Object, swSelData As Object)
    Dim swPartnerFace As SldWorks.Face2      'Partner face for the current face
    Dim swThisLoop As SldWorks.Loop2         'Current loop
    Dim swPartnerLoop As SldWorks.Loop2      'Partner to the current loop
    Dim swFirstCoEdge As SldWorks.CoEdge     'First coedge on a loop
    Dim swThisCoEdge As SldWorks.CoEdge      'Current coedge
    Dim swPartnerCoEdge As SldWorks.CoEdge   'Partner to the current coedge
    Dim swEntity As Entity          'Entity containing the face to be selected
    Dim varThisNormal As Variant    'Normal vector for the current face
    Dim varPartnerNormal As Variant 'Normal vector for the partner face
```

```
    Set swThisLoop = swFace.GetFirstLoop
```

```
    'For every loop on this face
    Do While Not swThisLoop Is Nothing
        'Get the first coedge of this loop
        Set swFirstCoEdge = swThisLoop.GetFirstCoEdge
        Set swThisCoEdge = swFirstCoEdge
        'Iterate through the coedges
        Do
            Set swPartnerCoEdge = swThisCoEdge.GetPartner
            'Get the normal vectors for the face, and its partner
            varThisNormal = GetFaceNormalAtMidCoEdge(swThisCoEdge)
            varPartnerNormal = GetFaceNormalAtMidCoEdge(swPartnerCoEdge)
           'If the normals are equal, then the faces are tangent
           'and the partner face should be selected
            If VectorsAreEqual(varThisNormal, varPartnerNormal) = True Then
                Set swPartnerLoop = swPartnerCoEdge.GetLoop
                Set swPartnerFace = swPartnerLoop.GetFace
                Set swEntity = swPartnerFace
                swEntity.Select4 True, swSelData
            End If
```

```
            ' Move to the next
            Set swThisCoEdge = swThisCoEdge.GetNext
            If swThisCoEdge Is swFirstCoEdge Then Exit Do
        Loop
        ' Move to the next loop
        Set swThisLoop = swThisLoop.GetNext
    Loop
End Sub
```

```
'This function returns the normal vector for the face at the provided coedge
Function GetFaceNormalAtMidCoEdge(swCoEdge As Object) As Variant
    Dim swFace As SldWorks.Face2        'Face containing swCoEdge
    Dim swSurface As SldWorks.Surface   'Surface containing swCoEdge,
                                        'used to get the normal
    Dim swLoop As SldWorks.Loop2        'Loop containing swCoEdge
    Dim varParams As Variant    'Curve parameters for swCoEdge
    Dim varPoint As Variant     'Array containing the location dblMidParam
    Dim dblMidParam As Double   'Middle of the coedge
    Dim dblNormal(2) As Double  'New vector
```

```
    varParams = swCoEdge.GetCurveParams
    'Set the evaluation point based on the coedge curve parameters
    If varParams(6) > varParams(7) Then
        dblMidParam = (varParams(6) - varParams(7)) / 2 + varParams(7)
    Else
        dblMidParam = (varParams(7) - varParams(6)) / 2 + varParams(6)
    End If
```

```
    'Get the location of the middle of the coedge
    varPoint = swCoEdge.Evaluate(dblMidParam)
```

```
    'Obtain the surface that contains swCoEdge
    Set swLoop = swCoEdge.GetLoop
    Set swFace = swLoop.GetFace
    Set swSurface = swFace.GetSurface
```

```
    'varParams contains the normal vector at the provided points (midpoint of edge)
    varParams = swSurface.EvaluateAtPoint(varPoint(0), varPoint(1), varPoint(2))
```

```
    'Build the normal vector
    dblNormal(0) = varParams(0)
    dblNormal(1) = varParams(1)
    dblNormal(2) = varParams(2)
```

```
    'Return the normal vector
    GetFaceNormalAtMidCoEdge = dblNormal
End Function
```

```
'Determines whether two vectors are equal within a tolerance of 1.0 * e^-10
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
    dblDot = Abs(Abs(dblDot) - 1#)
    If dblDot < 0.0000000001 Then '1.0e-10
        VectorsAreEqual = True
    Else
        VectorsAreEqual = False
    End If
End Function
```
