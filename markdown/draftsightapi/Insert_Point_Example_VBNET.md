---
title: "Insert Point Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Insert_Point_Example_VBNET.htm"
---

# Insert Point Example (VB.NET)

This example shows how to insert a point in a drawing.

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
' Postconditions: A message box pops up when a point is
' inserted in the drawing document. A SimpleNote is also
' added to the drawing that identifies where the point was inserted.
'----------------------------------------------------------------
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
        Dim dsPoint As Point
        Dim x, y, z As Double
        Dim dsSimpleNote As SimpleNote
        Dim noteValue As String
        Dim angle, height As Double
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
            'Point parameters
            x = 5.0#
            y = 5.0#
            z = 0.0#
```

```
            'Add a point
            dsPoint = dsSketchManager.InsertPoint(x, y, z)
```

```
            'SimpleNote parameters (angle value should be passed in radians)
            noteValue = "Sample text"
            angle = 3.14159265358979 / 4 '45 degrees in radians
            height = 1.0#

            'Add a SimpleNote
            dsSimpleNote = dsSketchManager.InsertSimpleNote(x, y, z, height, angle, noteValue)
```

```
            If Not dsPoint Is Nothing Then
                MsgBox("Point was added to drawing where SimpleNote was added.")
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
