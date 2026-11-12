---
title: "Visible Property (IDrawingComponent)"
project: "SOLIDWORKS API Help"
interface: "IDrawingComponent"
member: "Visible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Visible.html"
---

# Visible Property (IDrawingComponent)

Gets or sets the visibility state for this component for this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Property Visible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingComponent
Dim value As System.Boolean

instance.Visible = value

value = instance.Visible
```

### C#

```csharp
System.bool Visible {get; set;}
```

### C++/CLI

```cpp
property System.bool Visible {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the component is visible, false if hidden

## VBA Syntax

See [DrawingComponent::Visible](ms-its:sldworksapivb6.chm::/sldworks~DrawingComponent~Visible.html).

## Examples

[Get Components' Properties in Drawing View (VBA)](Get_Components_Properties_in_Drawing_View_Example_VB.htm)
[Hide Drawing Components (VBA)](Hide_Drawing_Components_Example_VB.htm)

## Remarks

Call the [IModelDoc2::Rebuild](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Rebuild.html) after setting this method.

## See Also

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.html)
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
