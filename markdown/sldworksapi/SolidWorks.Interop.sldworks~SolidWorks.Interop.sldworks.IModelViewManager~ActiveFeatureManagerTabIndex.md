---
title: "ActiveFeatureManagerTabIndex Property (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "ActiveFeatureManagerTabIndex"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ActiveFeatureManagerTabIndex.html"
---

# ActiveFeatureManagerTabIndex Property (IModelViewManager)

Gets or sets the index of the active tab in the Manager Pane.

## Syntax

### Visual Basic (Declaration)

```vb
Property ActiveFeatureManagerTabIndex As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim value As System.Integer

instance.ActiveFeatureManagerTabIndex = value

value = instance.ActiveFeatureManagerTabIndex
```

### C#

```csharp
System.int ActiveFeatureManagerTabIndex {get; set;}
```

### C++/CLI

```cpp
property System.int ActiveFeatureManagerTabIndex {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Index of the active tab in the Manager Pane

## VBA Syntax

See [ModelViewManager::ActiveFeatureManagerTabIndex](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~ActiveFeatureManagerTabIndex.html).

## Examples

[Change Active Tab in Manager Pane (C#)](Change_Active_Tab_in_Manager_Pane_Example_CSharp.htm)
[Change Active Tab in Manager Pane (VB.NET)](Change_Active_Tab_in_Manager_Pane_Example_VBNET.htm)
[Change Active Tab in Manager Pane (VBA)](Change_Active_Tab_in_Manager_Pane_Example_VB.htm)

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::FeatureManagerTabsVisible Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~FeatureManagerTabsVisible.html)
[IModelViewManager::GetConfigurationManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetConfigurationManagerTabIndex.html)
[IModelViewManager::GetDimXpertManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetDimXpertManagerTabIndex.html)
[IModelViewManager::GetDisplayManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetDisplayManagerTabIndex.html)
[IModelViewManager::GetFeatureManagerTabs Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureManagerTabs.html)
[IModelViewManager::GetFeatureManagerTreeTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureManagerTreeTabIndex.html)
[IModelViewManager::GetPropertyManagerTabIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetPropertyManagerTabIndex.html)
[DAssemblyDocEvents_FeatureManagerTabActivatedNotifyEventHandler Delegate (IModelViewManager)](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureManagerTabActivatedNotifyEventHandler.html)
[DAssemblyDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler Delegate (IModelViewManager)](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler.html)
[DDrawingDocEvents_FeatureManagerTabActivatedNotifyEventHandler Delegate (IModelViewManager)](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FeatureManagerTabActivatedNotifyEventHandler.html)
[DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler Delegate (IModelViewManager)](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler.html)
[DPartDocEvents_FeatureManagerTabActivatedNotifyEventHandler Delegate (IModelViewManager)](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FeatureManagerTabActivatedNotifyEventHandler.html)
[DPartDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler Delegate (IModelViewManager)](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
