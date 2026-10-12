---
title: "Select Face Using Intersecting Ray Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Face_Using_Intersecting_Ray_Example_VBNET.htm"
---

# Select Face Using Intersecting Ray Example (VB.NET)

This example shows how to select the first face that is intersected by a ray that starts at the specified point and runs parallel to the specified direction vector within the specified radius.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\box.sldrpt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Selects the first face intersected by a ray that starts
'    at the specified point and runs parallel to the specified
'    direction vector within the specified radius.
' 2. Examine the graphics area and Immediate window.
'-----------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim startPointX As Double
        Dim startPointY As Double
        Dim startPointZ As Double
        Dim rayVecX As Double
        Dim rayVecY As Double
        Dim rayVecZ As Double
        Dim radius As Double
        Dim status As Boolean

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension

        startPointX = 0.1
        startPointY = 0.0#
        startPointZ = 0.0#

        rayVecX = -1.0#
        rayVecY = 0.0#
        rayVecZ = 0.0#

        radius = 1.0#

        status = swModelDocExt.SelectByRay(startPointX, startPointY, startPointZ, rayVecX, rayVecY, rayVecZ, radius, swSelectType_e.swSelFACES, False, 0, swSelectOption_e.swSelectOptionDefault)
        Debug.Print("Selection status: " & status)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
