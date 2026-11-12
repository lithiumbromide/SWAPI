---
title: "IGetHoleTopMateEntity Method (IHoleSeriesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData"
member: "IGetHoleTopMateEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~IGetHoleTopMateEntity.html"
---

# IGetHoleTopMateEntity Method (IHoleSeriesFeatureData)

Obsolete. Superseded by [IHoleSeriesFeatureData2::IGetHoleTopMateEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~IGetHoleTopMateEntity.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetHoleTopMateEntity( _
   ByVal HoleInstance As System.Integer, _
   ByVal HoleType As System.Short _
) As Entity
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData
Dim HoleInstance As System.Integer
Dim HoleType As System.Short
Dim value As Entity

value = instance.IGetHoleTopMateEntity(HoleInstance, HoleType)
```

### C#

```csharp
Entity IGetHoleTopMateEntity(
   System.int HoleInstance,
   System.short HoleType
)
```

### C++/CLI

```cpp
Entity^ IGetHoleTopMateEntity(
   System.int HoleInstance,
   System.short HoleType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `HoleInstance`: Index number of the hole whose entity you want
- `HoleType`: Type of hole as defined by [swWzdHoleTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleTypes_e.html)

### Return Value

[Entity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) to which the top of the hole is mated

## See Also

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.html)
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.html)
[IHoleSeriesFeatureData::GetHoleTopMateEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetHoleTopMateEntity.html)
[IHoleSeriesFeatureData::GetHoleBottomMateEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetHoleBottomMateEntity.html)
[IHoleSeriesFeatureData::IGetHoleBottomMateEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~IGetHoleBottomMateEntity.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
