---
title: "CausticQuality Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "CausticQuality"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CausticQuality.html"
---

# CausticQuality Property (IRayTraceRendererOptions)

Gets or sets the number of photons sampled at each pixel, which controls the quality of the caustics.

## Syntax

### Visual Basic (Declaration)

```vb
Property CausticQuality As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Integer

instance.CausticQuality = value

value = instance.CausticQuality
```

### C#

```csharp
System.int CausticQuality {get; set;}
```

### C++/CLI

```cpp
property System.int CausticQuality {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of photons sampled at each pixel

## VBA Syntax

See [RayTraceRendererOptions::CausticQuality](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~CausticQuality.html).

## Remarks

Increasing the number of photons sampled at each pixel creates a smoother caustic effect at the expense of detail. Decreasing the number of photons results in a sharper caustic effect with increasing graininess.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::CausticAmount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CausticAmount.html)
[IRayTraceRendererOptions::DirectCaustics Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~DirectCaustics.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
