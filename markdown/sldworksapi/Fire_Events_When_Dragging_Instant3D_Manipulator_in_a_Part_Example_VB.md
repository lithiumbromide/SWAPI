---
title: "Fire Events When Dragging Instant3D Manipulator in a Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Dragging_Instant3D_Manipulator_in_a_Part_Example_VB.htm"
---

# Fire Events When Dragging Instant3D Manipulator in a Part Example (VBA)

This example shows how to fire events when dragging an Instant3D manipulator in a part document.

```vb
'------------------------------------
 ' Preconditions:
 ' 1. Open a part document.
 ' 2. Copy and paste Main into the main module.
 ' 3. Click Insert > Class module and copy and paste
 '    Class into the class module.
 ' 4. Open the Immediate window.
 '
 ' NOTE: Instant3D is enabled by the macro.
 '
 ' Postconditions:
 ' 1. Select an Instant3D manipulator in the
 '    open part. For example,
 '    double-click an extrude feature in a part,
 '    then select one of the Instant3D manipulators
 '    and drag it.
 ' 2. Writes a debug statement to the Immediate window
 '    informing you that dragging of an Instant3D
 '    manipulator has started.
 ' 3. Stop dragging the manipulator.
 ' 4. Writes a debug statement to the Immediate
 '    window informing you that dragging of
 '    an Instant3D manipulator has stopped.
 ' 5. Examine the Immediate window.
 '----------------------------------------
 ' Main

 Option Explicit

 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swFeatMgr As SldWorks.FeatureManager
 Dim partDoc As New Class1

 Sub main()

 Set swApp = Application.SldWorks
 Set swModel = swApp.ActiveDoc

 ' Enable Instant3D
 Set swFeatMgr = swModel.FeatureManager
 swFeatMgr.MoveSizeFeatures = True

 ' Execute its class module
 partDoc.init swModel

 End Sub
Back to top
```

**'** Class

```vb
Public WithEvents doc As partDoc
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
