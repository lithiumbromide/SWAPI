---
title: "GetDrawingComponent Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetDrawingComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetDrawingComponent.html"
---

# GetDrawingComponent Method (IComponent2)

Gets the drawing component for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDrawingComponent( _
   ByVal ViewIn As View _
) As DrawingComponent
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim ViewIn As View
Dim value As DrawingComponent

value = instance.GetDrawingComponent(ViewIn)
```

### C#

```csharp
DrawingComponent GetDrawingComponent(
   View ViewIn
)
```

### C++/CLI

```cpp
DrawingComponent^ GetDrawingComponent(
   View^ ViewIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewIn`: Pointer to [view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) from which to get the drawing component

### Return Value

Pointer to the [IDrawingComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent.html) object

## VBA Syntax

See [Component2::GetDrawingComponent](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetDrawingComponent.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
