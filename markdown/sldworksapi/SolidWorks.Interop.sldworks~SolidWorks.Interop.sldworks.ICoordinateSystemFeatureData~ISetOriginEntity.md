---
title: "ISetOriginEntity Method (ICoordinateSystemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemFeatureData"
member: "ISetOriginEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetOriginEntity.html"
---

# ISetOriginEntity Method (ICoordinateSystemFeatureData)

Sets the entity for the origin of this coordinate feature data.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetOriginEntity( _
   ByVal Ent As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemFeatureData
Dim Ent As System.Object

instance.ISetOriginEntity(Ent)
```

### C#

```csharp
void ISetOriginEntity(
   System.object Ent
)
```

### C++/CLI

```cpp
void ISetOriginEntity(
   System.Object^ Ent
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ent`: Entity for origin

## VBA Syntax

See [CoordinateSystemFeatureData::ISetOriginEntity](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemFeatureData~ISetOriginEntity.html).

## Remarks

See SOLIDWORKS Help for a list of valid entities.

## See Also

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html)
[ICoordinateSystemFeatureData::IGetOriginEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetOriginEntity.html)
[ICoordinateSystemFeatureData::OriginEntity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~OriginEntity.html)
[ICoordinateSystemFeatureData::GetOriginEntityType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetOriginEntityType.html)
[ICoordinateSystemFeatureData::IGetOriginEntityType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetOriginEntityType.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
