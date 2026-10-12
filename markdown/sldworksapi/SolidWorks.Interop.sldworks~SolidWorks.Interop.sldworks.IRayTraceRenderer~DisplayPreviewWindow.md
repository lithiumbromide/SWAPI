---
title: "DisplayPreviewWindow Method (IRayTraceRenderer)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRenderer"
member: "DisplayPreviewWindow"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~DisplayPreviewWindow.html"
---

# DisplayPreviewWindow Method (IRayTraceRenderer)

Displays the preview render window.

## Syntax

### Visual Basic (Declaration)

```vb
Function DisplayPreviewWindow() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRenderer
Dim value As System.Boolean

value = instance.DisplayPreviewWindow()
```

### C#

```csharp
System.bool DisplayPreviewWindow()
```

### C++/CLI

```cpp
System.bool DisplayPreviewWindow();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if preview render window is displayed, false if not

## VBA Syntax

See [RayTraceRenderer::DisplayPreviewWindow](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRenderer~DisplayPreviewWindow.html).

## Examples

[Render Model (C#)](Render_Model_Example_CSharp.htm)
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)
[Render Model (VBA)](Render_Model_Example_VB.htm)

## See Also

[IRayTraceRenderer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer.html)
[IRayTraceRenderer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer_members.html)
[IRayTraceRendererOptions::PreviewRenderQuality Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~PreviewRenderQuality.html)
[IRayTraceRenderer::CloseFinalRenderWindow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~CloseFinalRenderWindow.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
