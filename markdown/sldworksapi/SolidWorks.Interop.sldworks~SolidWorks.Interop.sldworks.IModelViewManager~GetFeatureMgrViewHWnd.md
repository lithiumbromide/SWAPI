---
title: "GetFeatureMgrViewHWnd Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "GetFeatureMgrViewHWnd"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWnd.html"
---

# GetFeatureMgrViewHWnd Method (IModelViewManager)

Obsolete. Superseded by [IModelViewManager::GetFeatureMgrViewHWndx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWndx64.html).

This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016.

The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used.

Gets the window handle for the specified FeatureManager design tree view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureMgrViewHWnd( _
   ByVal FeatMgrViewPane As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim FeatMgrViewPane As System.Integer
Dim value As System.Integer

value = instance.GetFeatureMgrViewHWnd(FeatMgrViewPane)
```

### C#

```csharp
System.int GetFeatureMgrViewHWnd(
   System.int FeatMgrViewPane
)
```

### C++/CLI

```cpp
System.int GetFeatureMgrViewHWnd(
   System.int FeatMgrViewPane
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FeatMgrViewPane`: FeatureManager design tree view as defined by [swFeatMgrPane_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

### Return Value

Window handle for the specified FeatMgrViewPane

## VBA Syntax

See [ModelViewManager::GetFeatureMgrViewHWnd](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~GetFeatureMgrViewHWnd.html).

## Remarks

**All applications are required to be compatible with SOLIDWORKS x64. You must replace all calls to 32-bit only APIs with calls to their 64-bit safe counterparts.**

See [Eliminating 32-bit only API use](sldworksapiprogguide.chm::/Overview/Eliminating_32-Bit_Only_API_Use.htm) for more information.

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
