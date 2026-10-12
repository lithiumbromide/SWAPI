---
title: "ForceUseSeedConfiguration Property (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "ForceUseSeedConfiguration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~ForceUseSeedConfiguration.html"
---

# ForceUseSeedConfiguration Property (IChainPatternFeatureData)

Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ForceUseSeedConfiguration As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Boolean

instance.ForceUseSeedConfiguration = value

value = instance.ForceUseSeedConfiguration
```

### C#

```csharp
System.bool ForceUseSeedConfiguration {get; set;}
```

### C++/CLI

```cpp
property System.bool ForceUseSeedConfiguration {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the seed component configuration for all pattern components, false to not

## VBA Syntax

See [ChainPatternFeatureData::ForceUseSeedConfiguration](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~ForceUseSeedConfiguration.html).

## Remarks

If this property is set to true, the **Referenced configuration** section of the Component Properties dialog is disabled, and you cannot use [IComponent2::ReferencedConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedConfiguration.html) to change the pattern instance configuration.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
