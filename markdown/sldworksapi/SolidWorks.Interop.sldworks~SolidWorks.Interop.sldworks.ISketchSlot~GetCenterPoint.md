---
title: "GetCenterPoint Method (ISketchSlot)"
project: "SOLIDWORKS API Help"
interface: "ISketchSlot"
member: "GetCenterPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~GetCenterPoint.html"
---

# GetCenterPoint Method (ISketchSlot)

Gets the centerpoint in this sketch slot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCenterPoint() As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSlot
Dim value As MathPoint

value = instance.GetCenterPoint()
```

### C#

```csharp
MathPoint GetCenterPoint()
```

### C++/CLI

```cpp
MathPoint^ GetCenterPoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Centerpoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)

## VBA Syntax

See [SketchSlot::GetCenterPoint](ms-its:sldworksapivb6.chm::/sldworks~SketchSlot~GetCenterPoint.html).

## Examples

[Get Sketch Slot Data (VBA)](Get_Sketch_Slot_Data_Example_vb.htm)

## See Also

[ISketchSlot Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot.html)
[ISketchSlot Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot_members.html)
[ISketchSlot::GetCenterPointHandle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~GetCenterPointHandle.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
