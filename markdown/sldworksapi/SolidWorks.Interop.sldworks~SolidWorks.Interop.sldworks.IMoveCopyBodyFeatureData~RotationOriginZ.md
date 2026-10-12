---
title: "RotationOriginZ Property (IMoveCopyBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveCopyBodyFeatureData"
member: "RotationOriginZ"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~RotationOriginZ.html"
---

# RotationOriginZ Property (IMoveCopyBodyFeatureData)

Gets or sets the z coordinate for the origin about which to rotate the selected bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotationOriginZ As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Double

instance.RotationOriginZ = value

value = instance.RotationOriginZ
```

### C#

```csharp
System.double RotationOriginZ {get; set;}
```

### C++/CLI

```cpp
property System.double RotationOriginZ {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

z coordinate

## VBA Syntax

See [MoveCopyBodyFeatureData::RotationOriginZ](ms-its:sldworksapivb6.chm::/sldworks~MoveCopyBodyFeatureData~RotationOriginZ.html).

## Remarks

[IMoveCopyBodyFeatureData::TransformReferenceEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~TransformReferenceEntity.html) must be NULL.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html)
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.html)
[IMoveCopyBodyFeatureData::RotationOriginX Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~RotationOriginX.html)
[IMoveCopyBodyFeatureData::RotationOriginY Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~RotationOriginY.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
