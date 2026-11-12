---
title: "Construct InfiniteLine Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_InfiniteLine_Example_VBNET.htm"
---

# Construct InfiniteLine Example (VB.NET)

This example shows how to construct an InfiniteLine.

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
' Postconditions: A message box pops up when a InfiniteLine is
' constructed in the drawing document.
'----------------------------------------------------------------
Imports DraftSight.Interop.dsAutomation
Module Module1
    Sub Main()
        Dim dsApp As Application
        Dim dsDoc As Document
        Dim dsModel As Model
        Dim dsSketchManager As SketchManager
        Dim dsInfiniteLine As InfiniteLine
        Dim x1, y1, z1, x2, y2, z2 As Double
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
            'InfiniteLine parameters
            x1 = 0.0#
            y1 = 0.0#
            z1 = 0.0#
            x2 = 1.0#
            y2 = 5.0#
            z2 = 0.0#
```

```
            'Draw an InfiniteLine
            dsInfiniteLine = dsSketchManager.InsertInfiniteLine(x1, y1, z1, x2, y2, z2)
```

```
            If Not dsInfiniteLine Is Nothing Then
                MsgBox("InfiniteLine was added to drawing.")
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
