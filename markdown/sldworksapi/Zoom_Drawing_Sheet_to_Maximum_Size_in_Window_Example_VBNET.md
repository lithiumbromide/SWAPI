---
title: "Zoom Drawing Sheet to Maximum Size in Window Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Zoom_Drawing_Sheet_to_Maximum_Size_in_Window_Example_VBNET.htm"
---

# Zoom Drawing Sheet to Maximum Size in Window Example (VB.NET)

This example shows how to zoom a drawing sheet to its maximum size within the window.

```
'------------------------------------------------------
' Preconditions: Verify that the drawing to open exists.
'
' Postconditions:
' 1. Opens the drawing.
' 2. Zooms the drawing sheet to its maximum size within
'    the window.
' 3. Examine the graphics area.
'
' NOTE: Because the drawing is used elsewhere, do not
' save changes.
'-------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\replaceview.slddrw"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        swModelDocExt.ViewZoomToSheet()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
