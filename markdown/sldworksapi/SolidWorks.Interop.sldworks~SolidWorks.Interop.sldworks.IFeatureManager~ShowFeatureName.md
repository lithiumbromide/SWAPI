---
title: "ShowFeatureName Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "ShowFeatureName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureName.html"
---

# ShowFeatureName Property (IFeatureManager)

Gets or sets whether to show the name of the feature in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowFeatureName As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Boolean

instance.ShowFeatureName = value

value = instance.ShowFeatureName
```

### C#

```csharp
System.bool ShowFeatureName {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowFeatureName {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True shows the name of the feature, false does not

## VBA Syntax

See [FeatureManager::ShowFeatureName](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~ShowFeatureName.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::ShowFeatureDescription Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureDescription.html)
[IFeatureManager::ShowComponentConfigurationDescriptions Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentConfigurationDescriptions.html)
[IFeatureManager::ShowComponentConfigurationNames Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentConfigurationNames.html)
[IFeatureManager::ShowComponentDescriptions Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentDescriptions.html)
[IFeatureManager::ShowComponentNames Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentNames.html)
[IFeatureManager::FeatureName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureName.html)
[IFeature::Name Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.html)
[IFeatureManager::ShowDisplayStateNames Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowDisplayStateNames.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
