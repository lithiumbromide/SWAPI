---
title: "Include Note in Render File Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Include_Note_in_Render_File_Example_VB.htm"
---

# Include Note in Render File Example (VBA)

This example shows how to include a note visible in a model in the render file.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Add a note to the model.
' 3. Verify that:
'    * a ray-trace rendering engine is loaded.
'    * c:\temp exists.
' 4. Open the Immediate window.
'
' Preconditions:
' 1. Sets the option to include the note visible in the model
'    in the render file.
' 2. If prompted to add camera or perspective, click Continue
'    without Camera or Perspective.
' 3. Examine the Immediate window and c:\temp\annotations.png.
'--------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
        Dim swApp As SldWorks.SldWorks
        Dim swModel As SldWorks.ModelDoc2
        Dim swRayTraceRenderer As SldWorks.RayTraceRenderer
        Dim swRayTraceRenderOptions As SldWorks.RayTraceRendererOptions
        Dim status As Boolean
```

```
        Set swApp = Application.SldWorks
        Set swModel = swApp.ActiveDoc
```

```
        'Access the ray-trace rendering engine
        'Set swRayTraceRenderer = swApp.GetRayTraceRenderer()
```

```
        'Set option to include note visible in the model in the render file
        Set swRayTraceRenderOptions = swRayTraceRenderer.RayTraceRendererOptions
        swRayTraceRenderOptions.IncludeAnnotationsInRendering = True
        Debug.Print ("Include note in render file? " & swRayTraceRenderOptions.IncludeAnnotationsInRendering)
        status = swRayTraceRenderer.RenderToFile("c:\temp\annotations.png", 0, 0)
        Debug.Print "Note included in render file? " & status
        status = swRayTraceRenderer.CloseFinalRenderWindow
```

```
End Sub
```
