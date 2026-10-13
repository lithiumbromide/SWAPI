---
title: "Render Model (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Render_Model_Example_VB.htm"
---

# Render Model (VBA)

This example shows how to use a ray-trace rendering engine to render a model and save the rendered image in BMP and HDR formats. You must have a Premium license to run this example.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that:
 '    * specified part exists.
 '    * c:\temp exists.
 '    * ray-trace rendering engine is loaded in SOLIDWORKS Design.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. If prompted to use perspective views in renderings, click
 '    Continue without Camera or Perspective.
 ' 2. Changes the specified rendering options.
 ' 3. Creates c:\temp\Filter_1.bmp and c:\temp\Filter_2.hdr containing
 '    rendered images of the part.
 ' 4. Examine the Immediate window and c:\temp.
 '
 ' NOTE: Rendering can take several minutes to complete.
 '---------------------------------------------------------------------------
 Option Explicit
 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swRayTraceRenderer As SldWorks.RayTraceRenderer
 Dim swRayTraceRenderOptions As SldWorks.RayTraceRendererOptions
 Dim errors As Long
 Dim warnings As Long
 Dim fileName As String
 Dim status As Boolean

 Sub main()

     Set swApp = Application.SldWorks
     fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\routing-pipes\fittings\filter.sldprt"
     Set swModel = swApp.OpenDoc6(fileName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)

    ' Access ray-trace rendering engine
    ' Set swRayTraceRenderer = swApp.GetRayTraceRenderer(ray_trace_rendering_engine_member)

    ' Get and set rendering options
     Set swRayTraceRenderOptions = swRayTraceRenderer.RayTraceRendererOptions

    ' Get current rendering values
     Debug.Print "Current rendering values"
     Debug.Print "  Image height = " & swRayTraceRenderOptions.ImageHeight
     Debug.Print "  Image width = " & swRayTraceRenderOptions.ImageWidth
     Debug.Print "  Image format = " & swRayTraceRenderOptions.ImageFormat
     Debug.Print "  Preview render quality = " & swRayTraceRenderOptions.PreviewRenderQuality
     Debug.Print "  Final render quality = " & swRayTraceRenderOptions.FinalRenderQuality
     Debug.Print "  Bloom enabled? " & swRayTraceRenderOptions.BloomEnabled
     Debug.Print "  Bloom threshold = " & swRayTraceRenderOptions.BloomThreshold
     Debug.Print "  Bloom radius = " & swRayTraceRenderOptions.BloomRadius
     Debug.Print "  Contour/cartoon enabled? " & swRayTraceRenderOptions.ContourCartoonRenderingEnabled
     Debug.Print "  Render type = " & swRayTraceRenderOptions.RenderType
     Debug.Print "  Shaded contour? " & swRayTraceRenderOptions.ShadedContour
     Debug.Print "  Contour line thickness = " & swRayTraceRenderOptions.ContourLineThickness
     Debug.Print "  Contour line color = " & swRayTraceRenderOptions.ContourLineColor
     Debug.Print "  Use SOLIDWORKS Design view aspect ratio? " & swRayTraceRenderOptions.UseSolidWorksViewAspectRatio
     Debug.Print "  Alpha output? " & swRayTraceRenderOptions.AlphaOutput
     Debug.Print " "

    ' Change rendering values
     Debug.Print "New rendering values"
     swRayTraceRenderOptions.ImageHeight = 567
     Debug.Print "  Image height = " & swRayTraceRenderOptions.ImageHeight
     swRayTraceRenderOptions.ImageWidth = 678
     Debug.Print "  Image width = " & swRayTraceRenderOptions.ImageWidth
     swRayTraceRenderOptions.ImageFormat = swImageFormat_HDR
     Debug.Print "  Image format = " & swRayTraceRenderOptions.ImageFormat
     swRayTraceRenderOptions.PreviewRenderQuality = swRenderQuality_Better
     Debug.Print "  Preview render quality = " & swRayTraceRenderOptions.PreviewRenderQuality
     swRayTraceRenderOptions.FinalRenderQuality = swRenderQuality_Best
     Debug.Print "  Final render quality = " & swRayTraceRenderOptions.FinalRenderQuality
     swRayTraceRenderOptions.BloomEnabled = False
     Debug.Print "  Bloom enabled? " & swRayTraceRenderOptions.BloomEnabled
     swRayTraceRenderOptions.BloomThreshold = 70
     Debug.Print "  Bloom threshold = " & swRayTraceRenderOptions.BloomThreshold
     swRayTraceRenderOptions.BloomRadius = 4
     Debug.Print "  Bloom radius = " & swRayTraceRenderOptions.BloomRadius
     swRayTraceRenderOptions.ContourCartoonRenderingEnabled = True
     Debug.Print "  Contour/cartoon enabled? " & swRayTraceRenderOptions.ContourCartoonRenderingEnabled
     swRayTraceRenderOptions.RenderType = swRayTraceRenderingType_e.swRayTraceContour
     Debug.Print "  Render type = " & swRayTraceRenderOptions.RenderType
     swRayTraceRenderOptions.ShadedContour = False
     Debug.Print "  Shaded contour? " & swRayTraceRenderOptions.ShadedContour
     swRayTraceRenderOptions.ContourLineThickness = 3
     Debug.Print "  Contour line thickness = " & swRayTraceRenderOptions.ContourLineThickness
     swRayTraceRenderOptions.ContourLineColor = 255
     Debug.Print "  Contour line color = " & swRayTraceRenderOptions.ContourLineColor
     swRayTraceRenderOptions.UseSolidWorksViewAspectRatio = True
     Debug.Print "  Use SOLIDWORKS Design view aspect ratio? " & swRayTraceRenderOptions.UseSolidWorksViewAspectRatio

    ' Display the preview window
     'status = swRayTraceRenderer.DisplayPreviewWindow
     ' Display final render window
     'status = swRayTraceRenderer.InvokeFinalRender

    ' Render in HDR format
     status = swRayTraceRenderer.RenderToFile("c:\temp\Filter_2", 0, 0)
     ' Render in BMP format
     swRayTraceRenderOptions.ImageFormat = swImageFormat_WindowsBmp
     status = swRayTraceRenderer.RenderToFile("c:\temp\Filter_1", 0, 0)

     ' Abort final render
     'status = swRayTraceRenderer.AbortFinalRender
     ' Close preview and final render windows
     'status = swRayTraceRenderer.CloseRayTraceRender

 End Sub
```
