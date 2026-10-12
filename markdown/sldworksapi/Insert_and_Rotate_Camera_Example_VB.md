---
title: "Insert and Rotate Camera Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Rotate_Camera_Example_VB.htm"
---

# Insert and Rotate Camera Example (VBA)

This example shows how to insert a camera and rotate a camera.

'------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified model document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Inserts a camera in the model, changes its type to floating,
' and rotates it (i.e., modifies its pitch and yaw).
' 2. Examine the Immediate window.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'------------------------------------------------------------------------

```vb
Option Explicit
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swCamera As SldWorks.Camera
Dim fileerror As Long, filewarning As Long
Dim boolstatus As Boolean

Sub main()
```

```vb
Set swApp = Application.SldWorks
' Open part document
swApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\coffeecup.sldprt", swDocPART, swOpenDocOptions_Silent, "", fileerror, filewarning
Set swModel = swApp.ActiveDoc
Set swModelDocExt = swModel.Extension

' Insert a camera
Set swCamera = swModelDocExt.InsertCamera

' Set camera type to floating
swCamera.Type = swCameraType_Floating

' Show camera
boolstatus = swModelDocExt.SelectByID2("Camera1", "CAMERAS", 0, 0, 0, False, 0, Nothing, 0)
boolstatus = swModel.SetUserPreferenceToggle(swUserPreferenceToggle_e.swDisplayCameras, True)
swModel.GraphicsRedraw2

' Get camera's pitch and yaw settings
' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
Debug.Print "Original pitch (up or down angle)     = " & swCamera.Pitch * 57.3 & " deg"
Debug.Print "Original yaw (side-to-side angle)     = " & swCamera.Yaw * 57.3 & " deg"
Debug.Print " "

' Rotate camera
swCamera.Pitch = -25
swCamera.Yaw = 150

' New pitch and yaw settings
Debug.Print "New pitch (up or down angle)          = " & swCamera.Pitch * 57.3 & " deg"
Debug.Print "New yaw (side-to-side angle)          = " & swCamera.Yaw * 57.3 & " deg"
swModel.GraphicsRedraw2
```

```vb
End Sub
```
