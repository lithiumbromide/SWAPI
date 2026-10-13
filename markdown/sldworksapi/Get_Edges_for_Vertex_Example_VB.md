---
title: "Get Edges for Vertex Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Edges_for_Vertex_Example_VB.htm"
---

# Get Edges for Vertex Example (VBA)

This example shows how to get a list of the edges that meet at the selected vertex.

```
'-----------------------------------------------------
' Preconditions: Open a part and select a vertex.
'
' Postconditions:
' 1. Selects all edges that meet at the selected vertex.
' 2. Examine the graphics area.
'-----------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swVert As SldWorks.Vertex
    Dim vEdgeArr As Variant
    Dim vEdge As Variant
    Dim swEdge As SldWorks.Edge
    Dim swEnt As SldWorks.Entity
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swVert = swSelMgr.GetSelectedObject6(1, -1)
```

```
    swModel.ClearSelection2 True
```

```
    vEdgeArr = swVert.GetEdges
    For Each vEdge In vEdgeArr
        Set swEdge = vEdge
        Set swEnt = swEdge
        bRet = swEnt.Select4(True, Nothing)
    Next vEdge
```

```
End Sub
```
