---
title: "Select Edges of All Holes on Face Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Edges_of_All_Holes_on_Face_Example_VB.htm"
---

# Select Edges of All Holes on Face Example (VBA)

This example shows how to select the edges on all circular holes on a face.

**NOTE:** A circular hole can be defined in a many ways; for example, a circle inside an extruded sketch or a circle that is part of a cut-extrude feature. Thus, there is no ready way to detect a hole solely based on the feature information. However, by directly examining the geometry and topology of the model, it is possible to deduce holes. This code uses many of the geometry- and topology-related objects and methods to traverse a face and look for circular holes.

```
'------------------------------------------------------------------
' Preconditions: Verify that the specified part to open exists.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Changes the view orientation to Back.
' 3. Selects a face.
' 4. Examines the geometry and topology of the selected face and
'    identifies the holes in the face.
' 5. Deselects the face.
' 6. Selects all edges of all circular holes on the face.
' 7. Examine the graphics area.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'------------------------------------------------------------------
Option Explicit
```

```
Function GetFaceNormalAtMidCoEdge(swCoEdge As SldWorks.CoEdge) As Variant
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
    ' Get the face of the given coedge
    ' Check for the sense of the face
    Set swLoop = swCoEdge.GetLoop
    Set swFace = swLoop.GetFace
    Set swSurface = swFace.GetSurface
    bFaceSenseReversed = swFace.FaceInSurfaceSense
    varParams = swSurface.EvaluateAtPoint(varPoint(0), varPoint(1), varPoint(2))
```

```
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
```

```
    GetFaceNormalAtMidCoEdge = dblNormal
```

```
End Function
```

```
Function GetTangentAtMidCoEdge(swCoEdge As SldWorks.CoEdge) As Variant
    Dim varParams As Variant
    Dim dblMidParam As Double
    Dim dblTangent(2) As Double
```

```
    varParams = swCoEdge.GetCurveParams
    If varParams(6) > varParams(7) Then
        dblMidParam = (varParams(6) - varParams(7)) / 2# + varParams(7)
    Else
        dblMidParam = (varParams(7) - varParams(6)) / 2# + varParams(6)
    End If
```

```
    varParams = swCoEdge.Evaluate(dblMidParam)
    dblTangent(0) = varParams(3)
    dblTangent(1) = varParams(4)
    dblTangent(2) = varParams(5)
    GetTangentAtMidCoEdge = dblTangent
```

```
End Function
```

```
Function GetCrossProduct(varVec1 As Variant, varVec2 As Variant) As Variant
    Dim dblCross(2) As Double
```

```
    dblCross(0) = varVec1(1) * varVec2(2) - varVec1(2) * varVec2(1)
    dblCross(1) = varVec1(2) * varVec2(0) - varVec1(0) * varVec2(2)
    dblCross(2) = varVec1(0) * varVec2(1) - varVec1(1) * varVec2(0)
    GetCrossProduct = dblCross
```

```
End Function
```

```
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
    ' Compare within a tolerance
    If dblDot < 0.0000000001 Then '1.0e-10
        VectorsAreEqual = True
    Else
        VectorsAreEqual = False
    End If
```

```
End Function
```

```
Sub SelectHoleEdges(swFace As SldWorks.Face2, swSelData As SldWorks.SelectData)
    Dim swThisLoop As SldWorks.Loop2
    Dim swThisCoEdge As SldWorks.CoEdge
    Dim swPartnerCoEdge  As SldWorks.CoEdge
    Dim swEntity As SldWorks.Entity
    Dim varThisNormal As Variant
    Dim varPartnerNormal As Variant
    Dim varCrossProduct As Variant
    Dim varTangent As Variant
    Dim vEdgeArr As Variant
    Dim swEdge As SldWorks.Edge
    Dim swCurve As SldWorks.Curve
    Dim bRet As Boolean
```

```
    Set swThisLoop = swFace.GetFirstLoop
    Do While Not swThisLoop Is Nothing
        ' Hole is inner loop
        ' Circular or elliptical hole has only one edge
        If swThisLoop.IsOuter = False And 1 = swThisLoop.GetEdgeCount Then
            Set swThisCoEdge = swThisLoop.GetFirstCoEdge
            Set swPartnerCoEdge = swThisCoEdge.GetPartner
            varThisNormal = GetFaceNormalAtMidCoEdge(swThisCoEdge)
            varPartnerNormal = GetFaceNormalAtMidCoEdge(swPartnerCoEdge)
            If Not VectorsAreEqual(varThisNormal, varPartnerNormal) Then
                ' There is a sufficient change between the two faces to determine
                ' what kind of transition is being made
                varCrossProduct = GetCrossProduct(varThisNormal, varPartnerNormal)
                varTangent = GetTangentAtMidCoEdge(swThisCoEdge)
                If VectorsAreEqual(varCrossProduct, varTangent) Then
                    ' Hole
                    vEdgeArr = swThisLoop.GetEdges
                    Debug.Assert 0 = UBound(vEdgeArr)
                    Set swEdge = vEdgeArr(0)
                    Set swCurve = swEdge.GetCurve
                    ' Ignore elliptical holes
                    If swCurve.IsCircle Then
                        Set swEntity = swEdge
                        bRet = swEntity.Select4(True, swSelData)
                        Debug.Assert bRet
                    End If
                End If
            End If
        End If
```

```
        ' Move on to the next
        Set swThisLoop = swThisLoop.GetNext
```

```
    Loop
```

```
End Sub
```

```
Sub main()
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelData As SldWorks.SelectData
    Dim swFace As SldWorks.Face2
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\gear- caddy.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    swModel.ShowNamedView2 "*Back", 2
    Set swModelDocExt = swModel.Extension
    bRet = swModelDocExt.SelectByID2("", "FACE", 2.90197084065686E-02, 1.11645373580202E-02, 0, False, 0, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
    Set swFace = swSelMgr.GetSelectedObject6(1, -1)
    Set swSelData = swSelMgr.CreateSelectData
```

```
    swModel.ClearSelection2 True
```

```
    SelectHoleEdges swFace, swSelData
```

```
End Sub
```
