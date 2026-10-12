---
title: "Get Component Via Display Dimension Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_Via_Display_Dimension_Example_VB.htm"
---

# Get Component Via Display Dimension Example (VBA)

This example shows how to get the component associated with the selected display dimension.

```vb
'----------------------------------------------
'
' Preconditions:
'           (1) Drawing is open with dimensions inserted
'           (2) A dimension is selected
'
' Postconditions: None
'
'----------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swDispDim As SldWorks.DisplayDimension
Dim swDim As SldWorks.Dimension
Dim swFeat As SldWorks.feature
Dim swEnt As SldWorks.entity
Dim swComp As SldWorks.Component2

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager
Set swDispDim = swSelMgr.GetSelectedObject5(1)
' Get the selected dimension
Set swDim = swDispDim.GetDimension
Debug.Print "Name of dimension: "; swDim.Name
' Get the feature that owns the selected dimension
Set swFeat = swDim.GetFeatureOwner
Debug.Print "Name of feature: "; swFeat.Name
' Feature is an entity
Set swEnt = swFeat
' Get the component for the feature whose dimension was selected
Set swComp = swEnt.GetComponent
Debug.Print "Name of component: "; swComp.Name2

End Sub
```
