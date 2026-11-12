---
title: "GetZAxisEntitiesCount Method (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "GetZAxisEntitiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetZAxisEntitiesCount.html"
---

# GetZAxisEntitiesCount Method (ICoordinateSystemFeatureData)

Gets the number of entities for the z axis for this coordinate system feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetZAxisEntitiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim value As System.Integer

value = instance.GetZAxisEntitiesCount()
```

### C#

```csharp
System.int GetZAxisEntitiesCount()
```

### C++/CLI

```cpp
System.int GetZAxisEntitiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of entities for the z axis

## VBA Syntax

See [CoordinateSystemFeatureData::GetZAxisEntitiesCount](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemFeatureData~GetZAxisEntitiesCount.html).

## Examples

[Create Coordinate System Feature (VBA)](Create_Coordinate_System_Feature_Example_VB.htm)

## Remarks

Call this method before calling [ICoordinateSystemFeatureData::IGetZAxisEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoordinateSystemFeatureData~IGetZAxisEntities.html) to determine the size of the array for that method.

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::ISetZAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetZAxisEntities.html)
[ICoordinateSystemFeatureData::ZAxisEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ZAxisEntities.html)
[ICoordinateSystemFeatureData::ZFlipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ZFlipped.html)
[ICoordinateSystemFeatureData::GetZAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetZAxisEntitiesTypes.html)
[ICoordinateSystemFeatureData::IGetZAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetZAxisEntities.html)
[ICoordinateSystemFeatureData::IGetZAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetZAxisEntitiesTypes.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
