---
title: "GetVisibleComponents Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetVisibleComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponents.html"
---

# GetVisibleComponents Method (IView)

Gets the visible components in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVisibleComponents() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetVisibleComponents()
```

### C#

```csharp
System.object GetVisibleComponents()
```

### C++/CLI

```cpp
System.Object^ GetVisibleComponents();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Visible [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) in this drawing view

## VBA Syntax

See [View::GetVisibleComponents](ms-its:sldworksapivb6.chm::/sldworks~View~GetVisibleComponents.html).

## Examples

[Get All Edges in Visible Component in Drawing View (VBA)](Get_All_Edges_in_Visible_Component_in_Drawing_View_Example_VB.htm)
[Get All Visible Components in Drawing View (VBA)](Get_All_Visible_Components_in_Drawing_View_Example_VB.htm)
[Get Visible Components and Entities in Drawing View (VBA)](Get_Visible_Components_and_Entities_in_Drawing_View_Example_VB.htm)

## Remarks

Visible components are components not completely obscured by other components in the view.

NOTE: This method does not retrieve a complete component object. For example, the component returned by this method does not support [IComponent2::GetBodies3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies3.html) (returns null). To retrieve a visible component that fully supports [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html) methods and properties, call:

1. [IView::GetVisibleDrawingComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleDrawingComponents.html)
2. [IDrawingComponent::Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Component.html)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetVisibleComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleComponentCount.html)
[IView::GetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities.html)
[IView::GetVisibleEntityCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntityCount.html)
[IView::IGetVisibleComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleComponents.html)
[IView::IGetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleEntities.html)
[IView::GetHiddenComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetHiddenComponents.html)
[IView::EnumHiddenComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumHiddenComponents2.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
