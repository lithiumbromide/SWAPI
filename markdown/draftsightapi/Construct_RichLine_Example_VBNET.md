---
title: "Construct RichLine Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_RichLine_Example_VBNET.htm"
---

# Construct RichLine Example (VB.NET)

This example shows how to construct a RichLine.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Start DraftSight and open a document.
' 5. Start debugging the project.
'
' Postconditions: A message box pops up when a RichLine is
' constructed in the drawing document.
'----------------------------------------------------------------
```

```
Imports DraftSight.Interop.dsAutomation
```

```
Module Module1
```

```
    Sub Main()
        Dim dsApp As Application
        Dim dsDoc As Document
        Dim dsModel As Model
        Dim dsSketchManager As SketchManager
        Dim dsRichLine As RichLine
        Dim coordinates(0 To 5) As Double
        Dim justification As dsRichLineJustification_e
        Dim closed As Boolean
        Dim scaleValue As Double
        Dim styleName As String
```

```
        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")
	dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands
```

```
        'Get active document
        dsDoc = dsApp.GetActiveDocument()
        If Not dsDoc Is Nothing Then
```

```
            'Get model space
            dsModel = dsDoc.GetModel()
```

```
            'Get Sketch Manager
            dsSketchManager = dsModel.GetSketchManager()
```

```
            'RichLine parameters
            coordinates(0) = 0 : coordinates(1) = 0 : coordinates(2) = 0
            coordinates(3) = 7 : coordinates(4) = 7 : coordinates(5) = 0
            justification = dsRichLineJustification_e.dsRichLineJustification_Bottom
            scaleValue = 1.0#
            styleName = "Standard"
            closed = False
```

```
            'Add a RichLine
            dsRichLine = dsSketchManager.InsertRichLine(coordinates, justification, scaleValue, styleName, closed)
```

```
            If Not dsRichLine Is Nothing Then
                MsgBox("RichLine was added to drawing.")
            End If
```

```
        Else
```

```
            MsgBox("There are no open documents in DraftSight.")
```

```
        End If
    End Sub
```

```
End Module
```
