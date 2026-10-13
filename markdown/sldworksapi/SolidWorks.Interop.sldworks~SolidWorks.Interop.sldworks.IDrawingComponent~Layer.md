---
title: "Layer Property (IDrawingComponent)"
project: "SOLIDWORKS API Help"
interface: "IDrawingComponent"
member: "Layer"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Layer.html"
---

# Layer Property (IDrawingComponent)

Gets or sets the name of the layer on which the component resides in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Property Layer As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingComponent
Dim value As System.String

instance.Layer = value

value = instance.Layer
```

### C#

```csharp
System.string Layer {get; set;}
```

### C++/CLI

```cpp
property System.String^ Layer {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the layer on which this component resides

## VBA Syntax

See [DrawingComponent::Layer](ms-its:sldworksapivb6.chm::/sldworks~DrawingComponent~Layer.html).

## Remarks

| If you specify... | Then... |
| --- | --- |
| Empty string | Name of the component's layer is set to None or to the name of the default layer. |
| Name of an existing layer | Component is placed on that layer. |
| Name of a non-existent layer | Layer does not change. |

If the drawing component is an assembly:

- you can set the layer, and the layers of child drawing components will also be set.
- the query returns an empty string because the layer is uniquely defined in case child
  drawing components reside on different layers.

## See Also

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.html)
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html)
[IDrawingComponent::Layer Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Layer.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
