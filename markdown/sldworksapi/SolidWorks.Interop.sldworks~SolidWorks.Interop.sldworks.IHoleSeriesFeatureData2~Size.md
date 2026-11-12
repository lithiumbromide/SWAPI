---
title: "Size Property (IHoleSeriesFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData2"
member: "Size"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~Size.html"
---

# Size Property (IHoleSeriesFeatureData2)

Gets the fastener size in the specified part in this hole series.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Size( _
   ByVal HoleSeriesWhichPart As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData2
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

See [HoleSeriesFeatureData2::Size](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData2~Size.html).

## Examples

See the examples in [IHoleSeriesFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2.html).

## See Also

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.html)
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
