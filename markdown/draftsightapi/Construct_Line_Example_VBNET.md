---
title: "Construct Line Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_Line_Example_VBNET.htm"
---

# Construct Line Example (VB.NET)

This example shows how to construct a Line.

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
' Postconditions: A message box pops up when a Line is
' constructed and its color changed in the drawing document.
'----------------------------------------------------------------
Imports DraftSight.Interop.dsAutomation

Module Module1

    Sub Main()

        Dim dsApp As Application
        Dim dsDoc As Document
        Dim dsModel As Model
        Dim dsSketchManager As SketchManager
        Dim dsLine As Line
        Dim dsColor as Color
        Dim startX, startY, startZ, endX, endY, endZ As Double

        'Connect to DraftSight
        dsApp = GetObject(, "DraftSight.Application")
	dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands

        'Get active document
        dsDoc = dsApp.GetActiveDocument()

        If Not dsDoc Is Nothing Then
            'Get model space
            dsModel = dsDoc.GetModel()

            'Get Sketch Manager
            dsSketchManager = dsModel.GetSketchManager()

            'Line parameters
            startX = 1.0#
            startY = 1.0#
            startZ = 0.0#
            endX = 6.0#
            endY = 1.0#
            endZ = 0.0#
```

```
            'Construct a Line
            dsLine = dsSketchManager.InsertLine(startX, startY, startZ, endX, endY, endZ)

            If Not dsLine Is Nothing Then

                'Change line's color
                dsColor = dsLine.Color
                dsColor.SetNamedColor(dsNamedColor_e.dsNamedColor_Red)
                dsLine.Color = dsColor

                MsgBox("Line was added to drawing and its color changed to red.")

            End If
        Else
            MsgBox("There are no open documents in DraftSight.")
        End If
```

```
    End Sub
End Module
```
