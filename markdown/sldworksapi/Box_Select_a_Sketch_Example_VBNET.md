---
title: "Box Select a Sketch Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Box_Select_a_Sketch_Example_VBNET.htm"
---

# Box Select a Sketch Example (VB.NET)

This example shows how to box select all of the entities in a sketch block.

'-----------------------------------------------------------------------------
' Preconditions: Open `public_documents`**\samples\tutorial\blocks\piston_mechanism.sldblk**.
'
' Postconditions:
' 1. Opens and box selects **Sketch1**.
' 2. Examine the list of selected entities
' in the PropertyManager page.
' 3. Interactively quit editing the sketch without
' saving any changes.
' 4. Close the document.
'--------------------------------------

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System

Partial Class SolidWorksMacros

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim boolstatus As Boolean

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension

        ' Select the sketch and open it
        boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        swModel.EditSketch()
        swModel.ViewZoomtofit2()

        ' Box select the sketch
        boolstatus = swModelDocExt.SketchBoxSelect("-0.663893", "1.322001", "0.000000", "-0.395073", "0.698568", "0.000000")

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
