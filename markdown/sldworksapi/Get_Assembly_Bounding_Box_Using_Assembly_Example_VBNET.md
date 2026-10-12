---
title: "Get Assembly Bounding Box Using Assembly Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Assembly_Bounding_Box_Using_Assembly_Example_VBNET.htm"
---

# Get Assembly Bounding Box Using Assembly Example (VB.NET)

This example shows how to get the box bounding an assembly using the assembly.

```
'--------------------------------------------
' Preconditions:
' 1. Open an assembly document.
' 2. Open the Immediate window.
' 3. Run the macro.
'
' Postconditions:
' 1. Adds a 3D sketch to the assembly showing the bounding box.
' 2. Examine the graphics area and Immediate window to verify.
'
' NOTE: The bounding box for the assembly is approximated
' and is oriented with the assembly coordinate system.
'----------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swAssy As AssemblyDoc
        Dim vBox As Object
        Dim X_max As Double
        Dim X_min As Double
        Dim Y_max As Double
        Dim Y_min As Double
        Dim Z_max As Double
        Dim Z_min As Double
        Dim swSketchMgr As SketchManager
        Dim swSketchPt(8) As SketchPoint
        Dim swSketchSeg(12) As SketchSegment

        swModel = swApp.ActiveDoc
        swAssy = swModel

        vBox = swAssy.GetBox(swBoundingBoxOptions_e.swBoundingBoxIncludeRefPlanes)

        ' Initialize values
        X_max = vBox(3)
        X_min = vBox(0)
        Y_max = vBox(4)
        Y_min = vBox(1)
        Z_max = vBox(5)
        Z_min = vBox(2)

        Debug.Print("Assembly Bounding Box (" + swModel.GetPathName + ") = ")
        Debug.Print("  (" + Str(X_min * 1000.0#) + "," + Str(Y_min * 1000.0#) + "," + Str(Z_min * 1000.0#) + ") mm")
        Debug.Print("  (" + Str(X_max * 1000.0#) + "," + Str(Y_max * 1000.0#) + "," + Str(Z_max * 1000.0#) + ") mm")
        swSketchMgr = swModel.SketchManager

        swSketchMgr.Insert3DSketch(True)
        swSketchMgr.AddToDB = True

        ' Draw points at each corner of bounding box
        swSketchPt(0) = swSketchMgr.CreatePoint(X_min, Y_min, Z_min)
        swSketchPt(1) = swSketchMgr.CreatePoint(X_min, Y_min, Z_max)
        swSketchPt(2) = swSketchMgr.CreatePoint(X_min, Y_max, Z_min)
        swSketchPt(3) = swSketchMgr.CreatePoint(X_min, Y_max, Z_max)
        swSketchPt(4) = swSketchMgr.CreatePoint(X_max, Y_min, Z_min)
        swSketchPt(5) = swSketchMgr.CreatePoint(X_max, Y_min, Z_max)
        swSketchPt(6) = swSketchMgr.CreatePoint(X_max, Y_max, Z_min)
        swSketchPt(7) = swSketchMgr.CreatePoint(X_max, Y_max, Z_max)

        ' Draw bounding box
        swSketchSeg(0) = swSketchMgr.CreateLine(X_min, Y_min, Z_min, X_max, Y_min, Z_min)
        swSketchSeg(1) = swSketchMgr.CreateLine(X_max, Y_min, Z_min, X_max, Y_min, Z_max)
        swSketchSeg(2) = swSketchMgr.CreateLine(X_max, Y_min, Z_max, X_min, Y_min, Z_max)
        swSketchSeg(3) = swSketchMgr.CreateLine(X_min, Y_min, Z_max, X_min, Y_min, Z_min)
        swSketchSeg(4) = swSketchMgr.CreateLine(X_min, Y_min, Z_min, X_min, Y_max, Z_min)
        swSketchSeg(5) = swSketchMgr.CreateLine(X_min, Y_min, Z_max, X_min, Y_max, Z_max)
        swSketchSeg(6) = swSketchMgr.CreateLine(X_max, Y_min, Z_min, X_max, Y_max, Z_min)
        swSketchSeg(7) = swSketchMgr.CreateLine(X_max, Y_min, Z_max, X_max, Y_max, Z_max)
        swSketchSeg(8) = swSketchMgr.CreateLine(X_min, Y_max, Z_min, X_max, Y_max, Z_min)
        swSketchSeg(9) = swSketchMgr.CreateLine(X_max, Y_max, Z_min, X_max, Y_max, Z_max)
        swSketchSeg(10) = swSketchMgr.CreateLine(X_max, Y_max, Z_max, X_min, Y_max, Z_max)
        swSketchSeg(11) = swSketchMgr.CreateLine(X_min, Y_max, Z_max, X_min, Y_max, Z_min)

        swSketchMgr.AddToDB = False
        swSketchMgr.Insert3DSketch(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
