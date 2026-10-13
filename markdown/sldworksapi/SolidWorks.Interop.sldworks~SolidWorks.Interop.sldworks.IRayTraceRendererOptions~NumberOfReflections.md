---
title: "NumberOfReflections Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "NumberOfReflections"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NumberOfReflections.html"
---

# NumberOfReflections Property (IRayTraceRendererOptions)

Gets or sets the number of reflections in the [final render](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property NumberOfReflections As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Integer

instance.NumberOfReflections = value

value = instance.NumberOfReflections
```

### C#

```csharp
System.int NumberOfReflections {get; set;}
```

### C++/CLI

```cpp
property System.int NumberOfReflections {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0 <= Number of reflections <= 32

## VBA Syntax

See [RayTraceRendererOptions::NumberOfReflections](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~NumberOfReflections.html).

## Remarks

This property is only available when [IRayTraceRendererOptions::CustomRenderSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CustomRenderSettings.html) is true.

The number of reflections impacts rendering performance, so only use a high number of reflections to correctly see objects in the rendering.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::NumberOfRefractions Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NumberOfRefractions.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
