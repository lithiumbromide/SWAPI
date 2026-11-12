---
title: "Set Radial Dimension Leader Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Edit_Radial_Dimension_Example_VBNET.htm"
---

# Set Radial Dimension Leader Example (VB.NET)

This example shows how to attach a radial dimension leader to an arc extension line.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Edits the sketch and creates a fillet.
' 3. Attaches the radial dimension leader to the arc extension
'    leader.
' 4. Gets whether the radial dimension leader is attached to
'    the arc extension leader.
' 5. Examine the graphics area, then press F5.
' 6. Exits the sketch.
' 7. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchManager As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim swSelectionMgr As SelectionMgr
        Dim swDisplayDimension As DisplayDimension
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        'Open the part
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        'Edit the sketch and create a fillet
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        swModel.EditSketch()
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Point1", "SKETCHPOINT", -0.0811067833265636, 0.0389478433654258, 0, False, 0, Nothing, 0)
        swSketchManager = swModel.SketchManager
        swSketchSegment = swSketchManager.CreateFillet(0.01, swConstrainedCornerAction_e.swConstrainedCornerDeleteGeometry)

        'Select and set the radial dimension
        status = swModelDocExt.SelectByID2("D1@Sketch1@box.SLDPRT", "DIMENSION", -5.09218235791179E-02, 2.23786104078373E-02, 6.93106363229314E-03, False, 0, Nothing, 0)
        Set swSelectionMgr = swModel.SelectionManager
        Set swDisplayDimension = swSelectionMgr.GetSelectedObject6(1, -1)
        swDisplayDimension.ArcExtensionLineOrOppositeSide = True
        Debug.Print "Leader attached to arc extension line? " & swDisplayDimension.ArcExtensionLineOrOppositeSide
```

```
        Stop
        'Examine the graphics area, then press F5

        'Exit the sketch
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
