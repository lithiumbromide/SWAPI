---
title: "Change the Plane of a Sketch Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Sketch_of_Plane_Example_VBNET.htm"
---

# Change the Plane of a Sketch Example (VB.NET)

This example shows how to modify the plane of a sketch.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Verify that the specified template exists.
 '
 ' Postconditions:
 ' 1. Creates a new part document with a sketch of a spline.
 ' 2. Changes the plane of the sketch Top Plane to the Front Plane.
 ' 3. Examine the FeatureManager design tree and graphics area.
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim skSegment As SketchSegment
     Dim boolstatus As Boolean

     Sub main()

         Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2017\templates\Part.prtdot", 0, 0, 0)

         boolstatus = Part.Extension.SelectByID2("Top Plane",  "PLANE", -0.0494443883882606, 0.010829578664819, 0.0187336739521956, True, 0, Nothing, 0)
         Part.SketchManager.InsertSketch(True)

         Dim pointArray As Object
         Dim points(11) As Double

         points(0) = -0.0696700449874595
         points(1) = -0.0205096087491173
         points(2) = 0
         points(3) = -0.0349133034431539
         points(4) = 0.0151865041882777
         points(5) = 0
         points(6) = 0.0183177421652422
         points(7) = 0
         points(8) = 0
         points(9) = 0.060902578651959
         points(10) = 0.0336608082523681
         points(11) = 0
         pointArray = points

         skSegment = Part.SketchManager.CreateSpline((pointArray))
         Part.SketchManager.InsertSketch(True)

         boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("Top Plane",  "PLANE", 0, 0, 0,  True, 0,  Nothing, 0)
         boolstatus = Part.DeSelectByID("Top Plane",  "PLANE", 0, 0, 0)

         ' Select sketch and new plane for the sketch
         boolstatus = Part.Extension.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,  True, 0,  Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
         ' Change the plane of the sketch
         boolstatus = Part.Extension.ChangeSketchPlane(1, Nothing)
         boolstatus = Part.EditRebuild3()

         Part.ShowNamedView2("*Isometric", 7)
         boolstatus = Part.Extension.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,  True, 0,  Nothing, 0)

     End Sub

     Public swApp As SldWorks

 End  Class
```
