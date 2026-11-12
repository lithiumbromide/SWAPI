---
title: "CloseRayTraceRender Method (IRayTraceRenderer)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRenderer"
member: "CloseRayTraceRender"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~CloseRayTraceRender.html"
---

# CloseRayTraceRender Method (IRayTraceRenderer)

Closes both the [preview](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRayTraceRenderer~DisplayPreviewWindow.html) and [final render windows](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRayTraceRenderer~CloseFinalRenderWindow.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CloseRayTraceRender() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRenderer
Dim value As System.Boolean

value = instance.CloseRayTraceRender()
```

### C#

```csharp
System.bool CloseRayTraceRender()
```

### C++/CLI

```cpp
System.bool CloseRayTraceRender();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if both the [preview](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRayTraceRenderer~DisplayPreviewWindow.html) and [final render windows](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRayTraceRenderer~CloseFinalRenderWindow.html) are closed, false if not

## VBA Syntax

See [RayTraceRenderer::CloseRayTraceRender](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRenderer~CloseRayTraceRender.html).

## Examples

[Render Model (C#)](Render_Model_Example_CSharp.htm)
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)
[Render Model (VBA)](Render_Model_Example_VB.htm)

## Remarks

When this method is called after calling [IRayTraceRenderer::Invoke FinalRender](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.html) or [IRayTraceRenderer::RenderToFile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRayTraceRenderer~RenderToFile.html), then both the preview and final render windows are closed.

To leave the preview render window open, call [IRayTraceRenderer::CloseFinalRenderWindow](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRayTraceRenderer~CloseFinalRenderWindow.html) instead of calling IRayTraceRender::CloseRayTraceRender.

## See Also

[IRayTraceRenderer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer.html)
[IRayTraceRenderer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
