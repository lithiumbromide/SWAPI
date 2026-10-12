---
title: "Create Temporary Bodies by Offsetting Surface Body Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Temporary_Bodies_by_Offsetting_Surface_Body_Example_VB.htm"
---

# Create Temporary Bodies by Offsetting Surface Body Example (VBA)

## Create Temporary Bodies by Offsetting a Surface Body Example (VBA)

This example shows how to create two temporary bodies by offsetting a surface body.

```
'----------------------------------------------------------------------------
' Preconditions: Verify that the specified part document template exists.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Creates a surface body.
' 3. Selects an edge on the surface body to offset.
' 4. Creates two temporary bodies of the surface
'    body using the selected edge.
' 5. Examine the graphics area.
'---------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swFeatureManager As SldWorks.FeatureManager
Dim sketchSegment As SldWorks.sketchSegment
Dim swSketchManager As SldWorks.SketchManager
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionManager As SldWorks.SelectionMgr
Dim swEdge As SldWorks.Edge
Dim swBody As SldWorks.Body2
Dim newBody1 As SldWorks.Body2
Dim newBody2 As SldWorks.Body2
Dim pointArray As Variant
Dim points(11) As Double
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
    Set swFeatureManager = swModel.FeatureManager
    Set swSketchManager = swModel.SketchManager
    Set swModelDocExt = swModel.Extension
    Set swSelectionManager = swModel.SelectionManager
```

```
    'Create extruded surface body
    points(0) = -7.20746414289124E-02
    points(1) = -2.83600245263074E-02
    points(2) = 0
    points(3) = -0.0514715593755
    points(4) = -3.45025084396866E-03
    points(5) = 0
    points(6) = 0
    points(7) = 0
    points(8) = 0
    points(9) = 8.72558597840225E-02
    points(10) = 5.21037067517796E-02
    points(11) = 0
    pointArray = points
    Set sketchSegment = swSketchManager.CreateSpline((pointArray))
    swSketchManager.InsertSketch True
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
    swFeatureManager.FeatureExtruRefSurface2 True, False, False, 0, 0, 0.0508, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, False, False, False, False
    swSelectionManager.EnableContourSelection = False
```

```
    'Offset selected edge and create two temporary bodies
    status = swModelDocExt.SelectByID2("", "EDGE", -6.23752003605205E-03, 3.29492391927033E-04, 0.050581684437077, False, 0, Nothing, 0)
    Set swEdge = swSelectionManager.GetSelectedObject6(1, -1)
    Set swBody = swEdge.GetBody
    Set swBody = swBody.Copy
    'Using a copy of the selected surface body, create two new temporary bodies
    Set newBody1 = swBody.MakeOffset(0.01, False)
    Set newBody2 = swBody.MakeOffset(0.01, True)
    'Display and color the new temporary body blue
    newBody1.Display3 swModel, RGB(0, 0, 255), swTempbodySelectOptions_e.swTempBodySelectOptionNone
    'Display and color the new temporary body red
    newBody2.Display3 swModel, RGB(255, 0, 0), swTempbodySelectOptions_e.swTempBodySelectOptionNone
```

```
End Sub
```
