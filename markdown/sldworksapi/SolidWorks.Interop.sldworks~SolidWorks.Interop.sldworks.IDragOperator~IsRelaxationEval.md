---
title: "IsRelaxationEval Property (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "IsRelaxationEval"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IsRelaxationEval.html"
---

# IsRelaxationEval Property (IDragOperator)

Gets or sets the relaxation evaluation.

## Syntax

### Visual Basic (Declaration)

```vb
Property IsRelaxationEval As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim value As System.Boolean

instance.IsRelaxationEval = value

value = instance.IsRelaxationEval
```

### C#

```csharp
System.bool IsRelaxationEval {get; set;}
```

### C++/CLI

```cpp
property System.bool IsRelaxationEval {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True for relaxation evaluation, false for standard evaluation

## VBA Syntax

See [DragOperator::IsRelaxationEval](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~IsRelaxationEval.html).

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
