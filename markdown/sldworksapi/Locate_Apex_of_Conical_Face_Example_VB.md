---
title: "Locate Apex of Conical Face Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Locate_Apex_of_Conical_Face_Example_VB.htm"
---

# Locate Apex of Conical Face Example (VBA)

This example shows how to locate the apex of a conical face.

```vb
'----------------------------------------------
 ' Preconditions:
 ' 1. Open a part or assembly containing a conical face.
 ' 2. Select the conical face.
 ' 3. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a 3D sketch with a single point at the apex of
 '    the conical face.
 ' 2. Examine the Immediate window.
 '
 ' NOTE: Conical face can be truncated.
 '------------------------------------------------
Option Explicit

Sub main()

    Dim swApp                   As SldWorks.SldWorks
    Dim swMathUtil              As SldWorks.MathUtility
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swSelMgr                As SldWorks.SelectionMgr
    Dim swFace                  As SldWorks.face2
    Dim swSurf                  As SldWorks.surface
    Dim vCone                   As Variant
    Dim nAxis(2)                As Double
    Dim vAxis                   As Variant
    Dim swAxis                  As SldWorks.MathVector
    Dim nOrigin(2)              As Double
    Dim vOrigin                 As Variant
    Dim swOrigin                As SldWorks.MathPoint
    Dim swApex                  As SldWorks.MathPoint
    Dim swApexPt                As SldWorks.SketchPoint

    Set swApp = Application.SldWorks
    Set swMathUtil = swApp.GetMathUtility
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFace = swSelMgr.GetSelectedObject5(1)
    Set swSurf = swFace.GetSurface: Debug.Assert swSurf.IsCone

    vCone = swSurf.ConeParams

    nOrigin(0) = vCone(0):  nOrigin(1) = vCone(1):  nOrigin(2) = vCone(2)
    vOrigin = nOrigin
    Set swOrigin = swMathUtil.CreatePoint((vOrigin))

    nAxis(0) = vCone(3):    nAxis(1) = vCone(4):    nAxis(2) = vCone(5)
    vAxis = nAxis
    Set swAxis = swMathUtil.CreateVector((vAxis))

    Set swAxis = swAxis.Scale(vCone(6) / Tan(vCone(7)))

    Set swApex = swOrigin.AddVector(swAxis)

    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  origin         = (" & vCone(0) * 1000# & ", " & vCone(1) * 1000# & ", " & vCone(2) * 1000# & ") mm"
    Debug.Print "  axis           = (" & vCone(3) & ", " & vCone(4) & ", " & vCone(5) & ")"
    Debug.Print "  radius         = " & vCone(6) * 1000# & " mm"
    ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
    Debug.Print "  half angle     = " & vCone(7) * 57.3 & " deg"
    Debug.Print "  Apex           = " & swApex.ArrayData(0) * 1000# & ", " & swApex.ArrayData(1) * 1000# & ", " & swApex.ArrayData(2) * 1000# & ") mm"

    swModel.Insert3DSketch2 False
    swModel.SetAddToDB True

    Set swApexPt = swModel.CreatePoint2(swApex.ArrayData(0), swApex.ArrayData(1), swApex.ArrayData(2))

    swModel.SetAddToDB False
    swModel.Insert3DSketch2 True
End Sub
```
