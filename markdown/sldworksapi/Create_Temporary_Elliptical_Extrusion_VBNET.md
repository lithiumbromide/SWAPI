---
title: "Create Temporary Elliptical Extrusion Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Temporary_Elliptical_Extrusion_VBNET.htm"
---

# Create Temporary Elliptical Extrusion Example (VB.NET)

This example shows how to create a temporary elliptical body.

```vb
 '------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document in SOLIDWORKS Design.
 ' 2. Open an Immediate Window.
 '
 ' Postconditions:
 ' 1. Creates a temporary elliptical extruded body.
 ' 2. Inspect the Immediate Window.
 '------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub Main()

         Dim swDocument As ModelDoc2
         Dim swPart As PartDoc
         Dim swModeler As Modeler

         Dim swCurve(0) As Curve
         Dim vCenter As Object
         Dim dMajorRadius As Double
         Dim dMinorRadius As Double
         Dim vMajorAxis As Object
         Dim vMinorAxis As Object
         Dim vEllipseParams As Object
         Dim aCenter(2) As Double
         Dim aMajorAxis(2) As Double
         Dim aMinorAxis(2) As Double
         Dim dStartParam As Double
         Dim dEndParam As Double
         Dim bIsClosed As Boolean
         Dim bIsPeriodic As Boolean
         Dim bStatus As Boolean

         swDocument = swApp.ActiveDoc

         If (swDocument Is Nothing) Then
             swDocument = swApp.NewPart
         End If

         If (swDocument.GetType <> swDocumentTypes_e.swDocPART)  Then
             Exit Sub
         End If

         swPart = swDocument
         swModeler = swApp.GetModeler

         aCenter(0) = 0.0#
         aCenter(1) = 0.0#
         aCenter(2) = 0.0#

         vCenter = aCenter

         dMajorRadius = 2.0#

         aMajorAxis(0) = 1.0#
         aMajorAxis(1) = 0.0#
         aMajorAxis(2) = 0.0#

         vMajorAxis = aMajorAxis

         dMinorRadius = 1.0#

         aMinorAxis(0) = 0.0#
         aMinorAxis(1) = 1.0#
         aMinorAxis(2) = 0.0#

         vMinorAxis = aMinorAxis

         swCurve(0) = swModeler.CreateEllipse(vCenter, dMajorRadius, dMinorRadius, vMajorAxis, vMinorAxis)

         If (swCurve(0) Is Nothing) Then
             Debug.Print(" No curve")
         Else

             Debug.Print("Curve:")
             Debug.Print("  is ellipse  = " & IIf(swCurve(0).IsEllipse = False, "False", "True"))
             Debug.Print("  type        = " & swCurve(0).Identity)
             Debug.Print("  is ellipse  = " & (swCurve(0).Identity = swCurveTypes_e.ELLIPSE_TYPE))
             Debug.Print("  trimmed     = " & IIf(swCurve(0).IsTrimmedCurve = False, "False", "True"))

             bStatus = swCurve(0).GetEndParams(dStartParam, dEndParam, bIsClosed, bIsPeriodic)

             Debug.Print("  start param = " & dStartParam)
             Debug.Print("  end   param = " & dEndParam)
             Debug.Print("  closed      = " & bIsClosed)
             Debug.Print("  periodic    = " & bIsPeriodic)

             Debug.Print("  length      = " & swCurve(0).GetLength3(dStartParam, dEndParam))

             If (Not (swCurve(0).IsEllipse = False)) Then
                 vEllipseParams = swCurve(0).GetEllipseParams

                 Debug.Print("  centre       = (" & vEllipseParams(0)   ", " & vEllipseParams(1) & ", " & vEllipseParams(2) & ")")
                 Debug.Print("  major radius = " & vEllipseParams(3))
                 Debug.Print("  major axis   = (" & vEllipseParams(4)   ", " & vEllipseParams(5) & ", " & vEllipseParams(6) & ")")
                 Debug.Print("  minor radius = " & vEllipseParams(7))
                 Debug.Print("  minor axis   = (" & vEllipseParams(8)   ", " & vEllipseParams(9) & ", " & vEllipseParams(10) & ")")
             End If

             Dim planeSurf As Surface
             Dim swMath As MathUtility
             Dim slotDepth As Double
             slotDepth = 0.01

             swMath = swApp.GetMathUtility

             Dim startArr(2) As Double
             Dim endArr(2) As Double
             Dim ptArr(2) As Double
             Dim dirArr(2) As Double

             ptArr(0) = 0.0#
             ptArr(1) = 0.0#
             ptArr(2) = 0.0#
             dirArr(0) = 0.0#
             dirArr(1) = 0.0#
             dirArr(2) = 1.0#
             startArr(0) = 1.0#
             startArr(1) = 0.0#
             startArr(2) = 0.0#

             planeSurf = swModeler.CreatePlanarSurface2((ptArr), (dirArr), (startArr))

             Dim profileBody As Body2
             Dim extrudedBody As Body2
             Dim dirVector As MathVector

             profileBody = planeSurf.CreateTrimmedSheet4((swCurve), True)

             dirArr(0) = 0.0#
             dirArr(1) = 0.0#
             dirArr(2) = -1.0#

             dirVector = swMath.CreateVector((dirArr))
             extrudedBody = swModeler.CreateExtrudedBody(profileBody, dirVector, slotDepth)
             extrudedBody.Display3(swDocument, RGB(1, 0, 0), 0)

         End If
         swDocument.ViewZoomtofit()
     End Sub

     Public swApp As SldWorks

 End  Class
```
