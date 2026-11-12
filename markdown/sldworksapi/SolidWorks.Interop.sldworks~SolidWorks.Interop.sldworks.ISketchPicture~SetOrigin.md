---
title: "SetOrigin Method (ISketchPicture)"
project: "SOLIDWORKS API Help"
interface: "ISketchPicture"
member: "SetOrigin"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~SetOrigin.html"
---

# SetOrigin Method (ISketchPicture)

Sets the origin of the picture of the sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetOrigin( _
   ByVal X As System.Double, _
   ByVal Y As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPicture
Dim X As System.Double
Dim Y As System.Double
Dim value As System.Boolean

value = instance.SetOrigin(X, Y)
```

### C#

```csharp
System.bool SetOrigin(
   System.double X,
   System.double Y
)
```

### C++/CLI

```cpp
System.bool SetOrigin(
   System.double X,
   System.double Y
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x coordinate
- `Y`: y coordinate

### Return Value

True if the origin is set, false if not

## VBA Syntax

See [SketchPicture::SetOrigin](ms-its:sldworksapivb6.chm::/Sldworks~SketchPicture~SetOrigin.html).

## Remarks

The coordinates in meters indicate the position of the lower-left corner of the picture in sketch space.

## See Also

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html)
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.html)
[ISketchPicture::GetOrigin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetOrigin.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
