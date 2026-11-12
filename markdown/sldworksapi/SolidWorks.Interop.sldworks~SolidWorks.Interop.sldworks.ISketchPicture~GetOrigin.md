---
title: "GetOrigin Method (ISketchPicture)"
project: "SOLIDWORKS API Help"
interface: "ISketchPicture"
member: "GetOrigin"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetOrigin.html"
---

# GetOrigin Method (ISketchPicture)

Gets the origin of the picture on the sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetOrigin( _
   ByRef X As System.Double, _
   ByRef Y As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPicture
Dim X As System.Double
Dim Y As System.Double

instance.GetOrigin(X, Y)
```

### C#

```csharp
void GetOrigin(
   out System.double X,
   out System.double Y
)
```

### C++/CLI

```cpp
void GetOrigin(
   [Out] System.double X,
   [Out] System.double Y
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x coordinate
- `Y`: y coordinate

## VBA Syntax

See [SketchPicture::GetOrigin](ms-its:sldworksapivb6.chm::/Sldworks~SketchPicture~GetOrigin.html).

## Remarks

The coordinates in meters indicate the position of the lower-left corner of the picture in sketch space.

## See Also

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html)
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.html)
[ISketchPicture::SetOrigin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~SetOrigin.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
