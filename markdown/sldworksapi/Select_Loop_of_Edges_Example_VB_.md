---
title: "Select Loop of Edges Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Loop_of_Edges_Example_VB_.htm"
---

# Select Loop of Edges Example (VBA)

This example shows how to use various geometry- and topology-related methods to select a set of edges that form a closed loop around a face.

```
'--------------------------------------------------------
' Preconditions:
' 1. Open a part or assembly.
' 2. Hold down the Ctrl key and select an edge and a
'    face adjacent to that edge.
'
' Postconditions:
' 1. Selects a loop of edges on the face.
' 2. Examine the graphics area.
'--------------------------------------------------------
Option Explicit
```

```
Sub SelectLoop(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swLoop As SldWorks.Loop2, swSelData As SldWorks.SelectData)
    Dim vEdgeArr As Variant
    Dim vEdge As Variant
    Dim swEdge As SldWorks.Edge
    Dim swEnt As SldWorks.Entity
    Dim bRet As Boolean
```

```
    vEdgeArr = swLoop.GetEdges
    Debug.Assert Not IsEmpty(vEdgeArr)
    For Each vEdge In vEdgeArr
        Set swEdge = vEdge
        Set swEnt = swEdge
        bRet = swEnt.Select4(True, swSelData)
    Next
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swEdge As SldWorks.Edge
    Dim swFace As SldWorks.Face2
    Dim swSelData As SldWorks.SelectData
    Dim vCoEdgeArr As Variant
    Dim vCoEdge As Variant
    Dim swCoEdge As SldWorks.CoEdge
    Dim swLoop As SldWorks.Loop2
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swEdge = swSelMgr.GetSelectedObject6(1, -1)
    Set swSelData = swSelMgr.CreateSelectData
    Set swFace = swSelMgr.GetSelectedObject6(2, -1)
    swModel.ClearSelection2 True
```

```
    vCoEdgeArr = swEdge.GetCoEdges
```

```
    ' 1 or 2: Coedges for an edge on a surface body
    ' 2: Coedges for an edge on a solid body
    Debug.Assert UBound(vCoEdgeArr) >= 0
```

```
    If 0 = UBound(vCoEdgeArr) Then
        Set swCoEdge = vCoEdgeArr(0)
        ' No ambiguity, so select
        Set swLoop = swCoEdge.GetLoop
        SelectLoop swApp, swModel, swLoop, swSelData
        Exit Sub
    End If
```

```
    ' 2: Coedges, so must have face to resolve ambiguity
    Debug.Assert Not swFace Is Nothing
```

```
    For Each vCoEdge In vCoEdgeArr
    Set swCoEdge = vCoEdge
        If swEdge Is swCoEdge.GetEdge Then
            Set swLoop = swCoEdge.GetLoop
            If swFace Is swLoop.GetFace Then
                SelectLoop swApp, swModel, swLoop, swSelData
            End If
        End If
    Next
```

```
End Sub
```
