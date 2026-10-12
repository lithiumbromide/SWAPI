---
title: "Zoom Drawing Sheet to Maximum Size in Window Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Zoom_Drawing_Sheet_to_Maximum_Size_in_Window_Example_VB.htm"
---

# Zoom Drawing Sheet to Maximum Size in Window Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim fileName As String
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\replaceview.slddrw"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    swModelDocExt.ViewZoomtoSheet
```

```
End Sub
```
