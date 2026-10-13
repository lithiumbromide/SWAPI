---
title: "Select Tangent Edges Topologically Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Tangent_Edges_Topologically_Example_VB.htm"
---

# Select Tangent Edges Topologically Example (VBA)

This example shows how to select tangent edges using IEdges::GetTangentEdges, which is a precise topological method.

**NOTE:** IEdge::GetTangentEdges does not give same results as IModelDoc2::SelectTangency, which behaves the same as if selecting tangent edges in the user interface. Because the user interface functionality automatically takes into account edges that lie on top of each other, IModelDoc2::SelectTangency is considered to be imprecise.

```
'---------------------------------------------------
' Preconditions: Open a part and select an edge
' tangent to other edges.
'
' Postconditions:
' 1. Selects the edges tangent to the selected edge.
' 2. Examine the graphics area.
'---------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelEdge As SldWorks.Edge
    Dim vTanEdgeArr As Variant
    Dim vTanEdge As Variant
    Dim swTanEdge As SldWorks.Edge
    Dim swTanEnt As SldWorks.Entity
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swSelEdge = swSelMgr.GetSelectedObject6(1, -1)
```

```
    vTanEdgeArr = swSelEdge.GetTangentEdges: If IsEmpty(vTanEdgeArr) Then Exit Sub
    For Each vTanEdge In vTanEdgeArr
        Set swTanEdge = vTanEdge
        Set swTanEnt = swTanEdge
        bRet = swTanEnt.Select4(True, Nothing): Debug.Assert bRet
    Next vTanEdge
```

```
End Sub
```
