---
title: "RenderType Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "RenderType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~RenderType.html"
---

# RenderType Property (IRayTraceRendererOptions)

Gets or sets whether to render with contour or cartoon lines.

## Syntax

### Visual Basic (Declaration)

```vb
Property RenderType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Integer

instance.RenderType = value

value = instance.RenderType
```

### C#

```csharp
System.int RenderType {get; set;}
```

### C++/CLI

```cpp
property System.int RenderType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Render type as defined by [swRayTraceRenderingType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRayTraceRenderingType_e.html)

## VBA Syntax

See [RayTraceRendererOptions::RenderType](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~RenderType.html).

## Examples

[Render Model (C#)](Render_Model_Example_CSharp.htm)
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)
[Render Model (VBA)](Render_Model_Example_VB.htm)
[Update Graphics Area After Changing Render Options (C#)](Update_Graphics_After_Changing_Render_Options_Example_CSharp.htm)
[Update Graphics Area After Changing Render Options (VB.NET)](Update_Graphics_After_Changing_Render_Options_Example_VBNET.htm)
[Update Graphics Area After Changing Render Options (VBA)](Update_Graphics_After_Changing_Render_Options_Example_VB.htm)

## Remarks

This property is only available when [IRayTraceRendererOptions::ContourCartoonRenderingEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourCartoonRenderingEnabled.html) is true.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::HasCartoonEdges Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~HasCartoonEdges.html)
[IRayTraceRendererOptions::HasCartoonShading Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~HasCartoonShading.html)
[IRayTraceRendererOptions::ShadedContour Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ShadedContour.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
