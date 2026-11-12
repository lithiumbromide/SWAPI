---
title: "Create Temporary Bodies by Offsetting a Surface Body Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Temporary_Bodies_by_Offsetting_Surface_Body_Example_VBNET.htm"
---

# Create Temporary Bodies by Offsetting a Surface Body Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swFeatureManager As FeatureManager
        Dim sketchSegment As SketchSegment
        Dim swSketchManager As SketchManager
        Dim swModelDocExt As ModelDocExtension
        Dim swSelectionManager As SelectionMgr
        Dim swEdge As Edge
        Dim swBody As Body2
        Dim newBody1 As Body2
        Dim newBody2 As Body2
        Dim pointArray As Object
        Dim points(11) As Double
        Dim status As Boolean

        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
        swFeatureManager = swModel.FeatureManager
        swSketchManager = swModel.SketchManager
        swModelDocExt = swModel.Extension
        swSelectionManager = swModel.SelectionManager

        'Create extruded surface body
        points(0) = -0.0720746414289124
        points(1) = -0.0283600245263074
        points(2) = 0
        points(3) = -0.0514715593755
        points(4) = -0.00345025084396866
        points(5) = 0
        points(6) = 0
        points(7) = 0
        points(8) = 0
        points(9) = 0.0872558597840225
        points(10) = 0.0521037067517796
        points(11) = 0
        pointArray = points
        sketchSegment = swSketchManager.CreateSpline((pointArray))
        swSketchManager.InsertSketch(True)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
        swFeatureManager.FeatureExtruRefSurface2(True, False, False, 0, 0, 0.0508, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, False, False, False, False)
        swSelectionManager.EnableContourSelection = False

        'Offset selected edge and create two temporary bodies
        status = swModelDocExt.SelectByID2("", "EDGE", -0.00623752003605205, 0.000329492391927033, 0.050581684437077, False, 0, Nothing, 0)
        swEdge = swSelectionManager.GetSelectedObject6(1, -1)
        swBody = swEdge.GetBody
        swBody = swBody.Copy
        'Using a copy of the selected surface body, create two new temporary bodies
        newBody1 = swBody.MakeOffset(0.01, False)
        newBody2 = swBody.MakeOffset(0.01, True)
        'Display and color the new temporary body blue
        newBody1.Display3(swModel, RGB(0, 0, 255), swTempBodySelectOptions_e.swTempBodySelectOptionNone)
        'Display and color the new temporary body red
        newBody2.Display3(swModel, RGB(255, 0, 0), swTempBodySelectOptions_e.swTempBodySelectOptionNone)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
