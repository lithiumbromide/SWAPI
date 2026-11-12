---
title: "Insert Ray Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Ray_Example_VBNET.htm"
---

# Insert Ray Example (VB.NET)

This example shows how to insert a Ray in a drawing document.

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
' Postconditions: A message box pops up when a Ray is
' inserted in the drawing document.
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
        Dim dsRay As Ray
        Dim startX, startY, startZ, throughX, throughY, throughZ As Double
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
            'Ray parameters
            startX = 0.0#
            startY = 0.0#
            startZ = 0.0#
            throughX = 2.0#
            throughY = 3.0#
            throughZ = 0.0#
```

```
            'Add a Ray
            dsRay = dsSketchManager.InsertRay(startX, startY, startZ, throughX, throughY, throughZ)
```

```
            If Not dsRay Is Nothing Then
                MsgBox("Ray was added to drawing.")
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
