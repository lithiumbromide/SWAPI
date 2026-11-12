---
title: "Box Select a Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Box_Select_a_Sketch_Example_VB.htm"
---

# Box Select a Sketch Example (VBA)

This example shows how to box select all of the entities in a sketch block.

```
'-----------------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\blocks\piston_mechanism.sldblk.
'
' Postconditions:
' 1. Opens and box selects Sketch1.
' 2. Examine the list of selected entities
'    in the PropertyManager page.
' 3. Interactively quit editing the sketch without
'    saving any changes.
' 4. Close the document.
'--------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim boolstatus As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    ' Select the sketch and open it
    boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    swModel.EditSketch
    swModel.ViewZoomtofit2
```

```
    ' Box select the sketch
    boolstatus = swModelDocExt.SketchBoxSelect("-0.663893", "1.322001", "0.000000", "-0.395073", "0.698568", "0.000000")
```

```
End Sub
```
