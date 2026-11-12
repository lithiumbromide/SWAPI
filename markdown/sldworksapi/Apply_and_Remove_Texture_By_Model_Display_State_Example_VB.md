---
title: "Apply and Remove Texture To and From a Model by Display State Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Apply_and_Remove_Texture_By_Model_Display_State_Example_VB.htm"
---

# Apply and Remove Texture To and From a Model by Display State Example (VBA)

This example shows how to add and remove texture to and from a model using the name of a display state model.

```
'----------------------------------------------------------------------------
' Preconditions: Verify that the specified part and texture exist.
'
' Postconditions:
' 1. Opens the specified part and applies texture to the part.
' 2. At Stop, examine the part to verify that the texture was applied.
' 3. In the IDE, click the Continue button to resume
'    execution of macro.
' 4. Examine the part to verify that the texture was removed.
'
' NOTE: Because the part document is used elsewhere, do not save
' changes.
'----------------------------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim texture As SldWorks.texture
Dim status As Boolean
Dim displayState As String
Dim errors As Long
Dim warnings As Long
Dim namStr As String

Sub main()

    ' Open document

Set swApp = Application.SldWorks
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\motionstudies\valve.sldprt", swDocPART, swOpenDocOptions_Silent, "", errors, warnings)

Set swModelDocExt = swModel.Extension

    ' Set
texture on the model in the
    ' specified display state
    displayState = "<Default>_Display State 1"
    namStr = "<SystemTexture>\images\textures\pattern\checker2.jpg"

Set texture = swModelDocExt.CreateTexture(namStr, 5, 45, False)

status = swModelDocExt.SetTextureByDisplayState(displayState, texture)

    ' Examine the model to verify texture applied

' In the IDE, click the Continue button to resume
    '
running macro

    Stop

    ' Remove
texture from model by display state
    status = swModelDocExt.RemoveTextureByDisplayState(displayState)

' Rebuild the model to verify texture was removed
    swModel.ForceRebuild3 False

End Sub
```
