---
title: "ReliefDepth Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "ReliefDepth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReliefDepth.html"
---

# ReliefDepth Property (IBaseFlangeFeatureData)

Gets the bend relief depth for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReliefDepth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Double

value = instance.ReliefDepth
```

### C#

```csharp
System.double ReliefDepth {get;}
```

### C++/CLI

```cpp
property System.double ReliefDepth {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Bend relief depth

## VBA Syntax

See [BaseFlangeFeatureData::ReliefDepth](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~ReliefDepth.html).

## Examples

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html) examples.

## Remarks

This property is valid when:

- [IBaseFlangeFeatureData::UseReliefRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseReliefRatio.html) returns false,

- and -

- [IBaseFlangeFeatureData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReliefType.html) is [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefRectangular or swSheetMetalReliefTypes_e.swSheetMetalReliefObround.

The relief depth is set during the [initialization](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.html) of this base flange and cannot be changed.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
