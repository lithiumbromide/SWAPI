---
title: "ShowDisplayStateNames Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "ShowDisplayStateNames"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowDisplayStateNames.html"
---

# ShowDisplayStateNames Property (IFeatureManager)

Gets or sets whether to show the display state names in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowDisplayStateNames As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Boolean

instance.ShowDisplayStateNames = value

value = instance.ShowDisplayStateNames
```

### C#

```csharp
System.bool ShowDisplayStateNames {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowDisplayStateNames {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to show display state names, false to not

## VBA Syntax

See [FeatureManager::ShowDisplayStateNames](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~ShowDisplayStateNames.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::ShowComponentConfigurationDescriptions Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentConfigurationDescriptions.html)
[IFeatureManager::ShowComponentConfigurationNames Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentConfigurationNames.html)
[IFeatureManager::ShowComponentDescriptions Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentDescriptions.html)
[IFeatureManager::ShowComponentNames Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowComponentNames.html)
[IFeatureManager::ShowFeatureDescription Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureDescription.html)
[IFeatureManager::ShowFeatureDetails Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureDetails.html)
[IFeatureManager::ShowFeatureName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureName.html)
[IFeatureManager::ShowHierarchyOnly Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowHierarchyOnly.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
