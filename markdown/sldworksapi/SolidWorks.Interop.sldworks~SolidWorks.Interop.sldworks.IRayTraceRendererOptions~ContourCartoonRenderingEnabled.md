---
title: "ContourCartoonRenderingEnabled Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "ContourCartoonRenderingEnabled"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourCartoonRenderingEnabled.html"
---

# ContourCartoonRenderingEnabled Property (IRayTraceRendererOptions)

Gets or sets whether to enable contour/cartoon rendering.

## Syntax

### Visual Basic (Declaration)

```vb
Property ContourCartoonRenderingEnabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean

instance.ContourCartoonRenderingEnabled = value

value = instance.ContourCartoonRenderingEnabled
```

### C#

```csharp
System.bool ContourCartoonRenderingEnabled {get; set;}
```

### C++/CLI

```cpp
property System.bool ContourCartoonRenderingEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable contour/cartoon rendering, false to not

## VBA Syntax

See [RayTraceRendererOptions::ContourCartoonRenderingEnabled](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~ContourCartoonRenderingEnabled.html).

## Examples

[Render Model (C#)](Render_Model_Example_CSharp.htm)
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)
[Render Model (VBA)](Render_Model_Example_VB.htm)
[Update Graphics Area After Changing Render Options (C#)](Update_Graphics_After_Changing_Render_Options_Example_CSharp.htm)
[Update Graphics Area After Changing Render Options (VB.NET)](Update_Graphics_After_Changing_Render_Options_Example_VBNET.htm)
[Update Graphics Area After Changing Render Options (VBA)](Update_Graphics_After_Changing_Render_Options_Example_VB.htm)

## Remarks

After setting this property, call [IRayTraceRendererOptions::RenderType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~RenderType.html) to set rendering to either contour or cartoon.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::ContourLineColor Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourLineColor.html)
[IRayTraceRendererOptions::ContourLineThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourLineThickness.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
