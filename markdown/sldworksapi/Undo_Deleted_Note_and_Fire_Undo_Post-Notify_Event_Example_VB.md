---
title: "Undo Deleted Note and Fire Undo Post-Notify Event Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_VB.htm"
---

# Undo Deleted Note and Fire Undo Post-Notify Event Example (VBA)

## Undo Deleted Note and Fire Undo Pre- and Post-notify Events Example (VBA)

This example demonstrates firing Undo pre- and post-notifications in a drawing document.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\AutoCAD\7550-021.slddrw.
' 2. Copy and paste Main into the main module.
' 3. Click Insert > Class Module and copy and paste Class1 into that module.
'
' Postconditions:
' 1. Selects and deletes the note in Drawing View1.
' 2. Undoes the deleted note.
' 3. Fires pre-notification event indicating that an undo action is about to
'    occur and fires post-notification event indicating that an undo
'    action occurred.
' 4. Click OK to close each message box.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
'Main
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDrawing As SldWorks.DrawingDoc
Dim boolstatus As Boolean
Dim swDrawingEvents As Class1
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    ' Event notification
    Set swDrawing = swModel
    Set swDrawingEvents = New Class1
    Set swDrawingEvents.swDrawing = swApp.ActiveDoc
```

```
    ' Activate the drawing view that contains
    ' the note you want to delete
    boolstatus = swDrawing.ActivateView("Drawing View1")
    boolstatus = swModelDocExt.SelectByID2("DetailItem66@Drawing View1", "NOTE", 0.357212931256279, 0.178674480463097, 0, False, 0, Nothing, 0)
```

```
    ' Delete the selected note
    swModel.EditDelete
```

```
    ' Undo deletion of note
    ' Pre- and post-notifications
    ' are fired
    swModel.EditUndo2 1
```

```
    ' Rebuild the drawing
    swModel.ForceRebuild3 True
```

```
End Sub
```

```
Go to top
```

```
'Class1
Option Explicit
```

```
Public WithEvents swDrawing As SldWorks.DrawingDoc
```

```
Private Function swDrawing_UndoPostNotify() As Long
'Display message after undo action occurs
    MsgBox "An Undo post-notification event has been fired."
End Function
```

```
Private Function swDrawing_UndoPreNotify() As Long
'Display message after undo action occurs
    MsgBox "An Undo pre-notification event has been fired."
End Function
```

```
Go to top
```
