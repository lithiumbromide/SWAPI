---
title: "GetZAxisEntitiesTypes Method (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "GetZAxisEntitiesTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetZAxisEntitiesTypes.html"
---

# GetZAxisEntitiesTypes Method (ICoordinateSystemFeatureData)

Gets the z-axis type of entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetZAxisEntitiesTypes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim value As System.Object

value = instance.GetZAxisEntitiesTypes()
```

### C#

```csharp
System.object GetZAxisEntitiesTypes()
```

### C++/CLI

```cpp
System.Object^ GetZAxisEntitiesTypes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of longs or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) representing the z-axis type of entities as defined by [swSelectType_e](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoordinateSystemFeatureData~GetXAxisEntitiesTypes.html)

## VBA Syntax

See [CoordinateSystemFeatureData::GetZAxisEntitiesTypes](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemFeatureData~GetZAxisEntitiesTypes.html).

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::GetZAxisEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetZAxisEntitiesCount.html)
[ICoordinateSystemFeatureData::IGetZAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetZAxisEntities.html)
[ICoordinateSystemFeatureData::IGetZAxisEntitiesTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetZAxisEntitiesTypes.html)
[ICoordinateSystemFeatureData::ISetZAxisEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetZAxisEntities.html)
[ICoordinateSystemFeatureData::ZAxisEntities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ZAxisEntities.html)
[ICoordinateSystemFeatureData::ZFlipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ZFlipped.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
