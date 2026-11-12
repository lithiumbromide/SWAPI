---
title: "OriginEntity Property (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "OriginEntity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~OriginEntity.html"
---

# OriginEntity Property (ICoordinateSystemFeatureData)

Gets or sets the entity for the origin of this coordinate system feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OriginEntity As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim value As System.Object

instance.OriginEntity = value

value = instance.OriginEntity
```

### C#

```csharp
System.object OriginEntity {get; set;}
```

### C++/CLI

```cpp
property System.Object^ OriginEntity {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Entity for the origin

## VBA Syntax

See [CoordinateSystemFeatureData::OriginEntity](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemFeatureData~OriginEntity.html).

## Examples

[Create Coordinate System Feature (VBA)](Create_Coordinate_System_Feature_Example_VB.htm)
[Insert Coordinate System Feature at Center of Mass (VBA)](Insert_Coordinate_System_Feature_at_Center_of_Mass_Example_VB.htm)

## Remarks

See SOLIDWORKS Help for a list of valid entities.

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::IGetOriginEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetOriginEntity.html)
[ICoordinateSystemFeatureData::ISetOriginEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetOriginEntity.html)
[ICoordinateSystemFeatureData::GetOriginEntityType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetOriginEntityType.html)
[ICoordinateSystemFeatureData::IGetOriginEntityType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetOriginEntityType.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
