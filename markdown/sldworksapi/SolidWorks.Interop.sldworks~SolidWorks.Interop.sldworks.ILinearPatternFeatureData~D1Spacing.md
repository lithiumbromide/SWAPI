---
title: "D1Spacing Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "D1Spacing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Spacing.html"
---

# D1Spacing Property (ILinearPatternFeatureData)

Gets or sets the spacing between pattern instances in Direction 1 of this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1Spacing As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Double

instance.D1Spacing = value

value = instance.D1Spacing
```

### C#

```csharp
System.double D1Spacing {get; set;}
```

### C++/CLI

```cpp
property System.double D1Spacing {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance in meters between pattern instances in Direction 1

## VBA Syntax

See [LinearPatternFeatureData::D1Spacing](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~D1Spacing.html).

## Examples

See the [ILinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html) example.

## Remarks

You can set this property when [ILinearPatternFeatureData::D1EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndCondition.html) is set to:

- [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition_SpacingAndInstances

- or -

- swPatternEndCondition_e.swPatternEndCondition_UpToReference and [ILinearPatternFeatureData::D1EndUseSpacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndUseSpacing.html) is set to true.

For more information, see the **Linear Patterns and the Linear Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::GetD1AxisType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetD1AxisType.html)
[ILinearPatternFeatureData::D1Axis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Axis.html)
[ILinearPatternFeatureData::D1ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1ReverseDirection.html)
[ILinearPatternFeatureData::D1TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1TotalInstances.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
