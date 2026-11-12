---
title: "IGetXAxisEntities Method (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "IGetXAxisEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetXAxisEntities.html"
---

# IGetXAxisEntities Method (ICoordinateSystemFeatureData)

Gets the entities for the x axis of this coordinate system feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetXAxisEntities( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetXAxisEntities(Count)
```

### C#

```csharp
System.object IGetXAxisEntities(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetXAxisEntities(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of entites for the x axis

### Return Value

- in-process, unmanaged C++: Pointer to an an array of entities for the x axis

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ICoordinateSystemFeatureData::GetXAxisEntitiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoordinateSystemFeatureData~GetXAxisEntitiesCount.html) before calling this method to get Count.

See SOLIDWORKS Help for a list of valid entities.

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::ISetXAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetXAxisEntities.html)
[ICoordinateSystemFeatureData::XAxisEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~XAxisEntities.html)
[ICoordinateSystemFeatureData::XFlipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~XFlipped.html)
[ICoordinateSystemFeatureData::GetXAxisEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetXAxisEntitiesCount.html)
[ICoordinateSystemFeatureData::GetXAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetXAxisEntitiesTypes.html)
[ICoordinateSystemFeatureData::IGetXAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetXAxisEntitiesTypes.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
