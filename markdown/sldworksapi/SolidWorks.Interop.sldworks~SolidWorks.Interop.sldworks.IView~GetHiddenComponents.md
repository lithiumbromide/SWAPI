---
title: "GetHiddenComponents Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetHiddenComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.html"
---

# GetHiddenComponents Method (IView)

Gets the hidden components in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHiddenComponents() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetHiddenComponents()
```

### C#

```csharp
System.object GetHiddenComponents()
```

### C++/CLI

```cpp
System.Object^ GetHiddenComponents();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of hidden components

## VBA Syntax

See [View::GetHiddenComponents](ms-its:sldworksapivb6.chm::/sldworks~View~GetHiddenComponents.html).

## Examples

[Get Components Hidden in Drawing View (VBA)](Get_Components_Hidden_In_Drawing_View_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::EnumHiddenComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.html)
[IView::GetVisibleComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.html)
[IView::GetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.html)
[IView::IGetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
