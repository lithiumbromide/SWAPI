---
title: "Width Property (IDrawingComponent)"
project: "SOLIDWORKS API Help"
interface: "IDrawingComponent"
member: "Width"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Width.html"
---

# Width Property (IDrawingComponent)

Gets or sets the width of the line for this component for this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Property Width As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingComponent
Dim value As System.Integer

instance.Width = value

value = instance.Width
```

### C#

```csharp
System.int Width {get; set;}
```

### C++/CLI

```cpp
property System.int Width {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Line width as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

## VBA Syntax

See [DrawingComponent::Width](ms-its:sldworksapivb6.chm::/sldworks~DrawingComponent~Width.html).

## Examples

[Get Components' Properties in Drawing View (VBA)](Get_Components_Properties_in_Drawing_View_Example_VB.htm)

## Remarks

Use [IDrawingComponent::LayerOverride](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent~LayerOverride.html) to determine if this component is using its default
layer line width.

## See Also

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.html)
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html)
[IDrawingComponent::Style Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Style.html)
[IDrawingComponent::Layer Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Layer.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
