---
title: "IGetZAxisEntities Method (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "IGetZAxisEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetZAxisEntities.html"
---

# IGetZAxisEntities Method (ICoordinateSystemFeatureData)

Gets the entities for the z axis for this coordinate system feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetZAxisEntities( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetZAxisEntities(Count)
```

### C#

```csharp
System.object IGetZAxisEntities(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetZAxisEntities(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of entities for the z axis

### Return Value

- in-process, unmanaged C++: Pointer to an an array of entities for the z axis

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ICoordinateSystemFeatureData::GetZAxisEntitiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoordinateSystemFeatureData~GetZAxisEntitiesCount.html) before calling this method to get Count.

See SOLIDWORKS Help for a list of valid entities.

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::ISetXAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetXAxisEntities.html)
[ICoordinateSystemFeatureData::ZAxisEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ZAxisEntities.html)
[ICoordinateSystemFeatureData::ZFlipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ZFlipped.html)
[ICoordinateSystemFeatureData::GetZAxisEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetZAxisEntitiesCount.html)
[ICoordinateSystemFeatureData::GetZAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetZAxisEntitiesTypes.html)
[ICoordinateSystemFeatureData::IGetZAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetZAxisEntitiesTypes.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
