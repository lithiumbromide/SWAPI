---
title: "D1ReverseDirection Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "D1ReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1ReverseDirection.html"
---

# D1ReverseDirection Property (ILinearPatternFeatureData)

Gets whether to reverse Direction 1 in this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1ReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Boolean

instance.D1ReverseDirection = value

value = instance.D1ReverseDirection
```

### C#

```csharp
System.bool D1ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool D1ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse Direction 1, false to not

## VBA Syntax

See [LinearPatternFeatureData::D1ReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~D1ReverseDirection.html).

## Examples

See the [ILinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html) example.

## Remarks

This property is valid only if [ILinearPatternFeatureData::D1EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndCondition.html) is set to [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition_SpacingAndInstances.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearFeaturePatternData::GetD1AxisType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetD1AxisType.html)
[ILinearFeaturePatternData::D1Axis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Axis.html)
[ILinearFeaturePatternData::D1Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Spacing.html)
[ILinearFeaturePatternData::D1TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1TotalInstances.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
