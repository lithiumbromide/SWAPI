---
title: "CreateFeatureMgrView2 Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "CreateFeatureMgrView2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.html"
---

# CreateFeatureMgrView2 Method (IModelViewManager)

Creates a new view (tab) in this FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFeatureMgrView2( _
   ByVal BitMapFile As System.String, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As FeatMgrView
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim BitMapFile As System.String
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As FeatMgrView

value = instance.CreateFeatureMgrView2(BitMapFile, ToolTip, WhichPane)
```

### C#

```csharp
FeatMgrView CreateFeatureMgrView2(
   System.string BitMapFile,
   System.string ToolTip,
   System.int WhichPane
)
```

### C++/CLI

```cpp
FeatMgrView^ CreateFeatureMgrView2(
   System.String^ BitMapFile,
   System.String^ ToolTip,
   System.int WhichPane
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BitMapFile`: Bitmap file that you want to use for the tab
- `ToolTip`: Text for the ToolTip
- `WhichPane`: Pane to use as defined in [swFeatMgrPane_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

### Return Value

Pointer to the new [tab](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatMgrView.html)

## VBA Syntax

See [ModelViewManager::CreateFeatureMgrView2](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~CreateFeatureMgrView2.html).

## Remarks

This method provides the ability to place your newly created Feature Manager tab on either the top or bottom pane. The pane may or may not be visible. However, the tab is added to the specified pane.

Under certain conditions, for example while the Surface, Extend command is active in the user interface, SOLIDWORKS locks the bottom pane and does not allow the activation of any other tab. If your application needs the ability to activate your new tab at all times, consider adding it either to the top pane or to both panes. If you add it to the top pane only, it may not be apparent to the user until the top pane is made visible.

If you receive a non-NULL return value, you can use [IFeatMgrView::GetFeatMgrViewWnd](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatMgrView~GetFeatMgrViewWnd.html) or [IFeatureMgrView::GetFeatMgrViewWndx64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatMgrView~GetFeatMgrViewWndx64.html) to get the new view handle. Because the view created is empty, you can use the new view handle in combination with standard MFC calls to draw, as desired, into the view.

The FeatureManager design tree view added to this document is not persistent. In other words, the FeatureManager design tree view is not stored with this document and must be recreated upon reloading the document.

This method automatically sets up to receive FeatMgrView [ActivateNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DFeatMgrViewEvents_ActivateNotifyEventHandler.html) and [DeactivateNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DFeatMgrViewEvents_DeactivateNotifyEventHandler.html) events. On the appropriate notification, you can call [IModelDoc2::DeleteFeatureMgrView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~DeleteFeatureMgrView.html) or [IModelDocExtension::DeleteFeatureMgrViewx64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~DeleteFeatureMgrViewx64.html) to clean up and delete your view.

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::CreateFeatureMgrControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl.html)
[IModelViewManager::CreateFeatureMgrControl2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl2.html)
[IModelViewManager::CreateFeatureMgrControl3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl3.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
