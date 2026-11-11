---
title: "Construct RichLine Example Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_RichLine_Example_VBA.htm"
---

# Construct RichLine Example Example (VBA)

This example shows how to construct a RichLine.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a document.
' 5. Run the macro.
'
' Postconditions: A message box pops up when a RichLine is
' constructed in the drawing document.
'----------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim dsApp As DraftSight.Application
    Dim dsDoc As DraftSight.Document
    Dim dsModel As DraftSight.Model
    Dim dsSketchManager As DraftSight.SketchManager
    Dim dsRichLine As DraftSight.RichLine
    Dim coordinates(0 To 5) As Double
    Dim justification As DraftSight.dsRichLineJustification_e
    Dim closed As Boolean
    Dim scaleValue As Double
    Dim styleName As String
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
        'RichLine parameters
        coordinates(0) = 0: coordinates(1) = 0: coordinates(2) = 0
        coordinates(3) = 7: coordinates(4) = 7: coordinates(5) = 0
        justification = dsRichLineJustification_Bottom
        scaleValue = 1#
        styleName = "Standard"
        closed = False
```

```
        'Add a RichLine
        Set dsRichLine = dsSketchManager.InsertRichLine(coordinates, justification, scaleValue, styleName, closed)
```

```
        If Not dsRichLine Is Nothing Then
            MsgBox "RichLine was added to drawing."
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
```

```
End Sub
```
