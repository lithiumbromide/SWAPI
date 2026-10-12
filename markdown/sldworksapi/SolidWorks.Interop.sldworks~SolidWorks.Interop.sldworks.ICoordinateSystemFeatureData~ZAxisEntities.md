---
title: "ZAxisEntities Property (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "ZAxisEntities"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ZAxisEntities.html"
---

# ZAxisEntities Property (ICoordinateSystemFeatureData)

Gets or sets the entities for the z axis of this coordinate system feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ZAxisEntities As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim value As System.Object

instance.ZAxisEntities = value

value = instance.ZAxisEntities
```

### C#

```csharp
System.object ZAxisEntities {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ZAxisEntities {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Entities for the z axis

## VBA Syntax

See [CoordinateSystemFeatureData::ZAxisEntities](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemFeatureData~ZAxisEntities.html).

## Examples

[Create Coordinate System Feature (VBA)](Create_Coordinate_System_Feature_Example_VB.htm)

## Remarks

See SOLIDWORKS Help for a list of valid entities.

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::GetZAxisEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetZAxisEntitiesCount.html)
[ICoordinateSystemFeatureData::IGetZAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetZAxisEntities.html)
[ICoordinateSystemFeatureData::ISetZAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetZAxisEntities.html)
[ICoordinateSystemFeatureData::ZFlipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ZFlipped.html)
[ICoordinateSystemFeatureData::GetZAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetZAxisEntitiesTypes.html)
[ICoordinateSystemFeatureData::IGetZAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetZAxisEntitiesTypes.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
