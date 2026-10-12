---
title: "Name Property (IDrawingComponent)"
project: "SOLIDWORKS API Help"
interface: "IDrawingComponent"
member: "Name"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Name.html"
---

# Name Property (IDrawingComponent)

Gets the name of the drawing component.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingComponent
Dim value As System.String

value = instance.Name
```

### C#

```csharp
System.string Name {get;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the drawing component

## VBA Syntax

See [DrawingComponent::Name](ms-its:sldworksapivb6.chm::/sldworks~DrawingComponent~Name.html).

## Examples

[Hide Drawing Components (VBA)](Hide_Drawing_Components_Example_VB.htm)
[Put Assembly Components in Drawing View on Different Layers (VBA)](Put_Assembly_Components_in_Drawing_View_on_Different_Layers_Example_VB.htm)

## See Also

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.html)
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
