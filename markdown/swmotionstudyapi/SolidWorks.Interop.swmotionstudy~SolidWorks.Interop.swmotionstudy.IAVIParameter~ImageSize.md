---
title: "ImageSize Property (IAVIParameter)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IAVIParameter"
member: "ImageSize"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter~ImageSize.html"
---

# ImageSize Property (IAVIParameter)

Gets or sets the image size of the animation.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImageSize As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAVIParameter
Dim value As System.Integer

instance.ImageSize = value

value = instance.ImageSize
```

### C#

```csharp
System.int ImageSize {get; set;}
```

### C++/CLI

```cpp
property System.int ImageSize {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Image size as defined by [swSaveAVIImageSize_e](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.swSaveAVIImageSize_e.html)

## VBA Syntax

See [AVIParameter::ImageSize](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~AVIParameter~ImageSize.html).

## See Also

[IAVIParameter Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter.html)
[IAVIParameter Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
