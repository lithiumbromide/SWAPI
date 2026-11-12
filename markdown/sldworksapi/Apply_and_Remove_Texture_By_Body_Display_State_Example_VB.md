---
title: "Apply and Remove Texture By Body Display State Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Apply_and_Remove_Texture_By_Body_Display_State_Example_VB.htm"
---

# Apply and Remove Texture By Body Display State Example (VBA)

This example shows how to add and remove texture to and from a body using the name of a display state of the model.

```
'--------------------------------------------------------------
' Preconditions: Verify that the specified part to open and
' texture exist.
'
' Postconditions:
' 1. Opens part and applies texture to the selected body.
' 2. Examine the part and press F5.
' 3. Examine the part again to verify that the texture was removed.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'--------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim body As SldWorks.Body2
Dim texture As SldWorks.texture
Dim modelview As SldWorks.modelview
Dim status As Boolean
Dim displayState As String
Dim errors As Long
Dim warnings As Long
Dim namStr As String
Dim atIndex(1) As Long
```

```
Sub main()
```

```
    ' Open document and select a body
    Set swApp = Application.SldWorks
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_bridge.sldprt", swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("hub", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
    Set body = swSelMgr.GetSelectedObject6(1, -1)
```

```
    ' Set texture on selected body in the
    ' specified display state
    displayState = "<Default>_Display State 1"
    namStr = "<SystemTexture>\images\textures\pattern\checker2.jpg"
    Set texture = swModelDocExt.CreateTexture(namStr, 5, 45, False)
    status = body.SetTextureByDisplayState(displayState, texture)
```

```
    ' Redraw the window view
    Set modelview = swModel.ActiveView
    modelview.GraphicsRedraw (Empty)
```

```
    ' Examine the selected body to verify
    ' that the specified texture was set
    ' Press F5
    Stop
```

```
    ' Remove texture from body by display state
    status = swModelDocExt.SelectByID2("hub", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
    Set body = swSelMgr.GetSelectedObject6(1, -1)
    status = body.RemoveTextureByDisplayState(displayState)
```

```
    ' Deselect the body to verify
    ' that the texture was removed
    atIndex(1) = 1
    status = swSelMgr.DeSelect2(atIndex, -1)
```

```
End Sub
```
