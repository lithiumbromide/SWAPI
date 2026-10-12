---
title: "CreateFeatureMgrControl4 Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "CreateFeatureMgrControl4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrControl4.html"
---

# CreateFeatureMgrControl4 Method (IModelViewManager)

Creates a new FeatureManager design tree view containing the specified ActiveX control with a tab that displays the specified scaleable icon.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFeatureMgrControl4( _
   ByVal BitMapFileNames As System.Object, _
   ByVal Class As System.String, _
   ByVal LicKey As System.String, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As FeatMgrView
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim BitMapFileNames As System.Object
Dim Class As System.String
Dim LicKey As System.String
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As FeatMgrView

value = instance.CreateFeatureMgrControl4(BitMapFileNames, Class, LicKey, ToolTip, WhichPane)
```

### C#

```csharp
FeatMgrView CreateFeatureMgrControl4(
   System.object BitMapFileNames,
   System.string Class,
   System.string LicKey,
   System.string ToolTip,
   System.int WhichPane
)
```

### C++/CLI

```cpp
FeatMgrView^ CreateFeatureMgrControl4(
   System.Object^ BitMapFileNames,
   System.String^ Class,
   System.String^ LicKey,
   System.String^ ToolTip,
   System.int WhichPane
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BitMapFileNames`: Array of fully qualified paths to three bitmap files, one for each size (small, medium, and large), to be used for the tab icon in different screen resolutions
- `Class`: CLSID or ProgID for the ActiveX control (see **Remarks**)
- `LicKey`: License key for the ActiveX control; empty string if unknown
- `ToolTip`: Text to display when hovering over the tab icon
- `WhichPane`: Pane where to add the tab as defined in [swFeatMgrPane_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html) (see **Remarks**)

### Return Value

Pointer to the new [tab](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatMgrView.html)

## VBA Syntax

See [ModelViewManager::CreateFeatureMgrControl4](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~CreateFeatureMgrControl4.html).

## Examples

[Add ActiveX Tab to FeatureManager Design Tree (VBA)](Add_ActiveX_Tab_to_FeatureManager_Design_Tree_Example_VB.htm)
[Add ActiveX Tab to FeatureManager Design Tree (VB.NET)](Add_ActiveX_Tab_to_FeatureManager_Design_Tree_Example_VBNET.htm)
[Add ActiveX Tab to FeatureManager Design Tree (C#)](Add_ActiveX_Tab_to_FeatureManager_Design_Tree_Example_CSharp.htm)

## Remarks

To:

- Add a tab to the FeatureManager design tree, specify WhichPane with swFeatMgrPane_e.FeatMgrPaneBottom.
- Add a tab to a split FeatureManager design tree, specify WhichPane with either swFeatMgrPane_e.swFeatMgrPaneTop or swFeatMgrPane_e.swFeatMgrPaneBottom. See [IModelDoc2::FeatureManagerSplitterPosition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureManagerSplitterPosition.html) for details on splitting and positioning the split panel bar in the FeatureManager design tree.
- Delete the tab created by this method, use [IFeatMgrView::DeleteView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatMgrView~DeleteView.html).

Specify Class with either the ProgID or the CLSID of the registered ActiveX control. You can obtain these strings by searching for the registered ActiveX control in the registry editor.

For example, **RichEditCtrol.ocx** resides in **c:\Program files\SOLIDWORKS Corp\SOLIDWORKS\sldUtils**. It is registered during the SOLIDWORKS installation. When you search for **RichEditCtrl.ocx** in the registry, you find ProgID = GTSWRICHEDITCTRL.RichEditCtrlCtrl.1 and CLSID = {7632C33C-A935-48FF-84D9-F0F173EF543D}. Use either the registry's ActiveX ProgID or CLSID to specify Class. The ActiveX control library names displayed in the Object Browser may not be the same as the ActiveX control names in the registry. Do not use the Object Browser to specify Class.

See also [Keystrokes and Accelerator Keys in ActiveX Modeless Dialogs and PropertyManager Pages](sldworksapiprogguide.chm::/overview/Keystrokes_and_Accelerator_Keys_and_ActiveX_Modeless_Dialogs_and_PropertyManager_Pages.htm).

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::CreateFeatureMgrView2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.html)
[IModelViewManager::AddControl3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl3.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
