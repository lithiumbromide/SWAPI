---
title: "Fire Undo and Redo Pre- and Post-notifications in Assembly Document (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Assembly_Document_Example_VB6.htm"
---

# Fire Undo and Redo Pre- and Post-notifications in Assembly Document (VBA)

This example shows how to fire Undo and Redo pre- and post-notifications in an assembly document.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\smartcomponents\stepped_shaft.sldasm.
' 2. Copy and paste Main into the main module.
' 3. Click Insert > Class Module and copy and paste Class1 into that module.
'
' Postconditions:
' 1. Selects  and hides the base-plate<1> component and
'    fires pre- and post-notifications indicating that an
'    Undo has occurred.
' 2. Performs a Redo and fires pre- and post-notifications.
' 3. Performs another Undo and fires pre- and post-notifications
'    so that the assembly document returns to its just-opened state.
' 4. Click OK to close each message box.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'-----------------------------------------------------------------
' Main
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swAssembly As SldWorks.AssemblyDoc
Dim boolstatus As Boolean
Dim swAssemblyEvents As Class1
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
    Set swAssembly = swModel
    Set swAssemblyEvents = New Class1
    Set swAssemblyEvents.swAssembly = swApp.ActiveDoc
    ' Select a component and hide it
    boolstatus = swModelDocExt.SelectByID2("base_plate-1@stepped_shaft", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    swModel.HideComponent2
```

```
    swModel.ClearSelection2 True
```

```
    ' Undo hiding of the component
    swModel.EditUndo2 1
```

```
    ' Redo hiding of the component
    swModel.EditRedo2 1
    ' Undo hiding of the component
    ' so that model document is unchanged
    swModel.EditUndo2 1
```

```
    ' Rebuild the model
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
Public WithEvents swAssembly As SldWorks.AssemblyDoc
```

```
Private Function swAssembly_UndoPostNotify() As Long
'Display message after an Undo
    MsgBox "An Undo post-notification event has been fired."
End Function
```

```
Private Function swAssembly_UndoPreNotify() As Long
'Display message before an Undo
    MsgBox "An Undo pre-notification event has been fired."
End Function
```

```
Private Function swAssembly_RedoPostNotify() As Long
'Display message after an Redo
    MsgBox "A Redo post-notification event has been fired."
End Function
```

```
Private Function swAssembly_RedoPreNotify() As Long
'Display message before an Redo
    MsgBox "A Redo pre-notification event has been fired."
End Function
```

```
Go to top
```
