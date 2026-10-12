---
title: "BlindDepth Property (IAdvancedHoleElementData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleElementData"
member: "BlindDepth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~BlindDepth.html"
---

# BlindDepth Property (IAdvancedHoleElementData)

Gets or sets the depth for the blind end condition of this Advanced Hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property BlindDepth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleElementData
Dim value As System.Double

instance.BlindDepth = value

value = instance.BlindDepth
```

### C#

```csharp
System.double BlindDepth {get; set;}
```

### C++/CLI

```cpp
property System.double BlindDepth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Blind depth

## VBA Syntax

See [AdvancedHoleElementData::BlindDepth](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleElementData~BlindDepth.html).

## Examples

See the [IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html) examples.

## Remarks

This property is valid only if [IAdvancedHoleFeatureData::UseBaselineDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~UseBaselineDimensions.html) is set to false, [IAdvancedHoleElementData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~EndCondition.html) is set to [swEndConditions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html).swEndCondBlind, and the hole element's corresponding override property is set to true:

- [ICounterboreElementData::EndConditionOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData~EndConditionOverride.html)
- [ICountersinkElementData::EndConditionOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData~EndConditionOverride.html)
- [ITaperedTapElementData::EndConditionOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData~EndConditionOverride.html)

## See Also

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html)
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.html)
[IStraightTapElementData::Equation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~Equation.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
