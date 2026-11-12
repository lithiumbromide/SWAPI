---
title: "UpdateGraphics Method (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "UpdateGraphics"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~UpdateGraphics.html"
---

# UpdateGraphics Method (IRayTraceRendererOptions)

Updates the graphics area.

## Syntax

### Visual Basic (Declaration)

```vb
Sub UpdateGraphics()
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions

instance.UpdateGraphics()
```

### C#

```csharp
void UpdateGraphics()
```

### C++/CLI

```cpp
void UpdateGraphics();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [RayTraceRendererOptions::UpdateGraphics](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~UpdateGraphics.html).

## Examples

[Update Graphics Area After Changing Render Options (C#)](Update_Graphics_After_Changing_Render_Options_Example_CSharp.htm)
[Update Graphics Area After Changing Render Options (VB.NET)](Update_Graphics_After_Changing_Render_Options_Example_VBNET.htm)
[Update Graphics Area After Changing Render Options (VBA)](Update_Graphics_After_Changing_Render_Options_Example_VB.htm)

## Remarks

To visually verify your changes after changing a model's ray-trace rendering engine's options and before rendering the model, call this method.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRenderer::InvokeFinalRender Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.html)
[IRayTraceRenderer::RenderToFile Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~RenderToFile.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
