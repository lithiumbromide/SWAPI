---
title: "ShadedContour Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "ShadedContour"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ShadedContour.html"
---

# ShadedContour Property (IRayTraceRendererOptions)

Gets or sets whether to shade the contours lines.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShadedContour As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean

instance.ShadedContour = value

value = instance.ShadedContour
```

### C#

```csharp
System.bool ShadedContour {get; set;}
```

### C++/CLI

```cpp
property System.bool ShadedContour {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to shade the contour lines, false to not

## VBA Syntax

See [RayTraceRendererOptions::ShadedContour](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~ShadedContour.html).

## Examples

[Render Model (C#)](Render_Model_Example_CSharp.htm)
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)
[Render Model (VBA)](Render_Model_Example_VB.htm)

## Remarks

This property is only available when [IRayTraceRendererOptions::ContourCartoonRenderingEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourCartoonRenderingEnabled.html) is true and [IRayTraceRendererOptions::RenderType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~RenderType.html) is swRayTraceRenderingType_e.swRayTraceContour.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::ContourLineColor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourLineColor.html)
[IRayTraceRendererOptions::ContourLineThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourLineThickness.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
