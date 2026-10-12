---
title: "Apply and Remove Texture By Display State Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Apply_and_Remove_Texture_By_Display_State_Example_VBNET.htm"
---

# Apply and Remove Texture By Display State Example (VB.NET)

This example shows how to apply and remove texture to and from a face by display state.

```vb
'---------------------------------------------------------------------------
 ' Preconditions: Verify that the specified part and texture exist.
 '
 ' Postconditions:
 ' 1. Opens the specified part and applies texture to the selected face.
 ' 2. Examine the part.
 ' 3. In the IDE, click the Continue button at Stop.
 ' 4. Removes the texture from the selected face.
 ' 5. To verify, click the Stop Debugging button in the IDE to stop
 '    execution of the macro, then click anywhere in the SOLIDWORKS Design
 '    graphics area.
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swModelDocExt As ModelDocExtension
        Dim face As Face2
        Dim texture As Texture
        Dim modelview As ModelView
        Dim status As Boolean
        Dim displayState As String
        Dim errors As Long
        Dim warnings As Long
        Dim namStr As String

        ' Open document and select a face
        swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\pplate.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("", "FACE", -0.02341747645642, 0.03900188771217, -0.008053400767039, False, 0, Nothing, 0)
        swSelMgr = swModel.SelectionManager
        face = swSelMgr.GetSelectedObject6(1, -1)

        ' Set texture on selected face in the
        ' specified display state
        displayState = "<Default>_Display State 1"
        namStr = "<SystemTexture>\images\textures\pattern\checker2.jpg"
        texture = swModelDocExt.CreateTexture(namStr, 5, 45, False)
        status = face.SetTextureByDisplayState(displayState, texture)

        ' Redraw the window view
        modelview = swModel.ActiveView
        modelview.GraphicsRedraw(Nothing)

        ' Examine the selected face to verify
        ' that the specified texture was set
        ' In the IDE, click the Continue button to
        ' resume running macro
        Stop

        ' Remove texture from face by display state
        status = swModelDocExt.SelectByID2("", "FACE", -0.02341747645642, 0.03900188771217, -0.008053400767039, False, 0, Nothing, 0)
        face = swSelMgr.GetSelectedObject6(1, -1)
        status = face.RemoveTextureByDisplayState(displayState)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
