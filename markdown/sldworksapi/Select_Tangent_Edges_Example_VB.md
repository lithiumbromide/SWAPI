---
title: "Select Tangent Edges via Iteration Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Tangent_Edges_Example_VB.htm"
---

# Select Tangent Edges via Iteration Example (VBA)

This example shows how to select tangent edges by iterating through an edge’s coedges and selecting all edges with tangent vectors.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open a part, assembly, or drawing document.
' 2. Select an edge tangent to other edges in the model.
'
' Postconditions:
' 1. Selects all edges tangent to the selected edge.
' 2. Examine the graphics area.
'------------------------------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swDoc As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swEdge As SldWorks.Edge
Dim swSelData As SldWorks.SelectData
```

```
Sub main()
```

```
    ' Access the running SOLIDWORKS Design application
    Set swApp = GetObject(, "SldWorks.Application")
    If swApp Is Nothing Then Exit Sub
```

```
    ' Get the active model
    Set swDoc = swApp.ActiveDoc
    If swDoc Is Nothing Then Exit Sub
```

```
    ' Get the SelectionMgr object and make sure that the selected object is an edge
    Set swSelMgr = swDoc.SelectionManager
    If swSelMgr.GetSelectedObjectCount <> 1 Then Exit Sub
    If swSelMgr.GetSelectedObjectType2(1) <> swSelEDGES Then Exit Sub
    Set swSelData = swSelMgr.CreateSelectData
```

```
    ' Get a pointer to the selected edge
    Set swEdge = swSelMgr.GetSelectedObject6(1, -1)
```

```
    ' Select all edges that are tangent to the selected edge
    Call SelectTangentEdges(swEdge)
```

```
End Sub
```

```
Sub SelectTangentEdges(swEdge As Edge)
    Dim varCoEdges As Variant           ' Coedges for edge
    Dim swCoEdge As SldWorks.CoEdge     ' Holds the current coedge
    Dim bUseStart As Boolean            ' Gets whether the coedge is in
                                        ' the same direction as edge
                                        ' Determines where to evaluate the edge from
    Dim varTangent As Variant           ' The tangent to edge
```

```
    ' Get all of the coedges for this edge
    varCoEdges = swEdge.GetCoEdges
```

```
    ' If this edge does not have exactly two coedges, then quit
    If UBound(varCoEdges) <> 1 Then Exit Sub
```

```
    ' For the first coedge
    Set swCoEdge = varCoEdges(0)
```

```
    ' Depends on whether the coedge and edge have the same direction
    bUseStart = swCoEdge.GetSense
    If bUseStart Then bUseStart = False Else bUseStart = True
```

```
    ' Get the tangent for this edge, bUseStart indicates from where to get tangent
    varTangent = GetEdgeTangent(swEdge, bUseStart)
```

```
    ' Recurse for all tangent edges for this edge starting with coedge
    Call TraverseTangentEdges(swEdge, swCoEdge, varTangent, swSelData)
```

```
    ' For the second coedge
    Set swCoEdge = varCoEdges(1)
```

```
    ' Depends on whether the coedge and edge have the same direction
    bUseStart = swCoEdge.GetSense
    If bUseStart Then bUseStart = False Else bUseStart = True
```

```
    ' Get the tangent for this edge, bUseStart indicates from where to get tangent
    varTangent = GetEdgeTangent(swEdge, bUseStart)
```

```
    ' Recurse for all tangent edges for this edge starting with coedge
    Call TraverseTangentEdges(swEdge, swCoEdge, varTangent, swSelData)
```

```
End Sub
```

```
' Selects all tangent edges starting at edge, and continuing out from coedge
Sub TraverseTangentEdges(swEdge As Edge, swCoEdge As CoEdge, varTangent As Variant, swSelData)
```

```
    Dim swNextCoEdge As SldWorks.CoEdge     ' Next coedge on coedge
    Dim swPartnerCoEdge As SldWorks.CoEdge  ' Partner to the coedge
    Dim swNextEdge As SldWorks.Edge         ' Next coedge
    Dim swEntity As SldWorks.Entity         ' Used to select the edge
    Dim varNextTangent As Variant           ' Holds the tangent for the next coedge
    Dim bUseNextStart As Boolean            ' Get whether the next tangent comes from the
                                            ' start of the edge or not
```

```
    ' Get the next edge
    Set swNextCoEdge = swCoEdge.GetNext
    Set swNextEdge = swNextCoEdge.GetEdge
```

```
    'While not visiting the edge started on
    Do While Not swNextEdge Is swEdge
        bUseNextStart = swNextCoEdge.GetSense
        varNextTangent = GetEdgeTangent(swNextEdge, bUseNextStart)
        If VectorsAreEqual(varTangent, varNextTangent) Then
            Set swEntity = swNextEdge
            ' Select the edge and append it to the list of selected items
            swEntity.Select4 True, swSelData
            ' Go to the next
            If bUseNextStart Then bUseNextStart = False Else bUseNextStart = True
            varNextTangent = GetEdgeTangent(swNextEdge, bUseNextStart)
            Call TraverseTangentEdges(swNextEdge, swNextCoEdge, varNextTangent, swSelData)
            Exit Sub
        Else
            ' Walk around the vertex
            Set swPartnerCoEdge = swNextCoEdge.GetPartner
            Set swNextCoEdge = swPartnerCoEdge.GetNext
            Set swNextEdge = swNextCoEdge.GetEdge
        End If
    Loop
```

```
End Sub
```

```
' Get the tangent for the current edge
Function GetEdgeTangent(swEdge As Edge, bUseStart As Boolean) As Variant
    Dim swCurve As SldWorks.Curve   ' swEdge's underlying curve
    Dim varEdgeParams As Variant    ' Curve parameters for swEdge
    Dim dblParam As Double          ' Edge parameter to evaluate
    Dim dblTangent(2) As Double     ' Tangent for swEdge
```

```
    ' Get the curve parameters for swEdge
    Set swCurve = swEdge.GetCurve
    varEdgeParams = swEdge.GetCurveParams2
```

```
    ' If the coedge has the same direction as swEdge, then evaluate from
    ' the start of the coedge; otherwise, evaluate from the end of
    ' the coedge (the start of the edge)
    If bUseStart Then
        dblParam = varEdgeParams(6)
    Else
        dblParam = varEdgeParams(7)
    End If
```

```
    ' Evaluate the edge at the start or end
    varEdgeParams = swEdge.Evaluate(dblParam)
    ' Get the tangent information out of the evaluation
    dblTangent(0) = varEdgeParams(3)
    dblTangent(1) = varEdgeParams(4)
    dblTangent(2) = varEdgeParams(5)
```

```
    'Return the tangent
    GetEdgeTangent = dblTangent
```

```
End Function
```

```
' Determines if the edges are equal within a tolerance of 1.0 * e^-10
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
```

```
    If dblDot < 0.0000000001 Then '1.0e-10
        VectorsAreEqual = True
    Else
        VectorsAreEqual = False
    End If
```

```
End Function
```
