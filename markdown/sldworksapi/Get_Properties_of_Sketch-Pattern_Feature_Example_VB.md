---
title: "Get Properties of Sketch Pattern Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Properties_of_Sketch-Pattern_Feature_Example_VB.htm"
---

# Get Properties of Sketch Pattern Feature Example (VBA)

This example shows how to create a sketch-driven pattern feature and gets some of its properties.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified document exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates Boss-Extrude2, Sketch3, and Sketch-Pattern1.
 ' 2. Inspect the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
 Dim swApp                   As SldWorks.SldWorks
 Dim Part                    As SldWorks.ModelDoc2
 Dim myFeature               As SldWorks.Feature
 Dim swSketchPatt            As SldWorks.SketchPatternFeatureData
 Dim vBasePt                 As Variant
 Dim skPoint                 As Object
 Dim vSkLines                As Variant
 Dim swSketch                As SldWorks.Sketch
 Dim swSketchFeat            As SldWorks.Feature
 Dim swPatternTransform      As SldWorks.MathTransform
 Dim boolstatus              As Boolean
 Dim i                       As Long
 Dim longstatus              As Long
 Dim longwarnings            As Long
Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\block20.sldprt", 1, 0, "", longstatus, longwarnings)
     swApp.ActivateDoc2 "block20", False, longstatus

    boolstatus = Part.Extension.SelectByID2("", "FACE", -4.07921768468213E-02, 3.96239999998329E-02, -4.02814031592129E-02, False, 0, Nothing, 0)
     boolstatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
     boolstatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
     vSkLines = Part.SketchManager.CreateCornerRectangle(-5.18589252521906E-02, 4.51811131877662E-02, 0, -3.57471289475484E-02, 2.86242963995278E-02, 0)
     Part.SketchManager.InsertSketch True

    boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
     Set myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.00254, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, 0, 0, False)

    Part.SketchManager.InsertSketch True
     boolstatus = Part.Extension.SelectByID2("", "FACE", -7.70328176440671E-03, 3.96239999998897E-02, -7.62437790422155E-03, False, 0, Nothing, 0)
     Set skPoint = Part.SketchManager.CreatePoint(-0.00527, 0.051345, 0#)
     Set skPoint = Part.SketchManager.CreatePoint(-0.005854, 0.025783, 0#)
     Set skPoint = Part.SketchManager.CreatePoint(-0.005888, -0.000009, 0#)
     Set skPoint = Part.SketchManager.CreatePoint(0.019408, 0.051285, 0#)
     Set skPoint = Part.SketchManager.CreatePoint(0.019093, 0.024628, 0#)
     Set skPoint = Part.SketchManager.CreatePoint(0.019629, -0.000148, 0#)
     Set skPoint = Part.SketchManager.CreatePoint(0.043756, 0.051962, 0#)
     Set skPoint = Part.SketchManager.CreatePoint(0.043146, 0.025865, 0#)
     Set skPoint = Part.SketchManager.CreatePoint(0.043401, 0.000225, 0#)
     Part.ClearSelection2 True
     Part.SketchManager.InsertSketch True

     boolstatus = Part.Extension.SelectByID2("Boss-Extrude2", "BODYFEATURE", -4.77922378944982E-02, 4.21639999998433E-02, 2.33214950450815E-02, False, 4, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, True, 64, Nothing, 0)

    Set swSketchPatt = Part.FeatureManager.CreateDefinition(swFmSketchPattern)
     swSketchPatt.GeometryPattern = False
     swSketchPatt.UseCentroid = True
     Set swSketchFeat = Part.FeatureManager.CreateFeature(swSketchPatt)

     Set swSketchPatt = swSketchFeat.GetDefinition
    swSketchPatt.AccessSelections Part, Nothing

    Set swSketch = swSketchPatt.Sketch
     i = swSketch.GetSketchPointsCount2

    Set swPatternTransform = swSketchPatt.GetTransform(i)

    vBasePt = swSketchPatt.GetBasePoint
    Debug.Print swSketchFeat.Name
     Debug.Print "  Create pattern using only geometry? " & swSketchPatt.GeometryPattern
     Debug.Print "  Pattern seed coordinates in mm:  (" & vBasePt(0) * 1000# & ", " & vBasePt(1) * 1000# & ", " & vBasePt(2) * 1000# & ")"
     Debug.Print "  Body count: " & swSketchPatt.GetPatternBodyCount
     Debug.Print "  Face count: " & swSketchPatt.GetPatternFaceCount
     Debug.Print "  Feature count: " & swSketchPatt.GetPatternFeatureCount
     Debug.Print "  Reference point type (-1 for centroid): " & swSketchPatt.GetReferencePointType
     Debug.Print "  Use centroid as the reference point? " & swSketchPatt.UseCentroid
     Debug.Print "  Propagate visual properties? " & swSketchPatt.PropagateVisualProperty

    swSketchPatt.ReleaseSelectionAccess
End Sub
```
