---
title: "DeActivateView Method (IFeatMgrView)"
project: "SOLIDWORKS API Help"
interface: "IFeatMgrView"
member: "DeActivateView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~DeActivateView.html"
---

# DeActivateView Method (IFeatMgrView)

Deactivates this view in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeActivateView() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatMgrView
Dim value As System.Boolean

value = instance.DeActivateView()
```

### C#

```csharp
System.bool DeActivateView()
```

### C++/CLI

```cpp
System.bool DeActivateView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the tab is deactivated, false if not

## VBA Syntax

See [FeatMgrView::DeActivateView](ms-its:sldworksapivb6.chm::/sldworks~FeatMgrView~DeActivateView.html).

## See Also

[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.html)
[IFeatMgrView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView_members.html)
[IFeatMgrView::ActivateView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~ActivateView.html)
[IFeatMgrView::DeleteView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~DeleteView.html)
[IModelDocExtension::DeActivateFeatureMgrViewx64 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeActivateFeatureMgrViewx64.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
