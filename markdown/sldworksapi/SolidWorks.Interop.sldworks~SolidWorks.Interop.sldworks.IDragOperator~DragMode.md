---
title: "DragMode Property (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "DragMode"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DragMode.html"
---

# DragMode Property (IDragOperator)

Gets or sets the drag mode for this drag operation.

## Syntax

### Visual Basic (Declaration)

```vb
Property DragMode As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim value As System.Short

instance.DragMode = value

value = instance.DragMode
```

### C#

```csharp
System.short DragMode {get; set;}
```

### C++/CLI

```cpp
property System.short DragMode {
   System.short get();
   void set (    System.short value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

- 0 = Maximum move (move geometries rigidly, if possible)
- 1 = Minimum move (move the smallest number of geometries)
- 2 = Relaxation (solve geometries using relaxation)
- 3 = No propagation (move geometries with minimal transform propagation)

## VBA Syntax

See [DragOperator::DragMode](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~DragMode.html).

## Examples

[Rotate Assembly Component on Axis Using IDragOperator::Drag (VBA)](Rotate_Assembly_Component_on_Axis_Example_VB.htm)
[Rotate Assembly Component on Axis Using IDragOperator::Drag (VB.NET)](Rotate_Assembly_Component_on_Axis_Example_VBNET.htm)
[Rotate Assembly Component on Axis Using IDragOperator::Drag (C#)](Rotate_Assembly_Component_on_Axis_Example_CSharp.htm)

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
