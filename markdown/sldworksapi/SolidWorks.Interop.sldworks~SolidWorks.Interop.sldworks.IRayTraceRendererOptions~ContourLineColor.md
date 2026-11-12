---
title: "ContourLineColor Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "ContourLineColor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourLineColor.html"
---

# ContourLineColor Property (IRayTraceRendererOptions)

Gets or sets the color of the contour lines.

## Syntax

### Visual Basic (Declaration)

```vb
Property ContourLineColor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Integer

instance.ContourLineColor = value

value = instance.ContourLineColor
```

### C#

```csharp
System.int ContourLineColor {get; set;}
```

### C++/CLI

```cpp
property System.int ContourLineColor {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

RGB value for color of contour lines

## VBA Syntax

See [RayTraceRendererOptions::ContourLineColor](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~ContourLineColor.html).

## Examples

[Render Model (C#)](Render_Model_Example_CSharp.htm)
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)
[Render Model (VBA)](Render_Model_Example_VB.htm)

## Remarks

This property is only available when [IRayTraceRendererOptions::ContourCartoonRenderingEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourCartoonRenderingEnabled.html) is true.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::ContourLineThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ContourLineThickness.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
