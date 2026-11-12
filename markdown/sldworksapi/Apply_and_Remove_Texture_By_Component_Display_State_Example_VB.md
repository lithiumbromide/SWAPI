---
title: "Apply and Remove Texture By Component Display State Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Apply_and_Remove_Texture_By_Component_Display_State_Example_VB.htm"
---

# Apply and Remove Texture By Component Display State Example (VBA)

## SOLIDWORKS API Helps

This example shows how to add and remove texture to and from a component using the name of a display state of the assembly.

```
'---------------------------------------------------------------------------
' Preconditions: Verify that the assembly to open and pattern exist.
'
' Postconditions:
' 1. Opens the specified assembly and applies texture to the
'    selected component.
' 2. At Stop, click the Rebuild button in SOLIDWORKS Design and examine the
'    component to verify that texture was applied.
' 3. In the IDE, click the Continue button to resume
'    execution of the macro.
' 4. Examine the component to verify that the texture
'    was removed.
'---------------------------------------------------------------------------
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim component As SldWorks.Component2
 Dim texture As SldWorks.texture
 Dim modelview As SldWorks.modelview
 Dim status As Boolean
 Dim displayState As String
 Dim errors As Long
 Dim warnings As Long
 Dim namStr As String
 Dim atIndex(1) As Long
Sub main()
```

```vb
' Open document and select a component
Set swApp = Application.SldWorks
Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\motionstudies\valve_cam.sldasm", swDocASSEMBLY, swOpenDocOptions_Silent, "", errors, warnings)
Set swModelDocExt = swModel.Extension
status = swModelDocExt.SelectByID2("rocker-1@valve_cam", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
Set swSelMgr = swModel.SelectionManager
Set component = swSelMgr.GetSelectedObject6(1, -1)

' Set texture on selected component in the
' specified display state
displayState = "Default_Display State-1"
namStr = "<SystemTexture>\images\textures\pattern\checker2.jpg"
Set texture = swModelDocExt.CreateTexture(namStr, 5, 45, False)
status = component.SetTextureByDisplayState(displayState, texture)

' Click the Rebuild button in SOLIDWORKS Design to verify
' that the specified texture was set
' In the IDE, click the Continue button to resume
' running macro
Stop

' Remove texture from component by display state
status = swModelDocExt.SelectByID2("rocker-1@valve_cam", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
Set component = swSelMgr.GetSelectedObject6(1, -1)
status = component.RemoveTextureByDisplayState(displayState)

' Deselect the component to verify
' that the texture was removed
atIndex(1) = 1
status = swSelMgr.DeSelect2(atIndex, -1)
```

```vb
End Sub
```
