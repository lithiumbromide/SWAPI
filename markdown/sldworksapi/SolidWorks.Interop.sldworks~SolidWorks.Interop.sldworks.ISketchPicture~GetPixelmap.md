---
title: "GetPixelmap Method (ISketchPicture)"
project: "SOLIDWORKS API Help"
interface: "ISketchPicture"
member: "GetPixelmap"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPixelmap.html"
---

# GetPixelmap Method (ISketchPicture)

Gets the picture pixels.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPixelmap() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPicture
Dim value As System.Object

value = instance.GetPixelmap()
```

### C#

```csharp
System.object GetPixelmap()
```

### C++/CLI

```cpp
System.Object^ GetPixelmap();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array containing groups of three or four values (see Remarks)

## VBA Syntax

See [SketchPicture::GetPixelmap](ms-its:sldworksapivb6.chm::/Sldworks~SketchPicture~GetPixelmap.html).

## Remarks

The array contains groups of three, the Red, Green, Blue (RGB) components of pixel color, and optionally a fourth value that indicates the transparency of the pixel, which can be a value from 0 (transparent) to 255 (opaque).

To determine the format of the data, you need the information returned by [ISketchPicture::GetPixelmapSize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPicture~IGetPixelmap.html):

Number of items per pixel = size / (rows * columns)

Each group of three or four goes across each pixel in a row of the bitmap. The next row follows in the array.

This raw data does not include translation, scaling, rotation, and flipping. SOLIDWORKS Design applies these properties to the raw bitmap data to draw it in the sketch.

## See Also

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html)
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.html)
[ISketchPicture::IGetPixelmap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~IGetPixelmap.html)
[ISketchPicture::GetPointOnSketchFromPixel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPointOnSketchFromPixel.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
