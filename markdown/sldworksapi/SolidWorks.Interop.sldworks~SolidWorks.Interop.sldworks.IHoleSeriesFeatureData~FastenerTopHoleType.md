---
title: "FastenerTopHoleType Property (IHoleSeriesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData"
member: "FastenerTopHoleType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~FastenerTopHoleType.html"
---

# FastenerTopHoleType Property (IHoleSeriesFeatureData)

Obsolete. Superseded by [IHoleSeriesFeatureData2::FastenerTopHoleType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~FastenerTopHoleType.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FastenerTopHoleType As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData
Dim value As System.Short

value = instance.FastenerTopHoleType
```

### C#

```csharp
System.short FastenerTopHoleType {get;}
```

### C++/CLI

```cpp
property System.short FastenerTopHoleType {
   System.short get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fastener top hole type as defined in [swWzdHoleStandardFastenerTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html)

## VBA Syntax

See [HoleSeriesFeatureData::FastenerTopHoleType](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData~FastenerTopHoleType.html).

## See Also

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.html)
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.html)
[IHoleSeriesFeatureData::FastenerBottomHoleType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~FastenerBottomHoleType.html)
[IHoleSeriesFeatureData::FastenerDefaultUnits Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~FastenerDefaultUnits.html)
[IHoleSeriesFeatureData::FastenerHoleCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~FastenerHoleCount.html)
[IHoleSeriesFeatureData::Size Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~Size.html)
[IHoleSeriesFeatureData::Type Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~Type.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
