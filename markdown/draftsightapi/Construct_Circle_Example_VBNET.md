---
title: "Construct Circle Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_Circle_Example_VBNET.htm"
---

# Construct Circle Example (VB.NET)

This example shows how to construct a Circle.

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
' Postconditions: A message box pops up when a Circle is
' constructed in the drawing document.
'----------------------------------------------------------------
Imports DraftSight.Interop.dsAutomation
```

```
Module Module1
```

```
    Sub Main()
```

```
        Dim dsApp As Application
        Dim dsDoc As Document
        Dim dsModel As Model
        Dim dsSketchManager As SketchManager
        Dim dsCircle As Circle
        Dim centerX, centerY, centerZ, radius As Double
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
            'Circle parameters
            centerX = 1.0#
            centerY = 2.0#
            centerZ = 0.0#
            radius = 5.0#
```

```
            'Construct a Circle
            dsCircle = dsSketchManager.InsertCircle(centerX, centerY, centerZ, radius)
```

```
            If Not dsCircle Is Nothing Then
                MsgBox("Circle was added to drawing.")
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
```

```
    End Sub
```

```
End Module
```
