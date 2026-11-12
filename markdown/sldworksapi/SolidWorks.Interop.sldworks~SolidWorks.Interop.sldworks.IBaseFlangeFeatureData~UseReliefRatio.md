---
title: "UseReliefRatio Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "UseReliefRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseReliefRatio.html"
---

# UseReliefRatio Property (IBaseFlangeFeatureData)

Gets whether the relief ratio is used in this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UseReliefRatio As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Boolean

value = instance.UseReliefRatio
```

### C#

```csharp
System.bool UseReliefRatio {get;}
```

### C++/CLI

```cpp
property System.bool UseReliefRatio {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True uses the relief ratio, false uses relief depth / relief width

## VBA Syntax

See [BaseFlangeFeatureData::UseReliefRatio](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~UseReliefRatio.html).

## Examples

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html) examples.

## Remarks

This property is valid when:

- [IBaseFlangeFeatureData::UseDefaultBendRelief](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseDefaultBendRelief.html) is false,

- and -

- [IBaseFlangeFeatureData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReliefType.html) is [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefRectangular or swSheetMetalReliefTypes_e.swSheetMetalReliefObround.

If this property is:

- True, then use [IBaseFlangeFeatureData::ReliefRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReliefRatio.html) to get the relief ratio used to [initialize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.html) this base flange.
- False, then use [IBaseFlangeFeatureData::ReliefWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReliefWidth.html) and [IBaseFlangeFeatureData::ReliefDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReliefDepth.html) to get the relief width and relief depth used to initialize this base flange.

Whether to use a relief ratio was set during the [initialization](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.html) of this base flange and cannot be changed.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
