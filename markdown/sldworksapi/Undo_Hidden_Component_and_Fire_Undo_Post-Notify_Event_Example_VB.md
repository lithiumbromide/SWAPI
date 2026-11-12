---
title: "Undo Hidden Component and Fire Undo Post-Notify Event Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Undo_Hidden_Component_and_Fire_Undo_Post-Notify_Event_Example_VB.htm"
---

# Undo Hidden Component and Fire Undo Post-Notify Event Example (VBA)

This example shows how to fire an undo post-notification in an assembly document.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\smartcomponents\stepped_shaft.sldasm.
' 2. Copy and paste Main into the main module.
' 3. Click Insert > Class Module and copy and paste Class1 into that module.
'
' Postconditions:
' 1. Selects and hides the base-plate<1> component.
' 2. Undoes the hiding of the base-plate<1> component.
' 3. Fires a post-notification indicating that an undo action occurred.
' 4. Click OK to close the message box.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'--------------------------------------------------------------------------
'Main
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
```

```
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

    ' Fire undo post-notification
```

```
    'Rebuild the assembly
    swModel.ForceRebuild3 True
```

```
End Sub
```

```
Go to top
```

```
'Class 1
Option Explicit

Public WithEvents swAssembly As SldWorks.AssemblyDoc

Private Function swAssembly_UndoPostNotify() As Long
	'Display message after undo action occurs
	MsgBox "An undo post-notification event has been fired."
End Function
```

```
Go to top
```
