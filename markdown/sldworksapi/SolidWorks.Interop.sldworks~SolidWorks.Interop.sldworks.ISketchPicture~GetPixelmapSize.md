---
title: "GetPixelmapSize Method (ISketchPicture)"
project: "SOLIDWORKS API Help"
interface: "ISketchPicture"
member: "GetPixelmapSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPixelmapSize.html"
---

# GetPixelmapSize Method (ISketchPicture)

Gets the size of the array for the picture pixels.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPixelmapSize( _
   ByRef Width As System.Integer, _
   ByRef Height As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPicture
Dim Width As System.Integer
Dim Height As System.Integer
Dim value As System.Integer

value = instance.GetPixelmapSize(Width, Height)
```

### C#

```csharp
System.int GetPixelmapSize(
   out System.int Width,
   out System.int Height
)
```

### C++/CLI

```cpp
System.int GetPixelmapSize(
   [Out] System.int Width,
   [Out] System.int Height
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Width`: Number of columns in the pixel map
- `Height`: Number of rows in the pixel map

### Return Value

Size of the array of the picture pixels

## VBA Syntax

See [SketchPicture::GetPixelmapSize](ms-its:sldworksapivb6.chm::/Sldworks~SketchPicture~GetPixelmapSize.html).

## Remarks

Call this method before calling [ISketchPicture::IGetPixelmap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPicture~IGetPixelmap.html) to get the size of the array for that method.

## See Also

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html)
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.html)
[ISketchPicture::GetPixelmap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPixelmap.html)
[ISketchPicture::GetPointOnSketchFromPixel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPointOnSketchFromPixel.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
