---
title: "FeatureManagerTabsVisible Property (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "FeatureManagerTabsVisible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~FeatureManagerTabsVisible.html"
---

# FeatureManagerTabsVisible Property (IModelViewManager)

Gets or sets whether all of the tabs in the Manager Pane are visible.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeatureManagerTabsVisible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim value As System.Boolean

instance.FeatureManagerTabsVisible = value

value = instance.FeatureManagerTabsVisible
```

### C#

```csharp
System.bool FeatureManagerTabsVisible {get; set;}
```

### C++/CLI

```cpp
property System.bool FeatureManagerTabsVisible {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if all of the tabs in the Manager Pane are visible, false if none of the tabs in the Manager Pane are visible

## VBA Syntax

See [ModelViewManager::FeatureManagerTabsVisible](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~FeatureManagerTabsVisible.html).

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelDocExtension::HideFeatureManager Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HideFeatureManager.html)
[IModelViewManager::GetConfigurationManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetConfigurationManagerTabIndex.html)
[IModelViewManager::GetDimXpertManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetDimXpertManagerTabIndex.html)
[IModelViewManager::GetDisplayManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetDisplayManagerTabIndex.html)
[IModelViewManager::GetFeatureManagerTabs Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureManagerTabs.html)
[IModelViewManager::GetFeatureManagerTreeTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureManagerTreeTabIndex.html)
[IModelViewManager::GetPropertyManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetPropertyManagerTabIndex.html)
[IModelViewManager::ActiveFeatureManagerTabIndex Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActiveFeatureManagerTabIndex.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
