---
title: "ForceUseSeedConfiguration Property (IMirrorComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorComponentFeatureData"
member: "ForceUseSeedConfiguration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~ForceUseSeedConfiguration.html"
---

# ForceUseSeedConfiguration Property (IMirrorComponentFeatureData)

Gets or sets whether to synchronize the configuration of mirror components with the configuration of the mirrored component in this mirror component feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ForceUseSeedConfiguration As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorComponentFeatureData
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

True to use the mirrored component configuration for all mirror components, false to not

## VBA Syntax

See [MirrorComponentFeatureData::ForceUseSeedConfiguration](ms-its:sldworksapivb6.chm::/sldworks~MirrorComponentFeatureData~ForceUseSeedConfiguration.html).

## Remarks

If this property is set to true, the **Referenced configuration** section of the Component Properties dialog is disabled, and you cannot use [IComponent2::ReferencedConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedConfiguration.html) to change the pattern instance configuration.

## See Also

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.html)
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
