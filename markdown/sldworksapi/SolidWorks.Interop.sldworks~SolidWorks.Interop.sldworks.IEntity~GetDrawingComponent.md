---
title: "GetDrawingComponent Method (IEntity)"
project: "SOLIDWORKS API Help"
interface: "IEntity"
member: "GetDrawingComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetDrawingComponent.html"
---

# GetDrawingComponent Method (IEntity)

Gets the drawing component that owns this entity, if the entity is in a drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDrawingComponent( _
   ByVal View As View _
) As DrawingComponent
```

### Visual Basic (Usage)

```vb
Dim instance As IEntity
Dim View As View
Dim value As DrawingComponent

value = instance.GetDrawingComponent(View)
```

### C#

```csharp
DrawingComponent GetDrawingComponent(
   View View
)
```

### C++/CLI

```cpp
DrawingComponent^ GetDrawingComponent(
   View^ View
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `View`: Name of the drawing view in which the entity resides

### Return Value

[IDrawingComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingComponent.html) object that owns the entity

## VBA Syntax

See [Entity::GetDrawingComponent](ms-its:sldworksapivb6.chm::/sldworks~Entity~GetDrawingComponent.html).

## Remarks

If the drawing component is a child component of the referenced assembly, then the drawing component should be a child drawing component in the drawing component configuration in the FeatureManager design tree.

If the entity is in the view, then the drawing component is returned. If the entity is not in the view, then NULL is returned.

## See Also

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.html)
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
