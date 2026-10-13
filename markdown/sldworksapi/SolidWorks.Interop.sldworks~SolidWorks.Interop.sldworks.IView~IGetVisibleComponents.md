---
title: "IGetVisibleComponents Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetVisibleComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.html"
---

# IGetVisibleComponents Method (IView)

Gets the visible components in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetVisibleComponents( _
   ByVal ViewComponentCount As System.Integer _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim ViewComponentCount As System.Integer
Dim value As Component2

value = instance.IGetVisibleComponents(ViewComponentCount)
```

### C#

```csharp
Component2 IGetVisibleComponents(
   System.int ViewComponentCount
)
```

### C++/CLI

```cpp
Component2^ IGetVisibleComponents(
   System.int ViewComponentCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewComponentCount`: Number of visible components

### Return Value

Visible [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) in this drawing view

## VBA Syntax

See [View::IGetVisibleComponents](ms-its:sldworksapivb6.chm::/sldworks~View~IGetVisibleComponents.html).

## Remarks

Visible components are only those components not completely obscured by other components in the view.

Call [IView::GetVisibleComponentCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetVisibleComponentCount.html) before calling this method to get the value of ViewComponentCount.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::EnumHiddenComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.html)
[IView::GetHiddenComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.html)
[IView::GetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.html)
[IView::GetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities.html)
[IView::GetVisibleEntityCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntityCount.html)
[IView::IGetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleEntities.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
