---
title: "DragCorrected Property (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "DragCorrected"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DragCorrected.html"
---

# DragCorrected Property (IDragOperator)

Gets whether or not the drag operation was corrected.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DragCorrected As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim value As System.Boolean

value = instance.DragCorrected
```

### C#

```csharp
System.bool DragCorrected {get;}
```

### C++/CLI

```cpp
property System.bool DragCorrected {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if remedial action occurred, false if not

## VBA Syntax

See [DragOperator::DragCorrected](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~DragCorrected.html).

## Remarks

If the desired orientation set by [IDragOperator::Drag](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragOperator~Drag.html) or [IDragOperator::IDrag](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragOperator~IDrag.html) was not honored and remedial action occurred, then this property is set. This property is not set by [IDragOperator::DragAsUI](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragOperator~DragAsUI.html).

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)

## Availability

SOLIDWORKS 2004 SP3, Revision Number 12.3
