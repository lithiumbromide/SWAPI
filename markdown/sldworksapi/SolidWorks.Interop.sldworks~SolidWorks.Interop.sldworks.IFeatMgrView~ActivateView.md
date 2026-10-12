---
title: "ActivateView Method (IFeatMgrView)"
project: "SOLIDWORKS API Help"
interface: "IFeatMgrView"
member: "ActivateView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~ActivateView.html"
---

# ActivateView Method (IFeatMgrView)

Activates this view in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function ActivateView() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatMgrView
Dim value As System.Integer

value = instance.ActivateView()
```

### C#

```csharp
System.int ActivateView()
```

### C++/CLI

```cpp
System.int ActivateView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pane on which to activate this tab as defined in [swFeatMgrPane_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

## VBA Syntax

See [FeatMgrView::ActivateView](ms-its:sldworksapivb6.chm::/sldworks~FeatMgrView~ActivateView.html).

## Examples

This method is valid only for x86 systems.

## Examples

[Add ActiveX Tabs to FeatureManager Design Tree (C#)](Add_ActiveX_Tabs_to_FeatureManager_Design_Tree_Example_CSharp.htm)
[Add ActiveX Tabs to FeatureManager Design Tree (VB.NET)](Add_ActiveX_Tabs_to_FeatureManager_Design_Tree_Example_VBNET.htm)
[Add ActiveX Tabs to FeatureManager Design Tree (VBA)](Add_ActiveX_Tabs_to_FeatureManager_Design_Tree_Example_VB.htm)
[Add .NET Controls to SOLIDWORKS Using an Add-in (C#)](Add_.NET_Controls_to_SOLIDWORKS_Using_an_Add-in_Example_CSharp.htm)
[Add .NET Controls to SOLIDWORKS using an Add-in (VB.NET)](Add_.NET_Controls_to_SolidWorks_Using_an_Add-in_Example_VBNET.htm)

## See Also

[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.html)
[IFeatMgrView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView_members.html)
[IFeatMgrView::DeActivateView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~DeActivateView.html)
[IFeatMgrView::DeleteView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~DeleteView.html)
[IModelViewManager::AddControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl.html)
[IModelViewManager::AddControl3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl3.html)
[IModelViewManager::CreateFeatureMgrControl2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl2.html)
[IModelViewManager::CreateFeatureMgrControl3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl3.html)
[IModelDocExtension::ActivateFeatureMgrViewx64 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActivateFeatureMgrViewx64.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
