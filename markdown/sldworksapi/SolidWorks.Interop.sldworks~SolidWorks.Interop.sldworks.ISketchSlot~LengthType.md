---
title: "LengthType Property (ISketchSlot)"
project: "SOLIDWORKS API Help"
interface: "ISketchSlot"
member: "LengthType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~LengthType.html"
---

# LengthType Property (ISketchSlot)

Gets or sets the type of length of this sketch slot.

## Syntax

### Visual Basic (Declaration)

```vb
Property LengthType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSlot
Dim value As System.Integer

instance.LengthType = value

value = instance.LengthType
```

### C#

```csharp
System.int LengthType {get; set;}
```

### C++/CLI

```cpp
property System.int LengthType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of length of this sketch slot as defined in [swSketchSlotLengthType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchSlotLengthType_e.html)

## VBA Syntax

See [SketchSlot::LengthType](ms-its:sldworksapivb6.chm::/sldworks~SketchSlot~LengthType.html).

## Examples

[Insert and Resize Sketch Slot (C#)](Insert_and_Resize_Sketch_Slot_Example_CSharp.htm)
[Insert and Resize Sketch Slot (VB.NET)](Insert_and_Resize_Sketch_Slot_Example_VBNET.htm)
[Insert and Resize Sketch Slot (VBA)](Insert_and_Resize_Sketch_Slot_Example_VB.htm)
[Get Sketch Slot Data (VBA)](Get_Sketch_Slot_Data_Example_vb.htm)

## See Also

[ISketchSlot Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot.html)
[ISketchSlot Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot_members.html)
[ISketchSlot::Length Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~Length.html)
[ISketchSlot::Width Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~Width.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
