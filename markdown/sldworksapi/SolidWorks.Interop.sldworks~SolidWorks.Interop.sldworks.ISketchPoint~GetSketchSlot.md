---
title: "GetSketchSlot Method (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "GetSketchSlot"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetSketchSlot.html"
---

# GetSketchSlot Method (ISketchPoint)

Gets sketch slot with which this sketch point is associated.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchSlot() As SketchSlot
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
Dim value As SketchSlot

value = instance.GetSketchSlot()
```

### C#

```csharp
SketchSlot GetSketchSlot()
```

### C++/CLI

```cpp
SketchSlot^ GetSketchSlot();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sketch slot](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSlot.html) if the sketch point is associated with a sketch slot, or null if the sketch point is not associated with a sketch slot

## VBA Syntax

See [SketchPoint::GetSketchSlot](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint~GetSketchSlot.html).

## Examples

[Get Sketch Slot Using Sketch Point and Segment (C#)](Get_Sketch_Slot_Using_Sketch_Point_and_Segment_Example_CSharp.htm)
[Get Sketch Slot Using Sketch Point and Segment (VB.NET)](Get_Sketch_Slot_Using_Sketch_Point_and_Segment_Example_VBNET.htm)
[Get Sketch Slot Using Sketch Point and Segment (VBA)](Get_Sketch_Slot_Using_Sketch_Point_and_Segment_Example_VB.htm)

## Remarks

Sketch slot information is independent of the sketch point type.

A sketch slot is returned if it is associated with the sketch point regardless if the sketch point is an internal point or a user point.

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
