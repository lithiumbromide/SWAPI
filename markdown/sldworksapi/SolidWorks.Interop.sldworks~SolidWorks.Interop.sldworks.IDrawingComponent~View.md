---
title: "View Property (IDrawingComponent)"
project: "SOLIDWORKS API Help"
interface: "IDrawingComponent"
member: "View"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~View.html"
---

# View Property (IDrawingComponent)

Gets the drawing view on which this component resides.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property View As View
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingComponent
Dim value As View

value = instance.View
```

### C#

```csharp
View View {get;}
```

### C++/CLI

```cpp
property View^ View {
   View^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the [IView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) object on which this component resides

## VBA Syntax

See [DrawingComponent::View](ms-its:sldworksapivb6.chm::/sldworks~DrawingComponent~View.html).

## See Also

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.html)
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
