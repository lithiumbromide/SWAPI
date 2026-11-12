---
title: "ReliefRatio Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "ReliefRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReliefRatio.html"
---

# ReliefRatio Property (IBaseFlangeFeatureData)

Gets the bend relief ratio for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReliefRatio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Double

value = instance.ReliefRatio
```

### C#

```csharp
System.double ReliefRatio {get;}
```

### C++/CLI

```cpp
property System.double ReliefRatio {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Ratio of bend relief width to bend relief depth

## VBA Syntax

See [BaseFlangeFeatureData::ReliefRatio](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~ReliefRatio.html).

## Examples

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html) examples.

## Remarks

This property is valid when:

- [IBaseFlangeFeatureData::UseReliefRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseReliefRatio.html) returns true,

- and -

- [IBaseFlangeFeatureData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReliefType.html) is [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefRectangular or swSheetMetalReliefTypes_e.swSheetMetalReliefObround.

The relief ratio is set during the [initialization](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.html) of this base flange and cannot be changed.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
