---
title: "IsRoot Method (IDrawingComponent)"
project: "SOLIDWORKS API Help"
interface: "IDrawingComponent"
member: "IsRoot"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~IsRoot.html"
---

# IsRoot Method (IDrawingComponent)

Gets whether this is the root drawing component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsRoot() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingComponent
Dim value As System.Boolean

value = instance.IsRoot()
```

### C#

```csharp
System.bool IsRoot()
```

### C++/CLI

```cpp
System.bool IsRoot();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this component is the root drawing component, false if not

## VBA Syntax

See [DrawingComponent::IsRoot](ms-its:sldworksapivb6.chm::/sldworks~DrawingComponent~IsRoot.html).

## Examples

[Get Components' Properties in Drawing View (VBA)](Get_Components_Properties_in_Drawing_View_Example_VB.htm)

## Remarks

This method assists with traversal.

## See Also

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.html)
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
