---
title: "D2ReverseDirection Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "D2ReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2ReverseDirection.html"
---

# D2ReverseDirection Property (ILinearPatternFeatureData)

Gets whether to reverse Direction 2 in this bidirectional linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2ReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Boolean

instance.D2ReverseDirection = value

value = instance.D2ReverseDirection
```

### C#

```csharp
System.bool D2ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool D2ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse Direction 2, false to not

## VBA Syntax

See [LinearPatternFeatureData::D2ReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~D2ReverseDirection.html).

## Examples

See the [ILinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html) example.

## Remarks

This property is valid only if [ILinearPatternFeatureData::D2EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2EndCondition.html) is set to [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition_SpacingAndInstances.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::GetD2AxisType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetD2AxisType.html)
[ILinearPatternFeatureData::IsDirection2Specified Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IsDirection2Specified.html)
[ILinearPatternFeatureData::D2Axis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2Axis.html)
[ILinearPatternFeatureData::D2Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2Spacing.html)
[ILinearPatternFeatureData::D2TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2TotalInstances.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
