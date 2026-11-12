---
title: "Fire Undo and Redo Pre- and Post-notifications in Part Document (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Undo_and_Redo_Pre_and_Post-notifications_in_Part_Document_Example_VB6.htm"
---

# Fire Undo and Redo Pre- and Post-notifications in Part Document (VBA)

This example shows how to fire undo and redo pre- and post-notifications in a part document.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\cstick.sldprt.
' 2. Copy and paste Main into the main module.
' 3. Click Insert > Class Module and copy and paste Class1 into that module.
'
' Postconditions:
' 1. Creates a circle, undoes it, redoes it, and undoes it again.
' 2. Fires a pre- and post-notification and displays a message box
'    before and after each Undo and Redo.
' 3. Click OK to close each message box.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'--------------------------------------------------------------------------
'Main
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swPart As SldWorks.PartDoc
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim boolstatus As Boolean
Dim swPartEvents As Class1
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    ' Event notification
    Set swPart = swModel
    Set swPartEvents = New Class1
    Set swPartEvents.swPart = swApp.ActiveDoc
```

```
    ' Create a circle on the
    ' top face of the candlestick
    Set swModelDocExt = swModel.Extension
    boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.00140404215739, 0.2199999999999, 0.001897848026772, False, 0, Nothing, 0)
    Set swSketchManager = swModel.SketchManager
    Set swSketchSegment = swSketchManager.CreateCircle(0#, 0#, 0#, 0.01296, -0.006347, 0#)
```

```
    ' Undo creation of circle
    ' and fire an undo pre - and post-
    ' notification
    swModel.EditUndo2 1
```

```
    ' Redo creation of circle
    ' and fire a redo pre- and post-
    ' notification
    swModel.EditRedo2 1
```

```
    ' Undo creation of circle again
    ' to leave model document unchanged
    ' and fire another Undo pre- and post-
    ' notification
    swModel.EditUndo2 1
```

```
    swModel.ClearSelection2 True
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
Public WithEvents swPart As SldWorks.PartDoc
```

```
Private Function swPart_UndoPostNotify() As Long
    MsgBox "An Undo post-notification event has been fired."
End Function
```

```
Private Function swPart_UndoPreNotify() As Long
    MsgBox "An Undo pre-notification event has been fired."
End Function
```

```
Private Function swPart_RedoPostNotify() As Long
    MsgBox "A Redo post-notification event has been fired."
End Function
```

```
Private Function swPart_RedoPreNotify() As Long
    MsgBox "A Redo pre-notification event has been fired."
End Function
```

```
Go to top
```
