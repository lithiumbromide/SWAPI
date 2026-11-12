---
title: "Apply and Remove Texture Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Apply_and_Remove_Texture_By_Configuration_Example_VB.htm"
---

# Apply and Remove Texture Example (VBA)

This example shows how to apply a texture to a face by display state and remove it by configuration.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions: Verify that the specified part to open and texture exist.
 '
 ' Postconditions:
 ' 1. Opens the part and applies the texture to the selected face.
 ' 2. Press F5 to continue running the macro.
 ' 3. Examine the part to verify that the texture
 '    was removed from the Default configuration.
 '----------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim face As SldWorks.Face2
 Dim texture As SldWorks.texture
 Dim modelview As SldWorks.modelview
 Dim status As Boolean
 Dim displayState As String
 Dim errors As Long
 Dim warnings As Long
 Dim namStr As String
 Dim atIndex(1) As Long
Sub main()
    ' Open the document and select a face
     Set swApp = Application.SldWorks
     Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\pplate.sldprt", swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
     Set swModelDocExt = swModel.Extension

    status = swModelDocExt.SelectByID2("", "FACE", -0.02341747645642, 0.03900188771217, -0.008053400767039, False, 0, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
     Set face = swSelMgr.GetSelectedObject6(1, -1)

    ' Set the texture on the selected face in the specified display state
     displayState = "<Default>_Display State 1"
     namStr = "<SystemTexture>\images\textures\pattern\checker2.jpg"
    Set texture = swModelDocExt.CreateTexture(namStr, 5, 45, False)
     status = face.SetTextureByDisplayState(displayState, texture)

    ' Redraw the window view
     Set modelview = swModel.ActiveView
     modelview.GraphicsRedraw (Empty)

    ' Examine the selected face to verify that the specified texture was set
     ' Press F5 to continue running macro
    Stop

    ' Remove the texture from the face in the specified configuration
     status = swModelDocExt.SelectByID2("", "FACE", -0.02341747645642, 0.03900188771217, -0.008053400767039, False, 0, Nothing, 0)
     Set face = swSelMgr.GetSelectedObject6(1, -1)
     status = face.RemoveTexture2("Default")

    ' Deselect the face to verify that the texture was removed
     atIndex(1) = 1
     status = swSelMgr.DeSelect2(atIndex, -1)
End Sub
```
