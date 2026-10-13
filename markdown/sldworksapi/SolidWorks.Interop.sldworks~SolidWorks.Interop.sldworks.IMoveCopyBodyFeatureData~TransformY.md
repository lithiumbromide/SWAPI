---
title: "TransformY Property (IMoveCopyBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveCopyBodyFeatureData"
member: "TransformY"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformY.html"
---

# TransformY Property (IMoveCopyBodyFeatureData)

Gets or sets the y coordinate for either moving or rotating the selected bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Property TransformY As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Double

instance.TransformY = value

value = instance.TransformY
```

### C#

```csharp
System.double TransformY {get; set;}
```

### C++/CLI

```cpp
property System.double TransformY {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Meters for moving or radians for rotating

## VBA Syntax

See [MoveCopyBodyFeatureData::TransformY](ms-its:sldworksapivb6.chm::/sldworks~MoveCopyBodyFeatureData~TransformY.html).

## Examples

[Move and Copy Body By Setting Transforms (VBA)](Move_and_Copy_Body_by_Setting_Transforms_Example_VB.htm)

## Remarks

Use [IMoveCopyBodyFeatureData::TransformType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~TransformType.html) to get or set the transform type before setting this property.

[IMoveCopyBodyFeatureData::TransformReferenceEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~TransformReferenceEntity.html) must be:

- NULL if moving the selected bodies
  - or -
- a vertex if rotating the selected bodies

## See Also

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html)
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.html)
[IMoeCopyBodyFeatureData::TransformX Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformX.html)
[IMoeCopyBodyFeatureData::TransformZ Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformZ.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
