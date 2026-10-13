---
title: "GetSketchPictures Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSketchPictures"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPictures.html"
---

# GetSketchPictures Method (ISketch)

Gets the pictures on this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchPictures() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Object

value = instance.GetSketchPictures()
```

### C#

```csharp
System.object GetSketchPictures()
```

### C++/CLI

```cpp
System.Object^ GetSketchPictures();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [pictures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPicture.html) on this sketch

## VBA Syntax

See [Sketch::GetSketchPictures](ms-its:sldworksapivb6.chm::/Sldworks~Sketch~GetSketchPictures.html).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchPictureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPictureCount.html)
[ISketch::IGetSketchPictures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchPictures.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
