---
title: "GetHoleTopMateEntity Method (IHoleSeriesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData"
member: "GetHoleTopMateEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetHoleTopMateEntity.html"
---

# GetHoleTopMateEntity Method (IHoleSeriesFeatureData)

Obsolete. Superseded by [IHoleSeriesFeatureData2::GetHoleTopMateEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~GetHoleTopMateEntity.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHoleTopMateEntity( _
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

value = instance.GetHoleTopMateEntity(HoleInstance, HoleType)
```

### C#

```csharp
System.object GetHoleTopMateEntity(
   System.int HoleInstance,
   System.short HoleType
)
```

### C++/CLI

```cpp
System.Object^ GetHoleTopMateEntity(
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

## VBA Syntax

See [HoleSeriesFeatureData::GetHoleTopMateEntity](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData~GetHoleTopMateEntity.html).

## See Also

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.html)
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.html)
[IHoleSeriesFeatureData::IGetHoleTopMateEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~IGetHoleTopMateEntity.html)
[IHoleSeriesFeatureData::GetHoleBottomMateEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetHoleBottomMateEntity.html)
[IHoleSeriesFeatureData::IGetHoleBottomMateEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~IGetHoleBottomMateEntity.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
