---
title: "UseBaselineDimensions Property (IAdvancedHoleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleFeatureData"
member: "UseBaselineDimensions"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~UseBaselineDimensions.html"
---

# UseBaselineDimensions Property (IAdvancedHoleFeatureData)

Gets or sets whether to use baseline dimensions in this Advanced Hole.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseBaselineDimensions As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleFeatureData
Dim value As System.Boolean

instance.UseBaselineDimensions = value

value = instance.UseBaselineDimensions
```

### C#

```csharp
System.bool UseBaselineDimensions {get; set;}
```

### C++/CLI

```cpp
property System.bool UseBaselineDimensions {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use baseline dimensions, false to not (see **Remarks**)

## VBA Syntax

See [AdvancedHoleFeatureData::UseBaselineDimensions](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleFeatureData~UseBaselineDimensions.html).

## Remarks

If you set this property to true, then you can get and set:

- [ICounterboreElementData::UseStandardDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData~UseStandardDepth.html)
- [ICountersinkElementData::UseStandardDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData~UseStandardDepth.html)
- [ITaperedTapElementData::UseStandardDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData~UseStandardDepth.html)
- [IStraightTapElementData::Equation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~Equation.html) (for the Offset From Surface end condition only)

but you cannot set any end conditions or end condition overrides.

If you set this property to false, then the UseStandardDepth properties above are not valid, but you can get and set:

- [ICounterboreElementData::EndConditionOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData~EndConditionOverride.html)
- [ICountersinkElementData::EndConditionOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData~EndConditionOverride.html)
- [ITaperedTapElementData::EndConditionOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData~EndConditionOverride.html)
- [IAdvancedHoleElementData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~EndCondition.html) (only if the corresponding EndConditionOverride for the element is set to true)
- [IAdvancedHoleElementData::BlindDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~BlindDepth.html) (for the Blind end condition only)
- IStraightTapElementData::Equation (for the Blind end condition only)

## See Also

[IAdvancedHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.html)
[IAdvancedHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
