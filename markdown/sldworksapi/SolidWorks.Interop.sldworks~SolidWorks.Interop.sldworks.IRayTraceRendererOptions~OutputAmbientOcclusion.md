---
title: "OutputAmbientOcclusion Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "OutputAmbientOcclusion"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~OutputAmbientOcclusion.html"
---

# OutputAmbientOcclusion Property (IRayTraceRendererOptions)

Gets or sets whether to render with ambient occlusion.

## Syntax

### Visual Basic (Declaration)

```vb
Property OutputAmbientOcclusion As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean

instance.OutputAmbientOcclusion = value

value = instance.OutputAmbientOcclusion
```

### C#

```csharp
System.bool OutputAmbientOcclusion {get; set;}
```

### C++/CLI

```cpp
property System.bool OutputAmbientOcclusion {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to render with ambient occlusion, false to not

## VBA Syntax

See [RayTraceRendererOptions::OutputAmbientOcclusion](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~OutputAmbientOcclusion.html).

## Remarks

Ambient occlusion is a global lighting method that adds realism to models by controlling the attenuation of ambient light due to occluded areas. Objects appear as they would on an overcast day.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
