---
title: "PreviewRenderQuality Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "PreviewRenderQuality"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~PreviewRenderQuality.html"
---

# PreviewRenderQuality Property (IRayTraceRendererOptions)

Gets or sets the quality of the rendering in the preview window.

## Syntax

### Visual Basic (Declaration)

```vb
Property PreviewRenderQuality As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Integer

instance.PreviewRenderQuality = value

value = instance.PreviewRenderQuality
```

### C#

```csharp
System.int PreviewRenderQuality {get; set;}
```

### C++/CLI

```cpp
property System.int PreviewRenderQuality {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Quality of the rendering in the preview window as defined in [swRayTraceRenderQuality_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRayTraceRenderQuality_e.html)

## VBA Syntax

See [RayTraceRendererOptions::PreviewRenderQuality](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~PreviewRenderQuality.html).

## Examples

[Render Model (C#)](Render_Model_Example_CSharp.htm)
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)
[Render Model (VBA)](Render_Model_Example_VB.htm)

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRenderer::DisplayPreviewWindow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~DisplayPreviewWindow.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
