---
title: "ClearGroup2Selections Method (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "ClearGroup2Selections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~ClearGroup2Selections.html"
---

# ClearGroup2Selections Method (IChainPatternFeatureData)

Clears **Chain Group 2** selections in this connected linkage chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function ClearGroup2Selections() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Boolean

value = instance.ClearGroup2Selections()
```

### C#

```csharp
System.bool ClearGroup2Selections()
```

### C++/CLI

```cpp
System.bool ClearGroup2Selections();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if **Chain Group 2** selections are cleared, false if no selections for **Chain Group 2** existed (see **Remarks**)

## VBA Syntax

See [ChainPatternFeatureData::ClearGroup2Selections](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~ClearGroup2Selections.html).

## Remarks

This method allows you to change a **Chain Group 1** and **Chain Group 2** connected linkage chain pattern feature to a **Chain Group 1** connected linkage chain pattern feature.

This property is only available to connected linkage chain patterns.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)
[IChainPatternFeatureData::Group2FlipPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2FlipPlane.html)
[IChainPatternFeatureData::Group2PathLink1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathLink1.html)
[IChainPatternFeatureData::Group2PathLink2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathLink2.html)
[IChainPatternFeatureData::Group2PathPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PathPlane.html)
[IChainPatternFeatureData::Group2PatternComponent Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group2PatternComponent.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
