---
title: "Replace Sketch Entity Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Replace_Sketch_Example_VBNET.htm"
---

# Replace Sketch Entity Example (VB.NET)

This example shows how to replace a sketch entity in a model with another sketch entity.

```
'----------------------------------------------------------------------------
' Preconditions: Verify that the specified template exists.
'
' Postconditions:
' 1. Opens a new part and creates Boss-Extrude1.
' 2. Replaces a sketch line with a sketch arc and modifies
'    Boss-Extrude1.
' 3. Examine the graphics area.
 ---------------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Partial Class SolidWorksMacro

	    Dim Part As ModelDoc2

	    Dim myFeature As Feature

	    Dim skSegment As SketchSegment

	    Dim boolstatus As Boolean

	    Sub main()

	        Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS
	2022\templates\Part.prtdot", 0, 0, 0)

	        Part = swApp.ActiveDoc

	        boolstatus = Part.Extension.SelectByID2("Front
	Plane", "PLANE", -0.048646278525398,
	0.0222864804840025, 0.0105288722478765, False, 0, Nothing, 0)

	        Dim vSkLines As Object

	        vSkLines = Part.SketchManager.CreateCornerRectangle(-0.0338155129850894,
	0.0167825138518592, 0, 0.0551067619016271, -0.0245475575743612, 0)

	        Part.ClearSelection2(True)

	        Part.SketchManager.InsertSketch(True)

	        Part.ShowNamedView2("*Trimetric",
	8)

	        boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH",
	0, 0, 0, False,
	4, Nothing,
	0)

	        myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, False, 0,
	0, 0.01778, 0.00254, False, False, False, False,
	0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)

	        Part.SelectionManager.EnableContourSelection = False

	        boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH",
	0, 0, 0, False,
	0, Nothing,
	0)

	        Part.EditSketch()

	        Part.ClearSelection2(True)

	        skSegment = Part.SketchManager.Create3PointArc(-0.033816,
	0.016783, 0.0#, 0.055107, 0.016783, 0.0#, 0.016009, 0.025458, 0.0#)

	        Part.ClearSelection2(True)

	        boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT",
	0.00202904300411839, 0.0119654152286464, -0.00709549576220667, True, 0, Nothing, 0)

	        boolstatus = Part.Extension.SelectByID2("Arc1", "SKETCHSEGMENT",
	0.00588878331207997, 0.0171023327681304, -0.0126221740799126, True, 0, Nothing, 0)

                'Replace Line1 with Arc1, delete Line1, and make Arc1 a contour
	        boolstatus = Part.SketchManager.SketchReplace2(False, True)

	        Part.SketchManager.InsertSketch(True)

	    End Sub

	    Public swApp As SldWorks

	End Class
```
