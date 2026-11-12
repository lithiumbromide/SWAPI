---
title: "Standard Property (IHoleSeriesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData"
member: "Standard"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~Standard.html"
---

# Standard Property (IHoleSeriesFeatureData)

Obsolete. Superseded by [IHoleSeriesFeatureData2::Standard](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~Standard.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Standard As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData
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

See [HoleSeriesFeatureData::Standard](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData~Standard.html).

## See Also

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.html)
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
