---
title: "Get Radius of Variable Radius Fillet Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Radius_of_Variable_Radius_Fillet_Example_VB.htm"
---

# Get Radius of Variable Radius Fillet Example (VBA)

This example shows how to get the radius of a variable radius fillet.

```vb
'----------------------------------------------
'
' Preconditions:
'          (1) Model document is open.
'          (2) Model contains a VarFillet2 feature.
'
' Postconditions: None
'
'----------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModelDoc As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim boolstatus As Boolean
Dim swFeat As SldWorks.Feature
Dim swFeatData As SldWorks.VariableFilletFeatureData2
Dim swEdge As SldWorks.Edge
Dim Vert1 As SldWorks.Vertex
Dim Vert2 As SldWorks.Vertex
Dim radius1 As Double
Dim radius2 As Double

Sub main()
Set swApp = Application.SldWorks
Set swModelDoc = swApp.ActiveDoc
Set swModelDocExt = swModelDoc.Extension
Set swSelMgr = swModelDoc.SelectionManager

boolstatus = swModelDocExt.SelectByID("VarFillet2", "BODYFEATURE", 0, 0, 0, False, 0, Nothing)
Set swFeat = swSelMgr.GetSelectedObject5(1): Debug.Assert Not swFeat Is Nothing
Set swFeatData = swFeat.GetDefinition()

boolstatus = swFeatData.AccessSelections(swModelDoc, Nothing): Debug.Assert boolstatus
Set swEdge = swFeatData.GetFilletEdgeAtIndex(0)
Set Vert1 = swEdge.GetStartVertex(): Debug.Assert Not Vert1 Is Nothing
radius1 = swFeatData.GetRadius2(Vert1, boolstatus)
Set Vert2 = swEdge.GetEndVertex(): Debug.Assert Not Vert2 Is Nothing
radius2 = swFeatData.GetRadius2(Vert2, boolstatus)
Debug.Print "Radius1 = " & radius1 * 1000# & " mm"
Debug.Print "Radius2 = " & radius2 * 1000# & " mm"
swFeatData.ReleaseSelectionAccess

End Sub
```
