---
title: "IGetOriginEntity Method (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "IGetOriginEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetOriginEntity.html"
---

# IGetOriginEntity Method (ICoordinateSystemFeatureData)

Gets the entity for the origin of this coordinate system feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetOriginEntity() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim value As System.Object

value = instance.IGetOriginEntity()
```

### C#

```csharp
System.object IGetOriginEntity()
```

### C++/CLI

```cpp
System.Object^ IGetOriginEntity();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Entity

## VBA Syntax

See [CoordinateSystemFeatureData::IGetOriginEntity](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemFeatureData~IGetOriginEntity.html).

## Remarks

See SOLIDWORKS Help for a list of valid entities.

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::ISetOriginEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetOriginEntity.html)
[ICoordinateSystemFeatureData::OriginEntity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~OriginEntity.html)
[ICoordinateSystemFeatureData::GetOriginEntityType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetOriginEntityType.html)
[ICoordinateSystemFeatureData::IGetOriginEntityType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetOriginEntityType.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
