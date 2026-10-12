---
title: "Get Chamfer Distances Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Chamfer_Distances_Example_VBNET.htm"
---

# Get Chamfer Distances Example (VB.NET)

This example shows how to get the distances associated with the selected chamfer.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part document with at least on chamfer.
 ' 2. Select a chamfer feature.
 ' 3. Open the Immediate window.
 '
 ' Postconditions: Examine the Immediate window for
 ' the chamfer data.
 '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()
         ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
         Const DegPerRad As Double = 57.3
         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swFeat As Feature
         Dim swChamfer As ChamferFeatureData2
         Dim swVertex As Vertex
         Dim vEdgeArr As Object
         Dim vEdge As Object
         Dim swEdge As Edge
         Dim vFaceArr As Object
         Dim vFace As Object
         Dim swFace As Face2
         Dim vLoopArr As Object
         Dim vLoop As Object
         Dim swLoop As Loop2
         Dim vLoopEdge As Object
         Dim vLoopEdgeArr As Object
         Dim swLoopEdge As Edge
         Dim swEnt As Entity
         Dim swSelData As SelectData
         Dim i As  Integer
         Dim bRet As Boolean

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swSelData = swSelMgr.CreateSelectData
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swChamfer = swFeat.GetDefinition

         ' Get chamfer information
         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("  " & swFeat.Name)
         Debug.Print("    EdgeChamferAngle          = " & swChamfer.EdgeChamferAngle * DegPerRad & " degrees")
         Debug.Print("    EqualDistance             = " & swChamfer.EqualDistance)
         Debug.Print("    EdgeChamferDistance(0)    = " & swChamfer.GetEdgeChamferDistance(0) * 1000.0# & " mm")
         Debug.Print("    EdgeChamferDistance(1)    = " & swChamfer.GetEdgeChamferDistance(1) * 1000.0# & " mm")
         Debug.Print("    VertexChamferDistance(0)  = " & swChamfer.GetVertexChamferDistance(0) * 1000.0# & " mm")
         Debug.Print("    VertexChamferDistance(1)  = " & swChamfer.GetVertexChamferDistance(1) * 1000.0# & " mm")
         Debug.Print("    VertexChamferDistance(2)  = " & swChamfer.GetVertexChamferDistance(2) * 1000.0# & " mm")
         Debug.Print("    KeepFeatures              = " & swChamfer.KeepFeatures)
         Debug.Print("    Number of chamfered faces = " & swChamfer.GetFaceCount)
         Debug.Print("    Number of chamfered edges = " & swChamfer.GetEdgeCount)
         Debug.Print("    Type                      = " & swChamfer.Type)
         ' ChamferFeatureData2::Type
         '   1 = Angle-Distance
         '   2 = Distance-Distance
         '   3 = Vertex

         ' Roll back to get access to geometric entities
         bRet = swChamfer.AccessSelections(swModel, Nothing) : Debug.Assert(bRet)

         swVertex = swChamfer.Vertex

         vEdgeArr = swChamfer.Edges
         vFaceArr = swChamfer.Faces
         vLoopArr = swChamfer.Loops

         If Not swVertex Is Nothing Then
             swModel.ClearSelection2(True)
             swEnt = swVertex
             bRet = swEnt.Select4(True, swSelData) : Debug.Assert(bRet)
         End If

         If Not IsNothing(vEdgeArr) Then
             swModel.ClearSelection2(True)
             i = 0
             bRet = False
             For Each vEdge In vEdgeArr
                 swEdge = vEdge
                 swEnt = swEdge

                 bRet = swEnt.Select4(True, swSelData) : Debug.Assert(bRet)

                 Debug.Print("    EdgeFlip(" & i & ")              = " & swChamfer.GetIsFlipped(swEdge))

                 i = i + 1
             Next

         End If

         If Not IsNothing(vFaceArr) Then
             swModel.ClearSelection2(True)
             i = 0
             bRet = False

             For Each vFace In vFaceArr
                 swFace = vFace
                 swEnt = swFace

                 bRet = swEnt.Select4(True, swSelData) : Debug.Assert(bRet)

                 Debug.Print("    FaceFlip(" & i & ")              = " & swChamfer.GetIsFlipped(swFace))

                 i = i + 1
             Next

         End If

         If Not IsNothing(vLoopArr) Then

             swModel.ClearSelection2(True)
             i = 0
             bRet = False

             For Each vLoop In vLoopArr
                 swLoop = vLoop

                 ' Cannot select loop-through-entity interface because loop
                 ' is topology; instead, get edges (geometry) and select through
                 ' entity from edge

                 vLoopEdgeArr = swLoop.GetEdges

                 For Each vLoopEdge In vLoopEdgeArr
                     swLoopEdge = vLoopEdge
                     swEnt = swLoopEdge

                     bRet = swEnt.Select4(True, swSelData) : Debug.Assert(bRet)
                 Next

                 Debug.Print("    LoopFlip(" & i & ")              = " & swChamfer.GetIsFlipped(swLoop))
                 i = i + 1
             Next

         End If

         'Cancel changes
         swChamfer.ReleaseSelectionAccess()

     End Sub

     Public swApp As SldWorks

 End  Class
```
