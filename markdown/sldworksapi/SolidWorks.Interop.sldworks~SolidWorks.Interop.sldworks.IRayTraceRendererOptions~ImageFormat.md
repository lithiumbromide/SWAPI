---
title: "ImageFormat Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "ImageFormat"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageFormat.html"
---

# ImageFormat Property (IRayTraceRendererOptions)

Gets or sets the format of the image.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImageFormat As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Integer

instance.ImageFormat = value

value = instance.ImageFormat
```

### C#

```csharp
System.int ImageFormat {get; set;}
```

### C++/CLI

```cpp
property System.int ImageFormat {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Format of the image as defined in [swRayTraceRenderImageFormat_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRayTraceRenderImageFormat_e.html)

## VBA Syntax

See [RayTraceRendererOptions::ImageFormat](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~ImageFormat.html).

## Examples

[Render Model (C#)](Render_Model_Example_CSharp.htm)
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)
[Render Model (VBA)](Render_Model_Example_VB.htm)

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::ImageHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageHeight.html)
[IRayTraceRendererOptions::ImageWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageWidth.html)
[IRayTraceRendererOptions::DefaultImagePath Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~DefaultImagePath.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
