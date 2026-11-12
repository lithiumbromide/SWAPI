---
title: "Angle Property (ISketchPicture)"
project: "SOLIDWORKS API Help"
interface: "ISketchPicture"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~Angle.html"
---

# Angle Property (ISketchPicture)

Gets or sets the rotation angle of the picture in the sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPicture
Dim value As System.Double

instance.Angle = value

value = instance.Angle
```

### C#

```csharp
System.double Angle {get; set;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Rotation angle in radians of the picture; counter-clockwise from the positive X

## VBA Syntax

See [SketchPicture::Angle](ms-its:sldworksapivb6.chm::/Sldworks~SketchPicture~Angle.html).

## Examples

See the [ISketchPicture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html) examples.

## See Also

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.html)
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
