---
title: "CloseFinalRenderWindow Method (IRayTraceRenderer)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRenderer"
member: "CloseFinalRenderWindow"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~CloseFinalRenderWindow.html"
---

# CloseFinalRenderWindow Method (IRayTraceRenderer)

Closes the final render window, but leaves the [preview window](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRayTraceRenderer~DisplayPreviewWindow.html) open.

## Syntax

### Visual Basic (Declaration)

```vb
Function CloseFinalRenderWindow() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRenderer
Dim value As System.Boolean

value = instance.CloseFinalRenderWindow()
```

### C#

```csharp
System.bool CloseFinalRenderWindow()
```

### C++/CLI

```cpp
System.bool CloseFinalRenderWindow();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the final render window closed, false if it did not

## VBA Syntax

See [RayTraceRenderer::CloseFinalRenderWindow](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRenderer~CloseFinalRenderWindow.html).

## See Also

[IRayTraceRenderer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer.html)
[IRayTraceRenderer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer_members.html)
[IRayTraceRenderer::CloseRayTraceRender Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~CloseRayTraceRender.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
