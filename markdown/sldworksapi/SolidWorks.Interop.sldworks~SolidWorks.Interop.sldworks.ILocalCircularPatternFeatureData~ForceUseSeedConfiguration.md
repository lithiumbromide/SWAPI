---
title: "ForceUseSeedConfiguration Property (ILocalCircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: "ForceUseSeedConfiguration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ForceUseSeedConfiguration.html"
---

# ForceUseSeedConfiguration Property (ILocalCircularPatternFeatureData)

Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this local circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ForceUseSeedConfiguration As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCircularPatternFeatureData
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

See [LocalCircularPatternFeatureData::ForceUseSeedConfiguration](ms-its:sldworksapivb6.chm::/sldworks~LocalCircularPatternFeatureData~ForceUseSeedConfiguration.html).

## Remarks

If this property is set to true, the **Referenced configuration** section of the Component Properties dialog is disabled, and you cannot use [IComponent2::ReferencedConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedConfiguration.html) to change the configuration of a pattern component.

## See Also

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
