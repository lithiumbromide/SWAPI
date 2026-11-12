---
title: "IsDragSpecific Property (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "IsDragSpecific"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IsDragSpecific.html"
---

# IsDragSpecific Property (IDragOperator)

Gets or sets the drag-specific setting.

## Syntax

### Visual Basic (Declaration)

```vb
Property IsDragSpecific As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim value As System.Boolean

instance.IsDragSpecific = value

value = instance.IsDragSpecific
```

### C#

```csharp
System.bool IsDragSpecific {get; set;}
```

### C++/CLI

```cpp
property System.bool IsDragSpecific {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True sets drag specific, false sets drag possible

## VBA Syntax

See [DragOperator::IsDragSpecific](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~IsDragSpecific.html).

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
