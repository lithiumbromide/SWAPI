---
title: "Get Chamfer Distances Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Chamfer_Distances_Example_VB.htm"
---

# Get Chamfer Distances Example (VBA)

This example shows how to get the distances associated with the selected chamfer.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open a part document that contains at least
'    one chamfer feature.
' 2. Select a chamfer feature.
' 3. Open the Immediate window.
'
' Postconditions: Examine the Immediate window for
' the chamfer data.
'---------------------------------------------------------------------------
```

```vb
Option Explicit
Sub main()
    ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
     Const DegPerRad         As Double = 57.3
     Dim swApp               As SldWorks.SldWorks
     Dim swModel             As SldWorks.ModelDoc2
     Dim swSelMgr            As SldWorks.SelectionMgr
     Dim swFeat              As SldWorks.Feature
     Dim swChamfer           As SldWorks.ChamferFeatureData2
     Dim swVertex            As SldWorks.Vertex
     Dim vEdgeArr            As Variant
     Dim vEdge               As Variant
     Dim swEdge              As SldWorks.Edge
     Dim vFaceArr            As Variant
     Dim vFace               As Variant
     Dim swFace              As SldWorks.Face2
     Dim vLoopArr            As Variant
     Dim vLoop               As Variant
     Dim swLoop              As SldWorks.Loop2
     Dim vLoopEdge           As Variant
     Dim vLoopEdgeArr        As Variant
     Dim swLoopEdge          As SldWorks.Edge
     Dim swEnt               As SldWorks.Entity
     Dim swSelData           As SldWorks.SelectData
     Dim i                   As Long
     Dim bRet                As Boolean
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swSelData = swSelMgr.CreateSelectData
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swChamfer = swFeat.GetDefinition
    ' Get chamfer information
     Debug.Print "File = " & swModel.GetPathName
     Debug.Print "  " & swFeat.Name
     Debug.Print "    EdgeChamferAngle          = " & swChamfer.EdgeChamferAngle * DegPerRad & " degrees"
     Debug.Print "    EqualDistance             = " & swChamfer.EqualDistance
     Debug.Print "    EdgeChamferDistance(0)    = " & swChamfer.GetEdgeChamferDistance(0) * 1000# & " mm"
     Debug.Print "    EdgeChamferDistance(1)    = " & swChamfer.GetEdgeChamferDistance(1) * 1000# & " mm"
     Debug.Print "    VertexChamferDistance(0)  = " & swChamfer.GetVertexChamferDistance(0) * 1000# & " mm"
     Debug.Print "    VertexChamferDistance(1)  = " & swChamfer.GetVertexChamferDistance(1) * 1000# & " mm"
     Debug.Print "    VertexChamferDistance(2)  = " & swChamfer.GetVertexChamferDistance(2) * 1000# & " mm"
     Debug.Print "    KeepFeatures              = " & swChamfer.KeepFeatures
     Debug.Print "    Number of chamfered faces = " & swChamfer.GetFaceCount
     Debug.Print "    Number of chamfered edges = " & swChamfer.GetEdgeCount
     Debug.Print "    Type                      = " & swChamfer.Type
         ' ChamferFeatureData2::Type
         '   1 = Angle-Distance
         '   2 = Distance-Distance
         '   3 = Vertex
    ' Roll back to get access to geometric entities
     bRet = swChamfer.AccessSelections(swModel, Nothing): Debug.Assert bRet

    Set swVertex = swChamfer.Vertex
    vEdgeArr = swChamfer.Edges
     vFaceArr = swChamfer.Faces
     vLoopArr = swChamfer.Loops
    If Not swVertex Is Nothing Then
         swModel.ClearSelection2 True
         Set swEnt = swVertex
         bRet = swEnt.Select4(True, swSelData): Debug.Assert bRet
     End If
    If Not IsEmpty(vEdgeArr) Then
         swModel.ClearSelection2 True
         i = 0
         bRet = False
         For Each vEdge In vEdgeArr
             Set swEdge = vEdge
             Set swEnt = swEdge
            bRet = swEnt.Select4(True, swSelData): Debug.Assert bRet
            Debug.Print "    EdgeFlip(" & i & ")              = " & swChamfer.GetIsFlipped(swEdge)
            i = i + 1
         Next
    End If

     If Not IsEmpty(vFaceArr) Then
         swModel.ClearSelection2 True
         i = 0
         bRet = False
        For Each vFace In vFaceArr
             Set swFace = vFace
             Set swEnt = swFace

            bRet = swEnt.Select4(True, swSelData): Debug.Assert bRet

            Debug.Print "    FaceFlip(" & i & ")              = " & swChamfer.GetIsFlipped(swFace)
            i = i + 1
         Next
    End If

     If Not IsEmpty(vLoopArr) Then
        swModel.ClearSelection2 True
         i = 0
         bRet = False
        For Each vLoop In vLoopArr
             Set swLoop = vLoop
            ' Cannot select loop-through-entity interface because loop
             ' is topology; instead, get edges (geometry) and select through
             ' entity from edge
            vLoopEdgeArr = swLoop.GetEdges
            For Each vLoopEdge In vLoopEdgeArr
                 Set swLoopEdge = vLoopEdge
                 Set swEnt = swLoopEdge
                bRet = swEnt.Select4(True, swSelData): Debug.Assert bRet
             Next
            Debug.Print "    LoopFlip(" & i & ")              = " & swChamfer.GetIsFlipped(swLoop)
             i = i + 1
         Next
    End If
    'Cancel changes
     swChamfer.ReleaseSelectionAccess
End Sub
```
