---
title: "Spacing Property (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "Spacing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Spacing.html"
---

# Spacing Property (IChainPatternFeatureData)

Gets or sets the distance between the pattern instances in the [path](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Path.html) in this chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Spacing As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Double

instance.Spacing = value

value = instance.Spacing
```

### C#

```csharp
System.double Spacing {get; set;}
```

### C++/CLI

```cpp
property System.double Spacing {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance between the pattern instances (see **Remarks**)

## VBA Syntax

See [ChainPatternFeatureData::Spacing](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~Spacing.html).

## Examples

[Create and Modify Distance Chain Pattern Feature (C#)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_CSharp.htm)
[Create and Modify Distance Chain Pattern Feature (VB.NET)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_VBNET.htm)
[Create and Modify Distance Chain Pattern Feature (VBA)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_VB.htm)

## Remarks

This property is only available for distance and linkage distance chain patterns when [equal spacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~SetEqualSpacing.html) is not set.

To:

- have SOLIDWORKS calculate the maximum number of pattern instances to fill the path using the specified distance, use [IChainPatternFeatureData::FillPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~FillPath.html).
  - or -
- set the number of pattern instances for the path using the specified distance, use [IChainPatternFeatureData::InstanceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~InstanceCount.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
