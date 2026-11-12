---
title: "Construct Line Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_Line_Example_VBA.htm"
---

# Construct Line Example (VBA)

This example shows how to construct a Line.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a drawing document.
' 5. Run the macro.
'
' Postconditions: A message box pops up when a Line is
' constructed and its color changed in the drawing document.
'----------------------------------------------------------------
Option Explicit

Sub main()

    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
    Dim dsModel As DraftSight.Model
    Dim dsSketchManager As DraftSight.SketchManager
    Dim dsLine As DraftSight.Line
    Dim dsColor As Color
    Dim startX, startY, startZ, endX, endY, endZ As Double
```

```
    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    'Get active document
    Set dsDoc = dsApp.GetActiveDocument()
    If Not dsDoc Is Nothing Then
```

```
        'Get model space
        Set dsModel = dsDoc.GetModel()
```

```
        'Get Sketch Manager
        Set dsSketchManager = dsModel.GetSketchManager()
```

```
        'Line parameters
        startX = 1#
        startY = 1#
        startZ = 0#
        endX = 6#
        endY = 1#
        endZ = 0#
```

```
        'Draw a line
        Set dsLine = dsSketchManager.InsertLine(startX, startY, startZ, endX, endY, endZ)

        If Not dsLine Is Nothing Then

            'Change line's color
            Set dsColor = dsLine.Color
            dsColor.SetNamedColor (dsNamedColor_Red)
            dsLine.Color = dsColor

            MsgBox "Line was added to drawing, and its color changed to red."

        End If
```

```
    Else
```

```
        MsgBox "There are no open documents in DraftSight."
```

```
    End If
End Sub
```
