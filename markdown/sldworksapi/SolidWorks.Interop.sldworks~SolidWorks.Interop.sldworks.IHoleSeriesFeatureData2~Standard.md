---
title: "Standard Property (IHoleSeriesFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData2"
member: "Standard"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~Standard.html"
---

# Standard Property (IHoleSeriesFeatureData2)

Gets the design standard for this hole series.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Standard As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData2
Dim value As System.Integer

value = instance.Standard
```

### C#

```csharp
System.int Standard {get;}
```

### C++/CLI

```cpp
property System.int Standard {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Design standard as defined in [swWzdHoleStandards_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandards_e.html)

## VBA Syntax

See [HoleSeriesFeatureData2::Standard](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData2~Standard.html).

## Examples

See the examples in [IHoleSeriesFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2.html).

## See Also

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.html)
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
