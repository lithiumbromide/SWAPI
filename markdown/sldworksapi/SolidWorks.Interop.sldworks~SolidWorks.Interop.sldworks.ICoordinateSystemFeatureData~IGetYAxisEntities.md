---
title: "IGetYAxisEntities Method (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "IGetYAxisEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetYAxisEntities.html"
---

# IGetYAxisEntities Method (ICoordinateSystemFeatureData)

Gets the entities for the y axis of this coordinate system feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetYAxisEntities( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetYAxisEntities(Count)
```

### C#

```csharp
System.object IGetYAxisEntities(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetYAxisEntities(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of entities for the y axis

### Return Value

- in-process, unmanaged C++: Pointer to an an array of entities for the y axis

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ICoordinateSystemFeatureData::GetYAxisEntitiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoordinateSystemFeatureData~GetYAxisEntitiesCount.html) before calling this method to get Count.

See SOLIDWORKS Help for a list of valid entities.

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::ICoordinateSystemFeatureData::ISetYAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetYAxisEntities.html)
[ICoordinateSystemFeatureData::ICoordinateSystemFeatureData::YAxisEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~YAxisEntities.html)
[ICoordinateSystemFeatureData::ICoordinateSystemFeatureData::YFlipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~YFlipped.html)
[ICoordinateSystemFeatureData::GetYAxisEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetYAxisEntitiesCount.html)
[ICoordinateSystemFeatureData::GetYAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetYAxisEntitiesTypes.html)
[ICoordinateSystemFeatureData::IGetYAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetYAxisEntitiesTypes.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
