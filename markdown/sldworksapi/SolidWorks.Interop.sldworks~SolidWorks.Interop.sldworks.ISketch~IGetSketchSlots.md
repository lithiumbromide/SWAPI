---
title: "IGetSketchSlots Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "IGetSketchSlots"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchSlots.html"
---

# IGetSketchSlots Method (ISketch)

Gets the sketch slots in this sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSketchSlots( _
   ByVal Count As System.Integer _
) As SketchSlot
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim Count As System.Integer
Dim value As SketchSlot

value = instance.IGetSketchSlots(Count)
```

### C#

```csharp
SketchSlot IGetSketchSlots(
   System.int Count
)
```

### C++/CLI

```cpp
SketchSlot^ IGetSketchSlots(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of sketch slots in this sketch

### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch slots](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSlot.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling htis method, call [ISketch::GetSketchSlotCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSketchSlotCount.html) to get Count.

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSketchSlots Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSlots.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
