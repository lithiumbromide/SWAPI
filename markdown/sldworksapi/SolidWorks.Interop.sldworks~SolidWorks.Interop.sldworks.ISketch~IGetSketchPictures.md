---
title: "IGetSketchPictures Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IGetSketchPictures"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchPictures.html"
---

# IGetSketchPictures Method (ISketch)

Gets the pictures on this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSketchPictures( _
   ByVal Count As System.Integer _
) As SketchPicture
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim Count As System.Integer
Dim value As SketchPicture

value = instance.IGetSketchPictures(Count)
```

### C#

```csharp
SketchPicture IGetSketchPictures(
   System.int Count
)
```

### C++/CLI

```cpp
SketchPicture^ IGetSketchPictures(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of pictures on this sketch

### Return Value

- in-process, unmanaged C++: Pointer to an array of [pictures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPicture.html) on this sketch

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [Sketch::IGetSketchPictures](ms-its:sldworksapivb6.chm::/Sldworks~Sketch~IGetSketchPictures.html).

## Remarks

Call [ISketch::GetSketchPictureCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchPictureCount.html) before calling this method to get the value of Count.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchPictures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPictures.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
