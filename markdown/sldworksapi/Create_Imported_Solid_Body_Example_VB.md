---
title: "Create Imported Solid Body Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Imported_Solid_Body_Example_VB.htm"
---

# Create Imported Solid Body Example (VBA)

This example shows how to create an imported solid body in the shape of a pyramid.

```
'-----------------------------------------------
' Preconditions:  Verify that the specified part
' document template exists.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Creates a pyramid-shaped, imported, solid body.
'------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim swBody As SldWorks.Body2
    Dim nPt() As Double
    Dim vPt As Variant
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\part.prtdot", 0, 0, 0)
    Set swPart = swModel
    Set swBody = swPart.CreateNewBody
```

```
    ' Front
    ReDim nPt(8)
    nPt(0) = 0#:    nPt(1) = 0#:    nPt(2) = 1#
    nPt(3) = -1#:   nPt(4) = -1#:   nPt(5) = 0#
    nPt(6) = 1#:    nPt(7) = -1#:   nPt(8) = 0#
    vPt = nPt
    bRet = swBody.CreatePlanarTrimSurfaceDLL((vPt), Empty)
```

```
    ' Left
    ReDim nPt(8)
    nPt(0) = 0#:    nPt(1) = 0#:    nPt(2) = 1#
    nPt(3) = -1#:   nPt(4) = -1#:   nPt(5) = 0#
    nPt(6) = -1#:   nPt(7) = 1#:    nPt(8) = 0#
    vPt = nPt
    bRet = swBody.CreatePlanarTrimSurfaceDLL((vPt), Empty)
```

```
    ' Back
    ReDim nPt(8)
    nPt(0) = 0#:    nPt(1) = 0#:    nPt(2) = 1#
    nPt(3) = -1#:   nPt(4) = 1#:    nPt(5) = 0#
    nPt(6) = 1#:    nPt(7) = 1#:    nPt(8) = 0#
    vPt = nPt
    bRet = swBody.CreatePlanarTrimSurfaceDLL((vPt), Empty)
```

```
    ' Right
    ReDim nPt(8)
    nPt(0) = 0#:    nPt(1) = 0#:    nPt(2) = 1#
    nPt(3) = 1#:    nPt(4) = 1#:    nPt(5) = 0#
    nPt(6) = 1#:    nPt(7) = -1#:   nPt(8) = 0#
    vPt = nPt
    bRet = swBody.CreatePlanarTrimSurfaceDLL((vPt), Empty)
```

```
    ' Bottom
    ReDim nPt(11)
    nPt(0) = -1#:   nPt(1) = -1#:   nPt(2) = 0#
    nPt(3) = -1#:   nPt(4) = 1#:    nPt(5) = 0#
    nPt(6) = 1#:    nPt(7) = 1#:    nPt(8) = 0#
    nPt(9) = 1#:    nPt(10) = -1#:  nPt(11) = 0#
    vPt = nPt
    bRet = swBody.CreatePlanarTrimSurfaceDLL((vPt), Empty)
```

```
    bRet = swBody.CreateBodyFromSurfaces
```

```
    swModel.ViewZoomtofit2
```

```
End Sub
```
