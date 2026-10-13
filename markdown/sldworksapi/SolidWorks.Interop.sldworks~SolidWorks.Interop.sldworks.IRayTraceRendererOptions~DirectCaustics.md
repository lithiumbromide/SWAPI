---
title: "DirectCaustics Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "DirectCaustics"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~DirectCaustics.html"
---

# DirectCaustics Property (IRayTraceRendererOptions)

Gets or sets whether to enable direct caustics in the [final render](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property DirectCaustics As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean

instance.DirectCaustics = value

value = instance.DirectCaustics
```

### C#

```csharp
System.bool DirectCaustics {get; set;}
```

### C++/CLI

```cpp
property System.bool DirectCaustics {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable direct caustics in the final render, false to not

## VBA Syntax

See [RayTraceRendererOptions::DirectCaustics](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~DirectCaustics.html).

## Remarks

Direct caustics are only visible in the final render and only when reflected off a floor appearance or physical geometry using a spot or point light. The light bounces off or filters through the model creating a bright pattern on the floor.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::CausticAmount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CausticAmount.html)
[IRayTraceRendererOptions::CausticQuality Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CausticQuality.html)
[IRayTraceRendererOptions::FinalRenderQuality Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~FinalRenderQuality.html)
[IRayTraceRendererOptions::PreviewRenderQuality Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~PreviewRenderQuality.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
