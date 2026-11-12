---
title: "RootDrawingComponent Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "RootDrawingComponent"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~RootDrawingComponent.html"
---

# RootDrawingComponent Property (IView)

Obsolete. Superseded by [IView::RootDrawingComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~RootDrawingComponent2.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property RootDrawingComponent As DrawingComponent
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As DrawingComponent

value = instance.RootDrawingComponent
```

### C#

```csharp
DrawingComponent RootDrawingComponent {get;}
```

### C++/CLI

```cpp
property DrawingComponent^ RootDrawingComponent {
   DrawingComponent^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Drawing component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent.html)

## VBA Syntax

See [View::RootDrawingComponent](ms-its:sldworksapivb6.chm::/sldworks~View~RootDrawingComponent.html).

## Examples

[Create Section View at Specified Location (VBA)](Create_Section_View_at_Specified_Location_Example_VB.htm)
[Get Components Properties in Drawing View (VBA)](Get_Components_Properties_in_Drawing_View_Example_VB.htm)
[Hide Drawing Components (VBA)](Hide_Drawing_Components_Example_VB.htm)
[Put Assembly Components in Drawing View on Different Layers (VBA)](Put_Assembly_Components_in_Drawing_View_on_Different_Layers_Example_VB.htm)
[Get Components in Drawing View (C#)](Get_Components_in_Drawing_View_Example_CSharp.htm)
[Get Components in Drawing View (VB.NET)](Get_Components_in_Drawing_View_Example_VBNET.htm)
[Get Components in Drawing View (VBA)](Get_Components_in_Drawing_View_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
