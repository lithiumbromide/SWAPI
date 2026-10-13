---
title: "GetFeatMgrViewWnd Method (IFeatMgrView)"
project: "SOLIDWORKS API Help"
interface: "IFeatMgrView"
member: "GetFeatMgrViewWnd"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~GetFeatMgrViewWnd.html"
---

# GetFeatMgrViewWnd Method (IFeatMgrView)

Obsolete. Superseded by [IFeatMgrView::GetFeatMgrViewWndx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~GetFeatMgrViewWndx64.html).

This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016.

The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used.

Gets the FeatureManager design tree view window handle as a CWnd object.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatMgrViewWnd() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatMgrView
Dim value As System.Integer

value = instance.GetFeatMgrViewWnd()
```

### C#

```csharp
System.int GetFeatMgrViewWnd()
```

### C++/CLI

```cpp
System.int GetFeatMgrViewWnd();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

CWnd handle of the FeatureManager design tree view

## VBA Syntax

See [FeatMgrView::GetFeatMgrViewWnd](ms-its:sldworksapivb6.chm::/sldworks~FeatMgrView~GetFeatMgrViewWnd.html).

## Remarks

If your application must be x64 compatible, then use [IFeatMgrView::GetFeatMgrViewWndx64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatMgrView~GetFeatMgrViewWndx64.html).

You can use this CWnd in combination with standard MFC calls to draw into this view.

Call this method when the FeatureManager design tree is created with [IModelViewManager::CreateFeatureMgrView2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.html). You do not need to call this method with [IModelDoc2::AddFeatureMgrView3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddFeatureMgrView3.html), because you created the view and already have its handle.

## See Also

[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.html)
[IFeatMgrView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView_members.html)
[IModelViewManager::GetFeatureMgrViewHWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWnd.html)
