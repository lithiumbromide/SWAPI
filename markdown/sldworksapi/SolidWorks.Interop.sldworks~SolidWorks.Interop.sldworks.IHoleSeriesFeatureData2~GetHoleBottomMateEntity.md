---
title: "GetHoleBottomMateEntity Method (IHoleSeriesFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData2"
member: "GetHoleBottomMateEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~GetHoleBottomMateEntity.html"
---

# GetHoleBottomMateEntity Method (IHoleSeriesFeatureData2)

Gets the entity to which the bottom of the hole is mated in this hole series.

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
Dim instance As IHoleSeriesFeatureData2
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

See [HoleSeriesFeatureData2::GetHoleBottomMateEntity](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData2~GetHoleBottomMateEntity.html).

## See Also

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.html)
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.html)
[IHoleSeriesFeatureData2::IGetHoleBottomMateEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~IGetHoleBottomMateEntity.html)
[IHoleSeriesFeatureData2::GetHoleTopMateEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~GetHoleTopMateEntity.html)
[IHoleSeriesFeatureData2::IGetHoleTopMateEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~IGetHoleTopMateEntity.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
