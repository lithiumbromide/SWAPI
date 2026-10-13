---
title: "Create Imported Solid Body Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Imported_Solid_Body_Example_VBNET.htm"
---

# Create Imported Solid Body Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swPart As PartDoc
        Dim swBody As Body2
        Dim nPt() As Double
        Dim vPt As Object
        Dim bRet As Boolean

        swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\part.prtdot", 0, 0, 0)
        swPart = swModel
        swBody = swPart.CreateNewBody
        ' Front
        ReDim nPt(8)
        nPt(0) = 0.0# : nPt(1) = 0.0# : nPt(2) = 1.0#
        nPt(3) = -1.0# : nPt(4) = -1.0# : nPt(5) = 0.0#
        nPt(6) = 1.0# : nPt(7) = -1.0# : nPt(8) = 0.0#
        vPt = nPt
        bRet = swBody.CreatePlanarTrimSurfaceDLL((vPt), Nothing)
        ' Left
        ReDim nPt(8)
        nPt(0) = 0.0# : nPt(1) = 0.0# : nPt(2) = 1.0#
        nPt(3) = -1.0# : nPt(4) = -1.0# : nPt(5) = 0.0#
        nPt(6) = -1.0# : nPt(7) = 1.0# : nPt(8) = 0.0#
        vPt = nPt
        bRet = swBody.CreatePlanarTrimSurfaceDLL((vPt), Nothing)
        ' Back
        ReDim nPt(8)
        nPt(0) = 0.0# : nPt(1) = 0.0# : nPt(2) = 1.0#
        nPt(3) = -1.0# : nPt(4) = 1.0# : nPt(5) = 0.0#
        nPt(6) = 1.0# : nPt(7) = 1.0# : nPt(8) = 0.0#
        vPt = nPt
        bRet = swBody.CreatePlanarTrimSurfaceDLL((vPt), Nothing)
        ' Right
        ReDim nPt(8)
        nPt(0) = 0.0# : nPt(1) = 0.0# : nPt(2) = 1.0#
        nPt(3) = 1.0# : nPt(4) = 1.0# : nPt(5) = 0.0#
        nPt(6) = 1.0# : nPt(7) = -1.0# : nPt(8) = 0.0#
        vPt = nPt
        bRet = swBody.CreatePlanarTrimSurfaceDLL((vPt), Nothing)
        ' Bottom
        ReDim nPt(11)
        nPt(0) = -1.0# : nPt(1) = -1.0# : nPt(2) = 0.0#
        nPt(3) = -1.0# : nPt(4) = 1.0# : nPt(5) = 0.0#
        nPt(6) = 1.0# : nPt(7) = 1.0# : nPt(8) = 0.0#
        nPt(9) = 1.0# : nPt(10) = -1.0# : nPt(11) = 0.0#
        vPt = nPt
        bRet = swBody.CreatePlanarTrimSurfaceDLL((vPt), Nothing)

        bRet = swBody.CreateBodyFromSurfaces

        swModel.ViewZoomtofit2()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
