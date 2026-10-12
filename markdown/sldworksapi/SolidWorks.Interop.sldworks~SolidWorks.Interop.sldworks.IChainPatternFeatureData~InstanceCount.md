---
title: "InstanceCount Property (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "InstanceCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~InstanceCount.html"
---

# InstanceCount Property (IChainPatternFeatureData)

Gets or sets the number of pattern instances in this chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property InstanceCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Integer

instance.InstanceCount = value

value = instance.InstanceCount
```

### C#

```csharp
System.int InstanceCount {get; set;}
```

### C++/CLI

```cpp
property System.int InstanceCount {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of pattern instances

## VBA Syntax

See [ChainPatternFeatureData::InstanceCount](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~InstanceCount.html).

## Examples

[Create and Modify Distance Chain Pattern Feature (C#)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_CSharp.htm)
[Create and Modify Distance Chain Pattern Feature (VB.NET)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_VBNET.htm)
[Create and Modify Distance Chain Pattern Feature (VBA)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_VB.htm)

## Remarks

This property is available to all types of chain patterns when [IChainPatternFeatureData::FillPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~FillPath.html) is false.

If the pattern instances are not [equally spaced](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~SetEqualSpacing.html), then use [IChainPatternFeatureData::Spacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Spacing.html) to specify the distance between each pattern instance.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
