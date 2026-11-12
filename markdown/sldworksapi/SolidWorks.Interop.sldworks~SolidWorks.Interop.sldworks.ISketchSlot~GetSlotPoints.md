---
title: "GetSlotPoints Method (ISketchSlot)"
project: "SOLIDWORKS API Help"
interface: "ISketchSlot"
member: "GetSlotPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~GetSlotPoints.html"
---

# GetSlotPoints Method (ISketchSlot)

Gets the points for this slot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSlotPoints() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSlot
Dim value As System.Object

value = instance.GetSlotPoints()
```

### C#

```csharp
System.object GetSlotPoints()
```

### C++/CLI

```cpp
System.Object^ GetSlotPoints();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [sketch points](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html)

## VBA Syntax

See [SketchSlot::GetSlotPoints](ms-its:sldworksapivb6.chm::/sldworks~SketchSlot~GetSlotPoints.html).

## See Also

[ISketchSlot Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot.html)
[ISketchSlot Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot_members.html)
[ISketchSlot::CreationType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~CreationType.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
