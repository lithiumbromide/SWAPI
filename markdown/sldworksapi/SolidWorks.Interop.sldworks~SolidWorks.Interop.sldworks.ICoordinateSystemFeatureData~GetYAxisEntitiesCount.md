---
title: "GetYAxisEntitiesCount Method (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "GetYAxisEntitiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetYAxisEntitiesCount.html"
---

# GetYAxisEntitiesCount Method (ICoordinateSystemFeatureData)

Gets the number of entities for the y axis of this coordinate system feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetYAxisEntitiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim value As System.Integer

value = instance.GetYAxisEntitiesCount()
```

### C#

```csharp
System.int GetYAxisEntitiesCount()
```

### C++/CLI

```cpp
System.int GetYAxisEntitiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of entities for the y axis

## VBA Syntax

See [CoordinateSystemFeatureData::GetYAxisEntitiesCount](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemFeatureData~GetYAxisEntitiesCount.html).

## Examples

[Create Coordinate System Feature (VBA)](Create_Coordinate_System_Feature_Example_VB.htm)

## Remarks

Call this method before calling [ICoordinateSystemFeatureData::IGetYAxisEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoordinateSystemFeatureData~IGetYAxisEntities.html) to determine the size of the array for that method.

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::ISetYAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetYAxisEntities.html)
[ICoordinateSystemFeatureData::YAxisEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~YAxisEntities.html)
[ICoordinateSystemFeatureData::YFlipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~YFlipped.html)
[ICoordinateSystemFeatureData::IGetYAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetYAxisEntitiesTypes.html)
[ICoordinateSystemFeatureData::GetYAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetYAxisEntitiesTypes.html)
[ICoordinateSystemFeatureData::IGetYAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetYAxisEntities.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
