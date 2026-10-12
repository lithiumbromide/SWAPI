---
title: "SetEqualSpacing Method (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "SetEqualSpacing"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~SetEqualSpacing.html"
---

# SetEqualSpacing Method (IChainPatternFeatureData)

Sets equal spacing between each chain pattern instance in this chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetEqualSpacing() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Boolean

value = instance.SetEqualSpacing()
```

### C#

```csharp
System.bool SetEqualSpacing()
```

### C++/CLI

```cpp
System.bool SetEqualSpacing();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if equal spacing is set between each chain pattern instance, false if not

## VBA Syntax

See [ChainPatternFeatureData::SetEqualSpacing](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~SetEqualSpacing.html).

## Remarks

This method is only available for distance and distance linkage chain patterns when [IChainPatternFeatureData::FillPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~FillPath.html) is false.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)
[IChainPatternFeatureData::InstanceCount ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~InstanceCount.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
