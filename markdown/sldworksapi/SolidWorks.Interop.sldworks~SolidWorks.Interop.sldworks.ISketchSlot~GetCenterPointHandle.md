---
title: "GetCenterPointHandle Method (ISketchSlot)"
project: "SOLIDWORKS API Help"
interface: "ISketchSlot"
member: "GetCenterPointHandle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~GetCenterPointHandle.html"
---

# GetCenterPointHandle Method (ISketchSlot)

Gets the sketch point representing the centerpoint of the sketch slot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCenterPointHandle() As SketchPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSlot
Dim value As SketchPoint

value = instance.GetCenterPointHandle()
```

### C#

```csharp
SketchPoint GetCenterPointHandle()
```

### C++/CLI

```cpp
SketchPoint^ GetCenterPointHandle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html)

## VBA Syntax

See [SketchSlot::GetCenterPointHandle](ms-its:sldworksapivb6.chm::/sldworks~SketchSlot~GetCenterPointHandle.html).

## Examples

[Get Sketch Slot Data (VBA)](Get_Sketch_Slot_Data_Example_vb.htm)

## See Also

[ISketchSlot Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot.html)
[ISketchSlot Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot_members.html)
[ISketchSlot::GetCenterPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~GetCenterPoint.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
