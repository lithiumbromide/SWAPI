---
title: "GetSketchSlotCount Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSketchSlotCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSlotCount.html"
---

# GetSketchSlotCount Method (ISketch)

Gets the number of sketch slots in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchSlotCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Integer

value = instance.GetSketchSlotCount()
```

### C#

```csharp
System.int GetSketchSlotCount()
```

### C++/CLI

```cpp
System.int GetSketchSlotCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of sketch slots in this sketch

## VBA Syntax

See [Sketch::GetSketchSlotCount](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSketchSlotCount.html).

## Examples

[Get Sketch Slot Data (VBA)](Get_Sketch_Slot_Data_Example_vb.htm)

## Remarks

Call this method before calling [ISketch::IGetSketchSlots](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetSketchSlots.html) to determine the size of the array for that method.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchSlots Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSlots.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
