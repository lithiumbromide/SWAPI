---
title: "NumberOfRefractions Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "NumberOfRefractions"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NumberOfRefractions.html"
---

# NumberOfRefractions Property (IRayTraceRendererOptions)

Gets or sets the number of refractions in the [final render](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property NumberOfRefractions As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Integer

instance.NumberOfRefractions = value

value = instance.NumberOfRefractions
```

### C#

```csharp
System.int NumberOfRefractions {get; set;}
```

### C++/CLI

```cpp
property System.int NumberOfRefractions {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0 <= Number of refractions <= 32

## VBA Syntax

See [RayTraceRendererOptions::NumberOfRefractions](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~NumberOfRefractions.html).

## Remarks

This property is only available when [IRayTraceRendererOptions::CustomRenderSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CustomRenderSettings.html) is true.

The number of refractions impacts rendering performance, so only use a high number of refractions to correctly see objects in the rendering.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::NumberOfReflections Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NumberOfReflections.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
