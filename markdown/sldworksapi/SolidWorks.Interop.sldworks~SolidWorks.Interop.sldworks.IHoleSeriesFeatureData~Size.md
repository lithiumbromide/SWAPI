---
title: "Size Property (IHoleSeriesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData"
member: "Size"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~Size.html"
---

# Size Property (IHoleSeriesFeatureData)

Obsolete. Superseded by [IHoleSeriesFeatureData2::Size](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~Size.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Size( _
   ByVal HoleSeriesWhichPart As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData
Dim HoleSeriesWhichPart As System.Integer
Dim value As System.String

value = instance.Size(HoleSeriesWhichPart)
```

### C#

```csharp
System.string Size(
   System.int HoleSeriesWhichPart
) {get;}
```

### C++/CLI

```cpp
property System.String^ Size {
   System.String^ get(System.int HoleSeriesWhichPart);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `HoleSeriesWhichPart`: Which part the hole series passes through as defined by [swHoleSeriesWhichParts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHoleSeriesWhichParts_e.html)

### Property Value

Fastener size

## VBA Syntax

See [HoleSeriesFeatureData::Size](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData~Size.html).

## See Also

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.html)
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.html)
[IHoleSeriesFeatureData::FastenerBottomHoleType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~FastenerBottomHoleType.html)
[IHoleSeriesFeatureData::FastenerDefaultUnits Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~FastenerDefaultUnits.html)
[IHoleSeriesFeatureData::FastenerHoleCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~FastenerHoleCount.html)
[IHoleSeriesFeatureData::FastenerTopHoleType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~FastenerTopHoleType.html)
[IHoleSeriesFeatureData::Type Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~Type.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
