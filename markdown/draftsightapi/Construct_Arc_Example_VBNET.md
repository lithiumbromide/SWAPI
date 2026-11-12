---
title: "Construct Arc Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_Arc_Example_VBNET.htm"
---

# Construct Arc Example (VB.NET)

This example shows how to construct an Arc.

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
' Postconditions: A message box pops up when a Arc is
' constructed in the drawing document.
'----------------------------------------------------------------
Imports DraftSight.Interop.dsAutomation
```

```
Module Module1

    Sub Main()

        Dim dsApp As Application
        Dim dsDoc As Document
        Dim dsModel As Model
        Dim dsSketchManager As SketchManager
        Dim dsArc As CircleArc
        Dim centerX, centerY, centerZ, radius As Double
        Dim startAngle, endAngle As Double
```

```
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

            'Arc parameters (start and end angle values should be in radians)
            centerX = 0.0#
            centerY = 0.0#
            centerZ = 0.0#
            radius = 4.0#
            startAngle = 0.0#
            endAngle = 3.14159265358979 '180 degrees in radians
```

```
            'Construct an Arc
            dsArc = dsSketchManager.InsertArc(centerX, centerY, centerZ, radius, startAngle, endAngle)
```

```
            If Not dsArc Is Nothing Then
                MsgBox("An Arc was added to drawing.")
            End If
```

```
        Else
            MsgBox("There are no open documents in DraftSight.")
        End If
```

```
    End Sub
End Module
```
