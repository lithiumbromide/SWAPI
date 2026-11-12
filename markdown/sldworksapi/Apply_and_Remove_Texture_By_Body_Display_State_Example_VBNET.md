---
title: "Apply and Remove Texture By Body Display State Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Apply_and_Remove_Texture_By_Body_Display_State_Example_VBNET.htm"
---

# Apply and Remove Texture By Body Display State Example (VB.NET)

This example shows how to add and remove texture to and from a body using the name of a display state of the model.

```
'--------------------------------------------------
' Preconditions: Verify that the specified part to open
' and texture exist.
'
' Postconditions:
' 1. Opens the specified part and applies texture to the
'    selected body.
' 2. In the IDE, click the Continue button
'    at Stop.
' 3. Removes texture from selected body.
' 4. To verify, click the Stop Debugging button in the
'    IDE to stop execution of the macro and click anywhere
'    in the graphics area.
'    - or -
'    If the Stop Debugging button is grayed out, click
'    anywhere in the graphics area.
'----------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
```

```vb
Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swModelDocExt As ModelDocExtension
        Dim body As Body2
        Dim texture As Texture
        Dim modelview As ModelView
        Dim status As Boolean
        Dim displayState As String
        Dim errors As Long
        Dim warnings As Long
        Dim namStr As String

        ' Open document and select a body
        swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2017\tutoria\multibody\multi_bridge.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("hub", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
        swSelMgr = swModel.SelectionManager
        body = swSelMgr.GetSelectedObject6(1, -1)

        ' Set texture on selected body in the
        ' specified display state
        displayState = "<Default>_Display State 1"
        namStr = "<SystemTexture>\images\textures\pattern\checker2.jpg"
        texture = swModelDocExt.CreateTexture(namStr, 5, 45, False)
        status = body.SetTextureByDisplayState(displayState, texture)

        ' Redraw the window view
        modelview = swModel.ActiveView
        modelview.GraphicsRedraw(Nothing)

        ' Examine the selected body to verify
        ' that the specified texture was set
        ' In the IDE, click the Continue button to
        ' resume running macro
        Stop

        ' Remove texture from body by display state
        status = swModelDocExt.SelectByID2("hub", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
        body = swSelMgr.GetSelectedObject6(1, -1)
        status = body.RemoveTextureByDisplayState(displayState)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
