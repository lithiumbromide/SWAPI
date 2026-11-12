---
title: "GetSketchSlots Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSketchSlots"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSlots.html"
---

# GetSketchSlots Method (ISketch)

Gets the sketch slots in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchSlots() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim value As System.Object

value = instance.GetSketchSlots()
```

### C#

```csharp
System.object GetSketchSlots()
```

### C++/CLI

```cpp
System.Object^ GetSketchSlots();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [sketch slots](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSlot.html)

## VBA Syntax

See [Sketch::GetSketchSlots](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSketchSlots.html).

## Examples

[Get Sketch Slot Data (VBA)](Get_Sketch_Slot_Data_Example_vb.htm)

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::IGetSketchSlots Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchSlots.html)
[ISketch::GetSketchSlotCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSlotCount.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
