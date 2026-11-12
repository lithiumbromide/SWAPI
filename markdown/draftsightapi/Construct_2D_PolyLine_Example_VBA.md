---
title: "Construct 2D PolyLine Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Construct_2D_PolyLine_Example_VBA.htm"
---

# Construct 2D PolyLine Example (VBA)

This example shows how to construct a 2D PolyLine in a drawing document.

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
' Postconditions: A message box pops up when a 2D PolyLine is
' constructed in the drawing document.
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
    Dim dsPolyline As DraftSight.PolyLine
    Dim coordinates(0 To 7) As Double
    Dim closed As Boolean
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
        '2D PolyLine parameters
        coordinates(0) = 0: coordinates(1) = 2
        coordinates(2) = 0: coordinates(3) = 0
        coordinates(4) = 6: coordinates(5) = 0
        coordinates(6) = 6: coordinates(7) = 2
        closed = True
```

```
        'Construct a 2D PolyLine
        Set dsPolyline = dsSketchManager.InsertPolyline2D(coordinates, closed)
```

```
        If Not dsPolyline Is Nothing Then
            MsgBox "2D PolyLine was added to drawing."
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
