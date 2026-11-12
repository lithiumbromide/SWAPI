---
title: "HighlightClashes Property (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "HighlightClashes"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~HighlightClashes.html"
---

# HighlightClashes Property (IDragOperator)

Gets or sets whether to highlight clashes.

## Syntax

### Visual Basic (Declaration)

```vb
Property HighlightClashes As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim value As System.Boolean

instance.HighlightClashes = value

value = instance.HighlightClashes
```

### C#

```csharp
System.bool HighlightClashes {get; set;}
```

### C++/CLI

```cpp
property System.bool HighlightClashes {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if clash highlighting is enabled, false if it is disabled

## VBA Syntax

See [DragOperator::HighlightClashes](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~HighlightClashes.html).

## Remarks

This property enables visual feedback when collisions occur between components selected for collision detection.

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::HearClashes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~HearClashes.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
