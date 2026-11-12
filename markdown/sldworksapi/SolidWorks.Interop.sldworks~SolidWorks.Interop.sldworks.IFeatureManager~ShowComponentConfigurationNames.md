---
title: "ShowComponentConfigurationNames Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "ShowComponentConfigurationNames"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentConfigurationNames.html"
---

# ShowComponentConfigurationNames Property (IFeatureManager)

Gets or sets whether to show the active configuration's component configuration names in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowComponentConfigurationNames As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Boolean

instance.ShowComponentConfigurationNames = value

value = instance.ShowComponentConfigurationNames
```

### C#

```csharp
System.bool ShowComponentConfigurationNames {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowComponentConfigurationNames {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True shows the active configuration's component configuration names, false does not

## VBA Syntax

See [FeatureManager::ShowComponentConfigurationNames](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~ShowComponentConfigurationNames.html).

## Examples

[Show Components and Component Configurations Names and Descriptions (VBA)](Show_Components_and_Component_Configurations_Names_and_Descriptions_Example_VB.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::ShowComponentConfigurationDescriptions Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentConfigurationDescriptions.html)
[IFeatureManager::ShowComponentDescriptions Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentDescriptions.html)
[IFeatureManager::ShowComponentNames Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentNames.html)
[IFeatureManager::ShowFeatureDescription Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureDescription.html)
[IFeatureManager::ShowFeatureName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureName.html)
[IFeatureManager::ShowDisplayStateNames Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowDisplayStateNames.html)

## Availability

SOLIDWORKS 2007 SP3, Revision Number 15.3
