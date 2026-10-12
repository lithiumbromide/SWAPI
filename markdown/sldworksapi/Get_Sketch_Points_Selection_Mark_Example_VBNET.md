---
title: "Get Sketch Point's Selection Mark Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Points_Selection_Mark_Example_VBNET.htm"
---

# Get Sketch Point's Selection Mark Example (VB.NET)

This example shows how to get the selection mark of a sketch point.

```
'------------------------------------------------
' Preconditions:
' 1. Open a part containing a sketch point.
' 2. Select the sketch containing the sketch point.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the selection mark of the sketch point.
' 2. Examine the Immediate window.
'-----------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swFeat As Feature
        Dim swSketch As Sketch
        Dim sketchPoints As Object
        Dim swSketchPt As SketchPoint
        Dim swSelData As SelectData
        Dim status As Boolean

        swModel = swApp.ActiveDoc
        swSelMgr = swModel.SelectionManager
        swFeat = swSelMgr.GetSelectedObject6(1, -1)
        swSketch = swFeat.GetSpecificFeature2
        sketchPoints = swSketch.GetSketchPoints2
        swSketchPt = sketchPoints(0)

        ' Get selection mark of sketch point
        swSelMgr = swModel.SelectionManager
        swSelData = swSelMgr.CreateSelectData
        status = swSketchPt.Select4(True, swSelData)
        Debug.Print("Selection mark of sketch point: " & swSelData.Mark)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
