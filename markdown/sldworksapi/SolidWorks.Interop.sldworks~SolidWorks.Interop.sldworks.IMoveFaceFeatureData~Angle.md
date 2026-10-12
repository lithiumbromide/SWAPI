---
title: "Angle Property (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~Angle.html"
---

# Angle Property (IMoveFaceFeatureData)

Gets or sets the angle for the Move Face feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
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

Angle in radians at which to draft the faces

## VBA Syntax

See [MoveFaceFeatureData::Angle](ms-its:sldworksapivb6.chm::/sldworks~MoveFaceFeatureData~Angle.html).

## Examples

[Rotate Move Face Feature (VB.NET)](Rotate_Move_Face_Feature_Example_VBNET.htm)
[Rotate Move Face Feature (VBA)](Rotate_MoveFace_Feature_Example_VB.htm)
[Rotate Move Face Feature (C#)](Rotate_Move_Face_Feature_Example_CSharp.htm)

## Remarks

The property is valid only if [IMoveFaceFeatureData::MoveType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~MoveType.html) is [swMoveFaceType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveFaceType_e.html).swMoveFaceTypeRotate.

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
