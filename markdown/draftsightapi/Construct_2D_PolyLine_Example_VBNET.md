---
title: "Construct 2D PolyLine Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_2D_PolyLine_Example_VBNET.htm"
---

# Construct 2D PolyLine Example (VB.NET)

This example shows how to construct a 2D PolyLine in a drawing document.

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
' Postconditions: A message box pops up when a 2D PolyLine is
' constructed in the drawing document.
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
        Dim dsPolyline As PolyLine
        Dim coordinates(0 To 7) As Double
        Dim closed As Boolean
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
            '2D PolyLine parameters
            coordinates(0) = 0 : coordinates(1) = 2
            coordinates(2) = 0 : coordinates(3) = 0
            coordinates(4) = 6 : coordinates(5) = 0
            coordinates(6) = 6 : coordinates(7) = 2
            closed = True
```

```
            'Construct a 2D PolyLine
            dsPolyline = dsSketchManager.InsertPolyline2D(coordinates, closed)
```

```
            If Not dsPolyline Is Nothing Then
                MsgBox("2D PolyLine was added to drawing.")
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
