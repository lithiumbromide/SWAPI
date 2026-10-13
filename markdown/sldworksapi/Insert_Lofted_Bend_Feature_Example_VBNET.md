---
title: "Insert Lofted Bend Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Lofted_Bend_Feature_Example_VBNET.htm"
---

# Insert Lofted Bend Feature Example (VB.NET)

This example shows how to insert a lofted bend feature in a sheet metal part and get the lofted bend feature data.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part.
' 2. Creates a sketch on Front Plane, a reference plane parallel to
'    Front Plane, and a sketch on that reference plane.
' 3. Selects the sketches and inserts a lofted bend.
' 4. Inspect the Immediate window, FeatureManager design, and graphics area.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim Part As ModelDoc2
    Dim refPlane As RefPlane
    Dim skSegment As SketchSegment
    Dim feat As Feature
    Dim lbfd As LoftedBendsFeatureData
    Dim boolstatus As Boolean

    Sub main()

        ' Open new part and create a sketch, a reference plane, and another sketch
        ' on that reference plane
        Part = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
        boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        Part.ClearSelection2(True)
        Part.SketchManager.InsertSketch(True)
        skSegment = Part.SketchManager.CreateLine(0.0#, 0.0#, 0.0#, 0.024074, 0.024074, 0.0#)
        skSegment = Part.SketchManager.CreateLine(0.024074, 0.024074, 0.0#, 0.076952, 0.024074, 0.0#)
        skSegment = Part.SketchManager.CreateLine(0.076952, 0.024074, 0.0#, 0.101026, 0.0#, 0.0#)
        Part.ClearSelection2(True)
        Part.SketchManager.InsertSketch(True)
        boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
        refPlane = Part.FeatureManager.InsertRefPlane(8, 0.05, 0, 0, 0, 0)
        Part.ClearSelection2(True)
        boolstatus = Part.Extension.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        Part.SketchManager.InsertSketch(True)
        skSegment = Part.SketchManager.CreateLine(-0.031383, 0.0#, 0.0#, 0.047146, 0.060616, 0.0#)
        skSegment = Part.SketchManager.CreateLine(0.047146, 0.060616, 0.0#, 0.058036, 0.060616, 0.0#)
        skSegment = Part.SketchManager.CreateLine(0.058036, 0.060616, 0.0#, 0.129686, 0.002436, 0.0#)
        Part.ClearSelection2(True)
        Part.SketchManager.InsertSketch(True)

        ' Select the sketches for the lofted bend feature
        boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 1, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, True, 1, Nothing, 0)

        ' Insert a lofted bend feature with two bends
        feat = Part.FeatureManager.InsertSheetMetalLoftedBend2(0, 0.0007366, False, 0.0007366, True, swLoftedBendFacetOptions_e.swBendsPerTransitionSegment, 0, 2, 0, 0)

        ' Get lofted bend feature data
        lbfd = feat.GetDefinition
        Debug.Print("Number of sketch profiles in this feature: " & lbfd.GetProfileCount)
        Debug.Print("Thickness: " & lbfd.Thickness)
        Debug.Print("Reverse thickness direction? " & lbfd.Direction)
        Debug.Print("Faceting option as defined in swLoftedBendFacetOptions_e: " & lbfd.FacetingOption)
        Debug.Print("Faceting option value: " & lbfd.FacetValue)
        Debug.Print("Formed? " & lbfd.FormedMethod)
        Debug.Print("Calculate facet transitions using vertexes? " & lbfd.ReferToEndPoint)

    End Sub

    Public swApp As SldWorks

End Class
```
