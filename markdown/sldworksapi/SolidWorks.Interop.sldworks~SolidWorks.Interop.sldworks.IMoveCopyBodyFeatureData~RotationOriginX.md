---
title: "RotationOriginX Property (IMoveCopyBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveCopyBodyFeatureData"
member: "RotationOriginX"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~RotationOriginX.html"
---

# RotationOriginX Property (IMoveCopyBodyFeatureData)

Gets or sets the x coordinate for the origin about which to rotate the selected bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotationOriginX As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Double

instance.RotationOriginX = value

value = instance.RotationOriginX
```

### C#

```csharp
System.double RotationOriginX {get; set;}
```

### C++/CLI

```cpp
property System.double RotationOriginX {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

x coordinate

## VBA Syntax

See [MoveCopyBodyFeatureData::RotationOriginX](ms-its:sldworksapivb6.chm::/sldworks~MoveCopyBodyFeatureData~RotationOriginX.html).

## Remarks

[IMoveCopyBodyFeatureData::TransformReferenceEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~TransformReferenceEntity.html) must be NULL.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html)
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.html)
[IMoveCopyBodyFeatureData::RotationOriginY Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~RotationOriginY.html)
[IMoveCopyBodyFeatureData::RotationOriginZ Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~RotationOriginZ.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
