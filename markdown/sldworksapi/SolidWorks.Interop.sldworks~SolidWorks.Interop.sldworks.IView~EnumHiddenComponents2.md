---
title: "EnumHiddenComponents2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "EnumHiddenComponents2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.html"
---

# EnumHiddenComponents2 Method (IView)

Gets the hidden components enumeration in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumHiddenComponents2() As EnumComponents2
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As EnumComponents2

value = instance.EnumHiddenComponents2()
```

### C#

```csharp
EnumComponents2 EnumHiddenComponents2()
```

### C++/CLI

```cpp
EnumComponents2^ EnumHiddenComponents2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Hidden component enumeration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumComponents2.html)

## VBA Syntax

See [View::EnumHiddenComponents2](ms-its:sldworksapivb6.chm::/sldworks~View~EnumHiddenComponents2.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetHiddenComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.html)
[IView::GetVisibleComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.html)
[IView::GetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.html)
[IView::IGetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
