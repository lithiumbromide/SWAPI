---
title: "GetPixels Method (IBitmapImageSource)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IBitmapImageSource"
member: "GetPixels"
kind: "method"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IBitmapImageSource~GetPixels.html"
---

# GetPixels Method (IBitmapImageSource)

Gets the raw pixel buffer of the bitmap image.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPixels() As System.Byte()
```

### Visual Basic (Usage)

```vb
Dim instance As IBitmapImageSource
Dim value() As System.Byte

value = instance.GetPixels()
```

### C#

```csharp
System.byte[] GetPixels()
```

### C++/CLI

```cpp
System.array<byte>^ GetPixels();
```

### Return Value

A byte array representing the pixel data of the image (see **Remarks**)

## VBA Syntax

See [IBitmapImageSource::GetPixels](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IBitmapImageSource~GetPixels.html).

## Remarks

This method returns the raw pixel buffer of the bitmap image in Bgr32 format. Bgr32 is a 32-bit sRGB pixel format in which each pixel is composed of 8 bits each for blue, green and red channels. There is an additional 8 unused bits, typically for alignment.

The byte array length is Width X Height X 4 bytes. Pixels are laid out in row-major order, left to right, top to bottom.

## See Also

[IBitmapImageSource Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IBitmapImageSource.html)
[IBitmapImageSource Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IBitmapImageSource_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2026 FCS
