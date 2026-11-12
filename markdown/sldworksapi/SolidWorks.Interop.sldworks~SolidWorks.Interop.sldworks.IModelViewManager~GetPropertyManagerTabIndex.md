---
title: "GetPropertyManagerTabIndex Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "GetPropertyManagerTabIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetPropertyManagerTabIndex.html"
---

# GetPropertyManagerTabIndex Method (IModelViewManager)

Gets the index of the PropertyManager tab in the Manager Pane.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPropertyManagerTabIndex() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim value As System.Integer

value = instance.GetPropertyManagerTabIndex()
```

### C#

```csharp
System.int GetPropertyManagerTabIndex()
```

### C++/CLI

```cpp
System.int GetPropertyManagerTabIndex();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

1

## VBA Syntax

See [ModelViewManager::GetPropertyManagerTabIndex](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~GetPropertyManagerTabIndex.html).

## Examples

[Change Active Tab in Manager Pane (C#)](Change_Active_Tab_in_Manager_Pane_Example_CSharp.htm)
[Change Active Tab in Manager Pane (VB.NET)](Change_Active_Tab_in_Manager_Pane_Example_VBNET.htm)
[Change Active Tab in Manager Pane (VBA)](Change_Active_Tab_in_Manager_Pane_Example_VB.htm)

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::GetConfigurationManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetConfigurationManagerTabIndex.html)
[IModelViewManager::GetDimXpertManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetDimXpertManagerTabIndex.html)
[IModelViewManager::GetDisplayManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetDisplayManagerTabIndex.html)
[IModelViewManager::GetFeatureManagerTabs Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureManagerTabs.html)
[IModelViewManager::GetFeatureManagerTreeTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureManagerTreeTabIndex.html)
[IModelViewManager::ActiveFeatureManagerTabIndex Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActiveFeatureManagerTabIndex.html)
[IModelViewManager::FeatureManagerTabsVisible Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~FeatureManagerTabsVisible.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
