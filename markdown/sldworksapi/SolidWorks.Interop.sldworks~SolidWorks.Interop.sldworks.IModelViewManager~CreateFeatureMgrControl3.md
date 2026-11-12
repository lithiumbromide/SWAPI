---
title: "CreateFeatureMgrControl3 Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "CreateFeatureMgrControl3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl3.html"
---

# CreateFeatureMgrControl3 Method (IModelViewManager)

Obsolete. Superseded by [IModelViewManager::CreateFeatureMgrControl4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFeatureMgrControl3( _
   ByVal BitMapFile As System.String, _
   ByVal Class As System.String, _
   ByVal LicKey As System.String, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As FeatMgrView
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim BitMapFile As System.String
Dim Class As System.String
Dim LicKey As System.String
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As FeatMgrView

value = instance.CreateFeatureMgrControl3(BitMapFile, Class, LicKey, ToolTip, WhichPane)
```

### C#

```csharp
FeatMgrView CreateFeatureMgrControl3(
   System.string BitMapFile,
   System.string Class,
   System.string LicKey,
   System.string ToolTip,
   System.int WhichPane
)
```

### C++/CLI

```cpp
FeatMgrView^ CreateFeatureMgrControl3(
   System.String^ BitMapFile,
   System.String^ Class,
   System.String^ LicKey,
   System.String^ ToolTip,
   System.int WhichPane
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BitMapFile`: Fully qualified path to the bitmap file that you want to use for the tab
- `Class`: Class ID for the ActiveX control
- `LicKey`: License key for the ActiveX control
- `ToolTip`: Text for the ToolTip
- `WhichPane`: Pane to use as defined in [swFeatMgrPane_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

### Return Value

Pointer to the new [tab](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatMgrView.html)

## VBA Syntax

See [ModelViewManager::CreateFeatureMgrControl3](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~CreateFeatureMgrControl3.html).

## Remarks

This method lets you add a tab for a registered ActiveX control to the FeatureManager design tree. A user can click the tab to activate the ActiveX control.

To add a tab to the FeatureManager design tree, specify swFeatMgrPane_e.FeatMgrPaneBottom for WhichPane. To add a tab to a FeatureManager design tree that has been split, specify swFeatMgrPane_e.swFeatMgrPaneTop and swFeatMgrPane_e.swFeatMgrPaneBottom, respectively, for WhichPane. See [IModelDoc2::FeatureManagerSplitterPosition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureManagerSplitterPosition.html) for details on splitting and positioning the split panel bar on a split FeatureManager design tree.

To delete a tab created by this method, use [IFeatMgrView::DeleteView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatMgrView~DeleteView.html).

Class can be either the name of the registered control (ProgID) or its class ID (CLSID), for example, "MSCAL.calendar" or "{8E27C92B-1264-101C-8A2F-040224009C02}". You must obtain these strings by searching for the registered ActiveX control in the registry editor. The ActiveX control library names displayed in the Object Browser may not be the same as the ActiveX control names in the registry. Do not use the Object Browser to specify Class.

See also [Keystrokes and Accelerator Keys in ActiveX Modeless Dialogs and PropertyManager Pages](sldworksapiprogguide.chm::/overview/Keystrokes_and_Accelerator_Keys_and_ActiveX_Modeless_Dialogs_and_PropertyManager_Pages.htm).

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::CreateFeatureMgrView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.html)
[IModelViewManager::AddControl3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl3.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
