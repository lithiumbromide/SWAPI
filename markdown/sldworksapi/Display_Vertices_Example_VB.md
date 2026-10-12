---
title: "Display Vertices Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_Vertices_Example_VB.htm"
---

# Display Vertices Example (VBA)

This example shows how to display vertices.

```vb
'----------------------------------------
'
' Preconditions:
'          (1) Part document is open and has one or more solid bodies.
'          (2) Each solid body does not contain any circular edges.
'
' Postconditions: All vertices are highlighted.
'
'----------------------------------------
Option Explicit

Sub main()

Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.PartDoc
Dim Body As SldWorks.Body2
Dim Edge As SldWorks.Edge
Dim Vertex As SldWorks.Vertex
Dim Bodyarr As Variant
Dim vbody As Variant
Dim Edgearr As Variant
Dim idx As Long
Dim vobj As Variant
Dim crgb As Long

Set swApp = Application.SldWorks
Set Part = swApp.ActiveDoc

Bodyarr = Part.GetBodies2(swSolidBody, True)
For Each vbody In Bodyarr
    Set Body = vbody
    Edgearr = Body.GetEdges
    idx = 0
    For Each vobj In Edgearr
        Set Edge = vobj
        Set Vertex = Edge.GetStartVertex
        Select Case CInt(idx Mod 8)
        Case 0
           crgb = RGB(0, 0, 0)
        Case 1
           crgb = RGB(0, 0, 255)
        Case 2
           crgb = RGB(0, 255, 0)
        Case 3
           crgb = RGB(0, 255, 255)
        Case 4
           crgb = RGB(255, 0, 0)
        Case 5
           crgb = RGB(255, 0, 255)
        Case 6
           crgb = RGB(255, 255, 0)
        Case 7
           crgb = RGB(255, 255, 255)
    End Select
    idx = idx + 1
    Vertex.Display Part, crgb, 1, True
   Next
Next

End Sub
```
