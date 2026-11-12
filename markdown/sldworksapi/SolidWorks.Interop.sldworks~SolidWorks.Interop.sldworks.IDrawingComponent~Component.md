---
title: "Component Property (IDrawingComponent)"
project: "SOLIDWORKS API Help"
interface: "IDrawingComponent"
member: "Component"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Component.html"
---

# Component Property (IDrawingComponent)

Gets the assembly component referenced in this drawing component.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Component As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingComponent
Dim value As Component2

value = instance.Component
```

### C#

```csharp
Component2 Component {get;}
```

### C++/CLI

```cpp
property Component2^ Component {
   Component2^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Associated [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) object for the referenced assembly document

## VBA Syntax

See [DrawingComponent::Component](ms-its:sldworksapivb6.chm::/sldworks~DrawingComponent~Component.html).

## Examples

[Get Components in Drawing View (VBA)](Get_Components_in_Drawing_View_Example_VB.htm)
[Get Components in Drawing View (VB.NET)](Get_Components_in_Drawing_View_Example_VBNET.htm)
[Get Components in Drawing View (C#)](Get_Components_in_Drawing_View_Example_CSharp.htm)
[Select Drawing Component (C#)](Select_Drawing_Component_Example_CSharp.htm)
[Select Drawing Component (VB.NET)](Select_Drawing_Component_Example_VBNET.htm)
[Select Drawing Component (VBA)](Select_Drawing_Component_Example_VB.htm)

## Remarks

The associated [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) object should have the same properties as the referenced configuration. For example, if the component is suppressed in the reference configuration, then the returned component should also be suppressed.

## See Also

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.html)
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
