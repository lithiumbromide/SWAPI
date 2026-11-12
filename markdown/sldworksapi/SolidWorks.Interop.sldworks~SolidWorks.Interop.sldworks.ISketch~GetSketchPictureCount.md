---
title: "GetSketchPictureCount Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSketchPictureCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPictureCount.html"
---

# GetSketchPictureCount Method (ISketch)

Gets the number of pictures on this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchPictureCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Integer

value = instance.GetSketchPictureCount()
```

### C#

```csharp
System.int GetSketchPictureCount()
```

### C++/CLI

```cpp
System.int GetSketchPictureCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of pictures on this sketch

## VBA Syntax

See [Sketch::GetSketchPictureCount](ms-its:sldworksapivb6.chm::/Sldworks~Sketch~GetSketchPictureCount.html).

## Remarks

Call this method before calling [ISketch::IGetSketchPcitures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetSketchPictures.html) to get the size of the array for that method.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchPictures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPictures.html)
[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
