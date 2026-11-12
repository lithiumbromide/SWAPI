---
title: "Create Macro Using Macro Manager Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Macro_Using_Macro_Manager_Example_VBA.htm"
---

# Create Macro Using Macro Manager Example (VBA)

This example shows how to create VBA macro using the macro manager and VBA.

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
'  2. Gets the active document.
'  3. Gets the macro manager.
'  4. Sets the macro language, level of detail, and path
'     where to save the macro.
'  5. Starts macro recording.
'  6. Creates a VBA macro containing the
'     macro at c:\temp\macros\CircleMacroVBA and inserts
'     a Circle and Arc in the drawing.
'  7. Stops macro recording.
'  8. Open a new drawing in DraftSight.
'  9. Open C:\temp\macros\CircleMacroVBA\CircleMacroVBA.swb in a
'     Microsoft software product in which VBA is embedded.
' 10. Run the macro.
'----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim dsApp As DraftSight.Application
```

```
    'Connect to DraftSight
    Set dsApp = GetObject(, "DraftSight.Application")
```

```
    'Abort any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    'Get active document
    Dim dsDoc As DraftSight.Document
    Set dsDoc = dsApp.GetActiveDocument
```

```
    If dsDoc Is Nothing Then
        MsgBox "There are no open documents in DraftSight."
        Exit Sub
    End If
```

```
    'Get macro manager
    Dim dsMacroManager As DraftSight.MacroManager
    Set dsMacroManager = dsApp.GetMacroManager
```

```
    'Set macro language
    dsMacroManager.Language = dsMacroLanguage_VBA
```

```
    'Set macro level of detail
    dsMacroManager.LevelOfDetail = dsMacroLevelOfDetail_Low
```

```
    'Set save file path
    dsMacroManager.SavePath = "c:\temp\macros"
```

```
    'Start macro recording
    dsMacroManager.StartMacroRecording
```

```
    'Get Sketch Manager
    Dim dsSketchMgr As DraftSight.SketchManager
    Set dsSketchMgr = dsDoc.GetModel.GetSketchManager
```

```
    'Insert Circle and Arc
    Dim dsCircle As DraftSight.Circle
    Dim dsCircleArc As DraftSight.CircleArc
    Set dsCircle = dsSketchMgr.InsertCircle(2#, 2#, 0#, 4#)
    Set dsCircleArc = dsSketchMgr.InsertArc(3#, 3#, 0#, 4#, 1#, 2#)
```

```
    'Stop macro recording
    dsMacroManager.StopMacroRecording "CircleMacroVBA"
```

```
End Sub
```
