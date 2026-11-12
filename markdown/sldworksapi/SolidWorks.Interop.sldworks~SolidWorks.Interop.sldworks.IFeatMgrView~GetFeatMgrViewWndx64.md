---
title: "GetFeatMgrViewWndx64 Method (IFeatMgrView)"
project: "SOLIDWORKS API Help"
interface: "IFeatMgrView"
member: "GetFeatMgrViewWndx64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~GetFeatMgrViewWndx64.html"
---

# GetFeatMgrViewWndx64 Method (IFeatMgrView)

Gets the FeatureManager design tree view window handle as a CWnd object in 64-bit applications.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatMgrViewWndx64() As System.Long
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatMgrView
Dim value As System.Long

value = instance.GetFeatMgrViewWndx64()
```

### C#

```csharp
System.long GetFeatMgrViewWndx64()
```

### C++/CLI

```cpp
System.int64 GetFeatMgrViewWndx64();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Window handle for this FeatureManager design tree view

## VBA Syntax

See [FeatMgrView::GetFeatMgrViewWndx64](ms-its:sldworksapivb6.chm::/sldworks~FeatMgrView~GetFeatMgrViewWndx64.html).

## Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS Design software.

## See Also

[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.html)
[IFeatMgrView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView_members.html)
[IFeatMgrView::GetFeatMgrViewWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~GetFeatMgrViewWnd.html)
[IModelViewManager::GetFeatureMgrViewHWndx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWndx64.html)

## Availability

SOLIDWORKS 2006 SP3, Revision Number 14.3
