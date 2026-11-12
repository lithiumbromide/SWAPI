---
title: "GetXAxisEntitiesCount Method (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "GetXAxisEntitiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetXAxisEntitiesCount.html"
---

# GetXAxisEntitiesCount Method (ICoordinateSystemFeatureData)

Gets the number of entities for the x axis of this coordinate system feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetXAxisEntitiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim value As System.Integer

value = instance.GetXAxisEntitiesCount()
```

### C#

```csharp
System.int GetXAxisEntitiesCount()
```

### C++/CLI

```cpp
System.int GetXAxisEntitiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of entities for the x axis

## VBA Syntax

See [CoordinateSystemFeatureData::GetXAxisEntitiesCount](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemFeatureData~GetXAxisEntitiesCount.html).

## Examples

[Create Coordinate System Feature (VBA)](Create_Coordinate_System_Feature_Example_VB.htm)
[Insert Coordinate System Feature at Center of Mass (VBA)](Insert_Coordinate_System_Feature_at_Center_of_Mass_Example_VB.htm)

## Remarks

Call this method before calling [ICoordinateSystemFeatureData::IGetXAxisEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoordinateSystemFeatureData~IGetXAxisEntities.html) to determine the size of the array for that method.

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::ISetXAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetXAxisEntities.html)
[ICoordinateSystemFeatureData::XAxisEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~XAxisEntities.html)
[ICoordinateSystemFeatureData::XFlipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~XFlipped.html)
[ICoordinateSystemFeatureData::GetXAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetXAxisEntitiesTypes.html)
[ICoordinateSystemFeatureData::IGetXAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetXAxisEntitiesTypes.html)
[ICoordinateSystemFeatureData::IGetXAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetXAxisEntities.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
