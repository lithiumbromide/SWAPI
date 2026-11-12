---
title: "Preload Property (IHoleSeriesFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData2"
member: "Preload"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~Preload.html"
---

# Preload Property (IHoleSeriesFeatureData2)

Gets the preload information for this hole series.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Preload As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData2
Dim value As System.String

value = instance.Preload
```

### C#

```csharp
System.string Preload {get;}
```

### C++/CLI

```cpp
property System.String^ Preload {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Preload information

## VBA Syntax

See [HoleSeriesFeatureData2::Preload](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData2~Preload.html).

## Examples

See the examples in [IHoleSeriesFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2.html).

## Remarks

The preload value is not available in the SOLIDWORKS Toolbox database.

## See Also

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.html)
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
