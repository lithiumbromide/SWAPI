---
title: "Insert Ray Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Ray_Example_VBA.htm"
---

# Insert Ray Example (VBA)

This example shows how to insert a Ray in a drawing document.

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
' Postconditions: A message box pops up when a Ray is
' inserted in the drawing document.
'----------------------------------------------------------------
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
    Dim dsRay As DraftSight.Ray
    Dim startX, startY, startZ, throughX, throughY, throughZ As Double
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

        'Ray parameters
        startX = 0#
        startY = 0#
        startZ = 0#
        throughX = 2#
        throughY = 3#
        throughZ = 0#
```

```
        'Add a Ray
        Set dsRay = dsSketchManager.InsertRay(startX, startY, startZ, throughX, throughY, throughZ)
```

```
        If Not dsRay Is Nothing Then
            MsgBox "Ray was added to drawing."
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
