---
title: "Change Texture on Face in Specified Configuration Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Texture_on_Face_in_Specified_Configuration_Example_VBNET.htm"
---

# Change Texture on Face in Specified Configuration Example (VB.NET)

This example shows how to change the texture on the selected face in the specified configuration.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Ensure the specified textures exist.
  ' 2. Open a part or assembly with a Default configuration.
 ' 3. Select a face.
 ' 4. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Applies texture to the selected face.
 ' 2. Inspect the Immediate window and the model.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swSelMgr As SelectionMgr
     Dim swModelDocExt As ModelDocExtension
     Dim face As Face2
     Dim texture As Texture
     Dim boolstatus As Boolean
     Dim namStr As String
     Dim configName As String

     Sub main()

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swModelDocExt = swModel.Extension

         configName = "Default"

         face = swSelMgr.GetSelectedObject6(1, -1)

         'Get existing texture on this face
         texture = face.GetTexture(configName)

         If Not texture Is Nothing Then

             Debug.Print("Texture before:")
             Debug.Print("Material: " & texture.MaterialName)
             Debug.Print("Granularity: " & texture.ScaleFactor)
             Debug.Print("Angle of rotation: " & texture.Angle)

             'Change texture on this face
             texture.Angle = 340
             texture.ScaleFactor = 25
             texture.MaterialName = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\data\Images\textures\plastic\brushed\bblue.jpg"
             boolstatus = face.SetTexture(configName, texture)

             Debug.Print("")
             Debug.Print("Texture after:")
             Debug.Print("Material: " & texture.MaterialName)
             Debug.Print("Granularity: " & texture.ScaleFactor)
             Debug.Print("Angle of rotation: " & texture.Angle)

         Else

             'If no texture exists on this face, then apply a texture to it
             namStr = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\data\Images\textures\pattern\checker2.jpg"
             texture = swModelDocExt.CreateTexture(namStr, 5, 45, False)
             boolstatus = face.SetTexture(configName, texture)

             Debug.Print("New texture:")
             Debug.Print("Material: " & texture.MaterialName)
             Debug.Print("Granularity: " & texture.ScaleFactor)
             Debug.Print("Angle of rotation: " & texture.Angle)

         End If

         Debug.Print(texture.GetSystemTextureName(texture.MaterialName, boolstatus))

     End Sub

     Public swApp As SldWorks

 End Class
```
