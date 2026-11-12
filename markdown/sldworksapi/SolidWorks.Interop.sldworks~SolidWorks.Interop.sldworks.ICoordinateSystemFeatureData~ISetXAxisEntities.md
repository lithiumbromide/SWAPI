---
title: "ISetXAxisEntities Method (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "ISetXAxisEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetXAxisEntities.html"
---

# ISetXAxisEntities Method (ICoordinateSystemFeatureData)

Sets the entities for the x axis of this coordinate system feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetXAxisEntities( _
   ByVal Count As System.Integer, _
   ByRef EntArray As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim Count As System.Integer
Dim EntArray As System.Object

instance.ISetXAxisEntities(Count, EntArray)
```

### C#

```csharp
void ISetXAxisEntities(
   System.int Count,
   ref System.object EntArray
)
```

### C++/CLI

```cpp
void ISetXAxisEntities(
   System.int Count,
   System.Object^% EntArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of entities for the x axis
- `EntArray`: - in-process, unmanaged C++: Pointer to an an array of entities for the x axis

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See SOLIDWORKS Help for a list of valid entities.

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::GetXAxisEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetXAxisEntitiesCount.html)
[ICoordinateSystemFeatureData::IGetXAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetXAxisEntities.html)
[ICoordinateSystemFeatureData::XAxisEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~XAxisEntities.html)
[ICoordinateSystemFeatureData::XFlipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~XFlipped.html)
[ICoordinateSystemFeatureData::GetXAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetXAxisEntitiesTypes.html)
[ICoordinateSystemFeatureData::IGetXAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetXAxisEntitiesTypes.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
