---
title: "HasCartoonShading Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "HasCartoonShading"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~HasCartoonShading.html"
---

# HasCartoonShading Property (IRayTraceRendererOptions)

Gets or sets whether to render with cartoon shading.

## Syntax

### Visual Basic (Declaration)

```vb
Property HasCartoonShading As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean

instance.HasCartoonShading = value

value = instance.HasCartoonShading
```

### C#

```csharp
System.bool HasCartoonShading {get; set;}
```

### C++/CLI

```cpp
property System.bool HasCartoonShading {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to render with cartoon shading, false to not

## VBA Syntax

See [RayTraceRendererOptions::HasCartoonShading](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~HasCartoonShading.html).

## Remarks

This property is only available when [IRayTraceRendererOptions::ContourCartoonRenderingEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourCartoonRenderingEnabled.html) is true and [IRayTraceRendererOptions::RenderType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~RenderType.html) is swRayTraceRenderingType_e.swRayTraceCartoon.

| To set cartoon... | Set IRayTraceRendererOptions::HasCartoonEdges to... | Set IRayTraceRendererOptions::HasCartoonShading to... |
| --- | --- | --- |
| Edges | True | False |
| Shading | False | True |
| Edges and shading | True | True |

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::ContourLineColor Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourLineColor.html)
[IRayTraceRendererOptions::ContourLineThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourLineThickness.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
