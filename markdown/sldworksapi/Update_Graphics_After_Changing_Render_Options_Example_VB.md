---
title: "Update Graphics Area After Changing Render Options Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Update_Graphics_After_Changing_Render_Options_Example_VB.htm"
---

# Update Graphics Area After Changing Render Options Example (VBA)

This example shows how to update the graphics area after changing the ray-trace rendering engine's options.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that:
'    * specified part exists.
'    * ray-trace rendering engine is loaded in SOLIDWORKS Design.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. If prompted to use perspective views in rendering, click
'    Continue without camera or perspective and OK.
' 2. Changes the specified render options and updates the graphics area.
' 3. Examine the graphics area and Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swRayTraceRenderer As SldWorks.RayTraceRenderer
Dim swRayTraceRenderOptions As SldWorks.RayTraceRendererOptions
Dim errors As Long
Dim warnings As Long
Dim fileName As String

Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\routing-pipes\fittings\filter.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
```

```
    ' Access ray-trace rendering engine
    Set swRayTraceRenderer = swApp.GetRayTraceRenderer(0)
```

```
    ' Get and set render options
    Set swRayTraceRenderOptions = swRayTraceRenderer.RayTraceRendererOptions
```

```
    ' Get current render values
    Debug.Print "Current render values"
    Debug.Print "  Contour/cartoon enabled? " & swRayTraceRenderOptions.ContourCartoonRenderingEnabled
    Debug.Print "  Render type (0 = cartoon; 1 = contour) = " & swRayTraceRenderOptions.RenderType
    Debug.Print " "
```

```
    ' Change render values and update graphics area
    Debug.Print "Changed render values"
    swRayTraceRenderOptions.ContourCartoonRenderingEnabled = True
    Debug.Print "  Contour/cartoon enabled? " & swRayTraceRenderOptions.ContourCartoonRenderingEnabled
    swRayTraceRenderOptions.RenderType = swRayTraceRenderingType_e.swRayTraceCartoon
    Debug.Print "  Render type (0 = cartoon; 1 = contour) = " & swRayTraceRenderOptions.RenderType
    swRayTraceRenderOptions.HasCartoonEdges = True
    Debug.Print "  Has cartoon edges? " & swRayTraceRenderOptions.HasCartoonEdges
    swRayTraceRenderOptions.UpdateGraphics
```

```
End Sub
```
