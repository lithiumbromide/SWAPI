---
title: "Get and Set Spline Handles Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Spline_Handles_Example_VB.htm"
---

# Get and Set Spline Handles Example (VBA)

This example shows how to get and set the properties of spline handles in a 2D spline.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified document template exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates Sketch1 in the graphics area and FeatureManager design tree.
 ' 2. Modifies some of the spline handles of Sketch1.
 ' 3. Inspect the Immediate window.
 '----------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swSpline As SldWorks.SketchSpline
 Dim skSegment As SldWorks.SketchSegment
 Dim swSplineHandle As Variant
 Dim boolstatus As Boolean
 Dim i As Long
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swModelDocExt = swModel.Extension

    Dim pointArray As Variant
     Dim points() As Double
     ReDim points(0 To 17) As Double
     points(0) = -7.25658847190971E-02
     points(1) = -2.84590725570979E-02
     points(2) = 0
     points(3) = -4.37940929359115E-02
     points(4) = 2.15374317625674E-02
     points(5) = 0
     points(6) = -2.45140262770747E-02
     points(7) = -0.026920232075895
     points(8) = 0
     points(9) = 2.73938454967038E-02
     points(10) = -4.14386885537397E-02
     points(11) = 0
     points(12) = 4.13348167730874E-02
     points(13) = 3.86761654855832E-02
     points(14) = 0
     points(15) = 0.101251331620574
     points(16) = 4.38481259864147E-02
     points(17) = 0
     pointArray = points

    Set skSegment = swModel.SketchManager.CreateSpline((pointArray))
     swModel.SketchManager.InsertSketch True

    boolstatus = swModelDocExt.SelectByID2("Spline1@Sketch1", "EXTSKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
     Set swSpline = swSelMgr.GetSelectedObject6(1, 0)

    ' Get the handles on the spline
     swSplineHandle = swSpline.GetSplineHandles()
    For i = 0 To UBound(swSplineHandle)
        Debug.Print "Spline handle " & swSplineHandle(i).SplinePointNumber
         Debug.Print " X: " & swSplineHandle(i).X * 1000
         Debug.Print " Y: " & swSplineHandle(i).Y * 1000
         Debug.Print " Z: " & swSplineHandle(i).Z * 1000
        If (i = 0) Then
            swSplineHandle(i).X = -62.33246528 / 1000
             swSplineHandle(i).Y = -14.71944444 / 1000
        End If
        Debug.Print " Tangent magnitude: " & swSplineHandle(i).TangentMagnitude(swTangentMagnitudeDirection1)
         Debug.Print " Tangent radial direction: " & swSplineHandle(i).TangentRadialDirection
        If (i = 2) Then
                swSplineHandle(i).TangentMagnitude(swTangentMagnitudeDirection1) = (swSplineHandle(i).TangentMagnitude(swTangentMagnitudeDirection1)) + 0.02
                 swSplineHandle(i).TangentRadialDirection = swSplineHandle(i).TangentRadialDirection + 0.5
        End If

        Debug.Print " Curvature: " & swSplineHandle(i).Curvature
         Debug.Print " Radius of curvature: " & swSplineHandle(i).RadiusOfCurvature

         If (i = 3) Then
             swSplineHandle(i).RadiusOfCurvature = swSplineHandle(i).RadiusOfCurvature / 2
        End If

        If (i = 3) Then
            Debug.Print " Tangent driving? " & swSplineHandle(i).TangentDriving
            If (swSplineHandle(i).TangentDriving) Then
                 swSplineHandle(i).TangentDriving = False
             Else
                 swSplineHandle(i).TangentDriving = True
             End If
            swSplineHandle(i).Reset

        End If
    Next

End Sub
```
