---
title: "Insert Protrusion Blend Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Protrusion_Blend_Example_VB.htm"
---

# Insert Protrusion Blend Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchSegment As SldWorks.SketchSegment
Dim swSketchManager As SldWorks.SketchManager
Dim swRefPlane As SldWorks.RefPlane
Dim swFeatureManager As SldWorks.FeatureManager
Dim status As Boolean

Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Create new part
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
```

```
    'Create profile sketch
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
    Set swSketchManager = swModel.SketchManager
    Set swSketchSegment = swSketchManager.CreateEllipse(0, 0, 0, 7.06113079019074E-02, 0, 0, 0, 3.74944141689373E-02, 0)
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
```

```
    ' Create reference plane and another profile sketch
    ' on that reference plane
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
    Set swFeatureManager = swModel.FeatureManager
    Set swRefPlane = swFeatureManager.InsertRefPlane(8, 0.07, 0, 0, 0, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSketchSegment = swSketchManager.CreateEllipse(0, 0, 0, 5.27205722070845E-02, 0, 0, 0, 1.54164850136235E-02, 0)
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
```

```
    ' Create guide curves
    status = swModelDocExt.SelectByID2("Point4@Sketch1", "EXTSKETCHPOINT", 0, 3.74944141689373E-02, 0, False, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("Point4@Sketch2", "EXTSKETCHPOINT", 0, 1.54164850136235E-02, 0, True, 1, Nothing, 0)
    swModel.Insert3DSplineCurve False
```

```
    status = swModelDocExt.SelectByID2("Point5@Sketch2", "EXTSKETCHPOINT", -5.27205722070845E-02, 0, 0, True, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("Point5@Sketch1", "EXTSKETCHPOINT", -7.06113079019074E-02, 0, 0, True, 1, Nothing, 0)
    swModel.Insert3DSplineCurve False
```

```
    status = swModelDocExt.SelectByID2("Point6@Sketch2", "EXTSKETCHPOINT", 0, -1.54164850136235E-02, 0, True, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("Point6@Sketch1", "EXTSKETCHPOINT", 0, -3.74944141689373E-02, 0, True, 1, Nothing, 0)
    swModel.Insert3DSplineCurve False
```

```
    status = swModelDocExt.SelectByID2("Point3@Sketch2", "EXTSKETCHPOINT", 5.27205722070845E-02, 0, 0, True, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("Point3@Sketch1", "EXTSKETCHPOINT", 7.06113079019074E-02, 0, 0, True, 1, Nothing, 0)
    swModel.Insert3DSplineCurve False
```

```
    ' Create centerline
    status = swModelDocExt.SelectByID2("Point2@Sketch2", "EXTSKETCHPOINT", 0, 0, 0, True, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("Point2@Sketch1", "EXTSKETCHPOINT", 0, 0, 0, True, 1, Nothing, 0)
    swModel.Insert3DSplineCurve False
```

```
    ' Create loft
    status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 7.06113079019074E-02, 0, 0, False, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 5.27205722070845E-02, 0, 0.07, True, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("Curve1", "REFERENCECURVES", 9.99754519565386E-02, 4.47609702560072E-02, 0.128010464418594, True, 4098, Nothing, 0)
    status = swModelDocExt.SelectByID2("Curve2", "REFERENCECURVES", 0.037643674311596, 2.21603475855119E-02, 0.115437869126538, True, 8194, Nothing, 0)
    status = swModelDocExt.SelectByID2("Curve3", "REFERENCECURVES", 9.99909384372586E-02, -7.44308680111772E-04, 0.131301605626447, True, 12290, Nothing, 0)
    status = swModelDocExt.SelectByID2("Curve4", "REFERENCECURVES", 0.158600974878482, 2.18780932746938E-02, 0.129235804629445, True, 16386, Nothing, 0)
    status = swModelDocExt.SelectByID2("Curve5", "REFERENCECURVES", 9.98735089003162E-02, 0.022159545044488, 0.108064927518626, True, 4, Nothing, 0)
    swFeatureManager.InsertProtrusionBlend2 False, True, False, 1, 0, 0, 1, 1, True, True, False, 0, 0, 0, True, True, True, swGuideCurveInfluence_e.swGuideCurveInfluenceNextEdge
```

```
End Sub
```
