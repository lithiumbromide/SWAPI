---
title: "ImageHeight Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "ImageHeight"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageHeight.html"
---

# ImageHeight Property (IRayTraceRendererOptions)

Gets or sets the height of the image.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImageHeight As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Integer

instance.ImageHeight = value

value = instance.ImageHeight
```

### C#

```csharp
System.int ImageHeight {get; set;}
```

### C++/CLI

```cpp
property System.int ImageHeight {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Height, in pixels, of the image

## VBA Syntax

See [RayTraceRendererOptions::ImageHeight](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~ImageHeight.html).

## Examples

[Render Model (C#)](Render_Model_Example_CSharp.htm)
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)
[Render Model (VBA)](Render_Model_Example_VB.htm)

## Remarks

You can override the values set in this property and [IRayTraceRendererOptions::ImageWidth](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRayTraceRendererOptions~ImageWidth.html) by specifying Width and Height in [IRayTraceRenderer::RenderToFile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRayTraceRenderer~RenderToFile.html).

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::ImageFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageFormat.html)
[IRayTraceRendererOptions::DefaultImagePath Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~DefaultImagePath.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
