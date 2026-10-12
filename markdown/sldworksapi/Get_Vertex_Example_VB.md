---
title: "Get Vertex Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Vertex_Example_VB.htm"
---

# Get Vertex Example (VBA)

This example shows how to get the x,y,z location of each vertex on the selected face:

- Query a face for edge information
- Traverse the topology of a part from the face down to the vertex
- Determine the selected object count
- Get objects selected by the user
- Determine object types

```vb
'------------------------------------------------------------
Public Sub GetEndPoints()

Dim i As Long
Dim Msg As String
Dim Style As Variant
Dim Title As String
Dim swApp, Part, SelMgr As Object
' Face object
Dim faceObj As Object

' Array of edge objects
Dim edgeList As Variant
Dim edgeCount As Long

' Edge object
Dim edgeObj As Object

' Vertex objects
Dim startVertexObj As Object
Dim endVertexObj As Object

' Edge startpoint and endpoint arrays
Dim startPt As Variant
Dim endPt As Variant

Set swApp = CreateObject("SldWorks.Application")
' Use the active document
Set Part = swApp.ActiveDoc
' Setup to handle user selections
Set SelMgr = Part.SelectionManager

' If no selection made, return an error
If (SelMgr.GetSelectedObjectCount = 0) Then
swApp.SendMsgToUser ("Select a face first...")

' Otherwise, continue
Else

If (SelMgr.GetSelectedObjectType(1) <> 2) Then
swApp.SendMsgToUser ("Must select a face")
Exit Sub
End If

' Get the selected Face object
Set faceObj = SelMgr.GetSelectedObject5(1)

' Get edge count from the face
edgeCount = faceObj.GetEdgeCount
' Get all edges from the face
edgeList = faceObj.GetEdges

' For each edge
For i = 0 To (edgeCount - 1)
Set edgeObj = edgeList(i)
' Get the "Start" vertex
Set startVertexObj = edgeObj.GetStartVertex
' Get the "End" vertex
Set endVertexObj = edgeObj.GetEndVertex

' Define message
Msg = "Edge points: " + Chr(10)
If (Not startVertexObj Is Nothing) Then
' Get the xyz vertex location
startPt = startVertexObj.GetPoint
Msg = Msg + Str$(startPt(0))+","+Str$(startPt(1))+","+Str$(startPt(2))+Chr(10)
End If

If (Not endVertexObj Is Nothing) Then
' Get the xyz vertex location
endPt = endVertexObj.GetPoint
Msg = Msg + Str$(endPt(0))+","+Str$(endPt(1))+","+Str$(endPt(2))
End If

' OK Button only
Style = vbOKOnly
' Define title
Title = "Vertex Info"
' Display message to user
Call MsgBox(Msg, Style, Title)

Next
End If

End Sub
```
