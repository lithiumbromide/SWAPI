---
title: "Run SOLIDWORKS Commands and Synthesize Mouse Events Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Run_SOLIDWORKS_Commands_and_Synthesize_Mouse_Events_Example_VB.htm"
---

# Run SOLIDWORKS Commands and Synthesize Mouse Events Example (VBA)

This example shows how to run SOLIDWORKS commands and synthesize mouse events.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document to open exists.
' 2. Right-click the project name in the Project Explorer and click
'    Insert > Class Module.
' 3. Copy Module to the main module.
' 4. Copy Class1 to the class module.
' 5. In the IDE, click Tools > References, click
'    SOLIDWORKS version Commands type library, and click OK.
' 6. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Fits the model to the graphics area.
' 3. Moves the mouse.
' 4. Changes the view orientation to *Front.
' 5. Select an edge on the model.
' 6. Left-click anywhere outside the model in the graphics area.
' 7. Click Reset in the IDE to stop executing the macro.
' 8. Examine the Immediate window.
'-----------------------------------------------------------
'Module
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swModelView As SldWorks.ModelView
Dim swMouse As SldWorks.mouse
Dim TheMouse As SldWorks.mouse
Dim obj As New Class1
Dim i As Long
Dim x As Double
Dim fileName As String
Dim errors As Long
Dim warnings As Long
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Set swModelView = swModel.GetFirstModelView
    Set TheMouse = swModelView.GetMouse
```

```
    obj.init TheMouse
```

```
    x = 0
```

```
    Debug.Print "Fit model to graphics area"
    swModelDocExt.RunCommand swCommands_ZoomToFit, ""

    'Move the mouse
    status = TheMouse.Move(50, 150, swMouse_Absolute + swMouse_MouseMove + swMouse_LeftDown)
    Debug.Print ("First call to Move: " & status)
```

```
       Debug.Print "Calls to Move within loop:"
       For i = 1 To 5
           DoEvents
           status = TheMouse.Move(5, 5, swMouse_MouseMove)
           Debug.Print ("  Call " & i & " to Move: " & status)
        Next
```

```
       status = TheMouse.Move(0, 0, swMouse_LeftUp)
       Debug.Print ("Last call to Move: " & status)
```

```
           Debug.Print("Call to MoveXYZ: " & status)
           status = TheMouse.MoveXYZ(0.03720615681732, 0.0316583060694, 0.04991700841805, swMouse_LeftDown)
           Debug.Print ("Calls to Move within next loop: ")
```

```
           For i = 1 To 5
               DoEvents
               status = TheMouse.Move(5, 5, swMouse_MouseMove)
               Debug.Print "    Call " & i + 1; " to Move: " & " & status
           Next

               status = TheMouse.Move(0, 0, swMouse_LeftUp)
               Debug.Print ("Call to Move after loop: " & status)
```

```
       Debug.Print "Change view orientation to *Front"
       swModelDocExt.RunCommand swCommands_Front, ""
```

```
 End Sub
```

```
Back to top
```

```vb
'Class1

 Dim WithEvents ms As SldWorks.mouse

 Private Sub Class_Initialize()
 End Sub

Public Sub init(mouse As Object)
     Set ms = mouse
 End Sub

 Private Function ms_MouseSelectNotify(ByVal Ix As Long, ByVal Iy As Long, ByVal x As Double, ByVal y As Double, ByVal z As Double) As Long
     Debug.Print "Selection made:"
     Debug.Print " Mouse location:"
     Debug.Print "   Window space coordinates:"
     Debug.Print "     " & Ix
     Debug.Print "     " & Iy
     Debug.Print "   World space coordinates:"
     Debug.Print "     " & x
     Debug.Print "     " & y
     Debug.Print "     " & z
 End Function

 Private Function ms_MouseLBtnDownNotify(ByVal x As Long, ByVal y As Long, ByVal WParam As Long) As Long
     Debug.Print "Left-mouse button pressed."
 End Function
```

[Back to top](#Top)
