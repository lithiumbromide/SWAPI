---
title: "Get and Set Constraint for Dome Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Constraint_for_Dome_Feature_Example_VB.htm"
---

# Get and Set Constraint for Dome Feature Example (VBA)

This example shows how to get and set a constraining point for a dome feature. A part containing a dome feature constrained by a sketch point on the origin is open.

```vb
'---------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.PartDoc
Dim component As SldWorks.Component2
Dim newPointFeat As SldWorks.SketchPoint
Dim dome As SldWorks.feature
Dim domeConstraintPoint As SldWorks.SketchPoint
Dim dome_featData As SldWorks.DomeFeatureData2
Dim boolstatus As Variant
Sub main()
'{
    Set swApp = Application.SldWorks
    Set Part = swApp.ActiveDoc
    boolstatus = Part.Extension.SelectByID2("Point1@Sketch1", "EXTSKETCHPOINT", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
    Set newPointFeat = Part.SelectionManager.GetSelectedObject5(1)

    Set dome = Part.FeatureByName("Dome1")
    Set dome_featData = dome.GetDefinition
    boolstatus = dome_featData.AccessSelections(Part, component)
    Set domeConstraintPoint = dome_featData.ConstraintPointOrSketch

    If Not domeConstraintPoint Is Nothing Then

        dome_featData.ConstraintPointOrSketch = newPointFeat

        boolstatus = dome.ModifyDefinition(dome_featData, Part, Nothing)

    End If

dome_featData.ReleaseSelectionAccess

'}
End Sub
```
