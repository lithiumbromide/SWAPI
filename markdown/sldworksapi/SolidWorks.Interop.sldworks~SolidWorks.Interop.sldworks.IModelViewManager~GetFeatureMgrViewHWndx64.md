---
title: "GetFeatureMgrViewHWndx64 Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "GetFeatureMgrViewHWndx64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWndx64.html"
---

# GetFeatureMgrViewHWndx64 Method (IModelViewManager)

Gets the window handle for the specified FeatureManager design tree view in 64-bit applications.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureMgrViewHWndx64( _
   ByVal FeatMgrViewPane As System.Integer _
) As System.Long
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim FeatMgrViewPane As System.Integer
Dim value As System.Long

value = instance.GetFeatureMgrViewHWndx64(FeatMgrViewPane)
```

### C#

```csharp
System.long GetFeatureMgrViewHWndx64(
   System.int FeatMgrViewPane
)
```

### C++/CLI

```cpp
System.int64 GetFeatureMgrViewHWndx64(
   System.int FeatMgrViewPane
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FeatMgrViewPane`: FeatureManager design tree view as defined by [swFeatMgrPane_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

### Return Value

Window handle for the specified FeatMgrViewPane

## Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS Design software.

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.html)
[IModelViewManager::GetFeatureMgrViewHWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWnd.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
