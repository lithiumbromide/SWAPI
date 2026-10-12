---
title: "DeleteView Method (IFeatMgrView)"
project: "SOLIDWORKS API Help"
interface: "IFeatMgrView"
member: "DeleteView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~DeleteView.html"
---

# DeleteView Method (IFeatMgrView)

Removes this view from the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteView() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatMgrView
Dim value As System.Boolean

value = instance.DeleteView()
```

### C#

```csharp
System.bool DeleteView()
```

### C++/CLI

```cpp
System.bool DeleteView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the tab is deleted, false if not

## VBA Syntax

See [FeatMgrView::DeleteView](ms-its:sldworksapivb6.chm::/sldworks~FeatMgrView~DeleteView.html).

## Remarks

Use this method to delete a tab created by [IModelViewManager::AddControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~AddControl.html).

## See Also

[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.html)
[IFeatMgrView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView_members.html)
[IFeatMgrView::ActivateView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~ActivateView.html)
[IFeatMgrView::DeActivateView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~DeActivateView.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
