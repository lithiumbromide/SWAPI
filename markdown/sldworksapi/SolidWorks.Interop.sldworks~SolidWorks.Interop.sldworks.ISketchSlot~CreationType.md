---
title: "CreationType Property (ISketchSlot)"
project: "SOLIDWORKS API Help"
interface: "ISketchSlot"
member: "CreationType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~CreationType.html"
---

# CreationType Property (ISketchSlot)

Gets the type of slot.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CreationType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSlot
Dim value As System.Integer

value = instance.CreationType
```

### C#

```csharp
System.int CreationType {get;}
```

### C++/CLI

```cpp
property System.int CreationType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of slot as defined in [swSketchSlotCreationType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchSlotCreationType_e.html)

**NOTE:** Only swSketchSlotCreateType_line or swSketchSlotCreateType_arc are valid return values.

## VBA Syntax

See [SketchSlot::CreationType](ms-its:sldworksapivb6.chm::/sldworks~SketchSlot~CreationType.html).

## See Also

[ISketchSlot Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot.html)
[ISketchSlot Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
