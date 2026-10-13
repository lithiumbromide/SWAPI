---
title: "Width Property (ISketchSlot)"
project: "SOLIDWORKS API Help"
interface: "ISketchSlot"
member: "Width"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~Width.html"
---

# Width Property (ISketchSlot)

Gets or sets the width of this sketch slot.

## Syntax

### Visual Basic (Declaration)

```vb
Property Width As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSlot
Dim value As System.Double

instance.Width = value

value = instance.Width
```

### C#

```csharp
System.double Width {get; set;}
```

### C++/CLI

```cpp
property System.double Width {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Width of sketch slot

## VBA Syntax

See [SketchSlot::Width](ms-its:sldworksapivb6.chm::/sldworks~SketchSlot~Width.html).

## Examples

[Insert and Resize Sketch Slot (C#)](Insert_and_Resize_Sketch_Slot_Example_CSharp.htm)
[Insert and Resize Sketch Slot (VB.NET)](Insert_and_Resize_Sketch_Slot_Example_VBNET.htm)
[Insert and Resize Sketch Slot (VBA)](Insert_and_Resize_Sketch_Slot_Example_VB.htm)
[Get Sketch Slot Data (VBA)](Get_Sketch_Slot_Data_Example_vb.htm)

## See Also

[ISketchSlot Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot.html)
[ISketchSlot Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot_members.html)
[ISketchSlot::Length Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~Length.html)
[ISketchSlot::LengthType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot~LengthType.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
