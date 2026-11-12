---
title: "YAxisEntities Property (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "YAxisEntities"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~YAxisEntities.html"
---

# YAxisEntities Property (ICoordinateSystemFeatureData)

Gets or sets the entities for the y axis of this coordinate system.

## Syntax

### Visual Basic (Declaration)

```vb
Property YAxisEntities As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim value As System.Object

instance.YAxisEntities = value

value = instance.YAxisEntities
```

### C#

```csharp
System.object YAxisEntities {get; set;}
```

### C++/CLI

```cpp
property System.Object^ YAxisEntities {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Entities for y axis

## VBA Syntax

See [CoordinateSystemFeatureData::YAxisEntities](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemFeatureData~YAxisEntities.html).

## Examples

[Create Coordinate System Feature (VBA)](Create_Coordinate_System_Feature_Example_VB.htm)

## Remarks

See SOLIDWORKS Help for a list of valid entities.

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::GetYAxisEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetYAxisEntitiesCount.html)
[ICoordinateSystemFeatureData::IGetYAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetYAxisEntities.html)
[ICoordinateSystemFeatureData::ISetYAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetYAxisEntities.html)
[ICoordinateSystemFeatureData::YFlipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~YFlipped.html)
[ICoordinateSystemFeatureData::GetYAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetYAxisEntitiesTypes.html)
[ICoordinateSystemFeatureData::IGetYAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetYAxisEntitiesTypes.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
