---
title: "Create Highlight Selection Set Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Highlight_Selection_Set_Example_VBA.htm"
---

# Create Highlight Selection Set Example (VBA)

This example shows how to create a highlight selection set.

```
'--------------------------------------------------------------
' Preconditions:
'  1. Create a VBA macro in a software product in which VBA is
'     embedded.
'  2. Copy and paste this example into the Visual Basic IDE.
'  3. Add a reference to the DraftSight type library,
'     install_dir\bin\dsAutomation.dll.
'  4. Start DraftSight.
'  5. Run the macro.
'
' Postconditions:
'  1. Connects to DraftSight.
'  2. Gets active document.
'  3. Gets Sketch Manager.
'  4. Inserts a Circle and an Arc.
'  5. Creates an instance of a highlight selection set.
'  6. Adds Arc to the highlight selection set.
'  7. Move the pointer over both the Arc and Circle. Only the Arc
'     is highlighted. Press F5 to continue.
'  8. Removes Arc from highlight selection set.
'  9. Adds Circle to highlight selection set.
' 10. Move the pointer over both the Arc and Circle. Only
'     the Circle is highlighted.
'--------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
        Dim dsApp As DraftSight.Application
```

```
        'Connect to DraftSight application
        Set dsApp = GetObject(, "DraftSight.Application")
        If dsApp Is Nothing Then
            Return
        End If
```

```
        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand
```

```
        'Get active document
        Dim dsDoc As DraftSight.Document
        Set dsDoc = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MsgBox ("There are no open documents in DraftSight.")
            Return
        End If
```

```
        'Get Sketch Manager
        Dim dsSketchMgr As DraftSight.SketchManager
        Set dsSketchMgr = dsDoc.GetModel.GetSketchManager
```

```
        'Construct Circle and Arc
        Dim dsCircle As DraftSight.Circle
        Dim dsCircleArc As DraftSight.CircleArc
        Set dsCircle = dsSketchMgr.InsertCircle(5#, 5#, 0#, 10#)
        Set dsCircleArc = dsSketchMgr.InsertArc(7.5, 7.5, 0#, 10#, 2.5, 5#)
        dsApp.Zoom dsZoomRange_Bounds, Nothing, Nothing
```

```
        'Create highlight selection set
        Dim dsEntities(1) As Object
        Set dsEntities(0) = dsCircleArc
```

```
        Dim dsHighlightSet As DraftSight.HighlightSet
        Set dsHighlightSet = dsDoc.CreateHighlightSet(dsEntities)
        dsHighlightSet.Highlight = True
        dsDoc.Rebuild dsRebuildType_AllViewports
```

```
        Stop
        'Move pointer over the Arc and Circle
        'Only the Arc is highlighted
        'Press F5 to continue
```

```
        'Remove entities from highlight selection set
        dsHighlightSet.RemoveEntities dsEntities
        dsDoc.Rebuild dsRebuildType_AllViewports
```

```
        'Add Circle to highlight selection set
        Set dsEntities(0) = Nothing
        Set dsEntities(0) = dsCircle
        dsHighlightSet.AddEntities dsEntities
        dsHighlightSet.Highlight = True
        dsDoc.Rebuild dsRebuildType_AllViewports
```

```
        'Move pointer over the Arc and Circle
        'Only the Circle is highlighted
```

```
End Sub
```
