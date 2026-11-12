---
title: "Apply and Remove Texture Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Apply_and_Remove_Texture_By_Configuration_Example_VBNET.htm"
---

# Apply and Remove Texture Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swSelMgr As SelectionMgr
     Dim swModelDocExt As ModelDocExtension
     Dim face As Face2
     Dim texture As Texture
     Dim modelview As ModelView
     Dim status As Boolean
     Dim displayState As String
     Dim errors As Integer
     Dim warnings As Integer
     Dim namStr As String
     Dim atIndex(1) As Integer

     Sub main()

         ' Open the document and select a face
         swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\pplate.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         swModelDocExt = swModel.Extension

         status = swModelDocExt.SelectByID2("", "FACE", -0.02341747645642, 0.03900188771217, -0.008053400767039,  False, 0,  Nothing, 0)

         swSelMgr = swModel.SelectionManager
         face = swSelMgr.GetSelectedObject6(1, -1)

         ' Set the texture on the selected face in the specified display state
         displayState =  "<Default>_Display State 1"
         namStr =  "<SystemTexture>\images\textures\pattern\checker2.jpg"
         texture = swModelDocExt.CreateTexture(namStr, 5, 45, False)
         status = face.SetTextureByDisplayState(displayState, texture)

         ' Redraw the window view
         modelview = swModel.ActiveView
         modelview.GraphicsRedraw(Nothing)

         ' Examine the selected face to verify that the specified texture was set
         ' Press F5 to continue running macro

         Stop

         ' Remove the texture from the face in the specified configuration
         status = swModelDocExt.SelectByID2("", "FACE", -0.02341747645642, 0.03900188771217, -0.008053400767039,  False, 0,  Nothing, 0)
         face = swSelMgr.GetSelectedObject6(1, -1)
         status = face.RemoveTexture2("Default")

         ' Deselect the face to verify that the texture was removed
         atIndex(1) = 1
         errors = swSelMgr.DeSelect2(atIndex, -1)

     End Sub

     Public swApp As SldWorks

 End  Class
```
