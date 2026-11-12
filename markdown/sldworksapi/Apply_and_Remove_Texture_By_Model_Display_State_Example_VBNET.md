---
title: "Apply and Remove Texture To and From Model By Display State (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Apply_and_Remove_Texture_By_Model_Display_State_Example_VBNET.htm"
---

# Apply and Remove Texture To and From Model By Display State (VB.NET)

This example shows how to apply and remove texture to and from a model using the name of a display state of the model.

```vb
'--------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified part to open and texture exist.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the specified part and applies texture to the part.
 ' 2. Examine the part to verify.
 ' 3. In the IDE, click the Continue button at Stop.
 ' 4. Removes the texture from the selected face.
 ' 5. Examine the Immediate window and the part.
 '
 ' NOTE: Because the part document is used elsewhere, do not save changes.
 '-------------------------------------------------------------------------
```

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

```vb
Partial
```

Class

SolidWorksMacro

Public Sub main()

```vb
Dim swModel As ModelDoc2
Dim swModelDocExt As ModelDocExtension
Dim texture As Texture
Dim displayState As String
```

Dim errors As Long

Dim warnings As Long

Dim namStr As String

' Open document

```vb
swModel = swApp.OpenDoc6(
```

"C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\motionstudies\valve.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, ""

, errors, warnings)

```vb
swModelDocExt = swModel.Extension
```

' Set texture on selected model in the

' specified display state

```vb
displayState =
```

"<Default>_Display State 1"

```vb
namStr =
```

"<SystemTexture>\images\textures\pattern\checker2.jpg"

```vb
texture = swModelDocExt.CreateTexture(namStr, 5, 45,
```

False

)

```vb
Debug.Print(
```

"Texture set: " & swModelDocExt.**SetTextureByDisplayState**(displayState, texture))

```vb
 ' Examine the selected face to verify
' that the specified texture was set
' In the IDE, click the Continue button to
' resume running macro
Stop

 ' Remove texture from model by display state
 Debug.Print("Texture removed: " & swModelDocExt.RemoveTextureByDisplayState(displayState))

swModel.ForceRebuild3(False)
```

```vb
End Sub
```

''' <summary>

''' The SldWorks swApp variable is pre-assigned for you.

''' </summary>

Public swApp As SldWorks

```vb
End
```

Class
