---
title: "FinalRenderQuality Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "FinalRenderQuality"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~FinalRenderQuality.html"
---

# FinalRenderQuality Property (IRayTraceRendererOptions)

Gets or sets quality of the [final render](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property FinalRenderQuality As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Integer

instance.FinalRenderQuality = value

value = instance.FinalRenderQuality
```

### C#

```csharp
System.int FinalRenderQuality {get; set;}
```

### C++/CLI

```cpp
property System.int FinalRenderQuality {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Quality of final render as defined in [swRayTraceRenderQuality_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRayTraceRenderQuality_e.html)

## VBA Syntax

See [RayTraceRendererOptions::FinalRenderQuality](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~FinalRenderQuality.html).

## Examples

[Render Model (C#)](Render_Model_Example_CSharp.htm)
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)
[Render Model (VBA)](Render_Model_Example_VB.htm)

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::PreviewRenderQuality Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~PreviewRenderQuality.html)
[IRayTraceRendererOptions::DirectCaustics Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~DirectCaustics.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
