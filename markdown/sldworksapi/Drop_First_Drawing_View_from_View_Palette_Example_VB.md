---
title: "Drop First Drawing View from View Palette Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Drop_First_Drawing_View_from_View_Palette_Example_VB.htm"
---

# Drop First Drawing View from View Palette Example (VBA)

## Drop First Drawing View from View Palette Example

This example shows how to drop the first drawing view on the View Palette onto the drawing.

```vb
'-----------------------------
'
' Preconditions: Part or assembly document
'                are open. An empty drawing
'                is open and active. Part or
'                assembly document is
'                selected in View Palette.
'
' Postconditions: The first view in the View
'                Palette is placed on
'                drawing sheet.
'
'-----------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swDraw As DrawingDoc
Dim swNewView As View
Dim vPaletteNames As Variant

Sub main()

Set swApp = Application.SldWorks
Set swDraw = swApp.ActiveDoc

' Get the names of the drawing views on the View Palette
vPaletteNames = swDraw.GetDrawingPaletteViewNames()
Debug.Print "Names of the drawing views on the View Palette"
Debug.Print "before placing any on the drawing"
Debug.Print "============================================="

' Print the names of the current views on the View Palette to the Immediate window
PrintPaletteNames vPaletteNames

' Get the names of the drawing before and after dropping it on the drawing
Debug.Print " "
Debug.Print "Drawing view to place: " & vPaletteNames(0)
Debug.Print " "
' Drop the drawing view
Set swNewView = swDraw.DropDrawingViewFromPalette2(vPaletteNames(0), 0.1, 0.1, 0.1)
Debug.Print "New drawing view name: " & swNewView.Name

' Print the names of the remaining views on the View Palette to the Immediate window
vPaletteNames = swDraw.GetDrawingPaletteViewNames()
Debug.Print " "
Debug.Print "Names of the drawing views remaining on the View Palette"
Debug.Print "after placing one on the drawing"
Debug.Print "========================================================"
PrintPaletteNames vPaletteNames

End Sub

' Print the names of the current views on the View Palette to the Immediate window
Public Sub PrintPaletteNames(vPaletteNames As Variant)
Dim index As Long
For index = 0 To UBound(vPaletteNames)
Debug.Print "View Palette view: " & vPaletteNames(index)
Next

End Sub
```
