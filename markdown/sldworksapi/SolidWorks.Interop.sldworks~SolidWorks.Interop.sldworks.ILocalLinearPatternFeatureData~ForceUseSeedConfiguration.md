---
title: "ForceUseSeedConfiguration Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "ForceUseSeedConfiguration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~ForceUseSeedConfiguration.html"
---

# ForceUseSeedConfiguration Property (ILocalLinearPatternFeatureData)

Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this local linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ForceUseSeedConfiguration As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
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

See [LocalLinearPatternFeatureData::ForceUseSeedConfiguration](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~ForceUseSeedConfiguration.html).

## Remarks

If this property is set to true, the **Referenced configuration** section of the Component Properties dialog is disabled, and you cannot use [IComponent2::ReferencedConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedConfiguration.html) to change the pattern instance configuration.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
