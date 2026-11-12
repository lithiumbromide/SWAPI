---
title: "DefaultImagePath Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "DefaultImagePath"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~DefaultImagePath.html"
---

# DefaultImagePath Property (IRayTraceRendererOptions)

Gets or sets the default path to which to save the image.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefaultImagePath As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.String

instance.DefaultImagePath = value

value = instance.DefaultImagePath
```

### C#

```csharp
System.string DefaultImagePath {get; set;}
```

### C++/CLI

```cpp
property System.String^ DefaultImagePath {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path to which to save the image

## VBA Syntax

See [RayTraceRendererOptions::DefaultImagePath](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~DefaultImagePath.html).

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::ImageFormat Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageFormat.html)
[IRayTraceRendererOptions::ImageHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageHeight.html)
[IRayTraceRendererOptions::ImageWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ImageWidth.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
