---
title: "Type Property (IHoleSeriesFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData2"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~Type.html"
---

# Type Property (IHoleSeriesFeatureData2)

Gets the type of fastener in the specified part in this hole series.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Type( _
   ByVal HoleSeriesWhichPart As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData2
Dim HoleSeriesWhichPart As System.Integer
Dim value As System.Integer

value = instance.Type(HoleSeriesWhichPart)
```

### C#

```csharp
System.int Type(
   System.int HoleSeriesWhichPart
) {get;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get(System.int HoleSeriesWhichPart);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `HoleSeriesWhichPart`: Which part the hole series passes through as defined by [swHoleSeriesWhichParts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHoleSeriesWhichParts_e.html)

### Property Value

Type of fastener as defined by [swWzdHoleStandardFastenerTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html)

## VBA Syntax

See [HoleSeriesFeatureData2::Type](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData2~Type.html).

## Examples

See the examples in [IHoleSeriesFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2.html).

## See Also

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.html)
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
