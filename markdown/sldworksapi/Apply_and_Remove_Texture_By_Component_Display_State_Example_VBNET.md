---
title: "Apply and Remove Texture To and From Component By Display State Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Apply_and_Remove_Texture_By_Component_Display_State_Example_VBNET.htm"
---

# Apply and Remove Texture To and From Component By Display State Example (VB.NET)

This example shows how to apply and remove texture to and from a component using the name of a display state of the model.

```
'-------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly to open and texture exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly and applies texture to
'    the selected component.
' 2. Examine the Immediate window.
' 3. Click anywhere in the SOLIDWORKS Design window
'    to verify that the texture was applied.
' 4. Follow the instructions in the macro
'    to remove the just-applied texture.
' 5. Run the macro again.
' 6. Examine the Immediate window.
' 7. Click anywhere in the SOLIDWORKS Design window to verify
'    that the texture was removed.
'
' NOTE: Because this assembly document is used elsewhere,
' do not save changes.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
```

```vb
Partial
```

Class SolidWorksMacro

```vb
    Public Sub main()
```

```vb
Dim swModel As ModelDoc2
Dim swSelMgr As SelectionMgr
Dim swModelDocExt As ModelDocExtension
Dim component As Component2
Dim texture As Texture
Dim status As  Boolean
```

Dim displayState As String

Dim errors As Long

Dim warnings As Long

Dim namStr As String

' Open document and select a component

```vb
swModel = swApp.OpenDoc6(
```

" C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\motionstudies\valve_cam.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, ""

, errors, warnings)

```vb
swModelDocExt = swModel.Extension
status = swModelDocExt.SelectByID2(
```

"rocker-1@valve_cam", "COMPONENT", 0, 0, 0, False, 0, Nothing

, 0)

```vb
swSelMgr = swModel.SelectionManager
component = swSelMgr.GetSelectedObject6(1, -1)

displayState = "Default_Display State-1"
```

```vb
namStr = "<SystemTexture>\images\textures\pattern\checker2.jpg"

' Set texture on selected component in the
```

' specified display state

' After running the macro the first time, edit the macro to

' insert the comment character (') before the following two

' lines of code

```vb
texture = swModelDocExt.CreateTexture(namStr, 5, 45,
```

False

)

```vb
Debug.Print(
```

"Texture set: " & component.**SetTextureByDisplayState**(displayState, texture))

```vb
' Remove texture from component by display state
```

' After running the macro the first time, edit it to

' remove the comment character (') before the following

' line of code

'Debug.Print("Texture removed: " & component.**RemoveTextureByDisplayState**(displayState))

```vb
End Sub
```

```vb
''' <summary>
```

''' The SldWorks swApp variable is pre-assigned for you.

''' </summary>

Public swApp As SldWorks

```vb
End
```

Class
