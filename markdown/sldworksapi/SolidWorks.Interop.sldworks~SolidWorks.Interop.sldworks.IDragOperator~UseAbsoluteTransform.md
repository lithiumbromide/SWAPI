---
title: "UseAbsoluteTransform Property (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "UseAbsoluteTransform"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~UseAbsoluteTransform.html"
---

# UseAbsoluteTransform Property (IDragOperator)

Gets or sets whether the transforms to use with [IDragOperator::Drag](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragOperator~Drag.html) or [IDragOperator::IDrag](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragOperator~IDrag.html) are absolute or relative.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseAbsoluteTransform As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim value As System.Boolean

instance.UseAbsoluteTransform = value

value = instance.UseAbsoluteTransform
```

### C#

```csharp
System.bool UseAbsoluteTransform {get; set;}
```

### C++/CLI

```cpp
property System.bool UseAbsoluteTransform {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use absolute transforms, false to use relative transforms

## VBA Syntax

See [DragOperator::UseAbsoluteTransform](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~UseAbsoluteTransform.html).

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::TransformType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~TransformType.html)

## Availability

SOLIDWORKS 2004 SP3, Revision Number 12.3
