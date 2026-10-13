---
title: "Get Coordinates of the Plane's Bounding Box Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Coordinates_of_the_Plane's_Bounding_Box_Example_VBNET.htm"
---

# Get Coordinates of the Plane's Bounding Box Example (VB.NET)

This example shows how to get top-left and bottom-right coordinates for a reference plane's bounding box.

```
'-----------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document template
'    exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Inserts a reference plane.
' 3. Gets the top-left and bottom-right coordinates
'    of the reference plane's bounding box.
' 4. Examine the Immediate window.
'------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swFeatureMgr As FeatureManager
        Dim swRefPlane As RefPlane
        Dim swModelDocExt As ModelDocExtension
        Dim status As Boolean
        Dim mathPoints() As Object
        Dim arrData() As Double
        Dim i As Integer

        'Create reference plane
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
        swFeatureMgr = swModel.FeatureManager
        swRefPlane = swFeatureMgr.InsertRefPlane(8, 0.0889, 0, 0, 0, 0)

        'Get top-left and bottom-right coordinates
        'of the reference plane's bounding box
        mathPoints = swRefPlane.BoundingBox 'Two (2) MathPoint objects are always returned
        For i = 0 To UBound(mathPoints)
            arrData = mathPoints(i).arrayData
            Debug.Print(" Points x, y, z = " & arrData(0) & ", " & arrData(1) & ", " & arrData(2))
        Next i
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
