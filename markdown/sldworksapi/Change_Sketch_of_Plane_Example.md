---
title: "Change the Plane of a Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Sketch_of_Plane_Example.htm"
---

# Change the Plane of a Sketch Example (VBA)

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
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim skSegment As SldWorks.SketchSegment
 Dim boolstatus As Boolean

Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2017\templates\Part.prtdot", 0, 0, 0)

    boolstatus = Part.Extension.SelectByID2("Top Plane", "PLANE", -4.94443883882606E-02, 0.010829578664819, 1.87336739521956E-02, True, 0, Nothing, 0)
     Part.SketchManager.InsertSketch True

    Dim pointArray As Variant
     Dim points() As Double
     ReDim points(0 To 11) As Double
     points(0) = -6.96700449874595E-02
     points(1) = -2.05096087491173E-02
     points(2) = 0
     points(3) = -3.49133034431539E-02
     points(4) = 1.51865041882777E-02
     points(5) = 0
     points(6) = 1.83177421652422E-02
     points(7) = 0
     points(8) = 0
     points(9) = 0.060902578651959
     points(10) = 3.36608082523681E-02
     points(11) = 0
     pointArray = points

    Set skSegment = Part.SketchManager.CreateSpline((pointArray))
     Part.SketchManager.InsertSketch True

    boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Top Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
     boolstatus = Part.DeSelectByID("Top Plane", "PLANE", 0, 0, 0)

    ' Select sketch and new plane for the sketch
     boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
     ' Change the plane of the sketch
     boolstatus = Part.Extension.ChangeSketchPlane(1, Nothing)
     boolstatus = Part.EditRebuild3()

    Part.ShowNamedView2 "*Isometric", 7
     boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)

End Sub
```
