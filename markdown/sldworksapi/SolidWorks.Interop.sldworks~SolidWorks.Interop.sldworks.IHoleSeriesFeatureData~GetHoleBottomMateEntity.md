---
title: "GetHoleBottomMateEntity Method (IHoleSeriesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData"
member: "GetHoleBottomMateEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetHoleBottomMateEntity.html"
---

# GetHoleBottomMateEntity Method (IHoleSeriesFeatureData)

Obsolete. Superseded by [IHoleSeriesFeatureData2::GetHoleBottomMateEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~GetHoleBottomMateEntity.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHoleBottomMateEntity( _
   ByVal HoleInstance As System.Integer, _
   ByVal HoleType As System.Short _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData
Dim HoleInstance As System.Integer
Dim HoleType As System.Short
Dim value As System.Object

value = instance.GetHoleBottomMateEntity(HoleInstance, HoleType)
```

### C#

```csharp
System.object GetHoleBottomMateEntity(
   System.int HoleInstance,
   System.short HoleType
)
```

### C++/CLI

```cpp
System.Object^ GetHoleBottomMateEntity(
   System.int HoleInstance,
   System.short HoleType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `HoleInstance`: Index number of the hole whose entity you want
- `HoleType`: Type of hole as defined by [swWzdHoleTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleTypes_e.html)

### Return Value

[Entity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) to which the bottom of the hole is mated

## VBA Syntax

See [HoleSeriesFeatureData::GetHoleBottomMateEntity](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData~GetHoleBottomMateEntity.html).

## See Also

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.html)
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.html)
[IHoleSeriesFeatureData::IGetHoleTopMateEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~IGetHoleTopMateEntity.html)
[IHoleSeriesFeatureData::GetHoleTopMateEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetHoleTopMateEntity.html)
[IHoleSeriesFeatureData::IGetHoleTopMateEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~IGetHoleTopMateEntity.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
