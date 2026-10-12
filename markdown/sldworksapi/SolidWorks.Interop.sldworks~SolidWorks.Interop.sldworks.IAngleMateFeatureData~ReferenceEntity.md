---
title: "ReferenceEntity Property (IAngleMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IAngleMateFeatureData"
member: "ReferenceEntity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData~ReferenceEntity.html"
---

# ReferenceEntity Property (IAngleMateFeatureData)

Gets or sets the direction reference entity for this angle mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferenceEntity As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAngleMateFeatureData
Dim value As System.Object

instance.ReferenceEntity = value

value = instance.ReferenceEntity
```

### C#

```csharp
System.object ReferenceEntity {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ReferenceEntity {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html), planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), or reference [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.html)

## VBA Syntax

See [AngleMateFeatureData::ReferenceEntity](ms-its:sldworksapivb6.chm::/sldworks~AngleMateFeatureData~ReferenceEntity.html).

## See Also

[IAngleMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.html)
[IAngleMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
