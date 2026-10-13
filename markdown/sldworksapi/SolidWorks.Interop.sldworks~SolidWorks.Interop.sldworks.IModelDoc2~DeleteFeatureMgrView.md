---
title: "DeleteFeatureMgrView Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "DeleteFeatureMgrView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteFeatureMgrView.html"
---

# DeleteFeatureMgrView Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::DeleteFeatureMgrViewx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteFeatureMgrViewx64.html).

This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016.

The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used.

Removes the specified tab in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DeleteFeatureMgrView( _
   ByRef AppView As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim AppView As System.Integer

instance.DeleteFeatureMgrView(AppView)
```

### C#

```csharp
void DeleteFeatureMgrView(
   ref System.int AppView
)
```

### C++/CLI

```cpp
void DeleteFeatureMgrView(
   System.int% AppView
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppView`: View handle of the FeatureManager design tree view to delete

## VBA Syntax

See [ModelDoc2::DeleteFeatureMgrView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~DeleteFeatureMgrView.html).

## Remarks

**All applications are required to be compatible with SOLIDWORKS x64. You must replace all calls to 32-bit only APIs with calls to their 64-bit safe counterparts.**

See [Eliminating 32-bit only API use](sldworksapiprogguide.chm::/Overview/Eliminating_32-Bit_Only_API_Use.htm) for more information.

On the appropriate notification, you can call this method to clean up and delete your FeatureManager design tree view.

Use this method with [IModelViewManager::CreateFeatureMgrView2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.html) or [IModelDoc2::AddFeatureMgrView3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddFeatureMgrView3.html).

| If you created the FeatureManager design tree view using... | Then... |
| --- | --- |
| IModelViewManager::CreateFeatureMgrView2 | Calling IModelDoc2::DeleteFeatureMgrView destroys the CView object used for the FeatureManager design tree view. |
| IModelDoc2::AddFeatureMgrView3 | Your application allocated the CView object and calling IModelDoc2::DeleteFeatureMgrView does not destroy the CView object. In this case, you must destroy the CVew object using the appropriate destructor. Never use the delete operator directly on the CView object. Always use one of the appropriate MFC view destructors. |

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
