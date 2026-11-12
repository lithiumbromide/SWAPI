---
title: "InvokeFinalRender Method (IRayTraceRenderer)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRenderer"
member: "InvokeFinalRender"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.html"
---

# InvokeFinalRender Method (IRayTraceRenderer)

Invokes the final render window.

## Syntax

### Visual Basic (Declaration)

```vb
Function InvokeFinalRender() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRenderer
Dim value As System.Boolean

value = instance.InvokeFinalRender()
```

### C#

```csharp
System.bool InvokeFinalRender()
```

### C++/CLI

```cpp
System.bool InvokeFinalRender();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if final render window is invoked, false if not

## VBA Syntax

See [RayTraceRenderer::InvokeFinalRender](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRenderer~InvokeFinalRender.html).

## Examples

[Render Model (C#)](Render_Model_Example_CSharp.htm)
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)
[Render Model (VBA)](Render_Model_Example_VB.htm)

## See Also

[IRayTraceRenderer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer.html)
[IRayTraceRenderer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer_members.html)
[IRayTraceRendererOptions::UpdateGraphics Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~UpdateGraphics.html)
[IRayTraceRendererOptions::FinalRenderQuality Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~FinalRenderQuality.html)
[IRayTraceRenderer::AbortFinalRender Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~AbortFinalRender.html)
[IRayTraceRenderer::CloseRayTraceRender Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~CloseRayTraceRender.html)
[IRayTraceRenderer::RenderToFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~RenderToFile.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
