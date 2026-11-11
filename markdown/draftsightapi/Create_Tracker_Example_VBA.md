---
title: "Create Tracker Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Tracker_Example_VBA.htm"
---

# Create Tracker Example (VBA)

This example shows how to create a tracker and add a temporary entity to the tracker.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
'    a. In Modules, copy and paste the Main module.
'    b. Insert a class called Class1, and paste the Class1 module.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight and open a document.
' 5. Run the macro.
'
' Postconditions:
' 1. Creates a temporary Circle for the tracker.
' 2. Creates a tracker and adds the temporary Circle to the
'    the tracker.
' 3. Examine the pointer in the drawing to verify.
' 4. Prompts you to click in the drawing to insert a Circle.
' 5. Inserts a Circle in the drawing at the point where you clicked.
'----------------------------------------------------------------
```

```
'Main module
Option Explicit
```

```
Public dsTrackerEvent As Class1
```

```
Public dsApp As DraftSight.Application
Public dsTempCircle As DraftSight.Circle
```

```
Sub main()
```

```
        Dim dsModel As DraftSight.Model
        Dim dsSketchMgr As DraftSight.SketchManager
```

```
        'Connect to DraftSight application
        Set dsApp = GetObject(, "DraftSight.Application")
```

```
        'Abort any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand
```

```
        If dsApp Is Nothing Then
            Return
        End If
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
        Set dsModel = dsDoc.GetModel()
        Set dsSketchMgr = dsModel.GetSketchManager()
```

```
        'Create temporary Circle
        dsApp.TemporaryEntityMode = True
        Set dsTempCircle = dsSketchMgr.InsertCircle(0, 0, 0, 10)
        dsApp.TemporaryEntityMode = False
```

```
        'Create tracker and add temporary Circle
        Dim dsTracker As DraftSight.Tracker
        Set dsTracker = dsApp.CreateTracker()
        dsTracker.AddTemporaryEntity dsTempCircle
```

```
        'Set up event
        Set dsTrackerEvent = New Class1
        Set dsTrackerEvent.myTracker = dsTracker
```

```
        'Prompt for point where to insert Circle
        'Before prompt, add tracker to command message
        Dim dsCmdMsg As CommandMessage
        Set dsCmdMsg = dsApp.GetCommandMessage()
        dsCmdMsg.AddTracker dsTracker
```

```
        Dim x As Double
        x = 0#
        Dim y As Double
        y = 0#
        Dim z As Double
        z = 0#
```

```
        Dim res As Boolean
        res = dsCmdMsg.PromptForPoint("Click to insert Circle", x, y, z)
```

```
        If res = True Then
            'Set the center of the Circle where user clicked
            dsTempCircle.SetCenter x, y, z
            'Add temporary Circle to drawing
            dsSketchMgr.AddTemporaryEntity dsTempCircle
        End If
```

```
        'Remove tracker from command message if no longer needed
        dsCmdMsg.RemoveTracker dsTracker
```

```
    End Sub
```

```
'Class1 module
```

```
Option Explicit
```

```
Public WithEvents myTracker As DraftSight.Tracker
```

```
Public Sub myTracker_UpdateNotify(ByVal CursorPosition As DraftSight.MathPoint)
```

```
        If CursorPosition Is Nothing Then
            Return
        End If
```

```
        Dim x As Double
        x = 0#
        Dim y As Double
        y = 0#
        Dim z As Double
        z = 0#
        CursorPosition.GetPosition x, y, z
```

```
        dsTempCircle.SetCenter x, y, z
```

```
End Sub
```
