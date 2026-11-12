---
title: "Get and Set Direction for Dome Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Direction_for_Dome_Feature_Example_VB.htm"
---

# Get and Set Direction for Dome Feature Example (VBA)

This example shows how to get and set the direction of a dome feature. You must have a part containing a dome feature created with an edge indicating the direction of the feature and preselect that edge.

```vb
'---------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
Dim part As SldWorks.PartDoc
Dim component As SldWorks.Component2
Dim newEdge As SldWorks.Edge
Dim dome As SldWorks.feature
Dim dome_featData As SldWorks.DomeFeatureData2
Dim domeDirection As SldWorks.Edge
Dim boolstatus As Variant
Sub main()
'{
    Set swApp = Application.SldWorks
    Set part = swApp.ActiveDoc
    Set newEdge = part.SelectionManager.GetSelectedObject5(1)
    Set dome = part.FeatureByName("Dome1")
    Set dome_featData = dome.GetDefinition
    boolstatus = dome_featData.AccessSelections(part, component)

    Set domeDirection = dome_featData.Direction

    If Not domeDirection Is Nothing Then

        dome_featData.Direction = newEdge

        boolstatus = dome.ModifyDefinition(dome_featData, part, Nothing)

    End If
    dome_featData.ReleaseSelectionAccess
'}
End Sub
```
