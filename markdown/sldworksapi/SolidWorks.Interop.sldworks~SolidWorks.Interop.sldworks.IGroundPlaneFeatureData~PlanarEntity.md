---
title: "PlanarEntity Property (IGroundPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGroundPlaneFeatureData"
member: "PlanarEntity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData~PlanarEntity.html"
---

# PlanarEntity Property (IGroundPlaneFeatureData)

Gets or sets the planar entity for this ground plane feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PlanarEntity As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGroundPlaneFeatureData
Dim value As System.Object

instance.PlanarEntity = value

value = instance.PlanarEntity
```

### C#

```csharp
System.object PlanarEntity {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PlanarEntity {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) or [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)

## VBA Syntax

See [GroundPlaneFeatureData::PlanarEntity](ms-its:sldworksapivb6.chm::/sldworks~GroundPlaneFeatureData~PlanarEntity.html).

## Examples

See the [IGroundPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData.html) example.

## See Also

[IGroundPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData.html)
[IGroundPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
