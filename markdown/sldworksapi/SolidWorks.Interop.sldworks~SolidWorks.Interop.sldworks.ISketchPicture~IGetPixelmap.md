---
title: "IGetPixelmap Method (ISketchPicture)"
project: "SOLIDWORKS API Help"
interface: "ISketchPicture"
member: "IGetPixelmap"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~IGetPixelmap.html"
---

# IGetPixelmap Method (ISketchPicture)

Gets the picture pixels.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPixelmap( _
   ByVal Count As System.Integer _
) As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPicture
Dim Count As System.Integer
Dim value As System.Short

value = instance.IGetPixelmap(Count)
```

### C#

```csharp
System.short IGetPixelmap(
   System.int Count
)
```

### C++/CLI

```cpp
System.short IGetPixelmap(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Size of the array

### Return Value

- in-process, unmanaged C++: Pointer to an array containing groups of 3 or 4 values (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The array contains groups of three, the Red, Green, Blue (RGB) components of pixel color, and optionally, a fourth value that indicates the transparency of the pixel, which can be a value from 0 (transparent) to 255 (opaque).

Before calling this method, call [ISketchPicture::GetPixelmapSize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPicture~GetPixelmapSize.html) to get the value of Count.

To determine the format of the data, you need the information returned by ISketchPicture::GetPixelmapSize:

Number of items per pixel = size / (rows * columns)

Each group of three or four goes across each pixel in a row of the bitmap. The next row follows in the array.

This raw data does not include translation, scaling, rotation, and flipping. SOLIDWORKS Design applies these properties to the raw bitmap data to draw it in the sketch.

## See Also

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html)
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.html)
[ISketchPicture::GetPixelmap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPixelmap.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
