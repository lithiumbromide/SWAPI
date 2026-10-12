---
title: "Create Ruled Surface Body From Edge (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Ruled_Surface_From_Edge_Example_VB.htm"
---

# Create Ruled Surface Body From Edge (VBA)

This example shows how to create a ruled surface body from an edge.

```vb
'--------------------------------------------------------
' Preconditions: Model document is open and an edge is
'                is selected on the model.
'
' Postconditions: Ruled surface body is created from the
'                 selected edge.
'--------------------------------------------------------
Option Explicit

Public Enum swBodyType_e
    swAllBodies = 0
    swSolidBody = 1
    swSheetBody = 2
    swWireBody = 3
    swMinimumBody = 4
    swGeneralBody = 5
    swEmptyBody = 6
End Enum

Dim swApp As SldWorks.SldWorks
Dim swDoc As SldWorks.ModelDoc2
Dim swModel As SldWorks.Modeler
Dim swSelMgr As SldWorks.SelectionMgr
Dim swEdge(0) As SldWorks.Edge
Dim swEdgeList As Variant
Dim swRuledBody As SldWorks.Body2

Sub main()

Set swApp = Application.SldWorks
Set swDoc = swApp.ActiveDoc
Set swModel = swApp.GetModeler
Set swSelMgr = swDoc.SelectionManager
Set swEdge(0) = swSelMgr.GetSelectedObject6(1, -1)
swEdgeList = swEdge
Dim error As Long
error = swModel.CreateRuledSurfaceFromEdge(swDoc, swEdgeList, 1, 0.02, True, False, True, 0#, False, 1#, 0#, 0#, False, swRuledBody)
Dim typeBody As Long
typeBody = swRuledBody.GetType()
Select Case typeBody
    Case swAllBodies
        Debug.Print "All solid and sheet bodies"
    Case swSolidBody
        Debug.Print "Solid body"
    Case swSheetBody
        Debug.Print "Sheet body"
    Case swWireBody
        Debug.Print "Wire body"
    Case swMinimumBody
        Debug.Print "Point body"
    Case swGeneralBody
        Debug.Print "General, nonmanifold body"
    Case swEmptyBody
        Debug.Print "NULL body"

End Select
End Sub
```
