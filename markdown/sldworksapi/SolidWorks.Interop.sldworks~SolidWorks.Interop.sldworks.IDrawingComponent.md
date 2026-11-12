---
title: "IDrawingComponent Interface"
project: "SOLIDWORKS API Help"
interface: "IDrawingComponent"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.html"
---

# IDrawingComponent Interface

Represents the referenced component in a drawing view.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IDrawingComponent
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingComponent
```

### C#

```csharp
public interface IDrawingComponent
```

### C++/CLI

```cpp
public interface class IDrawingComponent
```

## VBA Syntax

See [DrawingComponent](ms-its:sldworksapivb6.chm::/sldworks~DrawingComponent.html).

## Examples

[Get Components in Drawing View (VBA)](Get_Components_in_Drawing_View_Example_VB.htm)
[Get Components in Drawing View (VB.NET)](Get_Components_in_Drawing_View_Example_VBNET.htm)
[Get Components in Drawing View (C#)](Get_Components_in_Drawing_View_Example_CSharp.htm)
[Select Drawing Component (C#)](Select_Drawing_Component_Example_CSharp.htm)
[Select Drawing Component (VB.NET)](Select_Drawing_Component_Example_VBNET.htm)
[Select Drawing Component (VBA)](Select_Drawing_Component_Example_VB.htm)

## Remarks

This object ties the [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) object of the [IAssemblyDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc.html) object with the [IView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) object of the [IDrawingDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc.html) object. This functionality allows an application to manipulate the drawing-related settings of a referenced component without having to preselect that component.

## Accessors

[IComponent2::GetDrawingComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetDrawingComponent.html)

[IDrawingComponent::GetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent~GetChildren.html) and [IDrawingComponent::IGetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent~IGetChildren.html)

[IEntity::GetDrawingComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity~GetDrawingComponent.html)

[ISelectionMgr::GetSelectedObjectsComponent4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent4.html)

[IView::GetVisibleDrawingComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleDrawingComponents.html)

[IView::RootDrawingComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~RootDrawingComponent.html)

## Access Diagram

[DrawingComponent](SWObjectModel.pdf#DrawingComponent)

## See Also

[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
