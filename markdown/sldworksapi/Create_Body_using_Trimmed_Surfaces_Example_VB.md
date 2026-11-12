---
title: "Create Body using Trimmed Surfaces Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Body_using_Trimmed_Surfaces_Example_VB.htm"
---

# Create Body using Trimmed Surfaces Example (VBA)

## Create Body Using Trimmed Surfaces Example (VBA)

The basic outline for creating a body using trimmed surfaces is as follows:

1. Create a new temporary body in a part using IPartDoc::CreateNewBody.
2. Create trimmed surfaces to create a body (for example, create six square surfaces that intersect at the edges to form a cube):

  1. Create a planar surface using IBody2::CreatePlanarSurface(RootPoint, Normal).
  2. Add a trimming loop to the planar surface using
    ISurface::AddTrimmingLoop2(Numcurves, _
    Order, _
    Dimen, _
    Periodic, _
    NumKnots, _
    NumCtrlPoints, _
    Knots, _
    CtrlPointDbls, _
    UVRange)
  3. The arguments for Surface::AddTrimmingLoop2 and their values for a square trimming loop are:

    | Argument | Description |
    | --- | --- |
    | NumCurves | Number of spline curves that make up the trimming loop (Long 4) |
    | Order | Orders for the spline curves ({2, 2, 2, 2} Array of Longs. Second-order linear curves) |
    | Dimen | Dimension of the control points for the spline curves ({2, 2, 2, 2} Array of Longs) |
    | Periodic | Periodicity of the spline curves ({0, 0, 0, 0} Array of Longs) |
    | NumKnots | Number of knots of the spline curves ({4, 4, 4, 4} Array of Longs) |
    | NumCtrlPoints | Number of control points for the spline curves ({2, 2, 2, 2} Array of Longs) |
    | Knots | Describes the locations of the knots on the spline curves ({0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1} Array of Doubles. Each spline curve contains 4 knots) |
    | CtrlPointDbls | Coordinates of control points for the square trimming loop ({0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0} Array of Doubles. (Two for each spline curve of the square trimming loop * Dimen) = 16 coordinates for the square trimming loop) |
    | UVRange | Min and max for the U and V values ({0, 1, 0, 1} Array of Doubles) |
  4. Create a trimmed surface on the body based on the trimming loop that was just created.
3. Sew the surfaces together into a new body using IBody2::CreateBodyFromSurfaces.

This example shows how to create trimmed surfaces and use them to create bodies.

```
'-------------------------------------------------------------
' Preconditions: Verify that the specified
' part document template exists.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Creates a temporary body.
' 3. Creates six trimmed surfaces. For each:
'    a. Creates a planar surface.
'    b. Adds a trimming loop to the planar surface.
'    c. Creates a trimmed surface on the temporary body based
'       on the trimming loop.
' 4. Sews the six trimmed surfaces together to form a new cube body.
' 5. Creates a trimmed surface that is offset from the back of the cube.
' 6. Examine the FeatureManager design tree and
'    graphics area.
'----------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Model As SldWorks.ModelDoc2
Dim Part As SldWorks.PartDoc
Dim RootPoint(2) As Double
Dim Normal(2) As Double
Dim TempBody As SldWorks.Body2
Dim isGood As Boolean
```

```
Sub main()
```

```
   'Get the SOLIDWORKS application
    Set swApp = CreateObject("SldWorks.Application")
    swApp.UserControl = True
```

```
    'Create a new blank document
    Set swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2020\templates\part.prtdot", 0, 0, 0)
    Set Part = Model
```

```
    'Create a new temporary body in the part
    Set TempBody = Part.CreateNewBody
```

```
    If TempBody Is Nothing Then
        MsgBox "Could not create the new body."
        Exit Sub
    End If
```

```
    'Create the trimmed surfaces for a cube with one meter length sides

    'LEFT
    RootPoint(0) = 0 'X
    RootPoint(1) = 0 'Y
    RootPoint(2) = 0 'Z
    Normal(0) = 1 'X
    Normal(1) = 0 'Y
    Normal(2) = 0 'Z
    isGood = CreateSquareSurface(Part, TempBody, RootPoint, Normal, True)
```

```
    'RIGHT
    RootPoint(0) = 1
    RootPoint(1) = 0
    RootPoint(2) = 0
    Normal(0) = 1
    Normal(1) = 0
    Normal(2) = 0
    isGood = CreateSquareSurface(Part, TempBody, RootPoint, Normal, True)
```

```
    'BOTTOM
    RootPoint(0) = 0
    RootPoint(1) = 0
    RootPoint(2) = -1
    Normal(0) = 0
    Normal(1) = 1
    Normal(2) = 0
    isGood = CreateSquareSurface(Part, TempBody, RootPoint, Normal, True)
```

```
    'TOP
    RootPoint(0) = 0
    RootPoint(1) = 1
    RootPoint(2) = -1
    Normal(0) = 0
    Normal(1) = 1
    Normal(2) = 0
    isGood = CreateSquareSurface(Part, TempBody, RootPoint, Normal, True)
```

```
    'FRONT
    RootPoint(0) = 0
    RootPoint(1) = 0
    RootPoint(2) = 0
    Normal(0) = 0
    Normal(1) = 0
    Normal(2) = 1
    isGood = CreateSquareSurface(Part, TempBody, RootPoint, Normal, True)
```

