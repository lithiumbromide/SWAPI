---
title: "Render Annotations to Separate Image File Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Render_Annotations_to_Separate_Image_File_Example_VBNET.htm"
---

# Render Annotations to Separate Image File Example (VB.NET)

This example shows how to render annotations and dimensions visible in a model to a separate image file.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Add a note to the model.
' 3. Right-click Annotations in the FeatureManager design tree
'    and click Show Feature Dimensions, if dimensions
'    are not visible in the model.
' 4. Verify that:
'    * a ray-trace rendering engine is loaded.
'    * c:\temp exists.
'
' Preconditions:
' 1. Sets the options to include and render annotations and dimensions
'    visible in a model to a separate image file.
' 2. If prompted to add camera or perspective, click Continue
'    without Camera or Perspective.
' 3. Renders:
'    * model to c:\temp\annotations.png
'    * note and dimensions to c:\temp\annotations_1.png
' 4. Open both files to verify the previous step.
'--------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swRayTraceRenderer As RayTraceRenderer
        Dim swRayTraceRenderOptions As RayTraceRendererOptions
        Dim status As Boolean

        swModel = swApp.ActiveDoc

        'Access the ray-trace rendering engine
        'swRayTraceRenderer = swApp.GetRayTraceRenderer()

        'Set options to include and render annotations and dimensions
        'visible in a model to a separate image file
        swRayTraceRenderOptions = swRayTraceRenderer.RayTraceRendererOptions
        swRayTraceRenderOptions.IncludeAnnotationsInRendering = True
        swRayTraceRenderOptions.RenderAnnotationsToSeparateImage = True
        status = swRayTraceRenderer.RenderToFile("c:\temp\annotations.png", 0, 0)
        status = swRayTraceRenderer.CloseFinalRenderWindow

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
