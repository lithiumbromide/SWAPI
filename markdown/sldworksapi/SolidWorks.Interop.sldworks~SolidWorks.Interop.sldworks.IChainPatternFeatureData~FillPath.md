---
title: "FillPath Property (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "FillPath"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~FillPath.html"
---

# FillPath Property (IChainPatternFeatureData)

Gets or sets whether the maximum number of pattern instances to fill the path is calculated by SOLIDWORKS for this chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FillPath As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Boolean

instance.FillPath = value

value = instance.FillPath
```

### C#

```csharp
System.bool FillPath {get; set;}
```

### C++/CLI

```cpp
property System.bool FillPath {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the maximum number of pattern instances to fill the path is calculated by SOLIDWORKS, false if not (see **Remarks**)

## VBA Syntax

See [ChainPatternFeatureData::FillPath](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~FillPath.html).

## Examples

[Create and Modify Distance Chain Pattern Feature (C#)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_CSharp.htm)
[Create and Modify Distance Chain Pattern Feature (VB.NET)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_VBNET.htm)
[Create and Modify Distance Chain Pattern Feature (VBA)](Create_and_Modify_Distance_Chain_Pattern_Feature_Example_VB.htm)

## Remarks

This property is available for all types of chain patterns, but it is only available for distance and distance linkage chain patterns when [equal spacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~SetEqualSpacing.html) is not set.

To set the distance between the pattern instances, use [IChainPatternFeatureData::Spacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Spacing.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
