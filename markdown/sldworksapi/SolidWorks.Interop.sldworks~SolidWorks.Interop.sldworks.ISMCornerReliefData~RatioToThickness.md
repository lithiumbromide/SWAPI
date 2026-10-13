---
title: "RatioToThickness Property (ISMCornerReliefData)"
project: "SOLIDWORKS API Help"
interface: "ISMCornerReliefData"
member: "RatioToThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~RatioToThickness.html"
---

# RatioToThickness Property (ISMCornerReliefData)

Gets and sets whether to use a ratio of length/width over sheet metal thickness to cut the bend area so that the body can be folded.

## Syntax

### Visual Basic (Declaration)

```vb
Property RatioToThickness As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMCornerReliefData
Dim value As System.Boolean

instance.RatioToThickness = value

value = instance.RatioToThickness
```

### C#

```csharp
System.bool RatioToThickness {get; set;}
```

### C++/CLI

```cpp
property System.bool RatioToThickness {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use a ratio value to cut the bend area, false to not

## VBA Syntax

See [SMCornerReliefData::RatioToThickness](ms-its:sldworksapivb6.chm::/sldworks~SMCornerReliefData~RatioToThickness.html).

## Examples

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html) examples.

## Remarks

This property is valid only if [ISMCornerReliefData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~ReliefType.html) is set to [swCornerReliefType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html).:

- swCornerCircularRelief
- swCornerObroundRelief
- swCornerRectangularRelief

| If ISMCornerReliefData::ReliefType is set to swCornerReliefType_e .swCornerRectangularRelief. | Then the calculated ratio(s) is(are)... |
| --- | --- |
| swCornerCircularRelief | slot length / thickness of sheet metal |
| swCornerRectangularRelief | slot length / thickness of sheet metal |
| swCornerObroundRelief | slot length / thickness of sheet metal - And - slot width / thickness of sheet metal |

## See Also

[ISMCornerReliefData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.html)
[ISMCornerReliefData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
