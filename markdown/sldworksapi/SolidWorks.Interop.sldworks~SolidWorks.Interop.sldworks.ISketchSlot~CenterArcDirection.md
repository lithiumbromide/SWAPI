---
title: "CenterArcDirection Property (ISketchSlot)"
project: "SOLIDWORKS API Help"
interface: "ISketchSlot"
member: "CenterArcDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~CenterArcDirection.html"
---

# CenterArcDirection Property (ISketchSlot)

Gets the direction of the slot.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CenterArcDirection As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSlot
Dim value As System.Integer

value = instance.CenterArcDirection
```

### C#

```csharp
System.int CenterArcDirection {get;}
```

### C++/CLI

```cpp
property System.int CenterArcDirection {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

-1 for clockwise, 1 for counter-clockwise

## VBA Syntax

See [SketchSlot::CenterArcDirection](ms-its:sldworksapivb6.chm::/sldworks~SketchSlot~CenterArcDirection.html).

## See Also

[ISketchSlot Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot.html)
[ISketchSlot Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot_members.html)
[ISketchSlot::CreationType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~CreationType.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
