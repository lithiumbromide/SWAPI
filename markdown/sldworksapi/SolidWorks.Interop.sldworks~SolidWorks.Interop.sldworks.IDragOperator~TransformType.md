---
title: "TransformType Property (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "TransformType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~TransformType.html"
---

# TransformType Property (IDragOperator)

Gets or sets the type of transformation.

## Syntax

### Visual Basic (Declaration)

```vb
Property TransformType As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim value As System.Short

instance.TransformType = value

value = instance.TransformType
```

### C#

```csharp
System.short TransformType {get; set;}
```

### C++/CLI

```cpp
property System.short TransformType {
   System.short get();
   void set (    System.short value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

| Translation | 0 | Transform is translation only |
| --- | --- | --- |
| Axial Rotation | 1 | Transform is rotation only |
| General | 2 | Transform can be translation or rotation or both |

## VBA Syntax

See [DragOperator::TransformType](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~TransformType.html).

## Examples

[Rotate Assembly Component on Axis Using IDragOperator::Drag (VBA)](Rotate_Assembly_Component_on_Axis_Example_VB.htm)
[Rotate Assembly Component on Axis Using IDragOperator::Drag (VB.NET)](Rotate_Assembly_Component_on_Axis_Example_VBNET.htm)
[Rotate Assembly Component on Axis Using IDragOperator::Drag (C#)](Rotate_Assembly_Component_on_Axis_Example_CSharp.htm)
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VBA)](Rotate_Assembly_Component_on_Axis_Example2_VB.htm)
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VB.NET)](Rotate_Assembly_Component_on_Axis_Example2_VBNET.htm)
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (C#)](Rotate_Assembly_Component_on_Axis_Example2_CSharp.htm)

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::UseAbsoluteTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~UseAbsoluteTransform.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
