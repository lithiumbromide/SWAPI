---
title: "Insert Protrusion Blend Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Protrusion_Blend_Example_VBNET.htm"
---

# Insert Protrusion Blend Example (VB.NET)

This example shows how to create a loft using profiles, guide curves, and a centerline.

```
'---------------------------------------------------------------
' Preconditions: Verify that the specified part template exists.
'
' Postconditions:
' 1. Creates a new part.
' 2. Creates a profile sketch.
' 3. Creates a reference plane and another profile sketch on that
'    reference plane.
' 4. Creates five curves: four guide curves and one centerline.
' 5. Selects the profile sketches, four guide curves, and the
'    centerline.
' 6. Creates a loft feature.
' 7. Examine the FeatureManager design tree and graphics area.
'---------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchSegment As SketchSegment
        Dim swSketchManager As SketchManager
        Dim swRefPlane As RefPlane
        Dim swFeatureManager As FeatureManager
        Dim status As Boolean

        'Create new part
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)

        'Create profile sketch
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        swSketchManager = swModel.SketchManager
        swSketchSegment = swSketchManager.CreateEllipse(0, 0, 0, 0.0706113079019074, 0, 0, 0, 0.0374944141689373, 0)
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)

        ' Create reference plane and another profile sketch
        ' on that reference plane
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
        swFeatureManager = swModel.FeatureManager
        swRefPlane = swFeatureManager.InsertRefPlane(8, 0.07, 0, 0, 0, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSketchSegment = swSketchManager.CreateEllipse(0, 0, 0, 0.0527205722070845, 0, 0, 0, 0.0154164850136235, 0)
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)

        ' Create guide curves
        status = swModelDocExt.SelectByID2("Point4@Sketch1", "EXTSKETCHPOINT", 0, 0.0374944141689373, 0, False, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Point4@Sketch2", "EXTSKETCHPOINT", 0, 0.0154164850136235, 0, True, 1, Nothing, 0)
        swModel.Insert3DSplineCurve(False)

        status = swModelDocExt.SelectByID2("Point5@Sketch2", "EXTSKETCHPOINT", -0.0527205722070845, 0, 0, True, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Point5@Sketch1", "EXTSKETCHPOINT", -0.0706113079019074, 0, 0, True, 1, Nothing, 0)
        swModel.Insert3DSplineCurve(False)

        status = swModelDocExt.SelectByID2("Point6@Sketch2", "EXTSKETCHPOINT", 0, -0.0154164850136235, 0, True, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Point6@Sketch1", "EXTSKETCHPOINT", 0, -0.0374944141689373, 0, True, 1, Nothing, 0)
        swModel.Insert3DSplineCurve(False)

        status = swModelDocExt.SelectByID2("Point3@Sketch2", "EXTSKETCHPOINT", 0.0527205722070845, 0, 0, True, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Point3@Sketch1", "EXTSKETCHPOINT", 0.0706113079019074, 0, 0, True, 1, Nothing, 0)
        swModel.Insert3DSplineCurve(False)

        ' Create centerline
        status = swModelDocExt.SelectByID2("Point2@Sketch2", "EXTSKETCHPOINT", 0, 0, 0, True, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Point2@Sketch1", "EXTSKETCHPOINT", 0, 0, 0, True, 1, Nothing, 0)
        swModel.Insert3DSplineCurve(False)

        ' Create loft
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0.0706113079019074, 0, 0, False, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0.0527205722070845, 0, 0.07, True, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("Curve1", "REFERENCECURVES", 0.0999754519565386, 0.0447609702560072, 0.128010464418594, True, 4098, Nothing, 0)
        status = swModelDocExt.SelectByID2("Curve2", "REFERENCECURVES", 0.037643674311596, 0.0221603475855119, 0.115437869126538, True, 8194, Nothing, 0)
        status = swModelDocExt.SelectByID2("Curve3", "REFERENCECURVES", 0.0999909384372586, -0.000744308680111772, 0.131301605626447, True, 12290, Nothing, 0)
        status = swModelDocExt.SelectByID2("Curve4", "REFERENCECURVES", 0.158600974878482, 0.0218780932746938, 0.129235804629445, True, 16386, Nothing, 0)
        status = swModelDocExt.SelectByID2("Curve5", "REFERENCECURVES", 0.0998735089003162, 0.022159545044488, 0.108064927518626, True, 4, Nothing, 0)
        swFeatureManager.InsertProtrusionBlend2(False, True, False, 1, 0, 0, 1, 1, True, True, False, 0, 0, 0, True, True, True, swGuideCurveInfluence_e.swGuideCurveInfluenceNextEdge)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
