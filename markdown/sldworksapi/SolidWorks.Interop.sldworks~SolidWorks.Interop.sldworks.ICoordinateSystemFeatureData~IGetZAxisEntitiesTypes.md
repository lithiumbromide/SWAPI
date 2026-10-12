---
title: "IGetZAxisEntitiesTypes Method (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "IGetZAxisEntitiesTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetZAxisEntitiesTypes.html"
---

# IGetZAxisEntitiesTypes Method (ICoordinateSystemFeatureData)

Gets the z-axis type of entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetZAxisEntitiesTypes() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim value As System.Integer

value = instance.IGetZAxisEntitiesTypes()
```

### C#

```csharp
System.int IGetZAxisEntitiesTypes()
```

### C++/CLI

```cpp
System.int IGetZAxisEntitiesTypes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of longs representing the z-axis type of entities as defined by [swSelectType_e](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoordinateSystemFeatureData~GetXAxisEntitiesTypes.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [CoordinateSystemFeatureData::IGetZAxisEntitiesTypes](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemFeatureData~IGetZAxisEntitiesTypes.html).

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::GetZAxisEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetZAxisEntitiesCount.html)
[ICoordinateSystemFeatureData::GetZAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetZAxisEntitiesTypes.html)
[ICoordinateSystemFeatureData::IGetZAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetZAxisEntities.html)
[ICoordinateSystemFeatureData::ISetZAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetZAxisEntities.html)
[ICoordinateSystemFeatureData::ZAxisEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ZAxisEntities.html)
[ICoordinateSystemFeatureData::ZFlipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ZFlipped.html)

## Availability

SOLIDWORKS 2009 FCS, revision Number 17.0
