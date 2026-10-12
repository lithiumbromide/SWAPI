---
title: "Fire Events When Dragging Instant3D Manipulator in an Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Dragging_Instant3D_Manipulator_in_an_Assembly_Example_VB.htm"
---

# Fire Events When Dragging Instant3D Manipulator in an Assembly Example (VBA)

This example shows how to fire events when dragging an Instant3D manipulator in an assembly document.

```vb
'------------------------------------
 ' Preconditions:
 ' 1. Open an assembly document.
 ' 2. Copy and paste Main into the main module.
 ' 3. Click Insert > Class module and copy and paste
 '    Class1 into the class module.
 ' 4. Open the Immediate window.
 '
 ' NOTE: Instant3D is enabled by the macro.
 '
 ' Postconditions:
 ' 1. Select an Instant3D manipulator in the
 '    open assembly by right-clicking a floating
 '    assembly component, clicking the down arrows
 '    at the bottom of the shortcut menu, and selecting
 '    Move with Triad.
 ' 2. Drag the Instant3D handle to move the assembly
 '    component.
 ' 3. Writes a debug statement to the Immediate window
 '    informing you that dragging of an Instant3D
 '    manipulator has started.
 ' 4. Stop dragging the manipulator.
 ' 5. Writes a debug statement to the Immediate window
 '    informing you that dragging of an Instant3D
 '    manipulator has stopped.
 ' 6. Examine the Immediate window.
 '----------------------------------------
 ' Main
Option Explicit

Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swFeatMgr As SldWorks.FeatureManager
 Dim assemblyDoc As New Class1

 Sub main()
```

```vb
Set swApp = Application.SldWorks
 Set swModel = swApp.ActiveDoc

 ' Enable Instant3D
 Set swFeatMgr = swModel.FeatureManager
 swFeatMgr.MoveSizeFeatures = True

 ' Execute its class module
 assemblyDoc.init swModel
```

```vb
End Sub

 Back to top

 ' Class
Public WithEvents doc As assemblyDoc

Public Function init(ByRef docIn As Object)
     Set doc = docIn
 End Function

 Private Function doc_DragStateChangeNotify(ByVal State As Boolean) As Long
     ' Write debug statement when dragging of manipulator started and stopped
     If State = True Then
         Debug.Print "Dragging of manipulator started."
     Else
         Debug.Print "Dragging of manipulator stopped."
     End If
 End Function
Back to top
```