```
    'BACK
    RootPoint(0) = 0
    RootPoint(1) = 0
    RootPoint(2) = -1
    Normal(0) = 0
    Normal(1) = 0
    Normal(2) = 1
    isGood = CreateSquareSurface(Part, TempBody, RootPoint, Normal, True)
```

```
    'Create the body using the trimmed surfaces just created
    TempBody.CreateBodyFromSurfaces
```

```
    'Create an offset surface from the back of the cube body
    RootPoint(0) = 0
    RootPoint(1) = 0
    RootPoint(2) = -2
    Normal(0) = 0
    Normal(1) = 0
    Normal(2) = 1
    isGood = CreateSquareSurface(Part, TempBody, RootPoint, Normal, False)

    Model.ViewZoomtofit2
```

```
    'Clean up the memory
    Set swApp = Nothing
    Set Model = Nothing
    Set Part = Nothing
```

```
End Sub
```

```
'CreateSquareSurface creates a square trimmed surface

Private Function CreateSquareSurface(Part As PartDoc, SurfaceBody As Body2, RootPoint As Variant, Normal As Variant, IsPartOfTempBody As Boolean) As Boolean
```

```
    Dim isGood As Boolean
```

```
    'Temporary surface
    Dim TmpSurf As SldWorks.Surface
```

```
    'Arguments that define the trimming loop
    Dim NumCurves As Long
    Dim Order(3) As Long
    Dim Dimen(3) As Long
    Dim Periodic(3) As Long
    Dim NumKnots(3) As Long
    Dim NumCtrlPoints(3) As Long
    Dim Knots(15) As Double
    Dim CtrlPointDbls(15) As Double
    Dim UVRange(3) As Double
```

```
   'Initially this function has no problems,
   'set this value to false if errors encountered
    CreateSquareSurface = True
```

```
   'Create a new planar surface based at RootPoint with the normal vector Normal
    Set TmpSurf = SurfaceBody.CreatePlanarSurface(RootPoint, Normal)
    If TmpSurf Is Nothing Then
        CreateSquareSurface = False
        Exit Function
    End If
```

```
    'Set the arguments to define a square trimming loop

   'There are four spline curves (four sides) in the square
    NumCurves = 4
```

```
    'Order of each of the four sides of the square
    Order(0) = 2
    Order(1) = 2
    Order(2) = 2
    Order(3) = 2
```

```
    'Dimensions for the control points of each side of the square
    Dimen(0) = 2
    Dimen(1) = 2
    Dimen(2) = 2
    Dimen(3) = 2
```

```
    'Non-periodic sides of the square
    Periodic(0) = 0
    Periodic(1) = 0
    Periodic(2) = 0
    Periodic(3) = 0
```

```
    'Number of knots in each side of the square
    NumKnots(0) = 4
    NumKnots(1) = 4
    NumKnots(2) = 4
    NumKnots(3) = 4
```

```
    'Number of control points in each side of the square
    NumCtrlPoints(0) = 2
    NumCtrlPoints(1) = 2
    NumCtrlPoints(2) = 2
    NumCtrlPoints(3) = 2
```

```
    'Sixteen knots, four for each side of the square
    Knots(0) = 0
    Knots(1) = 0
    Knots(2) = 1
    Knots(3) = 1
    Knots(4) = 0
    Knots(5) = 0
    Knots(6) = 1
    Knots(7) = 1
    Knots(8) = 0
    Knots(9) = 0
    Knots(10) = 1
    Knots(11) = 1
    Knots(12) = 0
    Knots(13) = 0
    Knots(14) = 1
    Knots(15) = 1
```

```
    '16 control point coordinates for the square
    CtrlPointDbls(0) = 0: CtrlPointDbls(1) = 0
    CtrlPointDbls(2) = 1: CtrlPointDbls(3) = 0
    CtrlPointDbls(4) = 1: CtrlPointDbls(5) = 0
    CtrlPointDbls(6) = 1: CtrlPointDbls(7) = 1
    CtrlPointDbls(8) = 1: CtrlPointDbls(9) = 1
    CtrlPointDbls(10) = 0: CtrlPointDbls(11) = 1
    CtrlPointDbls(12) = 0: CtrlPointDbls(13) = 1
    CtrlPointDbls(14) = 0: CtrlPointDbls(15) = 0
```

```
    'UV ranges
    UVRange(0) = 0
    UVRange(1) = 1
    UVRange(2) = 0
    UVRange(3) = 1
```

```
    'Create the trimming loop on the surface
    isGood = TmpSurf.AddTrimmingLoop2(NumCurves, Order, Dimen, Periodic, NumKnots, NumCtrlPoints, Knots, CtrlPointDbls, UVRange)
    If isGood = False Then
        CreateSquareSurface = False
        Exit Function
    End If

    'Create the trimmed surface on the body
    'based on the trimming loop just created
    isGood = SurfaceBody.CreateTrimmedSurface
    If isGood = False Then
        CreateSquareSurface = False
        Exit Function
    End If

    If IsPartOfTempBody Then
       'If this surface is to be used in
       'a temporary body, then you must generate it
    Else
        SurfaceBody.CreateBodyFromSurfaces
    End If
```

```
End Function
```
