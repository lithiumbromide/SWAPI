---
title: "Set Radial Dimension Leader Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Edit_Radial_Dimension_Example_VB.htm"
---

# Set Radial Dimension Leader Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swDisplayDimension As SldWorks.DisplayDimension
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open the part
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    'Edit the sketch and create a fillet
    status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    swModel.EditSketch
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Point1", "SKETCHPOINT", -8.11067833265636E-02, 3.89478433654258E-02, 0, False, 0, Nothing, 0)
    Set swSketchManager = swModel.SketchManager
    Set swSketchSegment = swSketchManager.CreateFillet(0.01, swConstrainedCornerAction_e.swConstrainedCornerDeleteGeometry)
```

```
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
```

```
    'Exit the sketch
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
```

```
End Sub
```
