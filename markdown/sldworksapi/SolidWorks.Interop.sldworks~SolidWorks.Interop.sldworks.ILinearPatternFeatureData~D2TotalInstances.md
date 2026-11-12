---
title: "D2TotalInstances Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "D2TotalInstances"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2TotalInstances.html"
---

# D2TotalInstances Property (ILinearPatternFeatureData)

Gets or sets the total number of pattern instances in Direction 2 in this bidirectional linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2TotalInstances As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Integer

instance.D2TotalInstances = value

value = instance.D2TotalInstances
```

### C#

```csharp
System.int D2TotalInstances {get; set;}
```

### C++/CLI

```cpp
property System.int D2TotalInstances {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Total number of pattern instances in Direction 2

## VBA Syntax

See [LinearPatternFeatureData::D2TotalInstances](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~D2TotalInstances.html).

## Examples

See the [ILinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html) example.

## Examples

[Get Linear Pattern Feature Data (C#)](Get_Linear_Pattern_Feature_Data_Example_CSharp.htm)
[Get Linear Pattern Feature Data (VB.NET)](Get_Linear_Pattern_Feature_Data_Example_VBNET.htm)
[Get Linear Pattern Feature Data (VBA)](Get_Linear_Pattern_Feature_Data_Example_VB.htm)

## Remarks

You can set this property when [ILinearPatternFeatureData::D2EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2EndCondition.html) is set to:

- [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition_SpacingAndInstances

- or -

- swPatternEndCondition_e.swPatternEndCondition_UpToReference and [ILinearPatternFeatureData::D2EndUseSpacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2EndUseSpacing.html) is set to false.

For more information, see the **Linear Patterns and the Linear Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::GetD2AxisType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetD2AxisType.html)
[ILinearPatternFeatureData::IsDirection2Specified Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IsDirection2Specified.html)
[ILinearPatternFeatureData::D2Axis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2Axis.html)
[ILinearPatternFeatureData::D2PatternSeedOnly Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2PatternSeedOnly.html)
[ILinearPatternFeatureData::D2ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2ReverseDirection.html)
[ILinearPatternFeatureData::D2Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2Spacing.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
