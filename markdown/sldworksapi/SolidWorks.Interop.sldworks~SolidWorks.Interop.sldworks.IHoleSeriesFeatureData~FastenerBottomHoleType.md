---
title: "FastenerBottomHoleType Property (IHoleSeriesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData"
member: "FastenerBottomHoleType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~FastenerBottomHoleType.html"
---

# FastenerBottomHoleType Property (IHoleSeriesFeatureData)

Obsolete. Superseded by [IHoleSeriesFeatureData2::FastenerBottomHoleType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~FastenerBottomHoleType.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FastenerBottomHoleType As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData
Dim value As System.Short

value = instance.FastenerBottomHoleType
```

### C#

```csharp
System.short FastenerBottomHoleType {get;}
```

### C++/CLI

```cpp
property System.short FastenerBottomHoleType {
   System.short get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fastener bottom hole type as defined in [swWzdHoleStandardFastenerTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html)

## VBA Syntax

See [HoleSeriesFeatureData::FastenerBottomHoleType](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData~FastenerBottomHoleType.html).

## See Also

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.html)
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.html)
[IHoleSeriesFeatureData::FastenerDefaultUnits Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~FastenerDefaultUnits.html)
[IHoleSeriesFeatureData::FastenerHoleCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~FastenerHoleCount.html)
[IHoleSeriesFeatureData::FastenerTopHoleType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~FastenerTopHoleType.html)
[IHoleSeriesFeatureData::Size Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~Size.html)
[IHoleSeriesFeatureData::Type Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~Type.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
