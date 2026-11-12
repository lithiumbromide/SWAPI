---
title: "IModelViewManager Interface Methods"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_methods.html"
---

# IModelViewManager Interface Methods

For a list of all members of this type, see [IModelViewManager members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ActivateControlTab | Selects a control tab on the model view to be the active tab. |
| Method | ActivateModelTab | Selects a control tab on the model view. |
| Method | AddControl | Adds a tab to this model view using the specified ActiveX control. |
| Method | AddControl2 | Obsolete. Superseded by IModelViewManager::AddControl3 . |
| Method | AddControl3 | Adds a tab to this model view that supports tab traversal using the specified ActiveX control. |
| Method | AddSnapShot | Creates a snapshot with the specified name of an assembly. |
| Method | CreateFeatureMgrControl | Obsolete. Superseded by IModelViewManager::CreateFeatureMgrControl2 . |
| Method | CreateFeatureMgrControl2 | Obsolete. Superseded by IModelViewManager::CreateFeatureMgrControl3 . |
| Method | CreateFeatureMgrControl3 | Obsolete. Superseded by IModelViewManager::CreateFeatureMgrControl4 . |
| Method | CreateFeatureMgrControl4 | Creates a new FeatureManager design tree view containing the specified ActiveX control with a tab that displays the specified scaleable icon. |
| Method | CreateFeatureMgrView | Obsolete. Superseded by IModelViewManager::CreateFeatureMgrView2 . |
| Method | CreateFeatureMgrView2 | Creates a new view (tab) in this FeatureManager design tree. |
| Method | CreateFeatureMgrWindowFromHandle | Obsolete. Superseded by IModelViewManager::CreateFeatureMgrWindowFromHandlex64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. Creates a new view in the FeatureManager design tree using the specified .NET tab control. |
| Method | CreateFeatureMgrWindowFromHandlex64 | On 64-bit machines, creates a new view in the FeatureManager design tree using the specified .NET tab control. |
| Method | CreateManipulator | Creates a manipulator, which is similar to the triad in the SOLIDWORKS Design user interface. |
| Method | CreateSectionView | Creates a section view in parts and assemblies. |
| Method | CreateSectionViewData | Creates an empty ISectionViewData object whose properties you set before creating a section view in a part or an assembly . |
| Method | DeleteControlTab | Deletes the specified control tab. |
| Method | DeleteSnapShot | Deletes the specified snapshot from an assembly. |
| Method | DisplayWindowFromHandle | Obsolete. Superseded by IModelViewManager::DisplayWindowFromHandlex64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. Displays a .NET control in this model view. |
| Method | DisplayWindowFromHandlex64 | Displays a .NET control in this model view on 64-bit machines. |
| Method | GetConfigurationManagerTabIndex | Gets the index of the ConfigurationManager tab in the Manager Pane. |
| Method | GetControl | Gets the control associated with this model view. |
| Method | GetDimXpertManagerTabIndex | Gets the index of the DimXpertManager tab in the Manager Pane. |
| Method | GetDisplayManagerTabIndex | Gets the index of the DisplayManager tab in the Manager Pane. |
| Method | GetFeatureManagerTabs | Gets the tabs from right to left in the Manager Pane. |
| Method | GetFeatureManagerTreeTabIndex | Gets the index of the FeatureManager design tree tab in the Manager Pane. |
| Method | GetFeatureMgrViewHWnd | Obsolete. Superseded by IModelViewManager::GetFeatureMgrViewHWndx64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. Gets the window handle for the specified FeatureManager design tree view. |
| Method | GetFeatureMgrViewHWndx64 | Gets the window handle for the specified FeatureManager design tree view in 64-bit applications. |
| Method | GetPropertyManagerTabIndex | Gets the index of the PropertyManager tab in the Manager Pane. |
| Method | GetSectionViewData | Gets access to the data of the specified section view. |
| Method | GetSnapShot | Gets the specified snapshot of an assembly. |
| Method | GetSnapShots | Gets the snapshots of an assembly. |
| Method | IGetControl | Gets the control associated with this model view. |
| Method | IsControlTabActive | Gets whether the specified control is active. |
| Method | IsModelTabActive | Gets whether the control on this model view is active. |
| Method | RemoveSectionView | Removes a section view from a part and assembly. |

[Top](#topBookmark)

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.html)
[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.html)
