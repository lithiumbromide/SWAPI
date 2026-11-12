---
title: "GetSize Method (ISketchPicture)"
project: "SOLIDWORKS API Help"
interface: "ISketchPicture"
member: "GetSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetSize.html"
---

# GetSize Method (ISketchPicture)

Gets the size of the picture on the sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetSize( _
   ByRef Width As System.Double, _
   ByRef Height As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPicture
Dim Width As System.Double
Dim Height As System.Double

instance.GetSize(Width, Height)
```

### C#

```csharp
void GetSize(
   out System.double Width,
   out System.double Height
)
```

### C++/CLI

```cpp
void GetSize(
   [Out] System.double Width,
   [Out] System.double Height
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Width`: Width of the picture in meters
- `Height`: Height of the picture in meters

## VBA Syntax

See [SketchPicture::GetSize](ms-its:sldworksapivb6.chm::/Sldworks~SketchPicture~GetSize.html).

## Examples

See the [ISketchPicture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html) examples.

## See Also

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html)
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.html)
[ISketchPicture::SetSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~SetSize.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
