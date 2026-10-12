---
title: "IGetControl Method (IFeatMgrView)"
project: "SOLIDWORKS API Help"
interface: "IFeatMgrView"
member: "IGetControl"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~IGetControl.html"
---

# IGetControl Method (IFeatMgrView)

Gets the control associated with this FeatureManager design tree view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetControl() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatMgrView
Dim value As System.Object

value = instance.IGetControl()
```

### C#

```csharp
System.object IGetControl()
```

### C++/CLI

```cpp
System.Object^ IGetControl();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the associated control

## VBA Syntax

See [FeatMgrView::IGetControl](ms-its:sldworksapivb6.chm::/sldworks~FeatMgrView~IGetControl.html).

## See Also

[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.html)
[IFeatMgrView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView_members.html)
[IFeatMgrView::GetControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~GetControl.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
