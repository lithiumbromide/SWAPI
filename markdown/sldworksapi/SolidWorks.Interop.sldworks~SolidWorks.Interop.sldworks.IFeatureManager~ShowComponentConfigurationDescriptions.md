---
title: "ShowComponentConfigurationDescriptions Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "ShowComponentConfigurationDescriptions"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentConfigurationDescriptions.html"
---

# ShowComponentConfigurationDescriptions Property (IFeatureManager)

Gets or sets whether to show the active configuration's component configuration descriptions in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowComponentConfigurationDescriptions As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Boolean

instance.ShowComponentConfigurationDescriptions = value

value = instance.ShowComponentConfigurationDescriptions
```

### C#

```csharp
System.bool ShowComponentConfigurationDescriptions {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowComponentConfigurationDescriptions {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True shows the active configuration's component configuration descriptions, false does not

## VBA Syntax

See [FeatureManager::ShowComponentConfigurationDescriptions](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~ShowComponentConfigurationDescriptions.html).

## Examples

[Show Components and Component Configurations Names and Descriptions (VBA)](Show_Components_and_Component_Configurations_Names_and_Descriptions_Example_VB.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::ShowComponentConfigurationNames Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentConfigurationNames.html)
[IFeatureManager::ShowComponentDescriptions Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentDescriptions.html)
[IFeatureManager::ShowComponentNames Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentNames.html)
[IFeatureManager::ShowFeatureDescription Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureDescription.html)
[IFeatureManager::ShowFeatureName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureName.html)
[IFeatureManager::ShowDisplayStateNames Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowDisplayStateNames.html)

## Availability

SOLIDWORKS 2007 SP3, Revision Number 15.3
