---
title: "HasCartoonEdges Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "HasCartoonEdges"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~HasCartoonEdges.html"
---

# HasCartoonEdges Property (IRayTraceRendererOptions)

Gets or sets whether to render with cartoon edges.

## Syntax

### Visual Basic (Declaration)

```vb
Property HasCartoonEdges As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean

instance.HasCartoonEdges = value

value = instance.HasCartoonEdges
```

### C#

```csharp
System.bool HasCartoonEdges {get; set;}
```

### C++/CLI

```cpp
property System.bool HasCartoonEdges {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to render with cartoon edges, false to not

## VBA Syntax

See [RayTraceRendererOptions::HasCartoonEdges](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~HasCartoonEdges.html).

## Examples

[Update Graphics Area After Changing Render Options (C#)](Update_Graphics_After_Changing_Render_Options_Example_CSharp.htm)
[Update Graphics Area After Changing Render Options (VB.NET)](Update_Graphics_After_Changing_Render_Options_Example_VBNET.htm)
[Update Graphics Area After Changing Render Options (VBA)](Update_Graphics_After_Changing_Render_Options_Example_VB.htm)

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
