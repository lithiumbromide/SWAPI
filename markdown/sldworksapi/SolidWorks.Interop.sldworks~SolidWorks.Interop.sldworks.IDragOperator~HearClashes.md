---
title: "HearClashes Property (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "HearClashes"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~HearClashes.html"
---

# HearClashes Property (IDragOperator)

Gets or sets whether sound is associated with entity clashes.

## Syntax

### Visual Basic (Declaration)

```vb
Property HearClashes As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim value As System.Boolean

instance.HearClashes = value

value = instance.HearClashes
```

### C#

```csharp
System.bool HearClashes {get; set;}
```

### C++/CLI

```cpp
property System.bool HearClashes {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the sound for clashes is enabled, false if it is disabled

## VBA Syntax

See [DragOperator::HearClashes](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~HearClashes.html).

## Remarks

This property enables audio feedback when collisions occur between components selected for collision detection.

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::HighlightClashes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~HighlightClashes.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
