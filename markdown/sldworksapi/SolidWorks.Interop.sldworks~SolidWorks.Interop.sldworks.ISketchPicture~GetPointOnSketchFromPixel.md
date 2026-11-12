---
title: "GetPointOnSketchFromPixel Method (ISketchPicture)"
project: "SOLIDWORKS API Help"
interface: "ISketchPicture"
member: "GetPointOnSketchFromPixel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPointOnSketchFromPixel.html"
---

# GetPointOnSketchFromPixel Method (ISketchPicture)

Gets the sketch coordinate for the specified pixel.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPointOnSketchFromPixel( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPicture
Dim Row As System.Integer
Dim Column As System.Integer
Dim value As MathPoint

value = instance.GetPointOnSketchFromPixel(Row, Column)
```

### C#

```csharp
MathPoint GetPointOnSketchFromPixel(
   System.int Row,
   System.int Column
)
```

### C++/CLI

```cpp
MathPoint^ GetPointOnSketchFromPixel(
   System.int Row,
   System.int Column
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: Row for this pixel
- `Column`: Column for this pixel

### Return Value

[Point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) in the sketch space

## VBA Syntax

See [SketchPicture::GetPointOnSketchFromPixel](ms-its:sldworksapivb6.chm::/Sldworks~SketchPicture~GetPointOnSketchFromPixel.html).

## Remarks

This method gets a point in the sketch space for the specified 0-based row and column indices from the pixel map. Because the bitmap data is raw data, this method helps determine where a point on the sketch is for the pixel after all of the transformation information has been applied. This method helps connect the raw data to its sketch.

See [ISketchPicture::GetPixelmap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPicture~GetPixelmap.html) or [ISketchPicture::IGetPixelmap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPicture~IGetPixelmap.html) for more information about the pixel map.

## See Also

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html)
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.html)
[ISketchPicture::GetPixelmapSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPixelmapSize.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
