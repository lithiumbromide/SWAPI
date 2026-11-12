---
title: "GetChildren Method (IDrawingComponent)"
project: "SOLIDWORKS API Help"
interface: "IDrawingComponent"
member: "GetChildren"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetChildren.html"
---

# GetChildren Method (IDrawingComponent)

Gets the child components for this drawing component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetChildren() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingComponent
Dim value As System.Object

value = instance.GetChildren()
```

### C#

```csharp
System.object GetChildren()
```

### C++/CLI

```cpp
System.Object^ GetChildren();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IDrawingComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent.html) objects that are child components of the drawing component

## VBA Syntax

See [DrawingComponent::GetChildren](ms-its:sldworksapivb6.chm::/sldworks~DrawingComponent~GetChildren.html).

## Examples

[Create Section View at Specified Location (VBA)](Create_Section_View_at_Specified_Location_Example_VB.htm)
[Get Components' Properties in Drawing View (VBA)](Get_Components_Properties_in_Drawing_View_Example_VB.htm)
[Hide Drawing Components (VBA)](Hide_Drawing_Components_Example_VB.htm)
[Put Assembly Components in Drawing View on Different Layers (VBA)](Put_Assembly_Components_in_Drawing_View_on_Different_Layers_Example_VB.htm)
[Get Components in Drawing View (C#)](Get_Components_in_Drawing_View_Example_CSharp.htm)
[Get Components in Drawing View (VB.NET)](Get_Components_in_Drawing_View_Example_VBNET.htm)
[Get Components in Drawing View (VBA)](Get_Components_in_Drawing_View_Example_VB.htm)

## Remarks

This method traverses the referenced component tree in a given view. Use [IDrawingComponent::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent~Visible.html) to get or set the visibility of individual components in the given view.

## See Also

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.html)
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html)
[IDrawingComponent::GetChildrenCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetChildrenCount.html)
[IDrawingComponent::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~IGetChildren.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
