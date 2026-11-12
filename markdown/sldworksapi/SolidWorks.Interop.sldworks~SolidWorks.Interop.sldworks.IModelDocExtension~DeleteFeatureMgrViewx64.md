---
title: "DeleteFeatureMgrViewx64 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "DeleteFeatureMgrViewx64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteFeatureMgrViewx64.html"
---

# DeleteFeatureMgrViewx64 Method (IModelDocExtension)

Removes the specified tab in the FeatureManager design tree in 64-bit applications.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DeleteFeatureMgrViewx64( _
   ByRef AppView As System.Long _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim AppView As System.Long

instance.DeleteFeatureMgrViewx64(AppView)
```

### C#

```csharp
void DeleteFeatureMgrViewx64(
   ref System.long AppView
)
```

### C++/CLI

```cpp
void DeleteFeatureMgrViewx64(
   System.int64% AppView
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppView`: View handle of the FeatureManager design tree view to delete

## VBA Syntax

See [ModelDocExtension::DeleteFeatureMgrViewx64](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~DeleteFeatureMgrViewx64.html).

## Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS Design software.

On the appropriate notification, you can call this method to clean up and delete your FeatureManager design tree view.

Use this method with [IModelViewManager::CreateFeatureMgrView2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.html) or [IModelDoc2::AddFeatureMgrView3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddFeatureMgrView3.html).

| If you created the FeatureManager design tree view using... | Then... |
| --- | --- |
| IModelViewManager::CreateFeatureMgrView2 | Calling IModelDocExtension::DeleteFeatureMgrViewx64 destroys the CView object used for the FeatureManager design tree view. |
| IModelDoc2::AddFeatureMgrView3 | Your application allocated the CView object and calling IModelDocExtension::DeleteFeatureMgrViewx64 does not destroy the CView object. In this case, you must destroy the CView object using the appropriate destructor. Never use the delete operator directly on the CView object. Always use one of the appropriate MFC view destructors. |

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IFeatMgrView::GetFeatMgrViewWndx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~GetFeatMgrViewWndx64.html)
[IModelViewManager::GetFeatureMgrViewHWndx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWndx64.html)
[IModelDoc2::DeleteFeatureMgrView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteFeatureMgrView.html)

## Availability

SOLIDWORKS 2007 SP3, Revision Number 15.3
