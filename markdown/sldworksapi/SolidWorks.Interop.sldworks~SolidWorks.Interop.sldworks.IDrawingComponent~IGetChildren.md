---
title: "IGetChildren Method (IDrawingComponent)"
project: "SOLIDWORKS API Help"
interface: "IDrawingComponent"
member: "IGetChildren"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~IGetChildren.html"
---

# IGetChildren Method (IDrawingComponent)

Gets the child components for this drawing component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetChildren( _
   ByVal Count As System.Integer _
) As DrawingComponent
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingComponent
Dim Count As System.Integer
Dim value As DrawingComponent

value = instance.IGetChildren(Count)
```

### C#

```csharp
DrawingComponent IGetChildren(
   System.int Count
)
```

### C++/CLI

```cpp
DrawingComponent^ IGetChildren(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of drawing component objects that are child components of this drawing component

### Return Value

Array of [IDrawingComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent.html) objects that are child components of the drawing component

## VBA Syntax

See [DrawingComponent::IGetChildren](ms-its:sldworksapivb6.chm::/sldworks~DrawingComponent~IGetChildren.html).

## Remarks

This method traverses the referenced component tree in a given view. Use [IDrawingComponent::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent~Visible.html) to get or set the visibility of individual components in the given view.

Before calling this method, call [IDrawingComponent::GetChildrenCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent~GetChildrenCount.html) to determine the size of the array.

## See Also

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.html)
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html)
[IDrawingComponent::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetChildren.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
